"""
Author: Christina Elmore
Section Number: 02
RIN: 661542904
Assignment: HW 3 Part 2
Purpose: Track the position of a turtle moving on a grid.
"""
def step(x, y, direction): #turns the turtle 90 degrees counter-clockwise from the given direction or lets it move a given number of steps in that direction.
    choice = raw_input("Step choice (turn or walk) => ")
    print choice
    if choice.lower() == "turn":
            
        if direction == "right":
            direction = "down"
                        
        elif direction == "left":
            direction = "up"
                
        elif direction == "up":
            direction = "right"
            
        elif direction == "down":
            direction = "left"
                           
    elif choice.lower() == "walk":
        distance = int(raw_input("Number of steps => "))
        print distance
            
        if direction == "up":
            y = y - distance
                
                
        elif direction == "down":
            y = y + distance
        
                
        elif direction == "left":
            x = x - distance
            
                
        elif direction == "right":
            x = x + distance
                  
    else:
        print "Illegal step choice."
    return [x, y, direction]

turtle = [100, 100, "right"]
turtle_x = [turtle[0]]
turtle_y = [turtle[1]]
i = 1
while i < 7:
    turtle = step(turtle[0], turtle[1], turtle[2])
    turtle_x.append(turtle[0])
    turtle_y.append(turtle[1])
    i += 1
    if i == 4:
        print "After three steps: position (%d,%d), direction %s" %(turtle[0], turtle[1], turtle[2])
    if i == 7:
        print "After six steps: position (%d,%d), direction %s" %(turtle[0], turtle[1], turtle[2])
print "Min x %d" %min(turtle_x)
print "Min y %d" %min(turtle_y)
print "Max x %d" %max(turtle_x)
print "Max y %d" %max(turtle_y)