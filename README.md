# AirBnB_clone
- This is a miniture version of the Airbnb website that uses
the console as the main point interaction with the User(frontend)

- 'frontend' - console: cmd module

- 'Backend' - python OOP concepts

- 'Database' - file storage: JSON module

- 'Testing' - unitest module
_ 'pycodestyle' - version 2.8.*


# project structure
'''bash

├── AUTHORS
├── console.py
├── __init__.py
├── models
│   ├── amenity.py
│   ├── base_model.py
│   ├── city.py
│   ├── engine
│   │   ├── file_storage.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── file_storage.cpython-310.pyc
│   │       ├── file_storage.cpython-311.pyc
│   │       ├── __init__.cpython-310.pyc
│   │       └── __init__.cpython-311.pyc
│   ├── __init__.py
│   ├── place.py
│   ├── __pycache__
│   │   ├── amenity.cpython-310.pyc
│   │   ├── amenity.cpython-311.pyc
│   │   ├── base_model.cpython-310.pyc
│   │   ├── base_model.cpython-311.pyc
│   │   ├── city.cpython-310.pyc
│   │   ├── city.cpython-311.pyc
│   │   ├── __init__.cpython-310.pyc
│   │   ├── __init__.cpython-311.pyc
│   │   ├── place.cpython-310.pyc
│   │   ├── place.cpython-311.pyc
│   │   ├── review.cpython-310.pyc
│   │   ├── review.cpython-311.pyc
│   │   ├── state.cpython-310.pyc
│   │   ├── state.cpython-311.pyc
│   │   ├── user.cpython-310.pyc
│   │   └── user.cpython-311.pyc
│   ├── review.py
│   ├── state.py
│   └── user.py
├── __pycache__
│   ├── console.cpython-310.pyc
│   ├── console.cpython-311.pyc
│   └── test_base_mode.cpython-311.pyc
├── README.md
└── tests
    ├── __init__.py
    ├── __pycache__
    │   ├── __init__.cpython-310.pyc
    │   ├── __init__.cpython-311.pyc
    │   ├── test_base_mode.cpython-310.pyc
    │   ├── test_base_model.cpython-310.pyc
    │   ├── test_base_model_dict.cpython-310.pyc
    │   ├── test_console.cpython-310.pyc
    │   ├── test_console.cpython-311.pyc
    │   └── test_save_reload_base_model.cpython-310.pyc
    ├── test_console.py
    ├── test_models
    │   ├── __pycache__
    │   │   └── test_user.cpython-311.pyc
    │   ├── test_amenity.py
    │   ├── test_city.py
    │   ├── test_place.py
    │   ├── test_review.py
    │   ├── test_state.py
    │   └── test_user.py
    └── ~.vimrc



'''

- 'console,py' - this is the entry point of our
  program(where to use 'if __name__=="__main__")'

- 'models/' - contains all classes used for the entire project


- 'base_model' - This is the parent class and contains elements common to all other classes:
    ## attributes;
        'id':
        'created_at':
        'updated_at':
   ## methods;
        'save():'
        'to_json()':

- '__init__()' : this is  a magic method that converts our module to a package.

- 'engine/' - contains all storage classes


-'tests/' - Contains all our test files with the 'test_' prefix


# How to use:

# Examples:
