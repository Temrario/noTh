import turtle

# Ініціалізація вікна turtle
window = turtle.Screen()
window.bgcolor("white")

# Ініціалізація черепашки
star = turtle.Turtle()
star.color("blue")
star.speed(3)

# Малюємо зірку
star.begin_fill()
for _ in range(5):
    star.forward(100)
    star.right(144)
star.end_fill()

# Закриваємо вікно при кліку на нього
turtle.done()


print("avaha said - HI!")
