# matplotlib画廊
# 绘制简单的折线图
import matplotlib.pyplot as plt
input_value=[1,2,3,4,5]
squares = [1,4,9,16,25]
plt.plot(input_value,squares,linewidth=5)
# 修改标签文字和线条粗细
plt.title('the squares')
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value",fontsize=14)
plt.tick_params(axis='both',labelsize=14)
plt.show()