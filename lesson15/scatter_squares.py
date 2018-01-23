import matplotlib.pyplot as plt
# 使用scatter() 绘制散点图并设置其样式
plt.scatter(2,4,s=100)
plt.tick_params(axis='both',which='major',labelsize=14)
# plt.show()


x_value = [1,2,3,4,5]
y_value = [1,4,9,16,25]
plt.scatter(x_value,y_value,s=100)
# plt.show()

# 自动计算数据
x_value = list(range(1,1001))
y_value = [x**2 for x in x_value]
# 设置颜色
# plt.scatter(x_value,y_value,c='red',s=10)
# 设置颜色映射
plt.scatter(x_value,y_value,c=y_value, cmap=plt.cm.Blues,edgecolor='none',s=10)

# 设置每个坐标的取值范围
plt.axis([0, 1200, 0, 1200000])
# plt.show()

# 自动保存图表
plt.savefig('squares_plt.png',bbox_inches='tight')
