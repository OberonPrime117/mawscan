#!/usr/bin/python

import os
import yaml
import yara
from tqdm import tqdm
import logging
from concurrent.futures import ProcessPoolExecutor
import time
import sqlite3
import sys
import hashlib

# root + file = rule location, row = filesystem, logger1 = info, logger2 = error
def scanner(text, row, md5_path, logger1, logger2):
            
    logger1.info("Scanning File - %s",str(row))
    
    # CALCULATE HASH
    hash_md5 = hashlib.md5()
    with open(row, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""): 
            hash_md5.update(chunk)
    
    file_md5 = hash_md5.hexdigest()
    
    if file_md5 in text:
        print("==> HASH FILE - ",md5_path, " <==> MALICIOUS FILE - ",row)

def md5_scanner(category, processes=10):
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
        if category == "all":
            sql = f"SELECT fullpath FROM filesystem"
        else:
            sql = f"SELECT fullpath FROM filesystem WHERE category==\"{category}\""
        cursor = conn.execute(sql)
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
    
    with open("config.yml") as f:
        config = yaml.safe_load(f)
    
    MD5HASHES = config["md5_hash"]
    
    # MULTIPLE FILES FOR MD5
    for MD5 in MD5HASHES:
        
        # ITERATE THRU RULE LOCATION
        for root, dirs, files in os.walk(MD5):

            for file in files:
                                
                # CHECK IF HASH IS IN THIS FILE
                md5_path = os.path.join(root, file)
                
                f = open(md5_path, 'r')
                text = f.read()
                                
                with ProcessPoolExecutor(max_workers=processes) as executor:
                    futures = [executor.submit(scanner, text, row[0], md5_path, logger1, logger2) for row in rows]

                    for future in futures:
                        result = future.result()
                
                f.close()

                
    print("--- %s seconds ---" % (time.time() - start_time))

# Log some messages
# logger.debug('This is a debug message')
# logger.info('This is an info message')
# logger.warning('This is a warning message')
# logger.error('This is an error message')
# logger.critical('This is a critical message')