from identify import run_identify
from create_table import create_table
from md5_scanner import md5_scanner
from sha1_scanner import sha1_scanner
from sha256_scanner import sha256_scanner
from sha512_scanner import sha512_scanner
from yara_scanner import yara_scanner
import os
import argparse


def decision(choice, looping=False):
    if choice == "YARA":
        if looping:
            while True:
                yara_scanner(args.filetype, args.processes)
        else:
            yara_scanner(args.filetype, args.processes)
    elif choice == "MD5":
        if looping:
            while True:
                md5_scanner(args.filetype, args.processes)
        else:
            md5_scanner(args.filetype, args.processes)
    elif choice == "SHA1":
        if looping:
            while True:
                sha1_scanner(args.filetype, args.processes)
        else:
            sha1_scanner(args.filetype, args.processes)
    elif choice == "SHA256":
        if looping:
            while True:
                sha256_scanner(args.filetype, args.processes)
        else:
            sha256_scanner(args.filetype, args.processes)
    elif choice == "SHA512":
        if looping:
            while True:
                sha512_scanner(args.filetype, args.processes)
        else:
            sha512_scanner(args.filetype, args.processes)


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--index', action='store_true',
                        default=False, help="Refresh indexing cache and scan files")
    parser.add_argument("-t", "--threads", type=int, default=10,
                        help="Specify the number of threads required for indexing (default=10)")
    parser.add_argument("-p", "--processes", type=int, default=10,
                        help="Specify the number of processes required for scanning (default=10)")
    parser.add_argument('-ft', '--filetype', choices=['application', 'text', 'image', 'video', 'all'],
                        default='application', help="Specify the filetype that you want to scan (default=application)")
    parser.add_argument("-c", "--continuous", action='store_true', default=False,
                        help="Keep continuously scanning filesystem in the background")

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--yara', action='store_true',
                       help="Utilise YARA rules for scanning")
    group.add_argument('--md5', action='store_true',
                       help="Utilise MD5 hash for scanning")
    group.add_argument('--sha1', action='store_true',
                       help="Utilise SHA1 hash for scanning")
    group.add_argument('--sha256', action='store_true',
                       help="Utilise SHA256 hash for scanning")
    group.add_argument('-ns', '--noscan', action='store_true',
                       default=False, help="Perform only file indexing, no scan")

    args = parser.parse_args()

    # INITIAL -> FILE - T , INDEX - F
    # SCAN -> FILE - F , INDEX - F
    # REFRESH -> FILE - F , INDEX - T
    # INITIAL + FLAG -> FILE - T , INDEX - T

    if not os.path.exists('filesystem.db') or args.index:
        if os.path.exists('filesystem.db'):
            os.remove('filesystem.db')
            if os.path.exists('filesystem.db-journal'):
                os.remove('filesystem.db-journal')
        
        create_table()

        print('\n#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#')
        print(r'''
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
        print(r'''
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
                if args.yara:
                    decision("YARA", args.continuous)
                elif args.md5:
                    decision("MD5", args.continuous)
                elif args.sha1:
                    decision("SHA1", args.continuous)
                elif args.sha256:
                    decision("SHA256", args.continuous)
                elif args.sha512:
                    decision("SHA512", args.continuous)
