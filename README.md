
# Recipe Realm

Recipe Realm is a Python terminal application that operates within the mock terminal of Heroku. Users can effectively 
manage recipes by viewing others', creating their own, updating them, and deleting them according to their specific 
needs. 

A hierarchical structure is maintained wherein only the admin has the privileges to perform all functionalities.
However, if the user is not an admin, they can only modify or delete their own recipes, ensuring the integrity of other 
users' recipes.

![demo](./assets/images/all-devices-white.png)

Credentials for admin is as follows:

- Name: admin
- Password: RecipeRealm

## How to Use

Recipe Organizer offers a simple and intuitive interface to organize your recipes.

1. **List Recipes**: View all the recipes in one place.
2. **Create Recipe**: Add a new recipe, complete with recipe name, ingredients and preparation.
3. **Update Recipe**: Want to change something in existing dish? Easily modify any part of your recipe.
4. **Delete Recipe**: Clear out recipes you no longer need with just one click.

## Features

### Login Page
- Description of the application is available on this page
- user can enter here their name

![list](./assets/images/login.png)

### Main Menu
- Main menu where user can go to whatever option they want to go
- user can also press E to end the application

![list](./assets/images/menu.png)

### List Recipes
- Browse through all the dishes.
- Simply enter the number to quickly see the recipe of your desired dish.
  
![list](./assets/images/list.png)

### Create Recipe
- Add recipe name, ingredients, and detailed cooking steps.
- Your recipe will be automatically saved.

![list](./assets/images/create.png)

### Update Recipe
- Edit any part of the recipe, whether it's the name of the recipe, ingredients, or the cooking process.

![list](./assets/images/update.png)

### Delete Recipe
- A simple one-click process to remove unwanted recipe.

![list](./assets/images/delete.png)

## Testing

Extensive testing ensures a seamless experience:

- Manual testing of each feature for functionality and user experience in my terminal and Code Institute Heroku terminal.
- Conducted user tests to gather feedback and further refine the application.
- Passed the code through PEP8 Linter and confirmed there are no problems.

## Bugs

### Solved Bugs
- Update function was not callable. I explicitly imported update recipe function in menu.py

## Remaining Bugs
- No bugs remaining

## Deployment
The project was deployed on Github. The following steps were taken for deployment:

- Add dependencies to requirements.txt file with command "pip3 freeze > requirements.txt"
- Commit and push to GitHub
- Go to the Heroku Dashboard
- Click "Create new app"
- Name app and select location
- Add Config Vars for Creds and Port in Settings tab
- Add the buildbacks to Python and NodeJS in respective order
- Select appropriate deployment method, GitHub
- Connect to Github and link to repository
- Enable automatic deployment and/or deploy manually
- Click on Deploy

## Credits

- All the culinary enthusiasts for their valuable feedback.
- Code institute Love Sandwich's walk through project for step by step explanation.
- Various online free resources to have the idea of the project.
- Gencraft.com for the background image.

