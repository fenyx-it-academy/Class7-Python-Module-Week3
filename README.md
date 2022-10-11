# Week3-homework
Create an API function:

    Import necessary library for making an API call.
    Make the API call to this URL -> http://jsonplaceholder.typicode.com/users
    Check the status code, return object (res.json())
    Wrap the API function in try/except block.
    Return the return object.

Create a cleanup function:

    Take the return object as parameter and transform the return object. (Before starting with transforming this return object, check its data type as it may not be a dictionary. Plan your code according to its data type)
    Create a new Python dictionary containing all 10 users and their details from the return object. (Items to be included: id, name, username, email)
    Return the Python dictionary

Creata a function to write the users dictionary to a .json file:

    Take a dictionary as the parameter
    Open up a new file (or create if it isn't existing)
    Dump the Python dictionary into this file

Create a main.py file:

    Import all your modules
    Create the main app logic here

Things to remember:

    Use a virtual environment.
    Create separate functions for all the steps.
    Modularize your code (either create a separate file for each function or create a file called utils.py and store all the functions in this file)
    Wrap the necessary parts of your functions in try/except blocks.
    Create a requirements.txt file at the end of your project to store all the dependancy information. (pip freeze > requirements.txt)
