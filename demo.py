import numpy as np
steps1=np.array([[1,6012],[2,7079],[3,6886],[4,7230],[5,4598],[6,5564],[7,6941],[8,7763],[9,8063],[10,9569]])
print(steps1)
print('adding 2000')
steps1[:,1]+=2000
print(steps1)
print("gre")
steps_more_8000=steps1[steps1[:,1]>9000]
print(steps_more_8000)
print('sorted_steps')
sorted_steps=np.sort(steps1[:,1])
print(sorted_steps)
print('max_number')
max=np.max(steps1)
print(max)
print('min_number')
min=np.min(steps1)
print(min)