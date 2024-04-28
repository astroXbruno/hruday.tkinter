import turtle
import tkinter as tk
import random

screen = turtle.Screen()
screen.title("Snake Game")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "stop"

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []
score = 0
game_running = False
speed_level = 0.1 # Default speed (medium)

game_over_text = turtle.Turtle()
game_over_text.speed(0)
game_over_text.color("white")
game_over_text.penup()
game_over_text.hideturtle()
game_over_text.goto(0, 0)

def start_game():
    global game_running, game_over_text
    game_running = True
    game_over_text.clear()
    main_game_loop()

def pause_game():
    global game_running
    game_running = False

def restart_game():
    global score, segments, game_running, game_over_text
    game_over_text.clear()
    score = 0
    score_display.clear()
    score_display.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))
    head.goto(0, 0)
    head.direction = "stop"
    for segment in segments:
        segment.goto(1000, 1000)
    segments.clear()
    spawn_food()
    start_game()


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def spawn_food():
    x = random.randint(-14, 14) * 20
    y = random.randint(-14, 14) * 20
    food.goto(x, y)

def check_collision():
    for segment in segments:
        if segment.distance(head) < 20:
            return True
    return False

def update_score():
    global score
    score += 1
    score_display.clear()
    score_display.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))

def move_segments():
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

def check_border_collision():
    if (
        head.xcor() >= 290
        or head.xcor() <= -290
        or head.ycor() >= 290
        or head.ycor() <= -290
    ):
        game_over()
        return True
    return False

def game_over():
    global score, game_running, game_over_text
    screen.update()
    game_running = False
    game_over_text.write(f"Game Over! Your Score: {score}", align="center", font=("Courier", 24, "normal"))

def handle_food_collision():
    global score
    if head.distance(food) < 20:
        spawn_food()
        update_score()
        segment = turtle.Turtle()
        segment.speed(0)
        segment.shape("square")
        segment.color("grey")
        segment.penup()
        segments.append(segment)

def main_game_loop():
    global score
    screen.update()

    if not game_running:
        screen.ontimer(main_game_loop, 100)
        return

    move()

    if check_collision() or check_border_collision():
        return

    move_segments()
    handle_food_collision()

    root.after(int(speed_level * 1000), main_game_loop)

screen.listen()

root = tk.Tk()
root.title("Snake Game Controls")

start_button = tk.Button(root, text="Start Game", command=start_game, width=10)
start_button.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

pause_button = tk.Button(root, text="Pause Game", command=pause_game, width=10)
pause_button.grid(row=0, column=2, padx=5, pady=5, sticky="ew")

restart_button = tk.Button(root, text="Restart Game", command=restart_game, width=10)
restart_button.grid(row=0, column=3, padx=5, pady=5, sticky="ew")


up_button = tk.Button(root, text="Up", command=go_up, width=10)
up_button.grid(row=2, column=2, padx=5, pady=5, sticky="ew")

down_button = tk.Button(root, text="Down", command=go_down, width=10)
down_button.grid(row=3, column=2, padx=5, pady=5, sticky="ew")

left_button = tk.Button(root, text="Left", command=go_left, width=10)
left_button.grid(row=3, column=1, padx=5, pady=5, sticky="ew")

right_button = tk.Button(root, text="Right", command=go_right, width=10)
right_button.grid(row=3, column=3, padx=5, pady=5, sticky="ew")

score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Score: 0", align="center", font=("Courier", 24, "normal"))

root.mainloop()
