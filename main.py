import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game by Required")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


states = pandas.read_csv("50_states.csv")
states_in_list = states["state"].to_list()
guessed_states = []

while len(guessed_states) < 50:
    user_answer = turtle.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="Enter name of State").title()
                                   
    if user_answer == "Exit":
        break

    states_to_learn = []
    for state in states_in_list:
        if state not in guessed_states:
            states_to_learn.append(state)

    df = pandas.DataFrame(states_to_learn)
    df.to_csv("states_to_learnt.csv")
    
    if user_answer in states_in_list:
        guessed_states.append(user_answer)
        t = turtle.Turtle()
        t.shape("turtle")
        t.penup()
        t.hideturtle()
        state_data = states[states["state"] == user_answer]
        t.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))
        t.write(user_answer)
