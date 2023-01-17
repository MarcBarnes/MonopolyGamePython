# Marcus Barnes
#RealEstateDictionary.py
#


# ********README******
# most info for database pulled from --> http://www.math.yorku.ca/~zabrocki/math2042/Monopoly/prices.html
# This is a nested Dictionary
# must have following line at top of any file that wants to access to this nested dictionary:
# from RealEstateDictionary import EstateDict

#and can access dictionary fields by print(EstateDict[EstateName]['available'])
# 	 *and must be within same directory

# following fields must be contained in each dictionary
# 	position
# 	estateName
# 	price
# 	rent
# 	group
# 	available (1 if available, 0 if it is owned)
# 	ownerNumber (-1 if there is no owner)
# 	houses
# 	hotel (0 for no, 1 for yes)
# 	monopoly (0 for no, 1 for yes)
# 	own1HouseRent
# 	own2HouseRent
# 	own3HouseRent
# 	own4HouseRent
# 	hotelRent
# 	mortgaged
# 	mortgageValue
# 	houseCost



# Should keep formatting of tabspacing for easy editing: **USE Insert button on keyboard when editing

EstateDict = {	2:  {'estateName': 'Mediterranean Ave.'		,'price': '60'  	,'rent': '2' ,	'group': '0'		,'available': '1' ,		'ownerNumber': '-1',	'houses': '0',	'hotel': '0', 'monopoly': '0', 'own1HouseRent': '10'	, 'own2HouseRent':'30'		, 'own3HouseRent': '90'	 	, 'own4HouseRent': '160'	, 'hotelRent': '250'	, 'mortgaged': '0', 'mortgageValue': '30', 	'houseCost': '50'},
				4:  {'estateName': 'Baltic Ave.'          		,'price': '60'  	,'rent': '4' ,	'group': '0'		,'available': '1' , 	'ownerNumber': '-1', 	'houses': '0',	'hotel': '0', 'monopoly': '0', 'own1HouseRent': '20'	, 'own2HouseRent':'60'		, 'own3HouseRent': '180'	, 'own4HouseRent': '320'	, 'hotelRent': '450'	, 'mortgaged': '0', 'mortgageValue': '30', 	'houseCost': '50'},
				7:  {'estateName': 'Oriental Ave.'        		,'price': '100' 	,'rent': '6' ,	'group': '1' 	,'available': '1' , 	'ownerNumber': '-1', 	'houses': '0',	'hotel': '0', 'monopoly': '0', 'own1HouseRent': '30'	, 'own2HouseRent':'90'		, 'own3HouseRent': '270'	, 'own4HouseRent': '400'	, 'hotelRent': '550'	, 'mortgaged': '0', 'mortgageValue': '50', 	'houseCost': '50'},
				9:  {'estateName': 'Vermont Ave.'         		,'price': '100' 	,'rent': '6' ,	'group': '1' 	,'available': '1' , 	'ownerNumber': '-1', 	'houses': '0',	'hotel': '0', 'monopoly': '0', 'own1HouseRent': '30'	, 'own2HouseRent':'90'		, 'own3HouseRent': '270'	, 'own4HouseRent': '400'	, 'hotelRent': '550'	, 'mortgaged': '0', 'mortgageValue': '50', 	'houseCost': '50'},
				10: {'estateName': 'Connecticut Ave.'     		,'price': '120' 	,'rent': '8' ,	'group': '1' 	,'available': '1' , 	'ownerNumber': '-1', 	'houses': '0',	'hotel': '0', 'monopoly': '0', 'own1HouseRent': '40'	, 'own2HouseRent':'100'		, 'own3HouseRent': '300'	, 'own4HouseRent': '450'	, 'hotelRent': '600'	, 'mortgaged': '0', 'mortgageValue': '60', 	'houseCost': '50'},
				12: {'estateName': 'St. Charles Place'     	,'price': '140' 	,'rent': '10',	'group': '2'		,'available': '1' , 	'ownerNumber': '-1', 	'houses': '0',	'hotel': '0', 'monopoly': '0', 'own1HouseRent': '50'	, 'own2HouseRent':'150'		, 'own3HouseRent': '450'	, 'own4HouseRent': '625'	, 'hotelRent': '750'	, 'mortgaged': '0', 'mortgageValue': '70', 	'houseCost': '100'},
				14: {'estateName': 'States Ave.'           	,'price': '140' 	,'rent': '10', 	'group': '2'		,'available': '1' , 	'ownerNumber': '-1', 	'houses': '0',	'hotel': '0', 'monopoly': '0', 'own1HouseRent': '50'	, 'own2HouseRent':'150'		, 'own3HouseRent': '450'	, 'own4HouseRent': '625'	, 'hotelRent': '750'	, 'mortgaged': '0', 'mortgageValue': '70', 	'houseCost': '100'},
				15: {'estateName': 'Virginia Ave.'         	,'price': '160' 	,'rent': '12', 	'group': '2'		,'available': '1' , 	'ownerNumber': '-1', 	'houses': '0',	'hotel': '0', 'monopoly': '0', 'own1HouseRent': '60'	, 'own2HouseRent':'180'		, 'own3HouseRent': '500'	, 'own4HouseRent': '700'	, 'hotelRent': '900'	, 'mortgaged': '0', 'mortgageValue': '80', 	'houseCost': '100'},
				17: {'estateName': 'St. James Place'       	,'price': '180' 	,'rent': '14', 	'group': '3'		,'available': '1' , 	'ownerNumber': '-1', 	'houses': '0',	'hotel': '0', 'monopoly': '0', 'own1HouseRent': '70'	, 'own2HouseRent':'200'		, 'own3HouseRent': '550'	, 'own4HouseRent': '750'	, 'hotelRent': '950'	, 'mortgaged': '0', 'mortgageValue': '90', 	'houseCost': '100'},
				19: {'estateName': 'Tennessee Ave.'        	,'price': '180' 	,'rent': '14', 	'group': '3'		,'available': '1' , 	'ownerNumber': '-1', 	'houses': '0',	'hotel': '0', 'monopoly': '0', 'own1HouseRent': '70'	, 'own2HouseRent':'200'		, 'own3HouseRent': '550'	, 'own4HouseRent': '750'	, 'hotelRent': '950'	, 'mortgaged': '0', 'mortgageValue': '90', 	'houseCost': '100'},
				20: {'estateName': 'New York Ave.'         	,'price': '200' 	,'rent': '16', 	'group': '3'		,'available': '1' , 	'ownerNumber': '-1', 	'houses': '0',	'hotel': '0', 'monopoly': '0', 'own1HouseRent': '80'	, 'own2HouseRent':'220'		, 'own3HouseRent': '600'	, 'own4HouseRent': '800'	, 'hotelRent': '1000'	, 'mortgaged': '0', 'mortgageValue': '100', 	'houseCost': '100'},
				22: {'estateName': 'Kentucky Ave.'         	,'price': '220' 	,'rent': '18', 	'group': '4'			,'available': '1' , 	'ownerNumber': '-1', 	'houses': '0',	'hotel': '0', 'monopoly': '0', 'own1HouseRent': '90'	, 'own2HouseRent':'250'		, 'own3HouseRent': '700'	, 'own4HouseRent': '875'	, 'hotelRent': '1050'	, 'mortgaged': '0', 'mortgageValue': '110', 	'houseCost': '150'},
				24: {'estateName': 'Indiana Ave.'          	,'price': '220' 	,'rent': '18', 	'group': '4'			,'available': '1' , 	'ownerNumber': '-1', 	'houses': '0',	'hotel': '0', 'monopoly': '0', 'own1HouseRent': '90'	, 'own2HouseRent':'250'		, 'own3HouseRent': '700'	, 'own4HouseRent': '875'	, 'hotelRent': '1050'	, 'mortgaged': '0', 'mortgageValue': '110', 	'houseCost': '150'},
				25: {'estateName': 'Illinois Ave.'         	,'price': '240' 	,'rent': '20', 	'group': '4'			,'available': '1' , 	'ownerNumber': '-1', 	'houses': '0',	'hotel': '0', 'monopoly': '0', 'own1HouseRent': '100'	, 'own2HouseRent':'300'		, 'own3HouseRent': '750'	, 'own4HouseRent': '925'	, 'hotelRent': '1100'	, 'mortgaged': '0', 'mortgageValue': '120', 	'houseCost': '150'},
				27: {'estateName': 'Atlantic Ave.'         	,'price': '260' 	,'rent': '22', 	'group': '5'		,'available': '1' , 	'ownerNumber': '-1', 	'houses': '0',	'hotel': '0', 'monopoly': '0', 'own1HouseRent': '110'	, 'own2HouseRent':'330'		, 'own3HouseRent': '800'	, 'own4HouseRent': '975'	, 'hotelRent': '1150'	, 'mortgaged': '0', 'mortgageValue': '130', 	'houseCost': '150'},
				28: {'estateName': 'Ventnor Ave.'          	,'price': '260' 	,'rent': '22', 	'group': '5'		,'available': '1' , 	'ownerNumber': '-1', 	'houses': '0',	'hotel': '0', 'monopoly': '0', 'own1HouseRent': '110'	, 'own2HouseRent':'330'		, 'own3HouseRent': '800'	, 'own4HouseRent': '975'	, 'hotelRent': '1150'	, 'mortgaged': '0', 'mortgageValue': '130', 	'houseCost': '150'},
				30: {'estateName': 'Marvin Gardens'        	,'price': '280' 	,'rent': '24', 	'group': '5'		,'available': '1' , 	'ownerNumber': '-1', 	'houses': '0',	'hotel': '0', 'monopoly': '0', 'own1HouseRent': '120'	, 'own2HouseRent':'360'		, 'own3HouseRent': '850'	, 'own4HouseRent': '1025'	, 'hotelRent': '1200'	, 'mortgaged': '0', 'mortgageValue': '140', 	'houseCost': '150'},
				32: {'estateName': 'Pacific Ave.'          	,'price': '300' 	,'rent': '26', 	'group': '6'	,'available': '1' , 	'ownerNumber': '-1', 	'houses': '0',	'hotel': '0', 'monopoly': '0', 'own1HouseRent': '130'	, 'own2HouseRent':'390'		, 'own3HouseRent': '900'	, 'own4HouseRent': '1100'	, 'hotelRent': '1275'	, 'mortgaged': '0', 'mortgageValue': '150', 	'houseCost': '200'},
				33: {'estateName': 'North Carolina Ave.'   	,'price': '300' 	,'rent': '26', 	'group': '6'	,'available': '1' , 	'ownerNumber': '-1', 	'houses': '0',	'hotel': '0', 'monopoly': '0', 'own1HouseRent': '130'	, 'own2HouseRent':'390'		, 'own3HouseRent': '900'	, 'own4HouseRent': '1100'	, 'hotelRent': '1275'	, 'mortgaged': '0', 'mortgageValue': '150', 	'houseCost': '200'},
				35: {'estateName': 'Pennsylvania Ave.'     	,'price': '320' 	,'rent': '28', 	'group': '6'	,'available': '1' , 	'ownerNumber': '-1', 	'houses': '0',	'hotel': '0', 'monopoly': '0', 'own1HouseRent': '150'	, 'own2HouseRent':'450'		, 'own3HouseRent': '1000'	, 'own4HouseRent': '1200'	, 'hotelRent': '1400'	, 'mortgaged': '0', 'mortgageValue': '160', 	'houseCost': '200'},
				38: {'estateName': 'Park Place'            	,'price': '350' 	,'rent': '35', 	'group': '7'	,'available': '1' , 	'ownerNumber': '-1', 	'houses': '0',	'hotel': '0', 'monopoly': '0', 'own1HouseRent': '175'	, 'own2HouseRent':'500'		, 'own3HouseRent': '1100'	, 'own4HouseRent': '1300'	, 'hotelRent': '1500'	, 'mortgaged': '0', 'mortgageValue': '175', 	'houseCost': '200'},
				40: {'estateName': 'Boardwalk'					,'price': '400'		,'rent': '50', 	'group': '7'	,'available': '1' ,		'ownerNumber': '-1',	'houses': '0',	'hotel': '0', 'monopoly': '0',	'own1HouseRent': '200'	, 'own2HouseRent': '600'	, 'own3HouseRent': '1400'	, 'own4HouseRent': '1700'	, 'hotelRent': '2000'	, 'mortgaged': '0', 'mortgageValue': '200', 	'houseCost': '200'},
				13: {'estateName': 'Electric Company'			,'price': '150' 	,'rent': '0', 	'group': '8'	,'available': '1' , 	'ownerNumber': '-1', 	'houses': '0',	'hotel': '0', 'monopoly': '0', 'own1HouseRent': '0'	, 'own2HouseRent':'0'		, 'own3HouseRent': '0'		, 'own4HouseRent': '0'		, 'hotelRent': '0'		, 'mortgaged': '0', 'mortgageValue': '75', 	'houseCost': '0'},
				29: {'estateName': 'Water Works'				,'price': '150' 	,'rent': '0', 	'group': '8'	,'available': '1' , 	'ownerNumber': '-1', 	'houses': '0',	'hotel': '0', 'monopoly': '0', 'own1HouseRent': '0'	, 'own2HouseRent':'0'		, 'own3HouseRent': '0'		, 'own4HouseRent': '0'		, 'hotelRent': '0'		, 'mortgaged': '0', 'mortgageValue': '75', 	'houseCost': '0'},
				6: 	{'estateName': 'Reading Railroad'			,'price': '200' 	,'rent': '0', 	'group': '9'	    ,'available': '1' , 	'ownerNumber': '-1', 	'houses': '0',	'hotel': '0', 'monopoly': '0', 'own1HouseRent': '0'	, 'own2HouseRent':'0'		, 'own3HouseRent': '0'		, 'own4HouseRent': '0'		, 'hotelRent': '0'		, 'mortgaged': '0', 'mortgageValue': '100', 	'houseCost': '0'},
				16: {'estateName': 'Pennsylvania Railroad'		,'price': '200' 	,'rent': '0', 	'group': '9'	    ,'available': '1' , 	'ownerNumber': '-1', 	'houses': '0',	'hotel': '0', 'monopoly': '0', 'own1HouseRent': '0'	, 'own2HouseRent':'0'		, 'own3HouseRent': '0'		, 'own4HouseRent': '0'		, 'hotelRent': '0'		, 'mortgaged': '0', 'mortgageValue': '100', 	'houseCost': '0'},
				26: {'estateName': 'B. & O. Railroad'			,'price': '200' 	,'rent': '0', 	'group': '9'	    ,'available': '1' , 	'ownerNumber': '-1', 	'houses': '0',	'hotel': '0', 'monopoly': '0', 'own1HouseRent': '0'	, 'own2HouseRent':'0'		, 'own3HouseRent': '0'		, 'own4HouseRent': '0'		, 'hotelRent': '0'		, 'mortgaged': '0', 'mortgageValue': '100', 	'houseCost': '0'},
				36: {'estateName': 'Short Line Railroad'		,'price': '200' 	,'rent': '0', 	'group': '9'	    ,'available': '1' , 	'ownerNumber': '-1', 	'houses': '0',	'hotel': '0', 'monopoly': '0', 'own1HouseRent': '0'	, 'own2HouseRent':'0'		, 'own3HouseRent': '0'		, 'own4HouseRent': '0'		, 'hotelRent': '0'		, 'mortgaged': '0', 'mortgageValue': '100', 	'houseCost': '0'}
          	}
          	
# #these lines are to test 	
# print(EstateDict[2]['estateName'])
# print(EstateDict[4]['estateName'])
# print(EstateDict[7]['estateName'])
