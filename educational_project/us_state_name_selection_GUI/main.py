import turtle
import pandas

my_screen = turtle.Screen()
my_screen.title("U.S.State name selection")
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

data = pandas.read_csv("./50_states.csv")
all_states = data.state.to_list()
guess_state = []
while len(guess_state) <= 50:
    answer_state = turtle.textinput(title="Guess the state name, enter 'exit' to leave",
                                    prompt=f"Correct guess {50 - len(guess_state)}/50").title()
    if answer_state == 'Exit':
        states_to_learn = []
        for state in all_states:
            if state not in guess_state:
                states_to_learn.append(state)
        new_file = pandas.DataFrame(states_to_learn)
        new_file.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        guess_state.append(answer_state)
        tim = turtle.Turtle()
        tim.hideturtle()
        tim.penup()
        state_check = data[data.state == answer_state]
        tim.goto(int(state_check.x), int(state_check.y))
        tim.write(answer_state)

