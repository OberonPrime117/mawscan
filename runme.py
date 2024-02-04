from identify import run_identify
from create_table import create_table
from scanner import scanme
import sqlite3
import os
import logging
import yara
from concurrent.futures import ProcessPoolExecutor
import time
import sys
import concurrent.futures
import filetype
import argparse

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument('-i','--index', action='store_true', default=False, help="Refresh indexing cache")
    parser.add_argument('-ns','--noscan', action='store_true', default=False, help="Perform only file indexing, no scan")
    parser.add_argument("-t", "--threads", type=int, default=10, help="Specify the number of threads required for indexing (default=10)")
    parser.add_argument("-p", "--processes", type=int, default=10, help="Specify the number of processes required for scanning (default=10)")
    parser.add_argument('-ft','--filetype', choices=['application', 'text', 'image', 'video'], default='application',help="Specify the filetype that you want to scan")

    args = parser.parse_args()
            
    # INITIAL -> FILE - T , INDEX - F 
    # SCAN -> FILE - F , INDEX - F
    # REFRESH -> FILE - F , INDEX - T
    # INITIAL + FLAG -> FILE - T , INDEX - T

    if not os.path.exists('filesystem.db') or args.index:
        create_table()

        print('\n#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#')
        print('''
  _____ _   _ _____  ________   _______ _   _  _____     ______ _____ _      ______  _____ 
|_   _| \ | |  __ \|  ____\ \ / |_   _| \ | |/ ____|   |  ____|_   _| |    |  ____|/ ____|
  | | |  \| | |  | | |__   \ V /  | | |  \| | |  __    | |__    | | | |    | |__  | (___  
  | | | . ` | |  | |  __|   > <   | | | . ` | | |_ |   |  __|   | | | |    |  __|  \___ \ 
 _| |_| |\  | |__| | |____ / . \ _| |_| |\  | |__| |   | |     _| |_| |____| |____ ____) |
|_____|_| \_|_____/|______/_/ \_|_____|_| \_|\_____|   |_|    |_____|______|______|_____/ 

        ''')
        print('#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#\n')
        
        if args.threads:
            
            run_identify(args.threads)
    
    if not args.noscan:
    
        print('\n#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#')
        print('''
   _____  _____          _   _ _   _ _____ _   _  _____ 
  / ____|/ ____|   /\   | \ | | \ | |_   _| \ | |/ ____|
 | (___ | |       /  \  |  \| |  \| | | | |  \| | |  __ 
  \___ \| |      / /\ \ | . ` | . ` | | | | . ` | | |_ |
  ____) | |____ / ____ \| |\  | |\  |_| |_| |\  | |__| |
 |_____/ \_____/_/    \_|_| \_|_| \_|_____|_| \_|\_____|

''')
        print('#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#\n')
        
        if args.processes:
            if args.filetype:
                scanme(args.filetype, args.processes)