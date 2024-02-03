#!/usr/bin/python

import os
import yara
from tqdm import tqdm
import logging
from concurrent.futures import ProcessPoolExecutor
import time

def scanner(root1, dirs1, files1, file):

    
    rule = yara.compile(os.path.join(root, file))
    
    for file1 in files1:
        logger1.info("Scanning File - %s",str(file1))
        
        try:
            matches = rule.match(os.path.join(root1, file1))
            if matches and (".yara" not in file1 or ".yar" not in file1):
                print("---------","\t",matches," == ",os.path.join(root1, file1), " <==> ",file)
        except Exception as e:
            logger2.error(e)
        
    
start_time = time.time()

logger1 = logging.getLogger('logger1')
logger1.setLevel(logging.INFO)
file_handler1 = logging.FileHandler('app.log', mode='w')
logger1.addHandler(file_handler1)

logger2 = logging.getLogger('logger2')
logger2.setLevel(logging.ERROR)
file_handler2 = logging.FileHandler('error.log', mode='w')
logger2.addHandler(file_handler2)

# Log some messages
# logger.debug('This is a debug message')
# logger.info('This is an info message')
# logger.warning('This is a warning message')
# logger.error('This is an error message')
# logger.critical('This is a critical message')

for root, dirs, files in os.walk("/home/kali/Documents/GitHub/Yara-rules/rules"):
    #path = root.split(os.sep)

    for file in files:
        
        if ".yara" in file or ".yar" in file:
            with ProcessPoolExecutor(max_workers=5) as executor:
                futures = [executor.submit(scanner, root1, dirs1, files1, file) for root1, dirs1, files1 in os.walk("/home/kali")]
    
                for future in futures:
                    result = future.result()
        else:
            logger2.error("YARA should not compile a normal file - %s",file)
            continue

print("--- %s seconds ---" % (time.time() - start_time))
