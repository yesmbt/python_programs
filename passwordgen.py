import string
from random import *
for i in range(1,1000000):
	characters = string.ascii_letters
	password = "".join(choice(characters) for x in range(randint(8,9)))
	passdic = open('passdicfile.txt', 'a')
	passdic.write(password+"\n")
	passdic.close()

