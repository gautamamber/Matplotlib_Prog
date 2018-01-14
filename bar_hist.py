import matplotlib.pyplot as plt
x= [1,2,4,5,6]
y = [3,4,6,7,8]
pop = [1,2,3,5,6,7,8,9,7,6,4]
ids = [x for x in range (len(pop)) ]
plt.bar(ids,pop)
 # for bar plt.bar(x,y,label = "hello", color = '#000000')"""
plt.xlabel('plot no')
plt.ylabel('plo')
plt.title('first graph')
plt.show()