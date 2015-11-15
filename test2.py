import re

print(re.sub('[^a-zA-Z0-9-/-:-,-`-? \n\.\!\@\#\$\%\^\&\*\(\)\-\'\"\<\>]', '', "Look at me!"))