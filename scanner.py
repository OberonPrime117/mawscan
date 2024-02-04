#!/usr/bin/python

import os
import yara
from tqdm import tqdm
import logging
from concurrent.futures import ProcessPoolExecutor
import time
import sqlite3
import sys
from dotenv import dotenv_values

def scanner(root, row, file, logger1, logger2):

    rule = yara.compile(os.path.join(root, file))    
    logger1.info("Scanning File - %s",str(row))
    
    try:
        matches = rule.match(row)
        if matches and (".yara" not in row or ".yar" not in row):
            print("==>","\t",matches," <==> ",row, " <==> ",file)
    except Exception as e:
        logger2.error(e)

def scanme(processes=10):
    start_time = time.time()

    logger1 = logging.getLogger('logger1')
    logger1.setLevel(logging.INFO)
    file_handler1 = logging.FileHandler('app.log', mode='w')
    logger1.addHandler(file_handler1)

    logger2 = logging.getLogger('logger2')
    logger2.setLevel(logging.ERROR)
    file_handler2 = logging.FileHandler('error.log', mode='w')
    logger2.addHandler(file_handler2)

    conn = sqlite3.connect('filesystem.db')
    try:
        cursor = conn.execute("SELECT fullpath FROM filesystem WHERE filetype==\"exe\"")
    except sqlite3.OperationalError as e:
        print('\n#=#=#=#=#=#=#=#=#=#=#=#')
        logger2.error("The CREATE TABLE operation failed")
        logger2.error("Delete generated files (logs and db)")
        logger2.error("Retry running the files")
        logger2.error("If this consistently fails then manually run `create_table.py`")
        print("AN ERROR OCCURRED - PLEASE CHECK `error.log` TO DEBUG THE ERROR")
        print('#=#=#=#=#=#=#=#=#=#=#=#')
        sys.exit()

    rows = cursor.fetchall()
    
    config = dotenv_values(".env")
    RULES = config['RULES']

    for root, dirs, files in os.walk(RULES):

        for file in files:
            
            if ".yara" in file or ".yar" in file:
                with ProcessPoolExecutor(max_workers=processes) as executor:
                    futures = [executor.submit(scanner, root, row[0], file, logger1, logger2) for row in rows]

                    for future in futures:
                        result = future.result()

                
    print("--- %s seconds ---" % (time.time() - start_time))

# Log some messages
# logger.debug('This is a debug message')
# logger.info('This is an info message')
# logger.warning('This is a warning message')
# logger.error('This is an error message')
# logger.critical('This is a critical message')