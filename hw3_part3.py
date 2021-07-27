"""
Author: Christina Elmore
Section Number: 02
RIN: 661542904
Assignment: HW 3 Part 3
Purpose: Create a frame with a name displayed diagonally twice with a frame character and filles it in with a background character.
"""
import sys

def input_check(frame, background): #Checks if the given inputs are valid, and ends the progeam if not.
    j = 0
    if len(frame) > 1:
        print "Error: need a single frame char."
        j =+ 1
    if len(background) > 1:
        print "Error: need a single background char."
        j += 1
    if j > 0:
        print "At least one error so quitting."
        sys.exit()

def framer(i, name, frame, background): #Prints a line of the framed name box
    x = len(name)
    if x/2*2 == x: #If x is even
        if i < (len(name)/2):
            print "%s %s%s %s%s %s%s" %(frame, (background + " ") * (i+1), name[i], (background + " ") * (len(name)-(2*i)-2), name[-(i+1)], (background + " ") * (i+1), frame)
        elif i == (len(name)/2):
            print "%s %s%s %s %s%s" %(frame, (background + " ") * (i), name[i-1], name[i], (background + " ") * (i), frame)
        else:
            print "%s %s%s %s%s %s%s" %(frame, (background + " ") * (len(name)-(i)), name[-(i+1)], (background + " ") * 2*(i-(len(name)/2)), name[i], (background + " ") * (len(name)-(i)), frame)       
        
    else: #If x is odd    
        if i < (len(name)/2):
            print "%s %s%s %s %s %s%s" %(frame, (background + " ") * (i+1), name[i], (background + " ") * (len(name)-(i * 2)-3) + background, name[-(i+1)], (background + " ") * (i+1), frame)
        elif i == (len(name)/2):
            print "%s %s%s %s%s" %(frame, (background + " ") * (i+1), name[i], (background + " ") * (i+1), frame)
        else:
            print "%s %s%s %s%s %s%s" %(frame, (background + " ") * (len(name)-(i)), name[-(i+1)], (background + " ") * 2*(i - len(name)/2 - 1) + (background + " "), name[i], (background + " ") * (len(name)-(i)), frame)        
                                 
          
        
    
name = raw_input("Enter the name => ")
print name
frame = raw_input("Enter the frame character => ")
print frame
background = raw_input("Enter the background character => ")
print background 
input_check(frame, background)

print ((frame + " ") * (len(name)+3)) + frame
print "%s %s%s" %(frame, (background + " ") * (len(name)+2), frame)

i = 0
while i < len(name):
    framer(i, name, frame, background)
    i +=1
    
print "%s %s%s" %(frame, (background + " ") * (len(name)+2), frame)
print ((frame + " ") * (len(name)+3)) + frame