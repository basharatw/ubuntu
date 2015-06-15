#Example 16

# From Packsge sys get argv
from sys import argv

#input is needed as a filename 
script, filename = argv


print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
# Open the file and stored it as an object in variable target and the file is opened in write mode
#target = open(filename, 'w')
target = open(filename, 'a')

#the is clear the content the file 
print "Truncating the file.  Goodbye!"
#target.truncate()

print "Now I'm going to ask you for three lines."

#take input and store them in vars
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."


#Now write them into the target which is object based on the input file
target.write("\n"+line1+"\n"+line2+"\n"+line3)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")



#close
print "And finally, we close it."
target.close()
test = open(filename)
print test.read()
test.close()



