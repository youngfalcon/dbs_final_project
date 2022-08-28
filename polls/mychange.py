#Run after : python3 manage.py inspectdb > polls/models.py
#Code taken from:
#https://stackoverflow.com/questions/5315379/automatic-solution-for-add-a-related-name-argument-to-the-definition-for-xxx

import fileinput
textToSearch = "models.DO_NOTHING"

_no_related_name_counter = 1000

with fileinput.FileInput('./models.py', inplace=True, backup='.bak') as file:
    for line in file:
        _no_related_name_counter += 1
        textToReplace = 'models.DO_NOTHING, related_name="%(class)s_{}"'.format(_no_related_name_counter)
        print(line.replace(textToSearch, textToReplace), end='')