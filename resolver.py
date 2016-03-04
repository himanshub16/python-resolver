#!/usr/bin/python
#
# Author : Himanshu Shekhar < https://github.com/himanshushekharb16 >
# program to find if any python packages do not exist on a system
# this ensures that the python script do not fail because of missing modules

# It checks for all the files/source codes for required packages and then check whether they are installed in the system.

try:
	import sys, os
	import __main__ as main
except ImportError:
	print "The sys and os modules could not be loaded. Please check you python installation."
	exit(1)

print "Is this script in the required directory? (y/n) ", 
x = raw_input()

if not (x == "y" or x == "Y"):
	print "Make sure the above condition is satisfied!"
	exit(1)

'''filelist = ''
if not (x=="y" or x=="Y"):
	location = input("Enter the location of the directory : ")
	filelist = os.listdir(location)
	os.chdir(location)
else:
	filelist = os.listdir(os.getcwd()) 
'''

# get list of files
filelist = os.listdir(os.getcwd())
for file in filelist:
	if not(file.endswith('.py')):
		filelist.remove(file)
filelist.remove(main.__file__)

modulelist = list() # list of modules to be checked for
for file in filelist:
	f = open(file, 'r')
	print 'evaluating file ', file
	content = f.readlines()
	lines = list()
	for line in content:
		var = line.strip()
		if var.startswith('import'):
			tmp = var.replace('import','').split(',')
			for item in tmp:
				if 'as' in 'item':
					modulelist.append((item.split('as'))[0])
				else:
					modulelist.append(item.strip())
# now, we have the list of lines containing the import keyword
# the variable modulelist holds that

# removing duplicates from the list of modules obtained
modulelist = list(set(modulelist))

for modulename in modulelist:
	var = 'import ' + modulename
	try:
		exec var
	except ImportError:
		print '**"', var.replace('import',''), '" cannot be imported. **'
	else:
		print var.replace('import',''), 'imported successfully.'
		pass

print 'End of program. If you like it, you can star it at "https://github.com/himanshushekharb16/python-resolver/"'
print "Thanks for using! "
exit(0)