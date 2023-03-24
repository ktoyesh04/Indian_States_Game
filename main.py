import pandas as pd
import turtle as t
from time import sleep

screen = t.Screen()
screen.addshape("overhead\map.gif")
screen.title("Indian States")
t.shape("overhead\map.gif")

num_guesses = 0
prev_guesses = []

data = pd.read_csv("states.csv")
states = data["states"].to_list()

tim = t.Turtle()
tim.hideturtle()
tim.penup()
tim.speed("slow")
tim.goto(36.0, 244.0)
tim.write("NCT: National Capital Territory\nS:   State\nUT:  Union Territory", False, font=("courier", 9, "italic"))

while True:
    answer = t.textinput(f"Guess State {num_guesses}/36", "Enter State: ").title()
    codes = {" And": " and", "(Nct": "(NCT", "(Ut":"(UT"}
    for key in codes:
        answer = answer.replace(key, codes[key])
    print(answer)
    if answer == "Exit":
        missed_states = [state for state in states if state not in prev_guesses]
        pd.DataFrame(missed_states).to_csv("missed_states")
        break

    if answer not in prev_guesses and answer in states:
        num_guesses += 1
        prev_guesses.append(answer)
        row = data[data["states"] == answer]
        tim.goto(float(row.x), float(row.y))
        tim.write(answer, font=("arial",8 ,"bold"))
        sleep(0.1)

    if num_guesses == 36:
        break

screen.exitonclick()
