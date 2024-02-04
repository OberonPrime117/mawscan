from identify import run_identify
from create_table import create_table
from scanner import logic
import sqlite3
import os
import logging
import yara
from concurrent.futures import ProcessPoolExecutor
import time
import sys
import concurrent.futures
import filetype

if __name__ == '__main__':

    flag = 1

    if os.path.exists('filesystem.db'):
        flag = 0

    if flag == 1:
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

        run_identify()
    
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
    logic()