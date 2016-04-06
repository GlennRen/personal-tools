import hashlib

with open('') as a:
	encryptedPasswords = a.read().splitlines()

with open('') as f:
    lines = f.read().splitlines()
    for i in lines:
    	if (hashlib.md5(i.lower()).hexdigest()) in encryptedPasswords:
    		print (i.lower())
    		print (hashlib.md5(i.lower()).hexdigest())
    		print ("")
