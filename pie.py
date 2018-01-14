import matplotlib.pyplot as plt
slices = [2,3,5,6]
act = ['sleep','play','work','study']

plt.pie(slices,labels = act, startangle=90, shadow = True, explode = (0,.1,.2,.3) )
plt.xlabel('plot no')
plt.ylabel('plo')
plt.title('first graph')
plt.show()


#circular chart  sum is 100