# import filetype
# print(filetype.guess("/home/aditya/Documents/Notes/.obsidian/plugins/remotely-save/manifest.json"))

import hashlib

def get_md5(file_path):
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""): 
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

# Example usage  
my_file = 'sha1.txt'
md5_sum = get_md5(my_file)
print(md5_sum)