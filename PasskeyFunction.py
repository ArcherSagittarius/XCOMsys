import hashlib
import sys
import time

#Wait Functions
#to use a different character than the default, 
#   just put the function and (*insert character*)
def waitfunc_Xshort(y='¤'):
	for x in range(0, 9):
		sys.stdout.write(y)
		time.sleep(.035)	
		sys.stdout.flush()
def waitfunc_short(y='¤'):
	for x in range(0, 9):
		sys.stdout.write(y)
		time.sleep(.07)	
		sys.stdout.flush()
def waitfunc_long(y='¤'):
	for x in range(0, 19):
		sys.stdout.write(y)
		time.sleep(.07)
		sys.stdout.flush()
#Used for the fast methods of testing
def waitfunc_none(y='¤'):
	for x in range(0,9):
        sys.stdout.write(y)
		sys.stdout.flush()

"""
--------------------------Setup imports and functions-------------------------
"""

#Passkey varables
rerunpassword = 1
elsebreak = 1
runthisfunction = 0

#Passkey program
def run_this_function():
	print "Initializing //XCOM Roster program..."
	waitfunc_short()
	
	print "\nXCOM::ROSTER: Version 3.1.20.46..."
	time.sleep(.4)
	print "\nInitializtion complete, enter password:"
	#Maybe make this security protection change and actually change functionalities?...
	print "(Classified Security Protection in Force)"
	def rerun_passwork():
		ciao = "5f4dcc3b5aa765d61d8327deb882cf99"
		rinput = raw_input("\nPassword: ")
		#To quit, mearly press q or Q and enter
		if rinput.lower() == 'q':
			print "Exiting System..."
			waitfunc_short()
			print ''
			sys.exit()
		#If this is your 5th attempt, you've struck out or are about to
		elif rerunpassword == 5:
			waitfunc_Xshort('-')
			print "\nWARNING, final attempt."
			waitfunc_Xshort('-')
		if hashlib.md5(rinput).hexdigest() == ciao:
			print "\nWelcome Commander"
			waitfunc_short()
			global elsebreak
			elsebreak = 0
		
		#Special case to prevent EXALT sympathizers from gaining access.
		elif rinput.lower() == 'exalt':
			print "\nALERT" 
			print "EXALT hack detected..."
			waitfunc_long()
			time.sleep(.7)
			print "\nProtocal 'Ash and Temples' Iniziated - Emergency Shutdown Active"
			time.sleep(.7)
			print '\nE.S.A. complete, locking system'
			waitfunc_long()
			print "\nViglio Confido"
			sys.exit()
		
		#Effectively a function which regulates the number of times the password can be attempted.
		else:
			global rerunpassword
			print "\nIncorrect Password"
			
			if rerunpassword < 6:
				if True:	
					print "Attempt (%d/5)" % rerunpassword
					print '[To quit enter (q)]'
					rerunpassword = rerunpassword + 1
					rerun_passwork()
			else: 
				print "Locking System..."
				waitfunc_short()
				print "\nLocked"
				sys.exit()

	rerun_passwork()
run_this_function()	

#Passkey encryption site: http://www.unit-conversion.info/texttools/md5/ 
#Current Password is: password
