import matplotlib.pyplot as plt
# x = [x1 , x2]
# y = [y1 ,y2]
# input numbers
x1=float(input("enter x1 = "))
x2=float(input("enter x2 = "))
y1=float(input("enter y1 = "))
y2=float(input("enter y2 = "))
# Define x and y values for two sets of points
x = [x1 , x2]
y = [y1 ,y2]



# Create the plot and set the axis labels
plt.plot(x, y, label='Line')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Add a legend and show the plot
plt.legend()
plt.show()
