import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
answer = screen.textinput(title="Guess the state", prompt= "Can you guess another state?").title()
states = pandas.read_csv("50_states.csv")
states_names = states["state"]
states_names_list = states_names.to_list()
correct_guesses = []
# print(states_names_list)

# print(states_coor)
state = turtle.Turtle()
state.pu()
state.hideturtle()

while len(correct_guesses) < 50:
    if answer == "Exit":
        break
    for guess in states_names_list:
        if answer == guess and answer not in correct_guesses:
            correct_guesses.append(answer)
            state_coor = states[states.state == guess]
            state.goto(int(state_coor.x), int(state_coor["y"]))
            state.write(guess, "center")
    answer = screen.textinput(title=f"{len(correct_guesses)}/50 States Correct", prompt="Can you guess another state?").title()

not_answered = [state for state in states_names_list if state not in correct_guesses]

to_learn = pandas.DataFrame(not_answered)
to_learn.to_csv("To_Learn.csv")
# print(not_answered)
# print(len(not_answered))