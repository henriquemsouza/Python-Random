import os
import shutil

# dest=destination of the file
dest = 'H:\COPP'
print("Entre com  o caminho do Binario")
src=input();


src_files = os.listdir(src)
for file_name in src_files:
    full_file_name = os.path.join(src, file_name)
    if (os.path.isfile(full_file_name)and full_file_name.endswith(".txt")):
        shutil.copy(full_file_name, dest)
