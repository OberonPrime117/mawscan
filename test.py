# import filetype
# print(filetype.guess("/home/aditya/Documents/Notes/.obsidian/plugins/remotely-save/manifest.json"))

# import hashlib

# def get_md5(file_path):
#     hash_md5 = hashlib.md5()
#     with open(file_path, "rb") as f:
#         for chunk in iter(lambda: f.read(4096), b""): 
#             hash_md5.update(chunk)
#     return hash_md5.hexdigest()

# # Example usage  
# my_file = 'sha1.txt'
# md5_sum = get_md5(my_file)
# print(md5_sum)

# import psutil
# import os

# # Define the additional fields you want to retrieve
# extra_fields = ['pid', 'name', 'username', 'cpu_percent', 'memory_percent', 'create_time']

# # Get a list of all running processes
# processes = []
# for proc in psutil.process_iter(['pid', 'name', 'username', 'cpu_percent', 'memory_percent', 'create_time']):
#     try:
#         processes.append(proc.info)
#     except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
#         pass

# if not os.path.exists('processes.txt'):
#     with open('processes.txt', 'w') as f:
#         f.write('PID\tName\tUsername\tCPU%\tRAM%\tCREATETIME\n')

# # Write the process information to the file
# with open('processes.txt', 'a') as f:
#     for process in processes:
#         try:
#             f.write(f"{process['pid']}\t{process['name']}\t{process['username']}\t{process['cpu_percent']}\t{process['memory_percent']}\t{process['create_time']}\n")
#         except KeyError:
#             # Skip processes with missing information
#             pass

import csv
import psutil
import os

# Define the additional fields you want to retrieve
extra_fields = ['pid', 'name', 'username', 'cpu_percent', 'memory_percent', 'create_time']

# Get a list of all running processes
processes = []
for proc in psutil.process_iter(['pid', 'name', 'username', 'cpu_percent', 'memory_percent', 'create_time']):
    try:
        processes.append(proc.info)
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass

if not os.path.exists('processes.csv'):
    with open('processes.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['PID', 'Name', 'Username', 'CPU%', 'RAM%', 'CreateTime'])
        writer.writeheader()

# Write the process information to the CSV file
with open('processes.csv', 'a', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=['PID', 'Name', 'Username', 'CPU%', 'RAM%', 'CreateTime'])
    for process in processes:
        try:
            writer.writerow({
                'PID': process['pid'],
                'Name': process['name'],
                'Username': process['username'],
                'CPU%': process['cpu_percent'],
                'RAM%': process['memory_percent'],
                'CreateTime': process['create_time']
            })
        except KeyError:
            # Skip processes with missing information
            pass
