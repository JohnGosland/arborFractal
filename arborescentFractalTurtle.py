import turtle
MIN_BRANCH_LENGTH = 1
#Recrusive drawing function. Does most of the work. 
def construct_tree(turtle, current_branch_length, shorting_length, angle_from_parent):
    #Base Case ----------------------------------
    if MIN_BRANCH_LENGTH < current_branch_length:
    #--------------------------------------------
        #Recursive Work
        turtle.forward(current_branch_length)
        new_length = current_branch_length - shorting_length
        
        #Left Recurse 
        turtle.left(angle_from_parent)
        construct_tree(turtle, new_length, shorting_length, angle_from_parent)

        #Right Recurse
        turtle.right(2 * angle_from_parent)
            #Doubling the angle and adding it to its negative angle (moving left) results
            #in the postive value of angle (moving right)
        construct_tree(turtle, new_length, shorting_length, angle_from_parent)

        #Backward Recurse
        turtle.left(angle_from_parent)
            #Moving left (-1 angle) from the previous position (postive 1 angle)
            # results in being at your inital starting position
        turtle.backward(current_branch_length)
            #This (out of expediance) redraws over itself to get back to the inital position

#Initialize Turtle 
screen = turtle.Screen()
turtle.speed(speed = 0)

#Starts the inital position for the Turtle
#This also disables screen refreshing until turtle.update is called
#greatly improving performance.
turtle.tracer(0,0)

for x in range(4):

    #Set Tree Color Per Interation
    if x == 1 or x== 3:
        turtle.pencolor('orange')
    else:
        turtle.pencolor('black')
    #Rotate Starting position of fractal
    turtle.setheading(90 + x * 90)
    
    #Construct Fractal
    turtle.pendown()
    construct_tree(turtle, 50, 3, 15)
    turtle.penup()
    turtle.setpos(0,0)

#The turtle object holds within it the pathing of the sum of all the fractals.
turtle.hideturtle()
turtle.update()

#Stops the console from closing 
input("Press Any Key To End The Program")
