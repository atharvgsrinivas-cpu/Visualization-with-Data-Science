import matplotlib.pyplot as plt
x = [0, 5, 10, 15, 20,25,30]
y1=[10,15,20,25,30,35,40]
y2=[20,25,30,35,40,45,50]
plt.plot(x,y1, linestyle='dashed',marker='D')
plt.plot(x,y2, linestyle='dashed',marker='D')
plt.title('velocity-time graph')
plt.xlabel('velocity m/s')
plt.ylabel('time s')
plt.ylim(0, 50)
plt.ylim(5,25)
plt.legend()
plt.show()