import concurrent.futures
import filetype
import os
import sqlite3
import time
from dotenv import dotenv_values

def identify(file):
    
    try:
        kind = filetype.guess(file)
        if kind is None:
            file_ext = file.split(".")[-1]
            # print('----------------')
            # print("File extension: ", file_ext)
            # print("File name: %s" % file)
        else:
            file_ext = kind.extension
            # print('----------------')
            # print('File extension: %s' % kind.extension)
            # print('File MIME type: %s' % kind.mime)
            # print('File name: %s' % file)

    except Exception as e:
        file_ext = file.split(".")[-1]
        # print(e)
        # print("File extension: ", file.split(".")[-1])
        # print("File name: %s" % file)
    
    # Insert into the database
    sqliteConnection = sqlite3.connect('filesystem.db')
    cursor = sqliteConnection.cursor()
    data = (file_ext, file)
    sql_command = "INSERT INTO filesystem (filetype, fullpath) VALUES (?,?)"
    cursor.execute(sql_command, data)
    sqliteConnection.commit()
    cursor.close()

def run_identify():
    config = dotenv_values(".env")
    HOME = config['HOME']
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        for root, dirs, files in os.walk(HOME):
            for file in files:
                file_path = os.path.join(root, file)
                if len(file.split(".")) > 1:
                    executor.submit(identify, file_path)
