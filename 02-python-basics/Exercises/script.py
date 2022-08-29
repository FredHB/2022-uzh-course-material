from pipe import dedup, where, select, sort
print('\n')

# make a disctionary
phil_names = {'Marx' : 'Karl', 'Wittgenstein' : 'Ludwig', 'Sen' : 'Amartya'} 
phil_names['Hume'] = 'David'
phil_names['Wittgenstein'] = 'Ludwig von'
econ_names = {'Becker' : 'Gary', 'Heckman' : 'James J.'}

names = phil_names.copy()
names.update(econ_names)
del names['Heckman']
for str in names.values() : print(str)

print('\n', 'Marx' in names, '\n')

print([3,2,5,66, 66, 12] 
	| dedup
	| where(lambda x : x % 2 == 1)
	| select(lambda x : x**2)
	| sort
	, '\n')

recession = False
if recession:
	print('booh!')
else :
	print('yayy!')

print('\n')

color = 'gray'
if color == 'red' : 
	print('It\'s a tomato')
elif color == 'green' :
	print('It\'s a cucumber')
else :
	print('It\'s concrete')

x = 1
list = []
while x < 12 :
	list.append(x)
	x +=1

print(list,'\n')

#while True:
#	string = input('String to capitalize (type q to quit)')
#	if string == 'q' : break
#	print(string.capitalize())

yips = range(1,4)
zips = range(1,4)
anthrlst = [(yip, zip) for yip in yips for zip in zips]
for yip, zip in anthrlst : print(yip, zip)

import sys
for place in sys.path: print(place)