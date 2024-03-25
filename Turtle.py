
import turtle 
t = turtle. Turtle()
s = turtle. Screen()

def design_heart():
           s.bgcolor('white')
           t.hideturtle()
           t.goto(0,-10)

           t.pensize(3)
           t.color('red')
           t.begin_fill()
           t.left(140)
           t.forward(180)
           t.circle(-90,200)
           t.setheading(60)
           t.circle(-90,200)
           t.forward(178)
           t.end_fill()

           t.penup()
           t.goto(-75,130)
           t.pendown()
           t.color('white')

           t.write("Hello",font=("Verdana",40,"bold"))

def write_text():
         t.penup()
         t.goto(0, -250)
         t.pendown()
         t.pencolor("black")
         t.write("Every great journey starts with a single step.\n",align="center",font=("MS Serif",18,"bold"))
         t.write("Keep it Short & Simple",align="center",font=("MS Serif",18,"bold"))
def main():
        turtle.speed(0)
        design_heart()
        write_text()
        
if __name__=="__main__":
        main()
turtle.done()
 

