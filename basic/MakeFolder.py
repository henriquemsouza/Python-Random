import os
import getpass

path=os.path.join(*["C:/Users/"+getpass.getuser()+"/Documents/save"])
print(path)

os.makedirs(path, exist_ok=True)

