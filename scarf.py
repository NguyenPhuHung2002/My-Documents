#--------------------------------------------------
# Change these variables to design your own scarf!
# Add a comment describing what each variable does.
#--------------------------------------------------

#this variable...
colours = ['#','|']

#this variable...
colour_length = 1

#this variable...
pattern_length = 25

#this variable...
pattern_width = 10

#------------------------------------------------
# Don't change anything below this line!
#------------------------------------------------

print("Here is your scarf:\n")
for pos in range(int(pattern_width * pattern_length)):
    print( colours[ int((pos)/colour_length) % len(colours)], end="")
    if (pos % pattern_width) == pattern_width-1:
        print("")
