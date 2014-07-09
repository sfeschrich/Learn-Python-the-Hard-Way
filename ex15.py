#introduce argv command
from sys import argv

#define items in list as their own variables; first item will be called script, next item will be called filename
script, filename = argv

#new command for opening file (given filename)
txt = open(filename)

#take (filename) and insert in for %r; print file contents
print "Here's your file %r:" % filename
print txt.read()

#print script; request raw_input from user to type in same filename again
print "Type the filename again:"
file_again = raw_input("> ")

#reopen given filename
txt_again = open(file_again)

#print file contents
print txt_again.read()

