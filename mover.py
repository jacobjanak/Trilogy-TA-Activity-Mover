# imports
import sys
import os
import shutil


############################################################################
### enter the path to your local copy of the FullStack-Lesson-Plans repo ###
############################################################################
instructorRepoPath = '/Users/jacobjanak/documents/code/trilogy/FullStack-Lesson-Plans'


# get destination and source of activity files
source = instructorRepoPath + '/01-Class-Content/'
destination = os.getcwd()


# ensure the correct amount of arguments were entered
if len(sys.argv) != 3:
    raise ValueError("\n\nTo run this file, follow this format:\n" +
        "python <file-path> <week-number> <activity-number>\n")


# get user inputs from command line arguments
args = {
    'week': sys.argv[1],
    'activity': sys.argv[2]
}


# make sure user input is a number
def validateIsInt(s):
    try:
        int(s)

    except ValueError:
        raise ValueError("\n\nYou typed '" + s + "' but an integer was expected.\n")


# make sure it's a one or two digit number
def validateNumberLength(s):
    if 2 < len(s) or len(s) < 1:
        raise ValueError("\n\nYou typed '" + s + "' but a one or two digit integer was expected.\n")


# make sure the users command line args match desired format
def validateUserInput(s):
    validateIsInt(s)
    validateNumberLength(s)


# validate user input
validateUserInput(args['week'])
validateUserInput(args['activity'])


# reformat week
def makeDoubleDigit(s):
    if len(s) == 1:
        return '0' + s

    else:
        return s

args['week'] = makeDoubleDigit(args['week'])
args['activity'] = makeDoubleDigit(args['activity'])


# function to find a file within a dir based on a string
def autocompleteFileName(dir, s):
    for fileName in os.listdir(dir):
        if fileName[:len(s)] == s:
            return fileName


# auto complete week for source
source = source + autocompleteFileName(source, args['week'])


# add activities dir to file path
source = source + '/01-Activities/'


# auto complete activity for source
source = source + autocompleteFileName(source, args['activity'])


# only get solved folder
source = source + '/Solved/'


# auto complete activity for the destination
destination = destination + '/' + autocompleteFileName(destination, args['activity'])


# move the file
shutil.move(source, destination)
