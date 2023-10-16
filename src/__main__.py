from .features import login, main_menu
from .globals import StateVariables

if __name__ == "__main__":
    state_variables = StateVariables()
    login(state_variables)
    main_menu(state_variables)
