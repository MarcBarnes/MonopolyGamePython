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
# 	estateName
# 	available (1 if available, 0 if it is owned)
# 	ownerNumber (-1 if there is no owner)
# 	houses
# 	hotels
# 	position
# 	price
# 	rent
# 	group

#Should keep formatting of tabspacing for easy editing: **USE Insert button on keyboard when editing

EstateDict = {	2:  {'estateName': 'Mediterranean Ave.'		,	'price': '60'  	,'rent': '2' ,	'group': 'Purple'		,'available': '1' ,		'ownerNumber': '-1',	'houses': '0',	'hotels': '0'},
				4:  {'estateName': 'Baltic Ave.'            ,	'price': '60'  	,'rent': '4' ,	'group': 'Purple'		,'available': '1' , 	'ownerNumber': '-1', 	'houses': '0',	'hotels': '0'},
				7:  {'estateName': 'Oriental Ave.'          ,	'price': '100' 	,'rent': '6' ,	'group': 'Light-Blue' 	,'available': '1' , 	'ownerNumber': '-1', 	'houses': '0',	'hotels': '0'},
				9:  {'estateName': 'Vermont Ave.'           ,	'price': '100' 	,'rent': '6' ,	'group': 'Light-Blue' 	,'available': '1' , 	'ownerNumber': '-1', 	'houses': '0',	'hotels': '0'},
				10: {'estateName': 'Connecticut Ave.'       ,	'price': '120' 	,'rent': '8' ,	'group': 'Light-Blue' 	,'available': '1' , 	'ownerNumber': '-1', 	'houses': '0',	'hotels': '0'},
				12: {'estateName': 'St. Charles Place'     	,	'price': '140' 	,'rent': '10',	'group': 'Violet'		,'available': '1' , 	'ownerNumber': '-1', 	'houses': '0',	'hotels': '0'},
				14: {'estateName': 'States Ave.'           	,	'price': '140' 	,'rent': '10', 	'group': 'Violet'		,'available': '1' , 	'ownerNumber': '-1', 	'houses': '0',	'hotels': '0'},
				15: {'estateName': 'Virginia Ave.'         	,	'price': '160' 	,'rent': '12', 	'group': 'Violet'		,'available': '1' , 	'ownerNumber': '-1', 	'houses': '0',	'hotels': '0'},
				17: {'estateName': 'St. James Place'       	,	'price': '180' 	,'rent': '14', 	'group': 'Orange'		,'available': '1' , 	'ownerNumber': '-1', 	'houses': '0',	'hotels': '0'},
				19: {'estateName': 'Tennessee Ave.'        	,	'price': '180' 	,'rent': '14', 	'group': 'Orange'		,'available': '1' , 	'ownerNumber': '-1', 	'houses': '0',	'hotels': '0'},
				20: {'estateName': 'New York Ave.'         	,	'price': '200' 	,'rent': '16', 	'group': 'Orange'		,'available': '1' , 	'ownerNumber': '-1', 	'houses': '0',	'hotels': '0'},
				22: {'estateName': 'Kentucky Ave.'         	,	'price': '220' 	,'rent': '18', 	'group': 'Red'			,'available': '1' , 	'ownerNumber': '-1', 	'houses': '0',	'hotels': '0'},
				24: {'estateName': 'Indiana Ave.'          	,	'price': '220' 	,'rent': '18', 	'group': 'Red'			,'available': '1' , 	'ownerNumber': '-1', 	'houses': '0',	'hotels': '0'},
				25: {'estateName': 'Illinois Ave.'         	,	'price': '240' 	,'rent': '20', 	'group': 'Red'			,'available': '1' , 	'ownerNumber': '-1', 	'houses': '0',	'hotels': '0'},
				27: {'estateName': 'Atlantic Ave.'         	,	'price': '260' 	,'rent': '22', 	'group': 'Yellow'		,'available': '1' , 	'ownerNumber': '-1', 	'houses': '0',	'hotels': '0'},
				28: {'estateName': 'Ventnor Ave.'          	,	'price': '260' 	,'rent': '22', 	'group': 'Yellow'		,'available': '1' , 	'ownerNumber': '-1', 	'houses': '0',	'hotels': '0'},
				30: {'estateName': 'Marvin Gardens'        	,	'price': '280' 	,'rent': '24', 	'group': 'Yellow'		,'available': '1' , 	'ownerNumber': '-1', 	'houses': '0',	'hotels': '0'},
				32: {'estateName': 'Pacific Ave.'          	,	'price': '300' 	,'rent': '26', 	'group': 'Dark-Green'	,'available': '1' , 	'ownerNumber': '-1', 	'houses': '0',	'hotels': '0'},
				33: {'estateName': 'North Carolina Ave.'   	,	'price': '300' 	,'rent': '26', 	'group': 'Dark-Green'	,'available': '1' , 	'ownerNumber': '-1', 	'houses': '0',	'hotels': '0'},
				35: {'estateName': 'Pennsylvania Ave.'     	,	'price': '320' 	,'rent': '28', 	'group': 'Dark-Green'	,'available': '1' , 	'ownerNumber': '-1', 	'houses': '0',	'hotels': '0'},
				38: {'estateName': 'Park Place'            	,	'price': '350' 	,'rent': '35', 	'group': 'Dark-Blue'	,'available': '1' , 	'ownerNumber': '-1', 	'houses': '0',	'hotels': '0'},
				40: {'estateName': 'Boardwalk'				,	'price': '400' 	,'rent': '50', 	'group': 'Dark-Blue'	,'available': '1' , 	'ownerNumber': '-1', 	'houses': '0',	'hotels': '0'},
          	} 	
          	
# #these lines are to test 	
# print(EstateDict[2]['estateName'])
# print(EstateDict[4]['estateName'])
# print(EstateDict[7]['estateName'])
