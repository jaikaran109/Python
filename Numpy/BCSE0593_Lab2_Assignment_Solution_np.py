
Open In Colab
Introduction to NumPy
NumPy is an essential Python library. TensorFlow and scikit-learn use NumPy arrays as inputs, and pandas and Matplotlib are built on top of NumPy. In this Introduction to NumPy, you’ll become a master wrangler of NumPy’s core object: arrays! Using data from New York City’s tree census, you’ll create, sort, filter, and update arrays. You’ll discover why NumPy is so efficient and use broadcasting and vectorization to make your NumPy code even faster. By the end, you’ll be using 3D arrays to alter a Claude Monet painting, and you’ll understand why such array alterations are essential tools for machine learning.

Understanding NumPy Arrays
Meet the incredible NumPy array! Learn how to create and change array shapes to suit your needs. Finally, discover NumPy’s many data types and how they contribute to speedy array operations.

Introducing arrays
Your first NumPy array Once you’re comfortable with NumPy, you’ll find yourself converting Python lists into NumPy arrays all the time for increased speed and access to NumPy’s excellent array methods.

sudoku_list is a Python list containing a sudoku game:


sudoku_list = [[0, 0, 4, 3, 0, 0, 2, 0, 9],
                [0, 0, 5, 0, 0, 9, 0, 0, 1],
                [0, 7, 0, 0, 6, 0, 0, 4, 3],
                [0, 0, 6, 0, 0, 2, 0, 8, 7],
                [1, 9, 0, 0, 0, 7, 4, 0, 0],
                [0, 5, 0, 0, 8, 3, 0, 0, 0],
                [6, 0, 0, 0, 0, 0, 1, 0, 5],
                [0, 0, 3, 5, 0, 8, 6, 9, 0],
                [0, 4, 2, 9, 1, 0, 3, 0, 0]]
     
You’re going to change sudoku_list into a NumPy array so you can practice with it in later, for example by creating a 4D array of sudoku games along with their solutions!

Import NumPy using its generally accepted alias.
Convert sudoku_list into a NumPy array called sudoku_array.
Print the class type() of sudoku_array to check that your code has worked properly.

# Import NumPy
import numpy as np

# Convert sudoku_list into an array
sudoku_array = np.array(sudoku_list)

# Print the type of sudoku_array
print(sudoku_array)
print("Sudoku Array:\n", sudoku_array)
     
[[0 0 4 3 0 0 2 0 9]
 [0 0 5 0 0 9 0 0 1]
 [0 7 0 0 6 0 0 4 3]
 [0 0 6 0 0 2 0 8 7]
 [1 9 0 0 0 7 4 0 0]
 [0 5 0 0 8 3 0 0 0]
 [6 0 0 0 0 0 1 0 5]
 [0 0 3 5 0 8 6 9 0]
 [0 4 2 9 1 0 3 0 0]]
Sudoku Array:
 [[0 0 4 3 0 0 2 0 9]
 [0 0 5 0 0 9 0 0 1]
 [0 7 0 0 6 0 0 4 3]
 [0 0 6 0 0 2 0 8 7]
 [1 9 0 0 0 7 4 0 0]
 [0 5 0 0 8 3 0 0 0]
 [6 0 0 0 0 0 1 0 5]
 [0 0 3 5 0 8 6 9 0]
 [0 4 2 9 1 0 3 0 0]]
Creating arrays from scratch
It can be helpful to know how to create quick NumPy arrays from scratch in order to test your code. For example, when you are doing math with large multi-dimensional arrays, it’s nice to check whether the math works as expected on small test arrays before applying your code to the larger arrays. NumPy has many options for creating smaller synthetic arrays.

With this in mind, it’s time for you to create some arrays from scratch! numpy is imported for you as np.

Create and print an array filled with zeros called zero_array, which has two rows and four columns.
Create and print an array of random floats between 0 and 1 called random_array, which has three rows and six columns.

# Create an array of zeros which has four columns and two rows
zero_array = np.zeros((2,4))
print(zero_array)
     
[[0. 0. 0. 0.]
 [0. 0. 0. 0.]]

# Create an array of random floats which has six columns and three rows
random_array = np.random.random((3,6))
print(random_array)

print(np.round(random_array,3))
     
[[0.93439052 0.99079074 0.61276701 0.1187103  0.7079786  0.13841812]
 [0.88644804 0.35609204 0.09975945 0.95577092 0.17983744 0.14862081]
 [0.26786163 0.59306954 0.67751699 0.18118549 0.3262437  0.57294558]]
[[0.934 0.991 0.613 0.119 0.708 0.138]
 [0.886 0.356 0.1   0.956 0.18  0.149]
 [0.268 0.593 0.678 0.181 0.326 0.573]]
A range array
np.arange() has especially useful applications in graphing. Your task is to create a scatter plot with the values from doubling_array on the y-axis.


doubling_array = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
     
Recall that a scatter plot can be created using the following code:

plt.scatter(x_values, y_values)
plt.show()
With doubling_array on the y-axis, you now need values for the x-axis, which you can create with np.arange()!

numpy is loaded for you as np, and matplotlib.pyplot is imported as plt.


import numpy as np
from matplotlib import pyplot as plt
     
Using np.arange(), create a 1D array called one_to_ten which holds all integers from one to ten (inclusive).
Create a scatterplot with doubling_array as the y values and one_to_ten as the x values.

# Create an array of integers from one to ten
one_to_ten = np.arange(1,11)
print(one_to_ten)
print(doubling_array)

# Create your scatterplot
plt.scatter(one_to_ten,doubling_array)
plt.show()
     
[ 1  2  3  4  5  6  7  8  9 10]
[1, 2, 4, 8, 16, 32, 64, 128, 256, 512]

Array dimensionality
3D array creation
In the first section, you created a sudoku_game two-dimensional NumPy array. Perhaps you have hundreds of sudoku game arrays, and you’d like to save the solution for this one, sudoku_solution, as part of the same array as its corresponding game in order to organize your sudoku data better. You could accomplish this by stacking the two 2D arrays on top of each other to create a 3D array.

numpy is loaded as np, and the sudoku_game and sudoku_solution arrays are available.

Create a 3D array called game_and_solution by stacking the two 2D arrays, sudoku_game and sudoku_solution, on top of one another; in the final array, sudoku_game should appear before sudoku_solution.
Print game_and_solution.

sudoku_solution = np.array([[8, 6, 4, 3, 7, 1, 2, 5, 9],
                            [3, 2, 5, 8, 4, 9, 7, 6, 1],
                            [9, 7, 1, 2, 6, 5, 8, 4, 3],
                            [4, 3, 6, 1, 9, 2, 5, 8, 7],
                            [1, 9, 8, 6, 5, 7, 4, 3, 2],
                            [2, 5, 7, 4, 8, 3, 9, 1, 6],
                            [6, 8, 9, 7, 3, 4, 1, 2, 5],
                            [7, 1, 3, 5, 2, 8, 6, 9, 4],
                            [5, 4, 2, 9, 1, 6, 3, 7, 8]])
sudoku_game = np.array(sudoku_list)
print("suduko_game:\n",sudoku_game)
print("suduko_solution:\n",sudoku_solution)
     
suduko_game:
 [[0 0 4 3 0 0 2 0 9]
 [0 0 5 0 0 9 0 0 1]
 [0 7 0 0 6 0 0 4 3]
 [0 0 6 0 0 2 0 8 7]
 [1 9 0 0 0 7 4 0 0]
 [0 5 0 0 8 3 0 0 0]
 [6 0 0 0 0 0 1 0 5]
 [0 0 3 5 0 8 6 9 0]
 [0 4 2 9 1 0 3 0 0]]
suduko_solution:
 [[8 6 4 3 7 1 2 5 9]
 [3 2 5 8 4 9 7 6 1]
 [9 7 1 2 6 5 8 4 3]
 [4 3 6 1 9 2 5 8 7]
 [1 9 8 6 5 7 4 3 2]
 [2 5 7 4 8 3 9 1 6]
 [6 8 9 7 3 4 1 2 5]
 [7 1 3 5 2 8 6 9 4]
 [5 4 2 9 1 6 3 7 8]]

# Create the game_and_solution 3D array
game_and_solution = np.array([sudoku_game,sudoku_solution])

# Print game_and_solution
print(game_and_solution)
     
[[[0 0 4 3 0 0 2 0 9]
  [0 0 5 0 0 9 0 0 1]
  [0 7 0 0 6 0 0 4 3]
  [0 0 6 0 0 2 0 8 7]
  [1 9 0 0 0 7 4 0 0]
  [0 5 0 0 8 3 0 0 0]
  [6 0 0 0 0 0 1 0 5]
  [0 0 3 5 0 8 6 9 0]
  [0 4 2 9 1 0 3 0 0]]

 [[8 6 4 3 7 1 2 5 9]
  [3 2 5 8 4 9 7 6 1]
  [9 7 1 2 6 5 8 4 3]
  [4 3 6 1 9 2 5 8 7]
  [1 9 8 6 5 7 4 3 2]
  [2 5 7 4 8 3 9 1 6]
  [6 8 9 7 3 4 1 2 5]
  [7 1 3 5 2 8 6 9 4]
  [5 4 2 9 1 6 3 7 8]]]
The fourth dimension
Printing arrays is a good way to check code output for small arrays like sudoku_game_and_solution, but it becomes unwieldy when dealing with bigger arrays and those with higher dimensions. Another important check is to look at the array’s .shape.

Now, you’ll create a 4D array that contains two sudoku games and their solutions. numpy is loaded as np. The game_and_solution 3D array you created in the previous example is available, along with new_sudoku_game and new_sudoku_solution.

Create another 3D array called new_game_and_solution with a different 2D game and 2D solution pair: new_sudoku_game and new_sudoku_solution. new_sudoku_game should appear before new_sudoku_solution.
Create a 4D array called games_and_solutions by making an array out of the two 3D arrays: game_and_solution and new_game_and_solution, in that order.
Print the shape of games_and_solutions.

new_sudoku_game = np.array([[0, 0, 4, 3, 0, 0, 0, 0, 0],
                            [8, 9, 0, 2, 0, 0, 6, 7, 0],
                            [7, 0, 0, 9, 0, 0, 0, 5, 0],
                            [5, 0, 0, 0, 0, 8, 1, 4, 0],
                            [0, 7, 0, 0, 3, 2, 0, 6, 0],
                            [6, 0, 0, 0, 0, 1, 3, 0, 8],
                            [0, 0, 1, 7, 5, 0, 9, 0, 0],
                            [0, 0, 5, 0, 4, 0, 0, 1, 2],
                            [9, 8, 0, 0, 0, 6, 0, 0, 5]])
print(new_sudoku_game)
     
[[0 0 4 3 0 0 0 0 0]
 [8 9 0 2 0 0 6 7 0]
 [7 0 0 9 0 0 0 5 0]
 [5 0 0 0 0 8 1 4 0]
 [0 7 0 0 3 2 0 6 0]
 [6 0 0 0 0 1 3 0 8]
 [0 0 1 7 5 0 9 0 0]
 [0 0 5 0 4 0 0 1 2]
 [9 8 0 0 0 6 0 0 5]]

new_sudoku_solution = np.array([[2, 5, 4, 3, 6, 7, 8, 9, 1],
                                [8, 9, 3, 2, 1, 5, 6, 7, 4],
                                [7, 1, 6, 9, 8, 4, 2, 5, 3],
                                [5, 3, 2, 6, 9, 8, 1, 4, 7],
                                [1, 7, 8, 4, 3, 2, 5, 6, 9],
                                [6, 4, 9, 5, 7, 1, 3, 2, 8],
                                [4, 2, 1, 7, 5, 3, 9, 8, 6],
                                [3, 6, 5, 8, 4, 9, 7, 1, 2],
                                [9, 8, 7, 1, 2, 6, 4, 3, 5]])
print(new_sudoku_solution)
     
[[2 5 4 3 6 7 8 9 1]
 [8 9 3 2 1 5 6 7 4]
 [7 1 6 9 8 4 2 5 3]
 [5 3 2 6 9 8 1 4 7]
 [1 7 8 4 3 2 5 6 9]
 [6 4 9 5 7 1 3 2 8]
 [4 2 1 7 5 3 9 8 6]
 [3 6 5 8 4 9 7 1 2]
 [9 8 7 1 2 6 4 3 5]]
Create another 3D array called new_game_and_solution with a different 2D game and 2D solution pair: new_sudoku_game and new_sudoku_solution. new_sudoku_game should appear before new_sudoku_solution


# Create a second 3D array of another game and its solution
new_game_and_solution = np.array([new_sudoku_game,new_sudoku_solution])
print(new_game_and_solution)
     
[[[0 0 4 3 0 0 0 0 0]
  [8 9 0 2 0 0 6 7 0]
  [7 0 0 9 0 0 0 5 0]
  [5 0 0 0 0 8 1 4 0]
  [0 7 0 0 3 2 0 6 0]
  [6 0 0 0 0 1 3 0 8]
  [0 0 1 7 5 0 9 0 0]
  [0 0 5 0 4 0 0 1 2]
  [9 8 0 0 0 6 0 0 5]]

 [[2 5 4 3 6 7 8 9 1]
  [8 9 3 2 1 5 6 7 4]
  [7 1 6 9 8 4 2 5 3]
  [5 3 2 6 9 8 1 4 7]
  [1 7 8 4 3 2 5 6 9]
  [6 4 9 5 7 1 3 2 8]
  [4 2 1 7 5 3 9 8 6]
  [3 6 5 8 4 9 7 1 2]
  [9 8 7 1 2 6 4 3 5]]]
Create a 4D array called games_and_solutions by making an array out of the two 3D arrays: game_and_solution and new_game_and_solution, in that order.


# Create a 4D array of both game and solution 3D arrays
games_and_solutions = np.array([game_and_solution,new_game_and_solution])
print(games_and_solutions)
     
[[[[0 0 4 3 0 0 2 0 9]
   [0 0 5 0 0 9 0 0 1]
   [0 7 0 0 6 0 0 4 3]
   [0 0 6 0 0 2 0 8 7]
   [1 9 0 0 0 7 4 0 0]
   [0 5 0 0 8 3 0 0 0]
   [6 0 0 0 0 0 1 0 5]
   [0 0 3 5 0 8 6 9 0]
   [0 4 2 9 1 0 3 0 0]]

  [[8 6 4 3 7 1 2 5 9]
   [3 2 5 8 4 9 7 6 1]
   [9 7 1 2 6 5 8 4 3]
   [4 3 6 1 9 2 5 8 7]
   [1 9 8 6 5 7 4 3 2]
   [2 5 7 4 8 3 9 1 6]
   [6 8 9 7 3 4 1 2 5]
   [7 1 3 5 2 8 6 9 4]
   [5 4 2 9 1 6 3 7 8]]]


 [[[0 0 4 3 0 0 0 0 0]
   [8 9 0 2 0 0 6 7 0]
   [7 0 0 9 0 0 0 5 0]
   [5 0 0 0 0 8 1 4 0]
   [0 7 0 0 3 2 0 6 0]
   [6 0 0 0 0 1 3 0 8]
   [0 0 1 7 5 0 9 0 0]
   [0 0 5 0 4 0 0 1 2]
   [9 8 0 0 0 6 0 0 5]]

  [[2 5 4 3 6 7 8 9 1]
   [8 9 3 2 1 5 6 7 4]
   [7 1 6 9 8 4 2 5 3]
   [5 3 2 6 9 8 1 4 7]
   [1 7 8 4 3 2 5 6 9]
   [6 4 9 5 7 1 3 2 8]
   [4 2 1 7 5 3 9 8 6]
   [3 6 5 8 4 9 7 1 2]
   [9 8 7 1 2 6 4 3 5]]]]
Print the shape of games_and_solutions.


# Print the shape of your 4D array
games_and_solutions.shape
     
(2, 2, 9, 9)

print(games_and_solutions.shape)
     
(2, 2, 9, 9)
Flattening and reshaping
You’ve learned to change not only array shape but also the number of dimensions that an array has. To test these skills, you’ll change sudoku_game from a 2D array to a 1D array and back again. Can we trust NumPy to keep the array elements in the same order after being flattened and reshaped? Time to find out.

Flatten sudoku_game so that it is a 1D array, and save it as flattened_game.


print(sudoku_game)
     
[[0 0 4 3 0 0 2 0 9]
 [0 0 5 0 0 9 0 0 1]
 [0 7 0 0 6 0 0 4 3]
 [0 0 6 0 0 2 0 8 7]
 [1 9 0 0 0 7 4 0 0]
 [0 5 0 0 8 3 0 0 0]
 [6 0 0 0 0 0 1 0 5]
 [0 0 3 5 0 8 6 9 0]
 [0 4 2 9 1 0 3 0 0]]

# Flatten sudoku_game
print(sudoku_game.flatten())
flattened_game = sudoku_game.flatten()
print(flattened_game)
     
[0 0 4 3 0 0 2 0 9 0 0 5 0 0 9 0 0 1 0 7 0 0 6 0 0 4 3 0 0 6 0 0 2 0 8 7 1
 9 0 0 0 7 4 0 0 0 5 0 0 8 3 0 0 0 6 0 0 0 0 0 1 0 5 0 0 3 5 0 8 6 9 0 0 4
 2 9 1 0 3 0 0]
[0 0 4 3 0 0 2 0 9 0 0 5 0 0 9 0 0 1 0 7 0 0 6 0 0 4 3 0 0 6 0 0 2 0 8 7 1
 9 0 0 0 7 4 0 0 0 5 0 0 8 3 0 0 0 6 0 0 0 0 0 1 0 5 0 0 3 5 0 8 6 9 0 0 4
 2 9 1 0 3 0 0]
Print the .shape of flattened_game.


print(flattened_game.shape)
     
(81,)
Reshape the flattened_game back to its original shape of nine rows and nine columns; save the new array as reshaped_game.


# Reshape flattened_game back to a nine by nine array
reshaped_game = flattened_game.reshape((9,9))

# Print sudoku_game and reshaped_game
print(sudoku_game)
print(reshaped_game)
     
[[0 0 4 3 0 0 2 0 9]
 [0 0 5 0 0 9 0 0 1]
 [0 7 0 0 6 0 0 4 3]
 [0 0 6 0 0 2 0 8 7]
 [1 9 0 0 0 7 4 0 0]
 [0 5 0 0 8 3 0 0 0]
 [6 0 0 0 0 0 1 0 5]
 [0 0 3 5 0 8 6 9 0]
 [0 4 2 9 1 0 3 0 0]]
[[0 0 4 3 0 0 2 0 9]
 [0 0 5 0 0 9 0 0 1]
 [0 7 0 0 6 0 0 4 3]
 [0 0 6 0 0 2 0 8 7]
 [1 9 0 0 0 7 4 0 0]
 [0 5 0 0 8 3 0 0 0]
 [6 0 0 0 0 0 1 0 5]
 [0 0 3 5 0 8 6 9 0]
 [0 4 2 9 1 0 3 0 0]]
NumPy data types
The dtype argument One way to control the data type of a NumPy array is to declare it when the array is created using the dtype keyword argument. Take a look at the data type NumPy uses by default when creating an array with np.zeros(). Could it be updated?

Using np.zeros(), create an array of zeros that has three rows and two columns; call it zero_array.

Print the data type of zero_array.

Create a new array of zeros called zero_int_array, which will also have three rows and two columns, but the data type should be np.int32.

Print the data type of zero_int_array.


# Create an array of zeros with three rows and two columns
zero_array = np.zeros((3,2))

# Print the data type of zero_array
print(zero_array.dtype)

# Create a new array of int32 zeros with three rows and two columns
zero_int_array = np.zeros((3,2),dtype=np.int32)

# Print the data type of zero_int_array
print(zero_int_array)
     
float64
[[0 0]
 [0 0]
 [0 0]]
Anticipating data types
Anticipating what data type an array will have is very important since some NumPy functionality only works with certain data types. Let’s see what you’ve got.

For each of the given code snippets, determine which data type the resulting array will have by dragging the snippet to the proper box.
A string data type

np.array([78.988, "NumPy", True])
np.array([9, 1.12, True]).astype("<U5")
An integer data type

np.array([34.62, 70.13, 9]).astype(np.int64)
np.array([45.67, True], dtype=np.int8)
A float data type

np.array([[6, 15.7], [True, False]])
np.random.random((4, 5))

np.array([[6, 15.7], [True, False]], dtype="int")

     
array([[ 6, 15],
       [ 1,  0]])

np.array([[6, 15.7], [True, False]]).astype("int")
     
array([[ 6, 15],
       [ 1,  0]])

np.array([9, 1.12, True]).astype("
array(['9.0', '1.12', '1.0'], dtype='<U5')
A smaller sudoku game
NumPy data types, which emphasize speed, are more specific than Python data types, which emphasize flexibility. When working with large amounts of data in NumPy, it’s good practice to check the data type and consider whether a smaller data type is large enough for your data, since smaller data types use less memory.

It’s time to make your sudoku game more memory-efficient using your knowledge of data types! sudoku_game has been loaded for you as a NumPy array. numpy is imported as np.

Print the data type of the elements in sudoku_game.

# Print the data type of sudoku_game
print(type(sudoku_game))
print(sudoku_game.dtype)
     
<class 'numpy.ndarray'>
int64
The current data type of sudoku_game is int64.

Which of the following NumPy integers is the smallest bitsize that is still large enough to hold the data in sudoku_game?
If you have never played sudoku, know that sudoku games only ever store integers from one to nine. ** np.int64 ** np.int32 ** np.int16 ** np.int8
Change the data type of sudoku_game to be int8, an 8-bit integer; name the new array small_sudoku_game.


small_sudoku_game = sudoku_game.astype(np.int8)
print(small_sudoku_game.dtype)
     
int8
Print the data type of small_sudoku_game to be sure that your change to int8 is reflected.


small_sudoku_game
     
array([[0, 0, 4, 3, 0, 0, 2, 0, 9],
       [0, 0, 5, 0, 0, 9, 0, 0, 1],
       [0, 7, 0, 0, 6, 0, 0, 4, 3],
       [0, 0, 6, 0, 0, 2, 0, 8, 7],
       [1, 9, 0, 0, 0, 7, 4, 0, 0],
       [0, 5, 0, 0, 8, 3, 0, 0, 0],
       [6, 0, 0, 0, 0, 0, 1, 0, 5],
       [0, 0, 3, 5, 0, 8, 6, 9, 0],
       [0, 4, 2, 9, 1, 0, 3, 0, 0]], dtype=int8)
Selecting and Updating Data
Sharpen your NumPy data wrangling skills by slicing, filtering, and sorting New York City’s tree census data. Create new arrays by pulling data based on conditional statements, and add and remove data along any dimension to suit your purpose. Along the way, you’ll learn the shape and dimension compatibility principles to prepare for super-fast array math.

Indexing and slicing arrays
Slicing and indexing trees
Imagine you are a researcher working with data from New York City’s tree census. Each row of the tree_census 2D array lists information for a different tree: the tree ID, block ID, trunk diameter, and stump diameter in that order. Living trees do not have stump diameters, which explains why there are so many zeros in that column. Column order is important because NumPy does not have column names! The first and last three rows of tree_census are shown below.


import pandas as pd
tree_census = pd.read_csv("https://data.cityofnewyork.us/api/views/uvpi-gqnh/rows.csv?accessType=DOWNLOAD")
     

print(tree_census)
     
        tree_id  block_id  created_at  tree_dbh  stump_diam curb_loc status  \
0        180683    348711  08/27/2015         3           0   OnCurb  Alive   
1        200540    315986  09/03/2015        21           0   OnCurb  Alive   
2        204026    218365  09/05/2015         3           0   OnCurb  Alive   
3        204337    217969  09/05/2015        10           0   OnCurb  Alive   
4        189565    223043  08/30/2015        21           0   OnCurb  Alive   
...         ...       ...         ...       ...         ...      ...    ...   
683783   155433    217978  08/18/2015        25           0   OnCurb  Alive   
683784   183795    348185  08/29/2015         7           0   OnCurb  Alive   
683785   166161    401670  08/22/2015        12           0   OnCurb  Alive   
683786   184028    504204  08/29/2015         9           0   OnCurb  Alive   
683787   200607    306527  09/03/2015        23           0   OnCurb  Alive   

       health                           spc_latin           spc_common  ...  \
0        Fair                         Acer rubrum            red maple  ...   
1        Fair                   Quercus palustris              pin oak  ...   
2        Good  Gleditsia triacanthos var. inermis          honeylocust  ...   
3        Good  Gleditsia triacanthos var. inermis          honeylocust  ...   
4        Good                     Tilia americana      American linden  ...   
...       ...                                 ...                  ...  ...   
683783   Good                   Quercus palustris              pin oak  ...   
683784   Good                 Cladrastis kentukea  Kentucky yellowwood  ...   
683785   Good                         Acer rubrum            red maple  ...   
683786   Good                         Acer rubrum            red maple  ...   
683787   Fair                         Acer rubrum            red maple  ...   

        boro_ct     state   latitude  longitude          x_sp         y_sp  \
0       4073900  New York  40.723092 -73.844215  1.027431e+06  202756.7687   
1       4097300  New York  40.794111 -73.818679  1.034456e+06  228644.8374   
2       3044900  New York  40.717581 -73.936608  1.001823e+06  200716.8913   
3       3044900  New York  40.713537 -73.934456  1.002420e+06  199244.2531   
4       3016500  New York  40.666778 -73.975979  9.909138e+05  182202.4260   
...         ...       ...        ...        ...           ...          ...   
683783  3051900  New York  40.713211 -73.954944  9.967407e+05  199121.6363   
683784  4070700  New York  40.715194 -73.856650  1.023989e+06  199873.6475   
683785  5020100  New York  40.620762 -74.136517  9.463514e+05  165466.0763   
683786  2023502  New York  40.850828 -73.903115  1.011054e+06  249271.9507   
683787  4134100  New York  40.732165 -73.787526  1.043136e+06  206095.5383   

       council district census tract        bin           bbl  
0                  29.0        739.0  4052307.0  4.022210e+09  
1                  19.0        973.0  4101931.0  4.044750e+09  
2                  34.0        449.0  3338310.0  3.028870e+09  
3                  34.0        449.0  3338342.0  3.029250e+09  
4                  39.0        165.0  3025654.0  3.010850e+09  
...                 ...          ...        ...           ...  
683783             34.0        519.0  3062513.0  3.023690e+09  
683784             29.0        707.0  4075448.0  4.031810e+09  
683785             50.0        201.0  5011657.0  5.004080e+09  
683786             15.0      23502.0  2007757.0  2.028120e+09  
683787             24.0       1341.0  4153657.0  4.071360e+09  

[683788 rows x 45 columns]

tree_census = pd.DataFrame(tree_census)
     

tree_census.head()
     
tree_id	block_id	created_at	tree_dbh	stump_diam	curb_loc	status	health	spc_latin	spc_common	...	boro_ct	state	latitude	longitude	x_sp	y_sp	council district	census tract	bin	bbl
0	180683	348711	08/27/2015	3	0	OnCurb	Alive	Fair	Acer rubrum	red maple	...	4073900	New York	40.723092	-73.844215	1027431.148	202756.7687	29.0	739.0	4052307.0	4.022210e+09
1	200540	315986	09/03/2015	21	0	OnCurb	Alive	Fair	Quercus palustris	pin oak	...	4097300	New York	40.794111	-73.818679	1034455.701	228644.8374	19.0	973.0	4101931.0	4.044750e+09
2	204026	218365	09/05/2015	3	0	OnCurb	Alive	Good	Gleditsia triacanthos var. inermis	honeylocust	...	3044900	New York	40.717581	-73.936608	1001822.831	200716.8913	34.0	449.0	3338310.0	3.028870e+09
3	204337	217969	09/05/2015	10	0	OnCurb	Alive	Good	Gleditsia triacanthos var. inermis	honeylocust	...	3044900	New York	40.713537	-73.934456	1002420.358	199244.2531	34.0	449.0	3338342.0	3.029250e+09
4	189565	223043	08/30/2015	21	0	OnCurb	Alive	Good	Tilia americana	American linden	...	3016500	New York	40.666778	-73.975979	990913.775	182202.4260	39.0	165.0	3025654.0	3.010850e+09
5 rows × 45 columns


tree_census = tree_census[["tree_id","block_id","tree_dbh","stump_diam"]]
     

tree_census.head()
     
tree_id	block_id	tree_dbh	stump_diam
0	180683	348711	3	0
1	200540	315986	21	0
2	204026	218365	3	0
3	204337	217969	10	0
4	189565	223043	21	0

tree_census = np.array(tree_census)
     

print(tree_census)
     
[[180683 348711      3      0]
 [200540 315986     21      0]
 [204026 218365      3      0]
 ...
 [166161 401670     12      0]
 [184028 504204      9      0]
 [200607 306527     23      0]]
In this exercise, you’ll be working specifically with the second column, representing block IDs: your research requires you to select specific city blocks for further analysis using NumPy slicing and indexing. numpy is loaded as np, and the tree_census 2D array is available.

Select all rows of data from the second column, representing block IDs; save the resulting array as block_ids.

# Select all rows of block ID data from the second column
block_ids = tree_census[:,1]
print(block_ids)
     
[348711 315986 218365 ... 401670 504204 306527]
Print the first five block IDs from block_ids.

# Print the first five block_ids
print(block_ids[:5])
     
[348711 315986 218365 217969 223043]
Select the tenth block ID from block_ids, saving the result as tenth_block_id.


# Select the tenth block ID from block_ids
tenth_block_id = block_ids[9]
print(tenth_block_id)
     
207508
Select five consecutive block IDs from block_ids, starting with the tenth ID, and save as block_id_slice


# Select five block IDs from block_ids starting with the tenth ID
block_id_slice = block_ids[9:14]
print(block_id_slice)
     
[207508 302371 302371 415896 219493]
Stepping into 2D
Now assume that your research requires you to take an admittedly unrepresentative sample of trunk diameters, which are located in the third column of tree_census. Getting just a selection of trunk diameters can be done with NumPy’s slicing and stepping functionality.

numpy is loaded as np, and the tree_census 2D array is available.

Create an array called hundred_diameters which contains the first 100 trunk diameters in tree_census.

Create an array,every_other_diameter, which contains only trunk diameters for trees with even row indices from 50 to 100, inclusive.

Create an array called hundred_diameters which contains the first 100 trunk diameters in tree_census.


print(tree_census[:5,])
     
[[180683 348711      3      0]
 [200540 315986     21      0]
 [204026 218365      3      0]
 [204337 217969     10      0]
 [189565 223043     21      0]]

# Create an array of the first 100 trunk diameters from tree_census
hundred_diameters = tree_census[:100,2]
print(hundred_diameters)
     
[ 3 21  3 10 21 11 11  9  6 21 11  8 13 22 30 12  2 14 14 10 11 14  4  9
  2  5 33 19  9  9  7  3  7  5  4 12 13  0 12  3 24 20 13 12 36 29  6  9
 18 13 13  9 19 17 32 28  7  0 10  5  8 10  6  8  5  5 26 10 18 11 25 15
 13  5 26 36 16 13  2  2  4 22 28 42 12  3  3 26  3 26 18 24 32 13 11 22
 38 18  2 29]
Create an array,every_other_diameter, which contains only trunk diameters for trees with even row indices from 50 to 100, inclusive.


# Create an array of trunk diameters with even row indices from 50 to 100 inclusive
every_other_diameter = tree_census[50:101:2,2]
print(every_other_diameter)
     
[13 19 32  7 10  8  6  5 26 18 25 13 26 16  2  4 28 12  3  3 18 32 11 38
  2 11]
Sorting trees
Sometimes it’s easiest to understand data when it is sorted according to the value you are most interested in. Your new research task is to create an array containing the trunk diameters in the New York City tree census, sorted in order from smallest to largest.

numpy is loaded as np, and the tree_census 2D array is available.

Create an array called sorted_trunk_diameters which selects only the trunk diameter column from tree_census and sorts it so that the smallest trunk diameters are at the top of the array and the largest at the bottom.

# Extract trunk diameters information and sort from smallest to largest
sorted_trunk_diameters = np.sort(tree_census[:,2])
print(sorted_trunk_diameters)
     
[  0   0   0 ... 389 425 450]
Filtering arrays
Filtering with masks
In the last lesson, you sorted trees from smallest to largest. Now, you’ll use fancy indexing to return the row of data representing the largest tree in tree_census. You’ll also examine other trees located on the same block as the largest tree: are they also large?

numpy is loaded as np, and the tree_census array is available. As a reminder, the tree_census columns in order refer to a tree’s ID, its block ID, its trunk diameter, and its stump diameter.

Using Boolean indexing, create an array, largest_tree_data, which contains the row of data on the largest tree in tree_census corresponding to the tree with a diameter of 450.

tree_census[:,2]
     
array([ 3, 21,  3, ..., 12,  9, 23])

np.max(tree_census[:,2])
     
np.int64(450)

# Create an array which contains row data on the largest tree in tree_census
largest_tree_data = tree_census[tree_census[:,2] == 450]
print(largest_tree_data)
     
[[433258 507833    450      0]]

# Slice largest_tree_data to get only the block id
largest_tree_block_id = largest_tree_data[0,1]
print(largest_tree_block_id)
     
507833

# Create an array which contains row data on all trees with largest_tree_block_id
trees_on_largest_tree_block = tree_census[tree_census[:,1] == largest_tree_block_id]
print(trees_on_largest_tree_block)
     
[[433258 507833    450      0]
 [433261 507833      5      0]
 [433255 507833      6      0]
 [433259 507833      4      0]
 [433260 507833      4      0]
 [433256 507833      4      0]
 [433257 507833      4      0]]
Fancy indexing vs. np.where()
You and your tree research team are double-checking collection data by visiting a few trees in person to confirm their measurements. You’ve been assigned to check the data for trees on block 313879, and you’d like to make a small array of just the tree data that relates to your work.

numpy is loaded as np, and thetree_census array is available. As a reminder, thetree_census columns in order refer to a tree’s ID, its block ID, its trunk diameter, and its stump diameter.

Using fancy indexing, create an array calledblock_313879 which only contains data for trees with a block ID of 313879.

Using np.where(), create an array ofrow_indices for trees with a block ID of 313879.

Using row_indices, create block_313879, which contains data for trees on block 313879.


# Create the block_313879 array containing trees on block 313879
block_313879 = tree_census[tree_census[:,1] == 313879]
print(block_313879)

# Create an array of row_indices for trees on block 313879
row_indices = np.where(tree_census[:,1] == 313879)

# Create an array which only contains data for trees on block 313879
block_313879 = tree_census[row_indices]
print(block_313879)
     
[[  1115 313879      3      0]
 [  1116 313879     17      0]]
[[  1115 313879      3      0]
 [  1116 313879     17      0]]
Creating arrays from conditions
Currently, the stump diameter and trunk diameter values intree_census are in two different columns. Living trees have a stump diameter of zero while stumps have a trunk diameter of zero. If you’d like to include both living trees and stumps in certain research calculations, it might be useful to have their diameters together in just one column.

numpy is loaded as np, and thetree_census array is available. As a reminder, the tree census columns in order refer to a tree’s ID, its block ID, its trunk diameter, and its stump diameter.

Create and print a 1D array calledtrunk_stump_diameters, which replaces a tree’s trunk diameter with its stump diameter if the trunk diameter is zero.

# Create and print a 1D array of tree and stump diameters
trunk_stump_diameters = np.where(tree_census[:,2] == 0, tree_census[:,3], tree_census[:,2])
print(trunk_stump_diameters)
     
[ 3 21  3 ... 12  9 23]
Adding and removing data
Compatible or not?
Before concatenating, it’s important to check whether two arrays can be concatenated together. If not, the array may need to be reshaped before concatenation.

Each card lists two array shapes: determine whether they are compatible for concatenation, and if so, along which axis.
Compatible along the first axis
(4, 2) and (6, 2)
(15, 5) and (100, 5)
Compatible along the second axis
(4, 2) and (4, 3)
Not compatible
(5, 2) and (7, 4)
(4, 2) and (4,)
(4, 2) and (2,)
Adding rows
The research team has discovered two trees that were left off thetree_census. Your task is to add rows containing the data for these new trees to the end of the tree_census array. The new trees’ data is saved in a 2D array callednew_trees:

new_trees = np.array([[1211, 227386, 20, 0], [1212, 227386, 8, 0]])
numpy is loaded as np, and thetree_census and new_trees arrays are available.

Print the shapes of tree_census andnew_trees to confirm they are compatible to concatenate.
Add rows to the end of tree_census containing data for the new trees from the new_trees 2D array; save the new array as updated_tree_census.

new_trees = np.array([[1211, 227386, 20, 0], [1212, 227386, 8, 0]])

# Print the shapes of tree_census and new_trees
print(tree_census.shape, new_trees.shape)

# Add rows to tree_census which contain data for the new trees
updated_tree_census = np.concatenate((tree_census, new_trees))
print(updated_tree_census)
     
(683788, 4) (2, 4)
[[180683 348711      3      0]
 [200540 315986     21      0]
 [204026 218365      3      0]
 ...
 [200607 306527     23      0]
 [  1211 227386     20      0]
 [  1212 227386      8      0]]
Adding columns
You finished the last set of exercises by creating an array calledtrunk_stump_diameters, which combined data from the trunk diameter and stump diameter columns into a 1D array. Now, you’ll add that 1D array as a column to the tree_census array.

numpy is loaded as np, and both thetree_census and trunk_stump_diameters arrays are available.

Print the shapes of both tree_census andtrunk_stump_diameters.
Reshape trunk_stump_diameters so that it can be appended as the last column in tree_census; call the reshaped array reshaped_diameters.
Concatenate reshaped_diameters to the end oftree_census so that it becomes the last column; call the new array concatenated_tree_census.

# Print the shapes of tree_census and trunk_stump_diameters
print(trunk_stump_diameters.shape, tree_census.shape)

# Reshape trunk_stump_diameters
reshaped_diameters = trunk_stump_diameters.reshape((len(trunk_stump_diameters), 1))

# Concatenate reshaped_diameters to tree_census as the last column
concatenated_tree_census = np.concatenate((tree_census, reshaped_diameters), axis=1)
print(concatenated_tree_census)
     
(683788,) (683788, 4)
[[180683 348711      3      0      3]
 [200540 315986     21      0     21]
 [204026 218365      3      0      3]
 ...
 [166161 401670     12      0     12]
 [184028 504204      9      0      9]
 [200607 306527     23      0     23]]
Deleting with np.delete()
What if your tree research focuses only on living trees on publicly-owned city blocks? It might be helpful to delete some unneeded data like the stump diameter column and some trees located on private blocks.

You’ve learned that NumPy’s np.delete() function takes three arguments: the original array, the index or indices to be deleted, and the axis to delete along. If you don’t know the index or indices of the array you’d like to delete, recall that when it is only passed one argument,np.where() returns an array of indices where a condition is met!

numpy is loaded as np, and thetree_census 2D array is available. The columns in order refer to a tree’s ID, block number, trunk diameter, and stump diameter.

Delete the stump diameter column from tree_census, and save the new 2D array as tree_census_no_stumps.
Using np.where(), find the indices of any trees on block 313879, a private block. Save the indices in an array calledprivate_block_indices. Using the indices you just found using np.where(), delete the rows for trees on block 313879 from tree_census_no_stumps, saving the new 2D array astree_census_clean. Print the shape oftree_census_clean.

# Delete the stump diameter column from tree_census
tree_census_no_stumps = np.delete(tree_census, 3, axis=1)
print(tree_census_no_stumps)

# Save the indices of the trees on block 313879
private_block_indices = np.where(tree_census_no_stumps[:,1] == 313879)

# Delete the rows for trees on block 313879 from tree_census_no_stumps
tree_census_clean = np.delete(tree_census_no_stumps, private_block_indices, axis=0)

# Print the shape of tree_census_clean
print(tree_census_clean.shape)
     
[[180683 348711      3]
 [200540 315986     21]
 [204026 218365      3]
 ...
 [166161 401670     12]
 [184028 504204      9]
 [200607 306527     23]]
(683786, 3)
Array Mathematics!
Leverage NumPy’s speedy vectorized operations to gather summary insights on sales data for American liquor stores, restaurants, and department stores. Vectorize Python functions for use in your NumPy code. Finally, use broadcasting logic to perform mathematical operations between arrays of different sizes.

Summarizing data
Sales totals
The dataset you’ll be working with during this chapter is one year’s sales data by month for three different industries. Each row in thismonthly_sales array represents a month from January to December. The first column has monthly sales data for liquor stores, the second column has data for restaurants, and the last column tracks sales for department stores.

array([[ 4134, 23925,  8657],
       [ 4116, 23875,  9142],
       [ 4673, 27197, 10645],
       [ 4580, 25637, 10456],
       [ 5109, 27995, 11299],
       [ 5011, 27419, 10625],
       [ 5245, 27305, 10630],
       [ 5270, 27760, 11550],
       [ 4680, 24988,  9762],
       [ 4913, 25802, 10456],
       [ 5312, 25405, 13401],
       [ 6630, 27797, 18403]])
Your task is to create an array with all the information frommonthly_sales as well as a fourth column which totals the monthly sales across industries for each month.

numpy is loaded for you as np, and themonthly_sales array is available.

Create a 2D array which contains a single column of total monthly sales across industries; call itmonthly_industry_sales.
Concatenate monthly_industry_sales withmonthly_sales into a new array calledmonthly_sales_with_total, with the monthly cross-industry sales information in the final column.

monthly_sales = np.array([[ 4134, 23925,  8657],
       [ 4116, 23875,  9142],
       [ 4673, 27197, 10645],
       [ 4580, 25637, 10456],
       [ 5109, 27995, 11299],
       [ 5011, 27419, 10625],
       [ 5245, 27305, 10630],
       [ 5270, 27760, 11550],
       [ 4680, 24988,  9762],
       [ 4913, 25802, 10456],
       [ 5312, 25405, 13401],
       [ 6630, 27797, 18403]])

# Create a 2D array of total monthly sales across industries
monthly_industry_sales = np.sum(monthly_sales, axis=1, keepdims=True)
print(monthly_industry_sales)

# Add this column as the last column in monthly_sales
monthly_sales_with_total = np.concatenate((monthly_sales, monthly_industry_sales), axis=1)
print(monthly_sales_with_total)
     
[[36716]
 [37133]
 [42515]
 [40673]
 [44403]
 [43055]
 [43180]
 [44580]
 [39430]
 [41171]
 [44118]
 [52830]]
[[ 4134 23925  8657 36716]
 [ 4116 23875  9142 37133]
 [ 4673 27197 10645 42515]
 [ 4580 25637 10456 40673]
 [ 5109 27995 11299 44403]
 [ 5011 27419 10625 43055]
 [ 5245 27305 10630 43180]
 [ 5270 27760 11550 44580]
 [ 4680 24988  9762 39430]
 [ 4913 25802 10456 41171]
 [ 5312 25405 13401 44118]
 [ 6630 27797 18403 52830]]
Plotting averages
Perhaps you have a hunch that department stores see greater increased sales than average during the end of the year as people rush to buy gifts. You’d like to test this theory by comparing monthly department store sales to average sales across all three industries.

numpy is loaded for you as np, and themonthly_sales array is available. Themonthly_sales columns in order refer to liquor store, restaurant, and department store sales.

Create a 1D array called avg_monthly_sales, which contains an average sales amount for each month across the three industries.
Plot an array of the numbers one through twelve (representing each month) on the x-axis andavg_monthly_sales on the y-axis.
Plot an array of the numbers one through twelve on the x-axis and the department store sales column ofmonthly_sales on the y-axis.

# Create the 1D array avg_monthly_sales
avg_monthly_sales = np.mean(monthly_sales, axis=1)
print(avg_monthly_sales)

# Plot avg_monthly_sales by month
plt.plot(np.arange(1, 13), avg_monthly_sales, label="Average sales across industries")

# Plot department store sales by month
plt.plot(np.arange(1, 13), monthly_sales[:, 2], label="Department store sales")
plt.legend()
plt.show()
     
[12238.66666667 12377.66666667 14171.66666667 13557.66666667
 14801.         14351.66666667 14393.33333333 14860.
 13143.33333333 13723.66666667 14706.         17610.        ]

Cumulative sales
In the last exercise, you established that December is a big month for department stores. Are there other months where sales increase or decrease significantly?

Your task now is to look at monthly cumulative sales for each industry. The slope of the cumulative sales line will explain a lot about how steady sales are over time: a straight line will indicate steady growth, and changes in slope will indicate relative increases or decreases in sales.

numpy is loaded for you as np, and themonthly_sales array is available. Themonthly_sales columns in order refer to liquor store, restaurant, and department store sales.

Find cumulative monthly sales for each industry, saving this data in an array called cumulative_monthly_industry_sales.
Plot each industry’s cumulative sales by month as separate lines, with cumulative sales on the y-axis and month number on the x-axis.

# Find cumulative monthly sales for each industry
cumulative_monthly_industry_sales = np.cumsum(monthly_sales, axis=0)
print(cumulative_monthly_industry_sales)

# Find cumulative monthly sales for each industry
cumulative_monthly_industry_sales = np.cumsum(monthly_sales, axis=0)
print(cumulative_monthly_industry_sales)

# Plot each industry's cumulative sales by month as separate lines
plt.plot(np.arange(1, 13), cumulative_monthly_industry_sales[:, 0], label="Liquor Stores")
plt.plot(np.arange(1, 13), cumulative_monthly_industry_sales[:, 1], label="Restaurants")
plt.plot(np.arange(1, 13), cumulative_monthly_industry_sales[:, 2], label="Department stores")
plt.legend()
plt.show()
     
[[  4134  23925   8657]
 [  8250  47800  17799]
 [ 12923  74997  28444]
 [ 17503 100634  38900]
 [ 22612 128629  50199]
 [ 27623 156048  60824]
 [ 32868 183353  71454]
 [ 38138 211113  83004]
 [ 42818 236101  92766]
 [ 47731 261903 103222]
 [ 53043 287308 116623]
 [ 59673 315105 135026]]
[[  4134  23925   8657]
 [  8250  47800  17799]
 [ 12923  74997  28444]
 [ 17503 100634  38900]
 [ 22612 128629  50199]
 [ 27623 156048  60824]
 [ 32868 183353  71454]
 [ 38138 211113  83004]
 [ 42818 236101  92766]
 [ 47731 261903 103222]
 [ 53043 287308 116623]
 [ 59673 315105 135026]]

Vectorized operations
Tax calculations
It’s possible to use vectorized operations to calculate taxes for the liquor, restaurant, and department store industries! We’ll simplify the tax calculation process here and assume that government collects 5% of all sales across these industries as tax revenue.

Your task is to calculate the tax owed by each industry related to each month’s sales. numpy is loaded for you asnp, and the monthly_sales array is available.

Create an array called tax_collected which calculates tax collected by industry and month by multiplying each element inmonthly_sales by 0.05.
Create an array that keeps track oftotal_tax_and_revenue collected by each industry and month by adding each element in tax_collected with its corresponding element in monthly_sales.

# Create an array of tax collected by industry and month
tax_collected = monthly_sales * 0.05
print(tax_collected)


# Create an array of sales revenue plus tax collected by industry and month
total_tax_and_revenue = monthly_sales + tax_collected
print(total_tax_and_revenue)
     
[[ 206.7  1196.25  432.85]
 [ 205.8  1193.75  457.1 ]
 [ 233.65 1359.85  532.25]
 [ 229.   1281.85  522.8 ]
 [ 255.45 1399.75  564.95]
 [ 250.55 1370.95  531.25]
 [ 262.25 1365.25  531.5 ]
 [ 263.5  1388.    577.5 ]
 [ 234.   1249.4   488.1 ]
 [ 245.65 1290.1   522.8 ]
 [ 265.6  1270.25  670.05]
 [ 331.5  1389.85  920.15]]
[[ 4340.7  25121.25  9089.85]
 [ 4321.8  25068.75  9599.1 ]
 [ 4906.65 28556.85 11177.25]
 [ 4809.   26918.85 10978.8 ]
 [ 5364.45 29394.75 11863.95]
 [ 5261.55 28789.95 11156.25]
 [ 5507.25 28670.25 11161.5 ]
 [ 5533.5  29148.   12127.5 ]
 [ 4914.   26237.4  10250.1 ]
 [ 5158.65 27092.1  10978.8 ]
 [ 5577.6  26675.25 14071.05]
 [ 6961.5  29186.85 19323.15]]
Projecting sales
You’d like to be able to plan for next year’s operations by projecting what sales will be, and you’ve gathered multipliers specific to each month and industry. These multipliers are saved in an array called monthly_industry_multipliers. For example, the multiplier at monthly_industry_multipliers[0, 0] of0.98 means that the liquor store industry is projected to have 98% of this January’s sales in January of next year.

array([[0.98, 1.02, 1.  ],
       [1.00, 1.01, 0.97],
       [1.06, 1.03, 0.98],
       [1.08, 1.01, 0.98],
       [1.08, 0.98, 0.98],
       [1.1 , 0.99, 0.99],
       [1.12, 1.01, 1.  ],
       [1.1 , 1.02, 1.  ],
       [1.11, 1.01, 1.01],
       [1.08, 0.99, 0.97],
       [1.09, 1.  , 1.02],
       [1.13, 1.03, 1.02]])
numpy is loaded for you as np, and themonthly_sales and monthly_industry_multipliersarrays are available. The monthly_sales columns in order refer to liquor store, restaurant, and department store sales.

Create an array called projected_monthly_sales which contains projected sales for all three industries based on the multipliers you have gathered.
Create a graph that plots two lines: current liquor store sales by month and projected liquor store sales by month; months will be represented by an array of the numbers one through twelve.

monthly_industry_multipliers = np.array([[0.98, 1.02, 1.  ],
       [1.00, 1.01, 0.97],
       [1.06, 1.03, 0.98],
       [1.08, 1.01, 0.98],
       [1.08, 0.98, 0.98],
       [1.1 , 0.99, 0.99],
       [1.12, 1.01, 1.  ],
       [1.1 , 1.02, 1.  ],
       [1.11, 1.01, 1.01],
       [1.08, 0.99, 0.97],
       [1.09, 1.  , 1.02],
       [1.13, 1.03, 1.02]])

# Create an array of monthly projected sales for all industries
projected_monthly_sales = monthly_sales * monthly_industry_multipliers
print(projected_monthly_sales)

# Graph current liquor store sales and projected liquor store sales by month
plt.plot(np.arange(1, 13), monthly_sales[:, 0], label="Current liquor store sales")
plt.plot(np.arange(1, 13), projected_monthly_sales[:, 0], label="Projected liquor store sales")
plt.legend()
plt.show()
     
[[ 4051.32 24403.5   8657.  ]
 [ 4116.   24113.75  8867.74]
 [ 4953.38 28012.91 10432.1 ]
 [ 4946.4  25893.37 10246.88]
 [ 5517.72 27435.1  11073.02]
 [ 5512.1  27144.81 10518.75]
 [ 5874.4  27578.05 10630.  ]
 [ 5797.   28315.2  11550.  ]
 [ 5194.8  25237.88  9859.62]
 [ 5306.04 25543.98 10142.32]
 [ 5790.08 25405.   13669.02]
 [ 7491.9  28630.91 18771.06]]

Vectorizing .upper()
There are many situations where you might want to use Python methods and functions on array elements in NumPy. You can always write afor loop to do this, but vectorized operations are much faster and more efficient, so consider usingnp.vectorize()!

You’ve got an array called names which contains first and last names:

names = np.array([["Izzy", "Monica", "Marvin"],
                  ["Weber", "Patel", "Hernandez"]])
You’d like to use one of the Python methods you learned in this chapter,.upper(), to make all the letters of every name in the array uppercase. As a reminder, .upper() is a string method, meaning that it must be called on an instance of a string:str.upper().

Your task is to vectorize this Python method. numpy is loaded for you as np, and the names array is available.

Create a vectorized function called vectorized_upperfrom the Python .upper() string method.
Apply vectorized_upper() to the namesarray and save the resulting array as uppercase_names.

# edited/added
names = np.array([["Izzy", "Monica", "Marvin"],
                  ["Weber", "Patel", "Hernandez"]])

# Vectorize the .upper() string method
vectorized_upper = np.vectorize(str.upper)

# Apply vectorized_upper to the names array
uppercase_names = vectorized_upper(names)
print(uppercase_names)
     
[['IZZY' 'MONICA' 'MARVIN']
 ['WEBER' 'PATEL' 'HERNANDEZ']]
Broadcasting
Broadcastable or not?
Broadcasting takes the power of vectorized operations in NumPy one step further, saving memory and computing power. But before broadcasting, you’ll need to check whether it’s even possibleto use broadcasting in your mathematical operations!

Determine whether or not the array shapes given are broadcastable without reshaping.
Broadcastable
(3, 4) and (1, 4)
(3, 4) and (4, )
(3, 4) and (3, 1)
Not Broadcastable
(3, 4) and (1, 2)
(3, 4) and (4, 1)
(3, 4) and (3, )
Broadcasting across columns
Recall that when broadcasting across columns, NumPy requires you to be explicit that it should broadcast a vertical array, and horizontal and vertical 1D arrays do not exist in NumPy. Instead, you must first create a 2D array to declare that you have vertical data. Then, NumPy creates a copy of this 2D vertical array for each column and applies the desired operation.

A Python list called monthly_growth_rate withlen() of 12 is available. This list represents monthly year-over-year expected growth for the economy; your task is to use broadcasting to multiply this list by each column in themonthly_sales array. The monthly_sales array is loaded, along with numpy as np.

Convert monthly_growth_rate, currently a Python list, into a one-dimensional NumPy array calledmonthly_growth_1D.
Reshape monthly_growth_1D so that it is broadcastable column-wise across monthly_sales; call the new arraymonthly_growth_2D.
Using broadcasting, multiply each column inmonthly_sales by monthly_growth_2D.

monthly_growth_rate = [1.01, 1.03, 1.03, 1.02, 1.05, 1.03, 1.06, 1.04, 1.03, 1.04, 1.02, 1.01]

# Convert monthly_growth_rate into a NumPy array
monthly_growth_1D = np.array(monthly_growth_rate)

# Reshape monthly_growth_1D
monthly_growth_2D = monthly_growth_1D.reshape((12, 1))
print(monthly_growth_2D)

# Multiply each column in monthly_sales by monthly_growth_2D
print(monthly_growth_2D * monthly_sales)
     
[[1.01]
 [1.03]
 [1.03]
 [1.02]
 [1.05]
 [1.03]
 [1.06]
 [1.04]
 [1.03]
 [1.04]
 [1.02]
 [1.01]]
[[ 4175.34 24164.25  8743.57]
 [ 4239.48 24591.25  9416.26]
 [ 4813.19 28012.91 10964.35]
 [ 4671.6  26149.74 10665.12]
 [ 5364.45 29394.75 11863.95]
 [ 5161.33 28241.57 10943.75]
 [ 5559.7  28943.3  11267.8 ]
 [ 5480.8  28870.4  12012.  ]
 [ 4820.4  25737.64 10054.86]
 [ 5109.52 26834.08 10874.24]
 [ 5418.24 25913.1  13669.02]
 [ 6696.3  28074.97 18587.03]]
Broadcasting across rows
In the last set of exercises, you usedmonthly_industry_multipliers, to create sales predictions. Recall that monthly_industry_multipliers looks like this:

array([[0.98, 1.02, 1.  ],
       [1.00, 1.01, 0.97],
       [1.06, 1.03, 0.98],
       [1.08, 1.01, 0.98],
       [1.08, 0.98, 0.98],
       [1.1 , 0.99, 0.99],
       [1.12, 1.01, 1.  ],
       [1.1 , 1.02, 1.  ],
       [1.11, 1.01, 1.01],
       [1.08, 0.99, 0.97],
       [1.09, 1.  , 1.02],
       [1.13, 1.03, 1.02]])
Assume you’re not comfortable being so specific with your estimates. Rather, you’d like to use monthly_industry_multipliers to find a single average multiplier for each industry. Then you’ll use that multiplier to project next year’s sales.

numpy is loaded for you as np, and themonthly_sales and monthly_industry_multipliersarrays are available. The monthly_sales columns in order refer to liquor store, restaurant, and department store sales.

Find the mean sales projection multiplier for each industry; save in an array called mean_multipliers.
Print the shapes of mean_multipliers andmonthly_sales to ensure they are suitable for broadcasting.
Multiply each monthly sales value by the mean multiplier you found for that industry; save in an array calledprojected_sales.

# Find the mean sales projection multiplier for each industry
mean_multipliers = np.mean(monthly_industry_multipliers, axis=0)
print(mean_multipliers)

# Print the shapes of mean_multipliers and monthly_sales
print(mean_multipliers.shape, monthly_sales.shape)

# Multiply each value by the multiplier for that industry
projected_sales = monthly_sales * mean_multipliers
print(projected_sales)
     
[1.0775     1.00833333 0.99333333]
(3,) (12, 3)
[[ 4454.385      24124.375       8599.28666667]
 [ 4434.99       24073.95833333  9081.05333333]
 [ 5035.1575     27423.64166667 10574.03333333]
 [ 4934.95       25850.64166667 10386.29333333]
 [ 5504.9475     28228.29166667 11223.67333333]
 [ 5399.3525     27647.49166667 10554.16666667]
 [ 5651.4875     27532.54166667 10559.13333333]
 [ 5678.425      27991.33333333 11473.        ]
 [ 5042.7        25196.23333333  9696.92      ]
 [ 5293.7575     26017.01666667 10386.29333333]
 [ 5723.68       25616.70833333 13311.66      ]
 [ 7143.825      28028.64166667 18280.31333333]]
Array Transformations
NumPy meets the art world in this final chapter as we use image data from a Monet masterpiece to explore how you can use to augment image data. You’ll use flipping and transposing functionality to quickly transform our masterpiece. Next, you’ll pull the Monet array apart, make changes, and reconstruct it using array stacking to see the results.

Saving and loading arrays
Loading .npy files
The exercises for this chapter will use a NumPy array holding an image in RGB format. Which image? You’ll have to load the array from themystery_image.npy file to find out!

numpy is loaded as np, andmystery_image.npy is available.

Load the mystery_image.npy file using the aliasf, saving the contents as an array calledrgb_array.

!wget "https://assets.datacamp.com/production/repositories/5980/datasets/4f8315007ca8ddd7c4ad1d4be8cfe96f2877d141/rgb_array.npy"
     
--2025-11-10 11:31:44--  https://assets.datacamp.com/production/repositories/5980/datasets/4f8315007ca8ddd7c4ad1d4be8cfe96f2877d141/rgb_array.npy
Resolving assets.datacamp.com (assets.datacamp.com)... 172.64.144.94, 104.18.43.162
Connecting to assets.datacamp.com (assets.datacamp.com)|172.64.144.94|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1707203 (1.6M) [application/octet-stream]
Saving to: ‘rgb_array.npy’

rgb_array.npy       100%[===================>]   1.63M  --.-KB/s    in 0.1s    

2025-11-10 11:31:44 (14.8 MB/s) - ‘rgb_array.npy’ saved [1707203/1707203]


with open("rgb_array.npy", "rb") as f:
    rgb_array = np.load(f)

plt.imshow(rgb_array)
plt.show()
     

Getting help
You’ll need to use the .astype() array method we covered in the first chapter of this course for the next exercise. If you forget exactly how .astype() works, you could check out the course slides or NumPy’s documentation on numpy.org. There is, however, an even faster way to jog your memory…

numpy is loaded as np.

Return NumPy’s documentation text for .astype().

# Display the documentation for .astype()
help(np.ndarray.astype)
     
Help on method_descriptor:

astype(...) unbound numpy.ndarray method
    a.astype(dtype, order='K', casting='unsafe', subok=True, copy=True)

    Copy of the array, cast to a specified type.

    Parameters
    ----------
    dtype : str or dtype
        Typecode or data-type to which the array is cast.
    order : {'C', 'F', 'A', 'K'}, optional
        Controls the memory layout order of the result.
        'C' means C order, 'F' means Fortran order, 'A'
        means 'F' order if all the arrays are Fortran contiguous,
        'C' order otherwise, and 'K' means as close to the
        order the array elements appear in memory as possible.
        Default is 'K'.
    casting : {'no', 'equiv', 'safe', 'same_kind', 'unsafe'}, optional
        Controls what kind of data casting may occur. Defaults to 'unsafe'
        for backwards compatibility.

        * 'no' means the data types should not be cast at all.
        * 'equiv' means only byte-order changes are allowed.
        * 'safe' means only casts which can preserve values are allowed.
        * 'same_kind' means only safe casts or casts within a kind,
          like float64 to float32, are allowed.
        * 'unsafe' means any data conversions may be done.
    subok : bool, optional
        If True, then sub-classes will be passed-through (default), otherwise
        the returned array will be forced to be a base-class array.
    copy : bool, optional
        By default, astype always returns a newly allocated array. If this
        is set to false, and the `dtype`, `order`, and `subok`
        requirements are satisfied, the input array is returned instead
        of a copy.

    Returns
    -------
    arr_t : ndarray
        Unless `copy` is False and the other conditions for returning the input
        array are satisfied (see description for `copy` input parameter), `arr_t`
        is a new array of the same shape as the input array, with dtype, order
        given by `dtype`, `order`.

    Notes
    -----
    .. versionchanged:: 1.17.0
       Casting between a simple data type and a structured one is possible only
       for "unsafe" casting.  Casting to multiple fields is allowed, but
       casting from multiple fields is not.

    .. versionchanged:: 1.9.0
       Casting from numeric to string types in 'safe' casting mode requires
       that the string dtype length is long enough to store the max
       integer/float value converted.

    Raises
    ------
    ComplexWarning
        When casting from complex to float or int. To avoid this,
        one should use ``a.real.astype(t)``.

    Examples
    --------
    >>> x = np.array([1, 2, 2.5])
    >>> x
    array([1. ,  2. ,  2.5])

    >>> x.astype(int)
    array([1, 2, 2])

Update and save
Perhaps you are training a machine learning model to recognize ocean scenes. You’d like the model to understand that oceans are not only associated with bright, summery colors, so you’re careful to include images of oceans in bad weather or evening light as well. You may have to manually transform some images in order to balance the data, so your task is to darken the Monet ocean scene rgb_array.

Recall from the video that white is associated with the maximum RGB value of 255, while darker colors are associated with lower values.numpy is loaded as np, and the 3D Monetrgb_array that you loaded in the last exercise is available.

Reduce every value in rgb_array by 50 percent, saving the resulting array as darker_rgb_array.
Since RGB values must be integers, convertdarker_rgb_array into an array of integers calleddarker_rgb_int_array so that it can be plotted.
Save darker_rgb_int_array as an .npy file called darker_monet.npy using the aliasf.

# edited/added
rgb_array = np.load('rgb_array.npy')

# Reduce every value in rgb_array by 50 percent
darker_rgb_array = rgb_array / 2

# Convert darker_rgb_array into an array of integers
darker_rgb_int_array = darker_rgb_array.astype(int)
plt.imshow(darker_rgb_int_array)
plt.show()

# Save darker_rgb_int_array to an .npy file called darker_monet.npy
with open("darker_monet.npy", "wb") as f:
    np.save(f, darker_rgb_int_array)
     

Array acrobatics
Augmenting Monet
Perhaps you’re still working on that machine learning model that identifies ocean scenes in paintings. You’d like to generate a few extra images to augment your existing data. After all, a human can tell that a painting is of an ocean even if the painting is upside-down: why shouldn’t your machine learning model?

numpy is loaded as np, and the 3D Monetrgb_array is available.

Flip rgb_array so that it is the mirror image of the original, with the ocean on the right and grassy knoll on the left.

Flip rgb_array so that it is upside down but otherwise remains the same.


# Flip rgb_array so that it is the mirror image of the original
mirrored_monet = np.fliplr(rgb_array)
plt.imshow(mirrored_monet)
plt.show()

# Flip rgb_array so that it is upside down
upside_down_monet = np.flipud(rgb_array)
plt.imshow(upside_down_monet)
plt.show()
     


Transposing your masterpiece
You’ve learned that transposing an array reverses the order of the array’s axes. To transpose the axes in a different order, you can pass the desired axes order as arguments. You’ll practice with the 3D Monetrgb_array, loaded for you. numpy has been imported as np.

Transpose the 3-D rgb_array so that the image appears rotated 90 degrees left and as a mirror image of itself.

# Transpose rgb_array
transposed_rgb = np.transpose(rgb_array, axes=(1, 0, 2))
plt.imshow(transposed_rgb)
plt.show()
     

Stacking and splitting
2D split and stack
Splitting and stacking skills aren’t just useful with 3D RGB arrays: they are excellent for subsetting and organizing data of any type and dimension!

You’ll now take a quick trip down memory lane to reorganize themonthly_sales array as a 3D array. Recall that the first dimension of monthly_sales is rows of a single month’s sales across three industries, and the second dimension is columns of monthly sales data for a single industry.

Your task is to split this data into quarterly sales data and stack the quarterly sales data so that the new third dimension represents the four 2D arrays of quarterly sales.numpy is loaded asnp, and the monthly_sales array is available.

Split monthly_sales into four arrays representing quarterly data across industries; print q1_sales.
Stack the four quarterly sales arrays to create a 3D array,quarterly_sales, made up of the four quarterly 2D arrays in order from the first to last quarter.

# Split monthly_sales into quarterly data
q1_sales, q2_sales, q3_sales, q4_sales = np.split(monthly_sales, 4)
print(q1_sales)

# Stack the four quarterly sales arrays
quarterly_sales = np.stack((q1_sales, q2_sales, q3_sales, q4_sales))
print(quarterly_sales)
     
[[ 4134 23925  8657]
 [ 4116 23875  9142]
 [ 4673 27197 10645]]
[[[ 4134 23925  8657]
  [ 4116 23875  9142]
  [ 4673 27197 10645]]

 [[ 4580 25637 10456]
  [ 5109 27995 11299]
  [ 5011 27419 10625]]

 [[ 5245 27305 10630]
  [ 5270 27760 11550]
  [ 4680 24988  9762]]

 [[ 4913 25802 10456]
  [ 5312 25405 13401]
  [ 6630 27797 18403]]]
Splitting RGB data
Perhaps you’d like to better understand Monet’s use of the color blue. Your task is to create a version of the Monetrgb_array that emphasizes parts of the painting that use lots of blue by making them even bluer! You’ll perform the splitting portion of this task in this exercise and the stacking portion in the next.

numpy is loaded as np, and the Monetrgb_array is available.

Split the Monet rgb_array into red, green, and blue only pixel data; save the results as as red_array,green_array, and blue_array.
Create emphasized_blue_array, which replacesblue_array values with 255 if they are higher than the mean value of blue_array; otherwise, the value remains the same.
Print the .shape ofemphasized_blue_array.
Reshape emphasized_blue_array to remove the trailing third dimension; save as emphasized_blue_array_2D.

# Split rgb_array into red, green, and blue arrays
red_array, green_array, blue_array = np.split(rgb_array, 3, axis=2)

# Create emphasized_blue_array
emphasized_blue_array = np.where(blue_array > blue_array.mean(), 255, blue_array)

# Print the shape of emphasized_blue_array
print(emphasized_blue_array.shape)

# Remove the trailing dimension from emphasized_blue_array
emphasized_blue_array_2D = np.squeeze(emphasized_blue_array)
     
(675, 843, 1)
Stacking RGB data
Now you’ll combine red_array, green_array, and emphasized_blue_array_2D to see what Monet’s painting looks like with the blues emphasized!

numpy is loaded as np, and thered_array, green_array,blue_array and emphasized_blue_array_2Dobjects that you created in the last exercise are available.

Print the shapes of blue_array andemphasized_blue_array_2D.
Reshape red_array and green_array so that they can be stacked with emphasized_blue_array_2D.
Stack red_array_2D, green_array_2D, andemphasized_blue_array_2D together (in that order) into a 3D array called emphasized_blue_monet.

# Print the shapes of blue_array and emphasized_blue_array_2D
print(blue_array.shape, emphasized_blue_array_2D.shape)

# Reshape red_array and green_array
red_array_2D = red_array.reshape((675, 843))
green_array_2D = green_array.reshape((675, 843))

# Stack red_array_2D, green_array_2D, and emphasized_blue_array_2D
emphasized_blue_monet = np.stack((red_array_2D, green_array_2D, emphasized_blue_array_2D), axis=-1) # Stack along the last axis
plt.imshow(emphasized_blue_monet)
plt.show()
     
(675, 843, 1) (675, 843)

Congratulations!
Congratulations!
You made it!

Welcome to team NumPy
You’re now a card-carrying member of Team NumPy. I hope I’ve convinced you that NumPy is amazing.

NumPy is amazing!
It leverages the immense calculating power of C while keeping the friendly syntax of Python. In some places, it even makes Python syntax simpler by vectorizing operations!

What’s next?
What’s next on your NumPy journey? You could check out one of the many libraries built on top of NumPy’s API. Perhaps you’d like to explore data analysis with pandas, data visualization with Seaborn, parallel programming with Dask, machine learning with scikit-learn, or deep learning with TensorFlow. Every one of these libraries is built on top of NumPy, and DataCamp has courses dedicated to all of them.

Congratulations
No matter where you take your NumPy knowledge, thanks for taking this course all the way to the end. I’m Izzy Weber, and on behalf of all of us at GLA, congratulations on your wide new array of NumPy skills!

Thank you!
Thanks again!
