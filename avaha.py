import turtle

# Ініціалізація вікна turtle
window = turtle.Screen()
window.bgcolor("white")

# Ініціалізація черепашки
star = turtle.Turtle()
star.color("purple")
star.speed(3)

# Функція для малювання зірки
def draw_star():
    star.begin_fill()
    for _ in range(5):
        star.forward(100)
        star.right(144)
    star.end_fill()

# Малюємо першу зірку
draw_star()

# Переміщуємо черепашку для другої зірки
star.penup()
star.goto(200, 0)
star.pendown()

# Малюємо другу зірку
draw_star()

# Переміщуємо черепашку для третьої зірки
star.penup()
star.goto(-200, 0)
star.pendown()

# Малюємо третю зірку
draw_star()

# Закриваємо вікно при кліку на нього
turtle.done()

print("avaha said - HI!")
