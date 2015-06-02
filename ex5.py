#Example 5

name = 'Basharat B Wani'
age = 42 # not a lie
height = 74 # inches
weight = 140 # lbs
eyes = 'Black'
teeth = 'White'
hair = 'Dark Black'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    age, height, weight, age + height + weight)
test = age+height+weight

print "Age + Height + Weight = %d " % test


