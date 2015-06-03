#Exampln.

#\t is tabbed
tabby_cat = "\t\tI'm tabbed in."

#\n means start on  next line 
persian_cat = "I'm split\non a line."

#\\ means \ backslash
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat

print backslash_cat
print fat_cat

fat_catII = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''
print fat_catII

while True:
    for i in ["/","-","|","\\","|"]:
        print "%s\r" % i,


