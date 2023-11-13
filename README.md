# Fiction Express challenge 
Fiction Express technical assessment for the Backend Developer position.

## Installation

Create a Python virtual environment and activate it:

    python -m venv .env

Activation for Windows users:

    ./.env/Scripts/activate

Activation for Mac and Linux users:

    source .env/bin/activate

Once activated, we can go ahead and install the necessary dependencies:

    pip install -r requirements.txt

## Set up

Once the environment is activated and the requirements are installed, we should create a superuser that will have access to the Admin Panel. Execute the following:

    python manage.py createsuperuser

Now, we can start the server by running:

    python manage.py runserver


## Usage

We can now go ahead and visit the [login page](http://127.0.0.1:8000/posts/login/) to register a new user (regular for now).

Note that if you try to access the [home page](http://127.0.0.1:8000/posts/home/) and you're not logged in, you will be redirected to the mentioned login page.

Once registered, you will be able to see the list of posts, where you can access each of them to see their content and details. If a user is an Admin, a "Delete" button will be also visible.

To upgrade a regular user to admin, visit the [Admin Panel](http://127.0.0.1:8000/admin/), log in as the superuser we created before, navigate to the "Users" section, and select the one that you want to edit.
