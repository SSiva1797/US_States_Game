import turtle
import pandas

FONT = ("Courier", 8, "normal")

screen = turtle.Screen()
screen.setup(width=720, height=500)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("50_states.csv")
all_states = data["state"].tolist()
guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="what's another state's name?").title()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]

        states_to_learn_df = pandas.DataFrame(missing_states)
        states_to_learn_df.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        if answer_state not in guessed_states:
            guessed_states.append(answer_state)

            state_name = turtle.Turtle()
            state_name.penup()
            state_name.hideturtle()
            x_pos = (int(data[data.state == answer_state].x))
            y_pos = (int(data[data.state == answer_state].y))
            state_name.goto(x_pos, y_pos)
            state_name.write(answer_state, font=FONT)
