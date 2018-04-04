# imports
import sys
import os
import shutil


# enter the path to your local copy of the FullStack-Lesson-Plans repo
instructorRepoPath = '/Users/jacobjanak/documents/code/trilogy/FullStack-Lesson-Plans/'

# get destination and source of activity files
source = instructorRepoPath + '01-Class-Content/'
destination = os.getcwd()

# get user inputs from command line arguments
args = {
    'week': sys.argv[1],
    'activity': sys.argv[2]
}

# reformat week
if len(args['week']) == 1:
    args['week'] = '0' + args['week']
if len(args['activity']) == 1:
    args['activity'] = '0' + args['activity']

# if len of args is not right, break

# auto complete week
allWeeks = os.listdir(source)
for week in allWeeks:
    if week[:2] == args['week']:
        source = source + week
        break

# add activities dir to file path
source = source + '/01-Activities/'

# auto complete activity
allActivities = os.listdir(source)
for activity in allActivities:
    if activity[:2] == args['activity']:
        source = source + activity
        break

# only get solved folder
source = source + '/Solved/'

# auto complete activity for the destination
allActivities = os.listdir(destination)
for activity in allActivities:
    if activity[:2] == args['activity']:
        destination = destination + '/' + activity
        break

# move the file
shutil.move(source, destination)
