import time
import csv

input_arr= []#input_array is created here

# Timing Framework
start = time.perf_counter()
# Code goes here
end = time.perf_counter()

# Calculating Spreadsheet values
time_elapsed = end - start
element_numb = len(input_arr)

# Writes to spreadsheet
with open('./data.csv', 'w') as f:
  writer = csv.writer(f)
  writer.writerow([time_elapsed, element_numb])
