import time
import csv
import numpy
import sys
import random

# Required array length is provided as a command line argument
if __name__ == '__main__':
  required_array_length = sys.argv[1]
else:
  required_array_length = 1


# Create random array
def create_random_array(required_array_length):
  return numpy.random.randint(1,101,int(required_array_length))

# Function to test here:
def function_to_test(array):
  array.sort()


# Timing Framework
def return_function_runtime(required_array_length = required_array_length, function = function_to_test):
  array = create_random_array(required_array_length)
  start = time.perf_counter()
  function(array)
  end = time.perf_counter()
  return end - start

# Calculating Spreadsheet values
time_elapsed = return_function_runtime(required_array_length, function_to_test)
print('Array length:',required_array_length,'Runtime:', time_elapsed )

# Writes to spreadsheet
with open('./sort/data.csv', 'a') as f:
  writer = csv.writer(f)
  writer.writerow([time_elapsed, required_array_length])
  f.close()

# TODO: 
# - Create better file structure (one file for algos, one for results)
# - Let timing take command line argument of another file name which it then runs and times
# - Create a function that returns an array of random length