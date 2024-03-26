import turtle 
t = turtle. Turtle()
def write_text():
         t.penup()
         t.goto(0, 25)
         t.pendown()
         t.pencolor("red")
         t.write("R.Sujitha Rasu.\n",align="center",font=("MS Serif",18,"bold"))
         t.write("Learning Something New❤️",align="center",font=("MS Serif",18,"bold"))
def main():
        turtle.speed(0)
        write_text()
        
        
if __name__=="__main__":
        main()
turtle.hideturtle()
turtle.done()

 

