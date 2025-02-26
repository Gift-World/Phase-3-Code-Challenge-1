 # PYTHON FUNDAMENTALS COMPULSORY (Code Challenge 1)


## Description :
 - This repository has  a collection of Python functions and a `Car` class demonstrating various python programming fundamentals.

 ## Features
 This application has the following features.

 1. Basic arithmetic operation that adds two numbers and returns the correct value

 2. Checks if a number is even.
 3. Reverses a string changing its arrangement.
 4. Counts number of vowels in a string.
 5. Calculates the factorial of a number.
 6. Applies a decorator to a function.
 7. Sortes a list of tuples by age in ascending order.
 8. Merging two dictionaries.
 9 .Creating a simple Car class with attributes and methods


 ## Prerequisites
  - For easy usage, make sure you have the following:
   
   1. A reliable laptop or computer with at least 8GB RAM , core i5, 500GB HDD and stable internet access.
2. An Operating System preferably Linux or Windows 10+.
3. A text editor capable of running Python such as Visual Studio Code.
4. You have installed `Python 3.7 `or later.


## Installation

### Alternative One

To use this repo, follow these steps:

1. Open the terminal/CLI on your computer.
2. Clone this repository by running the following command:

        git@github.com:Gift-World/Phase-3-Code-Challenge-1.git

3. Change directory to the repo folder:

        cd Phase-3-Code-Challenge-1

4. Open it in your Text Editor by running the command:

        code  .




### Alternative Two

- On the top right corner of this page there is a button labelled Fork.

- Click on Fork to create a copy of the repository to your github account.

- Follow the process described in Alternative One above.


## Running the application

1. On Vs Code ternminal, run `pipenv install`

- This installs any required dependencies
2. Run the command `pipenv shell`

- This creates an active environment for the python programme.

### Usage
Here is how you can use some of the application features.

##### TASK 1
        print(add_numbers(5, 5)) #output will be 10

#### TASK 2 
        print(is_even(14))  # Output: True

#### TASK 3 
        print(reverse_string("hello"))  # Output will be "olleh"

#### TASK 4
        print(count_vowels("hello"))  # Output will be: 2

#### TASK 7
        list = [('Angila', 30), ('Charles', 25), ('Gift', 35)]
        sorted_list = sort_by_age(list)
        print(sorted_list) # Output: [('Charles', 25), ('Angila', 30), ('Gift', 35)]

#### TASK 8 
        d1={'a': 2, 'b': 3, 'c': 5}
        d2={'b': 7, 'c': 1, 'd': 4}
        merged = merge_dicts(d1, d2 )
        print(merged)  # Output will be: {'a': 2, 'b': 10, 'c': 6, 'd': 4}


#### TASK 9
        car = Car("Toyota", "Camry", 2022)
        car.display_info()
        # Output will be :Toyota, Camry ,2022   

## Author
 - Charles Gift           




        
 