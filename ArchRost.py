#!/usr/bin/python
#Version 1.0

class Arch_Rost(object):

	def __init__(self):
		super(Arch_Rost,self).__init__()
	
	
	@classmethod	
	#Prints 
	def con_printlist(self):
		x = 0
		printlistinput = input('Which list do you want?')
		global printlistinput
		printlistinput_value_func()
		#FIXME: change so that the XCOM sys with input this value instead
		s = list_of_lists[printlistinput]
		while x < len(s):
			print '\n[%s, %s, %s, %s]' % (s[x].name, s[x].callsign, s[x].clss, s[x].rank)
			x = x + 1

	@classmethod
	def raw_printlist(self):
		x = 0 
		printlistinput = input('Which list do you want?')
		global printlistinput
		printlistinput_value_func()
		#FIXME: change so that the XCOM sys with input this value instead
		s = list_of_lists[printlistinput]
		while x < len(s):
			print '\n[%s, %s, %s, %s, %s, %s, %s, %s, %s, %s ]' % (
			s[x].name, 
			s[x].callsign,
			s[x].nation,
			s[x].will,
			s[x].aim,
			s[x].health,
			s[x].mobility,
			s[x].defense,
			s[x].clss,
			s[x].rank
			)
			x = x + 1 

	@classmethod
	#Fancy Con Printlist
	def fcon_printlist(self):
		x = 0
		printlistinput = input('Which list do you want?')
		global printlistinput
		printlistinput_value_func()
		#FIXME: change so that the XCOM sys with input this value instead
		s = list_of_lists[printlistinput]
		while x < len(s):
			print '\n[Name:     %s\n Callsign: %s\n Class:    %s\n Rank:     %s]' % (s[x].name, s[x].callsign, s[x].clss, s[x].rank)
			x = x + 1

	@classmethod
	#Fancy Raw Printlist
	def fraw_printlist(self):
		x = 0 
		printlistinput = input('Which list do you want?')
		global printlistinput
		printlistinput_value_func()
		#FIXME: change so that the XCOM sys with input this value instead
		s = list_of_lists[printlistinput]
		while x < len(s):
			print '\n[Name:        %s\n Callsign:    %s\n Nationality: %s\n Willpower:   %s\n Aim:         %s\n Health:      %s\n Mobility:    %s\n Defense:     %s\n Class:       %s\n Rank:        %s]' % (
			s[x].name, 
			s[x].callsign,
			s[x].nation,
			s[x].will,
			s[x].aim,
			s[x].health,
			s[x].mobility,
			s[x].defense,
			s[x].clss,
			s[x].rank
			)
			x = x + 1 

#------------------------------Useful Functions----------------------------

ar = Arch_Rost()

def printlistinput_value_func():
	global printlistinput
	if printlistinput == 0:
		unfinished()
		#print""
		#print ">" *10
		#print "Soldiers from Legendary Campaigns"
		#print '>' *10
	elif printlistinput == 1:
		print '<' *10, '>' *10	
		print "Soldiers from the Third Normal Campaign"
		print '<' *10, '>' *10	
	elif printlistinput == 2:
		print ''
		print '<' *10, '>' *10	
		print "Soldiers from the First Classical Campaign"
		print '<' *10, '>' *10	
	elif printlistinput == 3:
		print ''
		print '<' *10, '>' *10	
		print "Soldiers from the Second Classical Campaign"
		print '<' *10, '>' *10	
	elif printlistinput == 4:
		print ''
		print '<' *10, '>' *10	
		print "Soldiers from the Easy (All Second Wave Enabled) Campaign"
		print '<' *10, '>' *10	
	elif printlistinput == 5:
		print unfinished()
		#print ''
		#print '<' *10, '>' *10	
		#print "Soldiers from the Long War Normal Campaign"
		#print '<' *10, '>' *10	
	elif printlistinput == 6:
		print ''
		print '<' *10, '>' *10	
		print "Soldiers from Failed Campaigns"
		print '<' *10, '>' *10	
def unfinished():
	print "\nError, attempting to access unfinished campaign...\n"
def stat_show(self):
		print "Name:      ", self.name, "\nCallsign:  ", self.callsign, "\nWill:      ", self.will, "\nAim:       ", self.aim, "\nHealth:    ", self.health, "\nMobility:  ", self.mobility, "\nDefense:   ", self.defense
def data_show(self):
	print "Name:        ", self.name, "\nCallsign:    ", self.callsign, "\nNationality: ", self.nation, "\nClass:       ", self.clss, "\nRank:        ", self.rank	
def show_show(self):
	print "Name:        ", self.name, "\nCallsign:    ", self.callsign, "\nNationality: ", self.nation, "\nClass:       ", self.clss, "\nRank:        ", self.rank, "\nWill:        ", self.will, "\nAim:         ", self.aim, "\nHealth:      ", self.health, "\nMobility:    ", self.mobility, "\nDefense:     ", self.defense

#----------------------------------LGND Info-------------------------------

class LGND(object):
	def __init__(self, details):
		super(LGND,self).__init__()
		self.name = details[0]
		self.callsign = details[1]
		self.nation = details[2]
		self.will = details[3]
		self.aim = details[4]
		self.health = details[5]
		self.mobility = details[6]
		self.defense = details[7]
		self.clss = details[8]
		self.rank = details[9]
#if True:

#----------------------------NIII Campaign Info---------------------------

class NIII(object):
	def __init__(self, details):
		super(NIII,self).__init__()
		self.name = details[0]
		self.callsign = details[1]
		self.nation = details[2]
		self.will = details[3]
		self.aim = details[4]
		self.health = details[5]
		self.mobility = details[6]
		self.defense = details[7]
		self.clss = details[8]
		self.rank = details[9]
if True:
	niii_list = [
		('Boris Ivanov', 'Chryssalid', 'Russian', 'unknown', 'unknown', 'unknown', 'unknown', 'unknown', 'Scout', 'Master Sergeant'),
		('Fiona McLoughlin', 'Rival', 'Irish', 'unknown', 'unknown', 'unknown', 'unknown', 'unknown', 'Medic', 'Corporal'),
		('Zarina Makhuba', 'Spitfire', 'Argentinian', 'unknown', 'unknown', 'unknown', 'unknown', 'unknown', 'Assault', 'Master Sergeant'),
		('Valerie Simmons', 'Wardog', 'Scotish', 'unknown', 'unknown', 'unknown', 'unknown', 'unknown', 'Assault', 'Master Sergeant'),
		('Tomasz Malinowshi', 'Kong', 'Nigerian', 'unknown', 'unknown', 'unknown', 'unknown', 'unknown', 'Gunner', 'Master Sergeant'),
		('Chloe Vanderberg', 'Echo', 'German', 'unknown', 'unknown', 'unknown', 'unknown', 'unknown', 'Sniper', 'Master Sergeant'),
		('Zuzanna Wozniak', 'Apostle', 'Netherlander', 'unknown', 'unknown', 'unknown', 'unknown', 'unknown', 'Medic', 'Master Sergeant'),
		
		('Guadalupe Garcia', 'Kabuki', 'Japanese', 'unknown', 'unknown', 'unknown', 'unknown', 'unknown', 'Jaeger', 'Master Sergeant'),
		('Fredrik Johansen', 'Bond', 'Norwegian', 'unknown', 'unknown', 'unknown', 'unknown', 'unknown', 'Assault', 'Master Sergeant' )
		]
	niii = [NIII(item) for item in niii_list]
	chryssalid = niii[0]
	rival = niii[1]
	spitfire = niii[2]
	wardog = niii[3]
	kong = niii[4]
	echo = niii[5]
	apostle = niii[6]
	
	kabuki = niii[7]
	bond = niii[8]


#----------------------------CI Campaign Info-----------------------------

class CI(object):
	def __init__(self, details):
		super(CI,self).__init__()
		self.name = details[0]
		self.callsign = details[1]
		self.nation = details[2]
		self.will = details[3]
		self.aim = details[4]
		self.health = details[5]
		self.mobility = details[6]
		self.defense = details[7]
		self.clss = details[8]
		self.rank = details[9]
if True:
	ci_list = [
		('Adriana Santiago', 'Doubletime', 'Argentinian', 'unknown', 'unknown', 'unknown', 'unknown', 'unknown', 'Medic', 'Sergeant'),
		('Sying Pan', 'Saturn', 'Japanese', 'unknown', 'unknown', 'unknown', 'unknown', 'unknown', 'Medic', 'Master Sergeant'),
		('Ana Guzman', 'Enigme', 'Swedish', 'unknown', 'unknown', 'unknown', 'unknown', 'unknown', 'Sniper', 'Master Sergeant'),
		('Thabo Baloyi', 'Bombard', 'South African', 'unknown', 'unknown', 'unknown', 'unknown', 'unknown', 'Rocketeer', 'Master Sergeant'),
		('Geoff Allen', 'Mustang', 'American', 'unknown', 'unknown', 'unknown', 'unknown', 'unknown', 'Infantry', 'Master Sergeant'),
		
		('Lisa Clark', 'Coney', 'American', 'unknown', 'unknown', 'unknown', 'unknown', 'unknown', 'Scout', 'Master Sergeant'),
		('Yuzuki Nakajimi', 'Missionary', 'Japanese', 'unknown', 'unknown', 'unknown', 'unknown', 'unknown', 'Guardian', 'Master Sergeant'),
		('Abigail Hugnes', 'All-In', 'South African', 'unknown', 'unknown', 'unknown', 'unknown', 'unknown', 'Scout', 'Master Sergeant'),
		('Andy Hill', 'Spider', 'American', 'unknown', 'unknown', 'unknown', 'unknown', 'unknown', 'Sniper', 'Master Sergeant'),
		('Henri Dubois', 'Dropper', 'French', 'unknown', 'unknown', 'unknown', 'unknown', 'unknown', 'Medic', 'Master Sergeant'),
		
		('Ruben Sanchez', 'Rascal', 'Brazilian', 'unknown', 'unknown', 'unknown', 'unknown', 'unknown', 'Scout', 'Master Sergeant')
		]
	ci = [CI(item) for item in ci_list]
	doubletime = ci[0]
	saturn = ci[1]
	enigme = ci[2]
	bombard = ci[3]
	mustang = ci[4]
	coney = ci[5]
	missionary = ci[6]
	allin = ci[7]
	spider = ci[8]
	dropper = ci[9]
	rascal = ci[10]
	
	
#----------------------------CII Campaign Info-----------------------------

class CII(object):
	def __init__(self, details):
		super(CII,self).__init__()
		self.name = details[0]
		self.callsign = details[1]
		self.nation = details[2]
		self.will = details[3]
		self.aim = details[4]
		self.health = details[5]
		self.mobility = details[6]
		self.defense = details[7]
		self.clss = details[8]
		self.rank = details[9]
if True:
	cii_list = [
		('Brad Harrison', 'Rapidfire', 'American', 'unknown', 'unknown', 'unknown', 'unknown', 'unknown', 'Scout', 'Master Sergeant'),
		('Mickey Reed', 'Deadbolt', 'American', 'unknown', 'unknown', 'unknown', 'unknown', 'unknown', 'Sniper', 'Master Sergeant'),
		('Juliette Martine', 'Vita', 'Canadian', 'unknown', 'unknown', 'unknown', 'unknown', 'unknown', 'Medic', 'Master Sergeant'),
		('Ewan Stewart', 'Richter', 'Scottish', 'unknown', 'unknown', 'unknown', 'unknown', 'unknown', 'Rocketeer', 'Master Sergeant'),
		('Ursula Ulrich', 'Freestyle', 'German', 'unknown', 'unknown', 'unknown', 'unknown', 'unknown', 'Assault', 'Master Sergeant'),
		('Andrey Volkov', 'Tombstone', 'Russian', 'unknown', 'unknown', 'unknown', 'unknown', 'unknown', 'Scout', 'Master Sergeant'),
		('Shigeru Yamaguchi', 'Bonus', 'Japanese', 'unknown', 'unknown', 'unknown', 'unknown', 'unknown', 'Guardian', 'Master Sergeant'),
		('Inez Castille', 'Holo', 'Portugese', 'unknown', 'unknown', 'unknown', 'unknown', 'unknown', 'Gunner', 'Master Sergeant'),
		('Freida Krause', 'Voodoo', 'German', 'unknown', 'unknown', 'unknown', 'unknown', 'unknown', 'Medic', 'Master Sergeant'),
		]
	#Classical 2 Campaign Solder Conversion:
	cii = [CII(item) for item in cii_list]
	rapidfire = cii[0]
	deadbolt = cii[1]
	vita = cii[2]
	richter = cii[3]
	freestyle = cii[4]
	tombstone = cii[5]
	bonus = cii[6]
	holo = cii[7]
	voodoo = cii[8]
	
	
#-----------------------------REI Campaign Info----------------------------

	
#Roulette Easy I Campaign Class
class REI(object):
	def __init__(self, details):
		super(REI,self).__init__()
		self.name = details[0]
		self.callsign = details[1]
		self.nation = details[2]
		self.will = details[3]
		self.aim = details[4]
		self.health = details[5]
		self.mobility = details[6]
		self.defense = details[7]
		self.clss = details[8]
		self.rank = details[9]
#Roulette Easy I Campaign Information
if True:
	rei_list = [
		("Ayn Lamoue", "Remove", "French", "Unknown", "Unknown", "Unknown", "Unknown",  "Unknown", "Maurader", "Master Sergeant"),
		("Marco Gasparatto", "ARC", "Italian", "Unknown", "Unknown", "Unknown","Unknown", "Unknown", "Engineer", "Master Sergeant"),
		("Oliver Evans", "Marksman", "British", "Unknown", "Unknown", "Unknown", "Unknown", "Unknown", "Assault", "Master Sergeant"),
		("Chidubem Gondogwana", "Nyx", "South African", "Unknown", "Unknown", "Unknown", "Unknown", "Unknown", "Sniper", "Master Sergeant"),
		("Therese Durand", "Nounou", "French", "Unknown", "Unknown", "Unknown", "Unknown", "Unknown", "Gunner", "Master Sergeant"),
		("Rina Malcah", "Phantom", "Israeli", "Unknown", "Unknown", "Unknown", "Unknown", "Unknown", "Scout", "Master Sergeant"),
		
		("Martha Krause", "Tankbuster", "German", "Unknown", "Unknown", "Unknown", "Unknown", "Unknown", "Rocketeer", "Master Sergeant"),
		("Samuel Lector", "Hannibal", "American", "Unknown", "Unknown", "Unknown", "Unknown", "Unknown", "Sniper", "Master Sergeant"),
		("Adriana Diaz", "Pistolwhip", "Mexican", "Unknown", "Unknown", "Unknown", "Unknown", "Unknown", "Assault", "Master Sergeant"),
		("Sam Johnson", "Successor", "American", "Unknown", "Unknown", "Unknown", "Unknown", "Unknown", "Sniper", "Master Sergeant"),
		("Li Mei Zhang", "Snapshot", "Chinese", "Unknown", "Unknown", "Unknown", "Unknown", "Unknown", "Infantry", "Master Sergeant")
		]
	#Roulette Easy I Solder Conversion:
	rei = [REI(item) for item in rei_list]
	remove = rei[0]
	arc = rei[1]
	marksman = rei[2]
	nyx = rei[3]
	nounou = rei[4]
	phantom = rei[5]
	
	tankbuster = rei[6]
	hannibal = rei[7]
	pistolwhip = rei[8]
	successor = rei[9]
	snapshot = rei[10]
	

#----------------------------NLW Campaign Info-----------------------------


class NLW(object):
	def __init__(self, details):
		super(NLW,self).__init__()
		self.name = details[0]
		self.callsign = details[1]
		self.nation = details[2]
		self.will = details[3]
		self.aim = details[4]
		self.health = details[5]
		self.mobility = details[6]
		self.defense = details[7]
		self.clss = details[8]
		self.rank = details[9]
#if True:

#---------------------------FAIL Campaign Info----------------------------

class FAIL(object):
	def __init__(self, details):
		super(FAIL,self).__init__()
		self.name = details[0]
		self.callsign = details[1]
		self.nation = details[2]
		self.will = details[3]
		self.aim = details[4]
		self.health = details[5]
		self.mobility = details[6]
		self.defense = details[7]
		self.clss = details[8]
		self.rank = details[9]
if True:
	fail_list = [
		('Nobu Ishikawa', 'rooftop', 'Japanese', "unknown", "unknown", "unknown", "unknown", "unknown", 'Sniper', 'Master Sergeant'),
		('Faiza Boroto', 'strobe', 'Belgien', "unknown", "unknown", "unknown", "unknown", "unknown", 'Gunner', 'Master Sergeant'),
		('Ali Mansoor', 'hammer', 'Israli', "unknown", "unknown", "unknown", "unknown", "unknown", 'Assault', 'Master Sergeant'),
		('Martin Hauffmen', 'ninja', 'Swedish', "unknown", "unknown", "unknown", "unknown", "unknown", 'Scout', 'Master Sergeant'),
		('Yolanda Munoz', 'greeny', 'Canadian', "unknown", "unknown", "unknown", "unknown", "unknown", 'Medic', 'Sergeant')
		]
	fail = [FAIL(item) for item in fail_list]
	rooftop = fail[0]
	strobe = fail[1]
	hammer = fail[2]
	ninja = fail[3]
	greeny = fail[4]
		

#----------------------------List Information-----------------------------

	
#List Directory
lgnd_callsign = []
niii_callsign = [chryssalid, rival, spitfire, wardog, kong, echo, apostle, kabuki, bond]
ci_callsign = [doubletime, saturn, enigme, bombard, mustang, coney,	missionary, allin, spider, dropper, rascal]
cii_callsign = [rapidfire, deadbolt, vita, richter, freestyle, tombstone, bonus, holo, voodoo]
rei_callsign = [remove, arc, marksman, nyx, nounou, phantom, tankbuster, hannibal, pistolwhip, successor, snapshot]
nlw_callsign = []
fail_callsign = [rooftop, strobe, hammer, ninja, greeny]

list_of_lists = [lgnd_callsign, niii_callsign, ci_callsign, cii_callsign, rei_callsign, nlw_callsign, fail_callsign]	

#-------------------------Temporary 'GUI'----------------------------------
print '[0] Legend List*\n[1] NIII List\n[2] CI List\n[3] CII List\n[4] REI List\n[5] NLW List*\n[6] FAIL List'
print "For printing options, enter 'assist()'"

def assist():
	print "Printing Total List"
	print "> ar.raw_printlist() <\n"
	print "Printing Condensed List"
	print "> ar.con_printlist() <\n"
	print "Printing Formatted Total List"
	print "> ar.fraw_printlist() <\n"
	print "Printing Formatted Condensed List"
	print "> ar.fcon_printlist() <\n"
