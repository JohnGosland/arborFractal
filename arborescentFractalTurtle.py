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
        
        #Hide the Cursor Render default on turtle objects
        turtle.hideturtle()



#Initialize Turtle 
screen = turtle.Screen()
screen.bgcolor('black')
turtle.speed(speed = 0)
turtle.setheading(90)
turtle.pencolor('orange')


#Starts the inital position for the Turtle
#This also disables screen refreshing until turtle.update is called
#greatly improving performance.
turtle.tracer(0,0)

#Turtle is Down and Drawing
turtle.pendown()

#Inital Function Call
construct_tree(turtle, 50, 5, 15)

#The Turtle Object should hold within it all the pathing (The graph of the tree). 
#
turtle.update()


#Stops the console from closing
input("Press Any Key To End The Program")
