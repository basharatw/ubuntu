#Example 15

#use the import functionality of argv
from sys import argv

#This will ask for the filename as an argument
script, filename = argv

#open the filename you passed as an argument and stored that in the variable TXT
txt = open(filename)

print "Here's your file %r:" % filename

#call read() on the txt variable
print txt.read()

txt.close()


print "Type the filename again:"
#Get the input 
file_again = raw_input("> ")
#store that in txt_again
txt_again = open(file_again)

#read it 
print txt_again.read()

txt_again.close()




