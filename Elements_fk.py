Jumps={
	'Salchov':{'1S':0.4,'2S':1.3,'3S':4.2,'4S':10.5},      # тут дефолтовые элементы

	'Toeloop':{'1T':0.4,'2T':1.3,'3T':4.1,'4T':10.3},

	'Loop':{'1Lo':0.5,'2Lo':1.8,'3Lo':5.1,'4Lo':12.0},

	'Flip':{'1F':0.5,'2F':1.8,'3F':5.3,'4F':12.3},

	'Lutz':{'1L':0.6,'2L':2.1,'3L':6.0,'4L':13.6},

	'Axel':{'1A':1.1,'2A':3.3,'3A':8.5,'4A':15.0},

	'1W':0.1 
}


Steps={
	'StSqB':1.5,
	'StSq1':1.8,
	'StSq2':2.6,
	'StSq3':3.3,
	'StSq4':3.9,
	'ChSq':2.0
}

Spins={
	'Up':{'USpB':1.0,'USp1':1.2,'USp2':1.5,'USp3':1.9,'USp4':2.4},

	'Layback':{'LSpB':1.2,'LSp1':1.5,'LSp2':1.9,'LSp3':2.4,'LSp4':2.7},

	'Sit':{'SSpB':1.1,'SSp1':1.3,'SSp2':1.6,'SSp3':1.6,'SSp4':2.5},
	
	'Libela':{'CSpB':1.1,'CSp1':1.4,'CSp2':1.8,'CSp3':2.3,'CSp4':2.6},

	'Change_foot':[{'CUSpB':1.5,'CUSp1':1.7,'CUSp2':2.0,'CUSp3':2.4,'CUSp4':2.9},
{'CCSpB':1.7,'CCSp1':2.0,'CCSp2':2.3,'CCSp3':2.8,'CCSp4':3.2,},{'CSSpB':1.6,'CSSp1':1.9,
'CSSp2':2.3,'CSSp3':2.6,'CSSp4':3.0}],

	'Comb':{'CoSpB':1.5,'CoSp1':1.7,'CoSp2':2.0,'CoSp3':2.5,'CoSp4':3.0},

	'Foot_and_Pos':{'CCoSpB':1.7,'CCoSp1':2.0,'CCoSp2':2.5,'CCoSp3':3.0,'CCoSp4':3.5},

	'Fly':[{'FCSpB':1.6,'FCSp1':1.9,'FCSp2':2.3,'FCSp3':2.8,'FCSp4':3.2},{'FSSpB':1.9,
'FSSp1':2.0,'FSSp2':2.3,'FSSp3':2.6,'FSSp4':3.0}]
}

second_part=1.1

print "U're welcome! Lets have fun!"

user_elements=[]          # epmty list for user's elements. Next loop will insert elements.

for i in user_elements:
	i=raw_input('Please, isert yr element just like it is written in ISU system. To insert a combintaion just insert two jumps separetly.') # Here user isert his fucking element
	if i in Jumps or i in Steps or i in Spins: # Here we look through our dictionaries and try to find element iserted
		user_elements.append(i) # here we append that element if we've found it in last action
		print user_elements # and here we let marasmatic user see what he just inserted
		raw_input('Is that all? y/n') 
		if 'y': break
		if 'n': continue
	else:
		print "Sorry, looks like there is a mistake here, try again please!" # that's what happens if we didn't find the crap inserted
		continue

# so we've got the list of elements we gonna work with. Let's have some fun with jump combintaions!

user_jumps=[] # here we filter only jumps from all user elements list to make combinations

for i in user_elemnts:
	if i in Jumps:
		user_jumps.append(i)



