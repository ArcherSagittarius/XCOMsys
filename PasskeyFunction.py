import hashlib
import sys
import time
from getpass import getpass
#Wait Functions

#To use a different character than the default, 
#just put the function and (*insert wanted character*)
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
#Used for a we time is of the essence, usually during testing
def waitfunc_none(y='¤'):
	for x in range(0,9):
		sys.stdout.write(y)
		sys.stdout.flush()
def correctpassword_com(s):
	for c in s:
		sys.stdout.write( '%s' % c )
		sys.stdout.flush()
		time.sleep(0.07)		
"""
-------------------Setup imports and functions--------------------
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
	print "(Classified Security Protection in Force)"
	def rerun_passwork():
		ciao = "5f4dcc3b5aa765d61d8327deb882cf99"
		#This will not work correctly on Repl.it
		rinput = getpass("\nPassword: ")
		if rinput.lower() == 'q':
			print "Exiting System..."
			waitfunc_short()
			print ''
			sys.exit()
		#This sets the number of attempts allowed 
		#and prints if you are about to exceed that number 
		elif rerunpassword == 5:
			waitfunc_Xshort('-')
			print "\nWARNING, final attempt."
			waitfunc_Xshort('-')
		if hashlib.md5(rinput).hexdigest() == ciao:
			print 'Correct Password'
			print '-' * 10
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
			print "\nProtocal 'Ash and Temples' Iniziated - Emergency Shutdown Active (E.S.A.)"
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

