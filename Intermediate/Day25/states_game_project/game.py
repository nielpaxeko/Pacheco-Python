from marker import Marker
import turtle
import pandas



# Starting values
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "states_game_project/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
marker = Marker()


# Get states
guessed_states = []
file = pandas.read_csv("states_game_project/50_states.csv")
states = file.state.tolist()

# Check answer
def check_answer(answer):
    if answer.title() in states and answer not in guessed_states:
        state_x = int(file.x[file.state == answer])
        state_y = int(file.y[file.state == answer])
        coordinates = (state_x, state_y)
        marker.write_state(answer, coordinates)
        state_info = {
            f"{answer}" : f"{coordinates}"
        }
        guessed_states.append(answer)
        

def give_remaining_states():
    missing_states = []
    for state in states:
        if state not in guessed_states:
            missing_states.append(state)
    misses = pandas.DataFrame(missing_states)
    misses.to_csv("states_game_project/missing_states.csv")
    print(f"You missed {len(missing_states)} states...")

game_over = False
while not game_over and len(guessed_states) < 50:
    answer = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="Enter a state's name")
    if answer == "exit":
        give_remaining_states()
        game_over = True
    else:
        check_answer(answer)
    
