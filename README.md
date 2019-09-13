
Environment: RHEL/CentOS, Python >2.7<br>
Python Scripts:<br>
**addUser.py** - will add a new user to the system. 
	

       usage: python addUser.py <userid> "<user full name>" <public key file name>
    	  ex: python addUser.py bob1 "Bob Smith" id_rsa.pub
    	note: <user full name> should be passed in as a String

**listUsers.py** - will list all users/userids/comments on the system. 
	

    usage: python listUsers.py
    
    	
**deleteUser.py** - will remove a user and associated directories from the system. 
	

     usage: python deleteUser <userid>
	   	ex: python deleteUser.py bob1 
