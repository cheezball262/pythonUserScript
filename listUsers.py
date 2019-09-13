#Written for RHEL/Centos
#Writes a tab-formatted list of user information pulled from /etc/passwd

import pwd
print('{:<20s} {:<20s} {:<20s}'.format("Username","Userid","Full Name"))
for entry in pwd.getpwall():
    print('{:<20s} {:<20s} {:<20s}'.format(str(entry[0]), str(entry[2]), str(entry[4])))
   