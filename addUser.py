import os
import sys
import shutil

#arg1 is the username
#arg2 is user full name (stored in comment field)
#arg3 is the name of the public key filename
#default shell is bash

username = sys.argv[1]
userComment = sys.argv[2]
pubkeyFilename = sys.argv[3]

userAddString = "useradd -m -c " + userComment + " -d /home/" + username+ "  -s /bin/bash " + username
userSshDir = " /home/"+username+"/.ssh/

os.system(userAddString)
if os.path.exists(userSshDir + "/authorized_keys"):
    with open(pubkeyFilename) as f:
        with open(userSshDir + "/authorized_keys", "w") as f1:
            for line in f:
             f1.write(line)
else:
     os.system("mkdir " + userSshDir)
     shutil.copy(pubkeyFilename,userSshDir + "/authorized_keys")

os.system("chown -R " + username + ":" + username + userSshDir)
os.system("chmod 700 "+ userSshDir)
os.system("chmod 600 "+ userSshDir + "/authorized_keys")