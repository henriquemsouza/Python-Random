import os, getpass

path=os.path.join(*["C:/Users/"+getpass.getuser()+"/Documents/save"])
print(path)

if os.path.exists(path):
    print("true")
else:
    os.makedirs(path, exist_ok=True)
    print("created")
