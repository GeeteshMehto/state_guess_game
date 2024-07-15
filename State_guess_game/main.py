import pandas as pd
import turtle



data = pd.read_csv("50_states.csv")
no_of_states = len(data["state"])
name_of_state = data.state.to_list()

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

is_game_on = True
right_guess = 0
guessed_state = []

while is_game_on or len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{right_guess}/{no_of_states} States correct", prompt="What,s "
                                                                                                 "another "
                                                                                                 "state's"
                                                                                                 " name?").title()

    if answer_state in name_of_state:
        if right_guess >= 50:
            is_game_on = False
            print("You won the game all the guesses are right")

        else:
            guessed_state.append(answer_state)
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_data = data[data.state == answer_state]
            t.goto(int(state_data.x), int(state_data.y))
            t.write(answer_state)
            right_guess += 1

    elif answer_state == "Exit":
        missing_states = []
        for state in name_of_state:
            if state not in guessed_state:
                missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    else:
        pass
