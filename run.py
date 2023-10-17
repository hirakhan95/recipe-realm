"""
RUN
---

Run is the starting point of the code try following
command on terminal to run the code

python run.py
"""
from src.features import main_menu, login
from src.globals import StateVariables

if __name__ == "__main__":
    while True:
        state_variables = StateVariables()
        login(state_variables)
        main_menu(state_variables)
