import turtle


def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        angles = [60, -120, 60, 0]
        for angle in angles:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)


def draw_koch_curve(order, size=300):
    window = turtle.Screen()
    window.bgcolor("black")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.color("white")
    t.goto(-size / 2, size / 3)
    t.pendown()

    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

    window.mainloop()


def main():
    level_of_recursion = int(input("Рівень рекурсії: "))
    draw_koch_curve(level_of_recursion)


if __name__ == "__main__":
    main()
