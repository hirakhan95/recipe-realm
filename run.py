from src.features import main_menu, login
from src.globals import StateVariables

if __name__ == "__main__":
    state_variables = StateVariables()
    login(state_variables)
    main_menu(state_variables)
