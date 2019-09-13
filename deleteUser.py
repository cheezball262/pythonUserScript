#Written for RHEL/Centos
#Delete a user and associated files

import os
import sys
 
# arg1 is the username to be removed from the server

username = sys.argv[1]
os.system("userdel --remove " + username)