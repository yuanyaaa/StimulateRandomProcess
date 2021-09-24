import numpy as np
import random
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import mark_inset
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

class MatchTurn:
    def __init__(self):
        self.epochs = [100, 1000, 10000]
        self.nrange = 51
        self.E_Rn_x = [[], [], []]
        self.E_Rn_y = [[], [], []]
        # print(self.E_Rn_x)

    def Q1(self):
        for n in range(2, self.nrange):
            print(n)
            for e_index, epoch in enumerate(self.epochs):
                print(e_index, epoch)
                average_Rn = 0
                for i in range(epoch):
                    init = [i for i in range(0, n)]
                    # print(init)
                    iter_nums = 0
                    # print(len(init))
                    while len(init) != 0:
                        old_init = init.copy()
                        # print('old', old_init)
                        random.shuffle(init)
                        # print(init)
                        init = [old_init[i] for i in range(len(init)) if init[i] != old_init[i]]
                        iter_nums += 1
                        # print(init)
                    average_Rn += iter_nums / epoch
                self.E_Rn_x[e_index].append(n)
                self.E_Rn_y[e_index].append(average_Rn)
        x = range(2, self.nrange)
        y = [x_ for x_ in x]
        fig, ax = plt.subplots(1, 1)
        handle_1, = plt.plot(x, y, lw=6, color='navajowhite')
        handle_2, = plt.plot(self.E_Rn_x[0], self.E_Rn_y[0], color='tomato', linestyle='--')
        handle_3, = plt.plot(self.E_Rn_x[1], self.E_Rn_y[1], color='violet', linestyle='--')
        handle_4, = plt.plot(self.E_Rn_x[2], self.E_Rn_y[2], color='aqua', linestyle='--')
        ax.legend(handles=[handle_1, handle_2, handle_3, handle_4],
                  labels=[' Theoretical value ', 'simulate: epoch=100', 'simulate: epoch=1000',
                          'simulate: epoch=10000'], loc='best')
        # plt.plot(self.E_Rn_x, self.E_Rn_y)
        # 嵌入绘制局部放大图的坐标系
        axins = inset_axes(ax, width="40%", height="30%", loc='lower left',
                           bbox_to_anchor=(0.5, 0.1, 1, 1),
                           bbox_transform=ax.transAxes)

        axins.plot(x, y, lw=6, color='navajowhite')
        axins.plot(self.E_Rn_x[0], self.E_Rn_y[0], color='tomato', linestyle='--')
        axins.plot(self.E_Rn_x[1], self.E_Rn_y[1], color='violet', linestyle='--')
        axins.plot(self.E_Rn_x[2], self.E_Rn_y[2], color='aqua', linestyle='--')
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
        y = np.hstack((self.E_Rn_y[2][zone_left:zone_right], self.E_Rn_y[2][zone_left:zone_right]))
        ylim0 = np.min(y) - (np.max(y) - np.min(y)) * y_ratio
        ylim1 = np.max(y) + (np.max(y) - np.min(y)) * y_ratio

        # 调整子坐标系的显示范围
        axins.set_xlim(xlim0, xlim1)
        axins.set_ylim(ylim0, ylim1)

        # 建立父坐标系与子坐标系的连接线
        # loc1 loc2: 坐标系的四个角
        # 1 (右上) 2 (左上) 3(左下) 4(右下)
        mark_inset(ax, axins, loc1=3, loc2=1, fc="none", ec='k', lw=1)

        self.plot_config(True, 'Num of People', 'E(Rn)', 'E(Rn)', '3_14_1_epoch10000.pdf')
        plt.savefig('3_14_1_epoch.pdf')

    def Q2(self):
        for n in range(2, self.nrange):
            print(n)
            for e_index, epoch in enumerate(self.epochs):
                print(e_index, epoch)
                average_Sn = 0
                for i in range(epoch):
                    init = [i for i in range(0, n)]
                    iter_nums = 0
                    while len(init) != 0:
                        old_init = init.copy()
                        iter_nums += len(old_init)
                        random.shuffle(init)
                        init = [old_init[i] for i in range(len(init)) if init[i] != old_init[i]]
                    average_Sn += iter_nums / epoch
                self.E_Rn_x[e_index].append(n)
                self.E_Rn_y[e_index].append(average_Sn)
        fig, ax = plt.subplots(1, 1)
        x = range(2, self.nrange)
        y = [x_ + x_ * x_ / 2 for x_ in x]
        handle_1, = plt.plot(x, y, lw=6, color='navajowhite')
        handle_2, = plt.plot(self.E_Rn_x[0], self.E_Rn_y[0], color='tomato', linestyle='--')
        handle_3, = plt.plot(self.E_Rn_x[1], self.E_Rn_y[1], color='violet', linestyle='--')
        handle_4, = plt.plot(self.E_Rn_x[2], self.E_Rn_y[2], color='aqua', linestyle='--')
        ax.legend(handles=[handle_1, handle_2, handle_3, handle_4],
                  labels=[' Theoretical value ', 'simulate: epoch=100', 'simulate: epoch=1000',
                          'simulate: epoch=10000'], loc='best')
        self.plot_config(True, 'Num of People', 'E(Sn)', 'E(Sn)', '3_14_2_epoch.pdf')

        # plt.plot(self.E_Rn_x, self.E_Rn_y)
        # 嵌入绘制局部放大图的坐标系
        axins = inset_axes(ax, width="40%", height="30%", loc='lower left',
                           bbox_to_anchor=(0.5, 0.1, 1, 1),
                           bbox_transform=ax.transAxes)

        axins.plot(x, y, lw=6, color='navajowhite')
        axins.plot(self.E_Rn_x[0], self.E_Rn_y[0], color='tomato', linestyle='--')
        axins.plot(self.E_Rn_x[1], self.E_Rn_y[1], color='violet', linestyle='--')
        axins.plot(self.E_Rn_x[2], self.E_Rn_y[2], color='aqua', linestyle='--')
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
        y = np.hstack((self.E_Rn_y[2][zone_left:zone_right], self.E_Rn_y[2][zone_left:zone_right]))
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
        self.plot_config(True, 'Num of People', 'E(Sn)', 'E(Sn)', '3_14_2_epoch100.pdf')
        plt.savefig('3_14_2_epoch.pdf')

    def Q3(self):
        for n in range(2, self.nrange):
            average_Cn = 0
            print(n)
            for i in range(self.epoch):
                init = [i for i in range(0, n)]
                iter_nums = 0
                while len(init) != 0:
                    old_init = init.copy()
                    random.shuffle(init)
                    init = [old_init[i] for i in range(len(init)) if init[i] != old_init[i]]
                    iter_nums += len(init)
                average_Cn += iter_nums / self.epoch / n
            self.E_Rn_x.append(n)
            self.E_Rn_y.append(average_Cn)
        fig, ax = plt.subplots(1, 1)
        x = range(2, self.nrange)
        y = [x_ / 2 for x_ in x]
        handle_1, = ax.plot(x, y, lw=6, color='thistle')
        handle_2, = ax.plot(self.E_Rn_x, self.E_Rn_y, color='darkslategray')
        self.plot_config(True, 'Num of People', 'E(Cn)', 'E(Cn)', '3_14_3_epoch' + str(self.epoch) + '.pdf')
        # plt.show()
        plt.legend(handles=[handle_1, handle_2], labels=['n/2', 'E(Cn)'], loc='best')
        # plt.savefig('test.pdf')

        # plt.plot(self.E_Rn_x, self.E_Rn_y)
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
        self.plot_config(True, 'Num of People', 'E(Cn)', 'E(Cn)', '3_14_3.png')
        plt.savefig('3_14_3_epoch' + str(self.epoch) + '.pdf')

    def plot_config(self, grid: bool, xlabel: str, ylabel: str, title: str, fig: str):
        if grid:
            plt.grid(linestyle='-.')
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        # plt.savefig(fig)
        # plt.show()


if __name__ == '__main__':
    match_turn = MatchTurn()
    match_turn.Q2()
