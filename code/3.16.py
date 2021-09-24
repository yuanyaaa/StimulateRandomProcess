import random
import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import mark_inset
from mpl_toolkits.axes_grid1.inset_locator import inset_axes



class QuickSort:
    def __init__(self):
        self.epoch = 10000
        self.nrange = 51
        self.E_Rn_x = []
        self.E_Rn_y = []
        self.compare_nums = 0

    def Q(self):
        for n in range(2, self.nrange):
            average_com = 0
            print(n)
            init = [i for i in range(0, n)]
            for i in range(self.epoch):
                # print(i)
                random.shuffle(init)
                self.compare_nums = 0
                quick_sort = init.copy()
                self.quick_sort(quick_sort, 0, n-1)
                # print('compare nums', self.compare_nums)
                average_com += self.compare_nums / self.epoch
                # print(average_com)
            self.E_Rn_x.append(n)
            self.E_Rn_y.append(average_com)

        fig, ax = plt.subplots(1, 1)
        x = range(2, self.nrange)
        y = [2 * (i + 1) * (
                2 * math.log(i + 1, math.e) - math.log(i, math.e) + math.log(1, math.e) - 2 * math.log(2, math.e))
             for i in x]
        handle_1, = ax.plot(x, y, lw=6, color='thistle')
        handle_2, = ax.plot(self.E_Rn_x, self.E_Rn_y, color='darkslategray')
        plt.legend(handles=[handle_1, handle_2], labels=['2(n+1)ln(n+1)', 'E'], loc='best')
        self.plot_config(True, 'Num of People', 'E(Cn)', 'E(Cn)', '3_14_3_epoch' + str(self.epoch) + '.pdf')
        # plt.show()
        # plt.savefig('test.pdf')

        # 嵌入绘制局部放大图的坐标系
        axins = inset_axes(ax, width="40%", height="30%", loc='lower left',
                           bbox_to_anchor=(0.5, 0.1, 1, 1),
                           bbox_transform=ax.transAxes)

        axins.plot(x, y, lw=6, color='thistle')
        axins.plot(self.E_Rn_x, self.E_Rn_y, color='darkslategray')
        # 设置放大区间
        zone_left = 45
        zone_right = 47

        # 坐标轴的扩展比例（根据实际数据调整）
        x_ratio = 0.5  # x轴显示范围的扩展比例
        y_ratio = 1  # y轴显示范围的扩展比例

        # X轴的显示范围
        xlim0 = x[zone_left] - (x[zone_right] - x[zone_left]) * x_ratio
        xlim1 = x[zone_right] + (x[zone_right] - x[zone_left]) * x_ratio

        # Y轴的显示范围
        y = np.hstack((self.E_Rn_y[zone_left:zone_right], self.E_Rn_y[zone_left:zone_right]))
        ylim0 = np.min(y) - (np.max(y) - np.min(y)) * y_ratio
        ylim1 = np.max(y) + (np.max(y) - np.min(y)) * y_ratio

        # 调整子坐标系的显示范围
        axins.set_xlim(xlim0, xlim1)
        axins.set_ylim(ylim0, ylim1)

        # 建立父坐标系与子坐标系的连接线
        # loc1 loc2: 坐标系的四个角
        # 1 (右上) 2 (左上) 3(左下) 4(右下)
        mark_inset(ax, axins, loc1=3, loc2=1, fc="none", ec='k', lw=1)
        # plt.gca().add_artist(l1)
        self.plot_config(True, 'Num of People', 'E(Cn)', 'E(Cn)', '3_16.png')
        plt.savefig('3_16_epoch' + str(self.epoch) + '.pdf')

    def quick_sort(self, quick_sort, left, right):
        if left < right:
            left_pivot = self.merge(quick_sort, left, right)
            self.quick_sort(quick_sort, left, left_pivot - 1)
            self.quick_sort(quick_sort, left_pivot+1, right)

    def merge(self, quick_sort, left, right):
        pivot = quick_sort[left]
        # print(quick_sort, left, right)
        while left < right:
            while left < right and quick_sort[right] >= pivot:
                self.compare_nums += 1
                right -= 1
            quick_sort[left] = quick_sort[right]
            while left < right and quick_sort[left] <= pivot:
                self.compare_nums += 1
                left += 1
            quick_sort[right] = quick_sort[left]
        quick_sort[right] = pivot
        return left

    def plot_config(self, grid: bool, xlabel: str, ylabel: str, title: str, fig: str):
        if grid:
            plt.grid(linestyle='-.')
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.savefig(fig)


if __name__ == '__main__':
    match_turn = QuickSort()
    match_turn.Q()
