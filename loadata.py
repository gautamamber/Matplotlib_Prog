import matplotlib.pyplot as plt
import csv #to read file
x = []
y = []
with open('file','r') as csvfile:
	plots = csv.reader(csvfile, delimiter = ',')
	for row in plots:
		x.append(int (row[0]))
		y.append(int (row[1]))

plt.plot(x,y)
plt.xlabel('plot no')
plt.ylabel('plo')
plt.title('first graph')
plt.legend()
plt.show()

#load data from files