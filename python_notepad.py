def createFile(fileName):
	fileName = open(fileName+'.txt', 'w')
	print('''Write YOUR NOTES below and click enter for every NEW LINE
		NOTE: type DONE to the next line if you are finished writing your documents
		____________________________________________________________________________
		\n''')
	rangelimit = ['done', 'Done', 'DONE']
	userInput = ''
	while userInput not in rangelimit:
		userInput = input('.....')
		if userInput in rangelimit:
			continue
		fileName.write(userInput + "\n")
		if userInput in rangelimit:
			fileName.close()
			break

def addFile(filename):
	filename = open(filename+'.txt', 'a')
	print('''Write your NOTES below and click enter for every NEW LINE
		NOTE: type DONE to the next line if you are finished writing your documents''')
	rangelimit = ['done', 'Done', 'DONE']
	userInput = ''
	while userInput not in rangelimit:
		userInput = input('....')
		if userInput in rangelimit:
			continue
		filename.write(userInput + "\n")
		if userInput in rangelimit:
			filename.close()
			break
		else:
			continue
question = int(input('''
	CHOOSE FROM THE FOLLOWING
	1. Write and Create a New File
	2. Read from a File
	____________________________________________
	\n
	'''))

if question == 1:
	print()
	file = input('Enter the name of the file: ')
	createFile(file)
elif question == 2:
	print('''
		NOTE: please enter a valid file name
		''')
	file = input('Enter the name of the file: ')
	addFile(file)
else:
	print('Done')

