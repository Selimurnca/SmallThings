import turtle
import random

grid_size = 25
#LAND AND BEAVER
land = turtle.Screen()
land.bgcolor("#008dfb")
land.title("Plane Catch")
#####################

#Timer
timer_writer = turtle.Turtle()
timer_writer.color("White")
timer_writer.hideturtle()
timer_writer.penup()
timer_writer.goto(-20,250)

times_up = True
def countdown():
    timer_writer.clear()
    global times_up
    global time_left
    if time_left > 0:
        timer_writer.write(f"Time: {time_left}", align="center", font=("Copperplate Gothic Bold", 20, "bold"))
        time_left -= 1
        turtle.ontimer(countdown, 1000)
    else:
        timer_writer.write("Time's up!", align="center", font=("Copperplate Gothic Bold", 30, "bold"))
        times_up = False
        congra()
time_left = 30

########################

#PLANE
plane = turtle.Turtle()
plane.color("White")
plane.penup()
plane.shapesize(2)
def move_beaver():
    if not times_up:
        return
    plane.hideturtle()
    x = random.randint(-8, 8) * grid_size
    y = random.randint(-8, 8) * grid_size
    plane.goto(x, y)
    turtle.ontimer(move_beaver, 1250)
    plane.showturtle()



#Score
skor = 0

score_write = turtle.Turtle()
score_write.hideturtle()
score_write.penup()
score_write.goto(-250,250)
score_write.color("white")

def scoreup(x,y):
    global time_left
    global times_up
    global skor
    if times_up:
        skor +=1
        skorup()

def skorup():
    global time_left
    global times_up
    global skor
    if times_up:
        score_write.clear()
        score_write.write(f"Skor: {skor}", align="center", font=("Copperplate Gothic Bold", 20, "bold"))
    else:
        times_up = False
###################################
end = turtle.Turtle()
end.color("white")
end.hideturtle()
end.penup()
end.goto(0,0)
def congra():
    global times_up
    global time_left
    if time_left == 0:
        end.write("CONGRATULATIONS",align="center",font=("Copperplate Gothic Bold",40, "bold"))




#Funcitons
skorup()
countdown()
move_beaver()
plane.onclick(scoreup)


#GameDone
turtle.mainloop()
