import os
​
# Starts a loop.
# Prompts user for directory.
directory = ''
while directory != 'q':
	directory = input('\nEnter directory path, for Windows use double \\\ Enter "q" to quit: \n')
	if directory == 'q':
		exit()
	try:
		# Lists files in directory.
		list = os.listdir(directory)
		print('\nCurrent:')
		print(list)
		
		# Handles the renaming, finds files and folders with spaces and changes to underscores.
		[os.rename(os.path.join(directory, f), os.path.join(directory, f).replace(' ', '_').lower()) for f in os.listdir(directory)]
		
		# Lists files in the directory again.
		print('\nNew:')
		list = os.listdir(directory)
		print(list)
	except FileNotFoundError:
		print ('Invalid directory, try again!')
		pass
