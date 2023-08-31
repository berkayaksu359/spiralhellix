import turtle

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("light blue")
turtle_screen.title("spiralhellix")
turtle.speed(1)

turtle_instance = turtle.Turtle()
# sekiz çizebiliriz bu şekilde basit bir animasyon
'''
turtle.circle(100)
turtle.circle(-100)
'''
#basit bir 8 animasyonu yapabiliriz
'''
for i in range(10):
    turtle_instance.circle(10 * i)
    turtle_instance.circle(-10 * i)
'''
'''
#sola yatkın 8
for i in range(10):
    turtle_instance.circle(10 * i)
    turtle_instance.circle(-10 * i)
    turtle_instance.left(i)
'''

#karıık bir şekilde listedeki renkleri atayıp gökkuşağı gibi bir 8 çizebiliriz
turtle_colors = ["red","blue","yellow","black","gray","orange","cyan"]


for i in range(10):
    turtle_instance.color(turtle_colors[i % 6])
    turtle_instance.circle(10 * i)
    turtle_instance.circle(-10 * i)

turtle.done()