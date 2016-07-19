import time
import sys
from getpass import getpass
import hashlib



"""
----------------------------Standard Functions---------------------------------
"""
#Useful Functions
def change_all_stats(self):
	self.will = input('Will: ')
	self.aim = input('Aim: ')
	self.health = input('Health: ')
	self.mobility = input('Mobility: ')
	self.defense = input('Defense: ')

#Wait Functions
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
def waitfunc_none(y='¤'):
	for x in range(0,9):
		sys.stdout.write(y)
		sys.stdout.flush()

#MEC Functions and Exceptions
class MECInvalidRank(Exception):
	#Augmentee's rank is too low, ERROR
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr(self.value)
def clss_changer(self):
	if self.clss == 'Scout':
		self.clss = self.clss.replace('Scout', 'Pathfinder', 1)
	elif self.clss == 'Assault':
		self.clss = self.clss.replace('Assault', 'Maurader', 1)
	elif self.clss == 'Infantry':
		self.clss = self.clss.replace('Infantry', 'Valkyrie', 1)
	elif self.clss == 'Rocketeer':
		self.clss = self.clss.replace('Rocketeer', 'Archer', 1)
	elif self.clss == 'Gunner':
		self.clss = self.clss.replace('Gunner', 'Goliath', 1)
	elif self.clss == 'Sniper':
		self.clss = self.clss.replace('Sniper', 'Jaeger', 1)
	elif self.clss == 'Medic':
		self.clss = self.clss.replace('Medic', 'Guardian', 1)
	elif self.clss == 'Engineer':
		self.clss = self.clss.replace("Engineer", "Shogun", 1)
def mec_demote_rank(self):
	if self.rank is "Lance Corporal":
		self.rank = "Specialist"
	elif self.rank is "Corporal":
		self.rank = "Lance Corporal"
	elif self.rank is "Sergeant":
		self.rank = "Corporal"
	elif self.rank is "Tech Sergeant":
		self.rank = "Sergeant"
	elif self.rank is "Gunnery Sergeant":
		self.rank = "Tech Sergeant"
	elif self.rank is "Master Sergeant":
		self.rank = "Gunnery Sergeant"
	elif self.rank is "Specialist" or self.rank is "Rookie":
		print "ERROR, rank is not high enough rank for Augmentation."
		time.sleep(1)
		print "-" * 10
		print "Exiting Augmentation..."
		time.sleep(1)
		print "Returning to Root Menu..."
		print "-" * 10
		print "Printing ERROR..."
		time.sleep(1)
		raise MECInvalidRank("Promotion to a Minimum of Lance Corporal is Mandatory")
def mec_test(self):
	clss = self.clss
	if clss == "Scout" or clss == "Assault" or clss == "Infantry" or clss == "Rocketeer" or clss == "Gunner" or clss == "Sniper" or clss == "Medic" or clss == "Engineer" :
		print "False"
	elif clss == "Pathfinder" or clss == "Maurader" or clss == "Valkyrie" or clss == "Archer" or clss == "Goliath" or clss == "Jaegar" or clss == "Guardian" or clss == "Shogun":
		print "True"
	else:
		print "Undefined"	
def mec_respo_yesfunc(self):
			print "\nFor MEC augmentation, double authorization is required."
			print "Continue with operation?\n"
			mec_response = raw_input('Yes/No:')
			if mec_response.lower() == 'yes':
				mec_respo_yesfunc2(self)
			elif mec_response.lower() == 'y':
				mec_respo_yesfunc2(self)
			elif mec_response.lower() == 'no':
				print "-" * 10
				print "Augmentation aborted, returning to main menu..."
				print "-" * 10 
			elif mec_response.lower() == 'n':
				print "-" * 10
				print "Augmentation aborted, returning to main menu..."
				print "-" * 10 
			else:
				print "\nERROR - invalid input, please select a valid input\n"
				time.sleep(1)
				self.mec_train(self)
def mec_respo_yesfunc2(self):
		mec_demote_rank(self)
		clss_changer(self)
		print "-" * 10
		print "Augmentation machinery initializing..."
		time.sleep(1)
		print "Procedure in progress..."
		print "-" * 10
		time.sleep(1)
		print "\nPlease input new stats for selected Soldier."
		change_all_stats(self)
		waitfunc_long()
		print "\nAugmentation complete, soldier ready for deployment."
		self.show_show()
	
		#A simple test to see if a soldier is a MEC or not
	
			
	
		#Because Master Sergeants aren't promoted, but receive stat boosts, from missions...
		#This function allows you to adjust the stats.
		#def adjust_ms_stats():
		
#Promote Functions
class PromoteInvalidRank(Exception):
	#Soldier is already a rookie, and can't be demoted.
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr(self.value)

"""
--------------------------------Passkey Program--------------------------------
"""


#Paste Passkey program here --
#Passkey Variables
elsebreak = 0
#Paste Passkey program here --
	
	
"""
----------------------------------Menu Functions-------------------------------
"""

#FIXME: change all campaigns to correct values and numbers

#Opening Screen for Roster, prompts user with functions and help
def main_menu():
	if elsebreak == 0:
		print "\nMAIN MENU"
		print "-" * 20
		print "\nFeatures"
		print "-" * 20
		print "[1]Enter New Soldier\n[2]Augment Soldier\n[3]Promote Soldier\n[4]Show Data, Stats, or All\n"
		print "\nRoster Lists"
		print ">" * 20
		print "[A]Legendary Soldiers\n[B]Normal Campaign III\n[C]Classical Campaign I\n[D]Classical Campaign II\n[E]Roulette Easy\n[F]Normal Long War\n[X]Failed Campaigns\n" 
		print "\nTo ask for syntax for a feature, Type ' menu_help() '"
		print "\nTo see the campaign roster lists, Type ' menu_lists() '\n"

#This is the menu help prompts, will be updated with new functions
def menu_help():	
	if elsebreak == 0:
		print "To Ask for a Syntax, type that Feature's [ ] code in."
		menu_help_response = raw_input() 
		if menu_help_response == "1":
			print "Entering New Soldier Syntax..."
			time.sleep(1)
			print "--"*10
			print "nicknameofsoldier = XCOM('Name of Soldier', 'Nationality', Will #, Aim #, Health #, Mobility #, Defense #, 'Class', 'Rank')"
			print "\nExample: arrow = XCOM('Joseph Ward', 'American', 30, 65, 4, 13, 0, 'Infantry', 'Sergeant' )"
			print "--"*10
	
		elif menu_help_response == '2':
			print "Entering Augment Soldier Syntax..."
			time.sleep(1)
			print "--"*10
			print "nicknameofsoldier.mec_train()"
			print "\nExample: arrow.mec_train()"
			print '--'*10
		
		elif menu_help_response == '3':
			print "Entering Promote Soldier Syntax..."
			time.sleep(1)
			print '--'*10
			print "nicknameofsoldier.promote_rank()"
			print "\nExample: arrow.promote_rank()"
			print '--'*10

		elif menu_help_response == '4':
			print "Entering Show Data, Stats, or All Syntax..."
			time.sleep(1)
			print '--'*10
			print "nicknameofsoldier.data_show()\nnicknameofsoldier.stat_show()\nnicknameofsoldier.show_show()"
			print "\nExamples:\narrow.data_show()\narrow.stat_show()\narrow.show_show()"
			print '--'*10
		
		else:
			print "ERROR - Invalid entry. Remember to input a valid Feature code and remove the []s."
			print "Returning to Main Menu..."
			return
	elif elsebreak == 1:
		print 'Access Denied'

#This is the menu lists prompt, update with new soldiers and new campaigns.
def menu_lists():
	if elsebreak == 0:
		print "To see roster, type the list's [] code."
		menu_list_response = raw_input().lower()
		#archrost = Arch_Rost()
		def menu_list_response_func():
			print "Downloading Legendary Soldiers list..."
			waitfunc_short()
			print "\nDownload Complete."
			#res2 = menu_list_response2
			global res2
			res2 = raw_input("Would you like the Condensed or Raw list of Soldiers? (Con/Raw)").lower()
	#All of the if,elif,else menu_list_response(s):			
		if menu_list_response == "a":
			menu_list_response_func()
			if res2 == 'raw':
				archrost.Legendary_Soldiers_Full()
			elif res2 == 'con':
				archrost.Legendary_Soldiers()
			
		elif menu_list_response == "b":
			menu_list_response_func()
			if res2 == 'raw':
				archrost.Normal_Campaign_III_Soldiers_Full()
			elif res2 == 'con':
				archrost.Normal_Campaign_III_Soldiers()
				
		elif menu_list_response == "c":
			menu_list_response_func()
			if res2 == 'raw':
				archrost.Classical_Campaign_I_Soldiers_Full()
			elif res2 == 'con':
				archrost.Classical_Campaign_I_Soldiers()
			
		elif menu_list_response == "d":
			menu_list_response_func()
			if res2 == 'raw':
				archrost.Classical_Campaign_II_Soldiers_Full()
			elif res2 == 'con':
				archrost.Classical_Campaign_II_Soldiers()
		
		elif menu_list_response == "e":
			menu_list_response_func()
			if res2 == 'raw':
				archrost.Roulette_Easy_I_Soldiers_Full()
			elif res2 == 'con':
				archrost.Roulette_Easy_I_Soldiers()
				
		elif menu_list_response == "f":
			menu_list_response_func()
			if res2 == 'raw':
				archrost.Normal_Long_War_Soldiers_Full()
			elif res2 == 'con':
				archrost.Normal_Long_War_Soldiers()
		
		elif menu_list_response == "x":
			menu_list_response_func()
			if res2 == 'raw':
				archrost.Failed_Campaign_Soldiers_Full()
			elif res2 == 'con':
				archrost.Failed_Campaign_Soldiers()
		
		else:
			print "ERROR - Invalid entry. Remember to input a valid list code and remove the []s."
			print "Returning to Main Menu..."
			return
	elif elsebreak == 1:
		print 'Access Denied'

"""
----------------------------------Arch_Rost-------------------------------------
"""

#Holds the functions for storing and view Archived Rosters.
#To edit the stats of a soldier, edit their ..._Full list,
#The other list mearly holds identity info.

#Paste Arch_Rost here --


#Paste Arch_Rost Here -- 
	
"""
----------------------------------XCOM Class-----------------------------------
"""


#Holds all the functions for creating, promoting and specializing soldiers.
class XCOM(object):
	main_menu()
	
	if elsebreak == 0:
		def __init__(self, name, callsign, nation, will, aim, health, mobility, defense, clss, rank):
			#Basic set-up function, establishes a new soldier's stats
			"""
			For consistant syntax, use the self. as the nickname and the name as the full name with space. 
			"""
			super(XCOM,self).__init__()
			self.name = name
			self.callsign = callsign
			self.nation = nation
			self.will = will
			self.aim = aim
			self.health = health
			self.mobility = mobility
			self.defense = defense
			self.clss = clss
			self.rank = rank
	else:
		print 'Database Locked'
	
	"""
	Show Functions, show stats (numbers), data (personal information), and show (All)
	"""
	
	def stat_show(self):
		print "Name:      ", self.name, "\nCallsign:  ", self.callsign, "\nWill:      ", self.will, "\nAim:       ", self.aim, "\nHealth:    ", self.health, "\nMobility:  ", self.mobility, "\nDefense:   ", self.defense
	
	def data_show(self):
		print "Name:        ", self.name, "\nCallsign:    ", self.callsign, "\nNationality: ", self.nation, "\nClass:       ", self.clss, "\nRank:        ", self.rank	
	
	def show_show(self):
		print "Name:        ", self.name, "\nCallsign:    ", self.callsign, "\nNationality: ", self.nation, "\nClass:       ", self.clss, "\nRank:        ", self.rank, "\nWill:        ", self.will, "\nAim:         ", self.aim, "\nHealth:      ", self.health, "\nMobility:    ", self.mobility, "\nDefense:     ", self.defense
	
	"""
	Main Training and Promotion Functions
	"""
	
	def promote_rank(self):
		if self.rank is "Rookie":
			self.rank = "Specialist"
			print "Promotion!\nNew rank: %s"  % self.rank
		elif self.rank is "Specialist":
			self.rank = "Lance Corporal"
			print "Promotion!\nNew rank: %s"  % self.rank
		elif self.rank is "Lance Corporal":
			self.rank = "Corporal"
			print "Promotion!\nNew rank: %s"  % self.rank
		elif self.rank is "Corporal":
			self.rank = "Sergeant"
			print "Promotion!\nNew rank: %s"  % self.rank
		elif self.rank is "Sergeant":
			self.rank = "Tech Sergeant"
			print "Promotion!\nNew rank: %s"  % self.rank
		elif self.rank is "Tech Sergeant":
			self.rank = "Gunnery Sergeant"
			print "Promotion!\nNew rank: %s"  % self.rank
		elif self.rank is "Gunnery Sergeant":
			self.rank = "Master Sergeant"
			print "Promotion!\nNew rank: %s"  % self.rank
		elif self.rank is "Master Sergeant":
			print "Max Rank Attained\nCurrent rank: %s"  % self.rank
		else:
			print "Rank is invalid, please change the soldier to have a valid rank."
	
	def demote_rank(self):
			if self.rank is "Specialist":
				self.rank = "Rookie"
			elif self.rank is "Lance Corporal":
				self.rank = "Specialist"
			elif self.rank is "Corporal":
				self.rank = "Lance Corporal"
			elif self.rank is "Sergeant":
				self.rank = "Corporal"
			elif self.rank is "Tech Sergeant":
				self.rank = "Sergeant"
			elif self.rank is "Gunnery Sergeant":
				self.rank = "Tech Sergeant"
			elif self.rank is "Master Sergeant":
				self.rank = "Gunnery Sergeant"
			elif self.rank is "Rookie":
				raise PromoteInvalidRank("Soldier is already at minimum rank")
			
	#def promote_officer():
	
	#def psi_train():
	
	#Includes the ability to Augment soldiers: complete with stat tweaking, class translation, and rank reduction.
	def mec_train(self):
		print "Are you sure? This process is irreversible.\n"
		mec_response = raw_input('Yes/No:')
		if mec_response.lower() == 'yeah':
			#This demotes the soldier down a rank, one of the prices of becoming a MEC
			mec_demote_rank(self)
			#This translates the class from normal to MEC, this is mainly for the databases.
			clss_changer(self)
			print "-" * 5
			print "Emergency overide active, //safety.mec overridden"
			print "Procedure in progress..."
			print "-" * 5
			print "Input new stats for selected Soldier."
			#Because I don't know how to program the stats to translate, you will have to input them here.
			change_all_stats(self)
			waitfunc_none()
			print "\nAugmentation complete, soldier ready for deployment."
			self.show_show()
		#Yeah is for debugging and quick checking. The difference is that it removes the flair and time waiting for faster augmentation.
		elif mec_response.lower() == 'no':
			print "-" * 10
			print "Augmentation aborted, returning to main menu..."
			print "-" * 10 
		elif mec_response.lower() == 'n':
			print "-" * 10
			print "Augmentation aborted, returning to main menu..."
			print "-" * 10 
		#No is in case you mistyped or changed your mind.
		elif mec_response.lower() == 'yes':
			mec_respo_yesfunc(self)
		elif mec_response.lower() == 'y':
			mec_respo_yesfunc(self)
			
			
		#This one should be obvious
		else:
				print "\nERROR - invalid input, please select a valid input\n"
				time.sleep(1)
				self.mec_train()


"""
--------------------------------Sample Soldiers--------------------------------
"""

lamou = XCOM("Ayn Lamou", "Remove", "French", 109, 87, 12, 15, 0, "Maurader", "Master Sergeant")
arrow = XCOM("Joseph Ward", "Sagitarius", "American", 30, 65, 4, 13, 0, "Infantry", "Sergeant" )
freaky = XCOM("John Friendly", "Freaky",  "American", 30, 65, 4, 13, 0, "Engineer", "Sergeant")
spaz = XCOM("John Ward", "Meltdown", "American", 30, 65, 4, 13, 0, "Assault", "Rookie" )
