# Artificial Intelligence Nanodegree
## Introductory Project: Diagonal Sudoku Solver

# Question 1 (Naked Twins)
Q: How do we use constraint propagation to solve the naked twins problem?  

The naked twins strategy identifies two squares in the same unit which both contain two digits that are the same (also known as twin pair). 

By eliminating the twin pair from all other squares in the unit(s), the naked twin strategy constraints that except from the naked twin squares no other squares can contain a twin digit. 

Taking the unit squares { 'A5': '26', 'A6': '26', ... }, as an example, we can conclude that 2 and 6 must be in A5 and A6, and we can therefore eliminate 2 and 6 from every other square in the A row unit. 

By repetitively applying the eliminate and naked_twins functions, we use constraint propagation to reduce the search space of our Sudoku puzzle. 


# Question 2 (Diagonal Sudoku)
Q: How do we use constraint propagation to solve the diagonal sudoku problem?  

The Diagonal Sudoku problem extends the Sudoku problem by introducing two additional diagonal units {A1, … , I9} and {I1, … , A9} with the same unit constraints as the regular Sudoku problem. 

To solve the Diagonal Sudoku we hence apply the same solution techniques of elimination, only_choice and naked_twins to the Sudoku puzzle in order to reduce the search space for finding a solution to the Diagonal Sudoku problem. 

### Install

This project requires **Python 3**.

We recommend students install [Anaconda](https://www.continuum.io/downloads), a pre-packaged Python distribution that contains all of the necessary libraries and software for this project. 
Please try using the environment we provided in the Anaconda lesson of the Nanodegree.

##### Optional: Pygame

Optionally, you can also install pygame if you want to see your visualization. If you've followed our instructions for setting up our conda environment, you should be all set.

If not, please see how to download pygame [here](http://www.pygame.org/download.shtml).

### Code

* `solution.py` - You'll fill this in as part of your solution.
* `solution_test.py` - Do not modify this. You can test your solution by running `python solution_test.py`.
* `PySudoku.py` - Do not modify this. This is code for visualizing your solution.
* `visualize.py` - Do not modify this. This is code for visualizing your solution.

### Visualizing

To visualize your solution, please only assign values to the values_dict using the ```assign_values``` function provided in solution.py

### Submission
Before submitting your solution to a reviewer, you are required to submit your project to Udacity's Project Assistant, which will provide some initial feedback.  

The setup is simple.  If you have not installed the client tool already, then you may do so with the command `pip install udacity-pa`.  

To submit your code to the project assistant, run `udacity submit` from within the top-level directory of this project.  You will be prompted for a username and password.  If you login using google or facebook, visit [this link](https://project-assistant.udacity.com/auth_tokens/jwt_login for alternate login instructions.

This process will create a zipfile in your top-level directory named sudoku-<id>.zip.  This is the file that you should submit to the Udacity reviews system.

