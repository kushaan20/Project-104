import csv 

with open('HeightWeight.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)
file_data.pop(0)
new_data = []
for i in range(len(file_data)):
    n = file_data[i][1]
    new_data.append(float(n))
num = len(new_data)
total = 0 
for x in new_data:
    total += x
mean = total/num
print("The mean is:", mean)

