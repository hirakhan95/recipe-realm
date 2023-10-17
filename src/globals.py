import src.sheet_db as db


class StateVariables:

    def __init__(self):
        self.RECIPES = db.get_data('recipes')
        self.USER_NAME = None
        self.ADMIN_PASSWORD = 'RecipeRealm'
