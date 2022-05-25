import csv

with open('height-weight.csv',newline='') as f:
     r = csv.reader( f )
     file_data = list( r )

file_data.pop(0)

new_data = []
for i in range( len(file_data) ):
     num = file_data[i][2] # weight column
     #type casting to float or else the value after point will not be there
     new_data.append( float(num) )


import statistics
print(f"The Mean is {statistics.mean(new_data)}")
print("\n")

print(f"The Median is {statistics.median(new_data)}")

print(f"The Mode is {statistics.mode(new_data)}")