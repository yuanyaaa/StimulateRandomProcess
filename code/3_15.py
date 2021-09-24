import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import mark_inset
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
import random

if __name__ == '__main__':
    epochs = [100, 1000, 10000]
    first_axis = 7
    second_axis = 1
    array = np.zeros([len(epochs), first_axis])
    index = -1
    p = 0.5
    for epoch, e_index in zip(epochs, range(len(epochs))):
        print(epoch, e_index)
        index = -1
        for k in range(1, 8):
            # k = 3
        # for p in np.linspace(0.3, 1, first_axis):
            index += 1
            average = 0
            for i in range(epoch):
                sum_ = 0
                now = 0
                while now < k:
                    r = random.random()
                    if r < p:
                        now += 1
                    else:
                        now = 0
                    sum_ += 1
                average += sum_ / epoch
            # print(k)
            array[e_index, index] = average

    fig, ax = plt.subplots(1, 1)
    x = range(1, 8)
    y_tmp = [pow(1/p, x_) for x_ in x]
    print([y_tmp[0:m] for m in range(1, 8)])
    y = [sum(y_tmp[0:m]) for m in range(1, 8)]
    # y = [1/x_ + 1/x_/x_ + 1/x_/x_/x_ for x_ in x]
    handle_1, = ax.plot(x, y, lw=6, color='navajowhite')
    handle_2, = ax.plot(x, array[0], color='tomato', linestyle='--')
    handle_3, = ax.plot(x, array[1], color='violet', linestyle='--')
    handle_4, = ax.plot(x, array[2], color='aqua', linestyle='--')
    plt.xlabel('K')
    plt.ylabel('Value')
    plt.title('Simulate')
    ax.legend(handles=[handle_1, handle_2, handle_3, handle_4], labels=[' Theoretical value ', 'simulate: epoch=100', 'simulate: epoch=1000', 'simulate: epoch=10000'], loc='best')

    # # 嵌入绘制局部放大图的坐标系
    # axins = inset_axes(ax, width="40%", height="30%", loc='lower left',
    #                    bbox_to_anchor=(0.5, 0.1, 1, 1),
    #                    bbox_transform=ax.transAxes)
    #
    # axins.plot(x, y, lw=6, color='navajowhite')
    # axins.plot(x, array[0], color='tomato', linestyle='--')
    # axins.plot(x, array[1], color='violet', linestyle='--')
    # axins.plot(x, array[2], color='aqua', linestyle='--')
    # # 设置放大区间
    # zone_left = 5
    # zone_right = 6
    #
    # # 坐标轴的扩展比例（根据实际数据调整）
    # x_ratio = 0.5  # x轴显示范围的扩展比例
    # y_ratio = 1  # y轴显示范围的扩展比例
    #
    # # X轴的显示范围
    # xlim0 = x[zone_left] - (x[zone_right] - x[zone_left]) * x_ratio
    # xlim1 = x[zone_right] + (x[zone_right] - x[zone_left]) * x_ratio
    #
    # # Y轴的显示范围
    # y = np.hstack((y[zone_left:zone_right], y[zone_left:zone_right]))
    # ylim0 = np.min(y) - (np.max(y) - np.min(y)) * y_ratio
    # ylim1 = np.max(y) + (np.max(y) - np.min(y)) * y_ratio
    #
    # # 调整子坐标系的显示范围
    # axins.set_xlim(xlim0, xlim1)
    # axins.set_ylim(ylim0, ylim1)
    #
    # # 建立父坐标系与子坐标系的连接线
    # # loc1 loc2: 坐标系的四个角
    # # 1 (右上) 2 (左上) 3(左下) 4(右下)
    # mark_inset(ax, axins, loc1=2, loc2=2, fc="none", ec='k', lw=1)
    plt.savefig("3_15p0.5k3.pdf")
    plt.show()