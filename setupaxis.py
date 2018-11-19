import numpy as np
import matplotlib.pyplot as plt


def setup_axis(is_multi_plot=True):
    ax = plt.gca()

    if is_multi_plot:
        ax.xaxis.set_major_locator(plt.MultipleLocator(50.0))  # 设置x主坐标间隔 1
        ax.xaxis.set_minor_locator(plt.MultipleLocator(10.0))  # 设置x从坐标间隔 0.1
    else:
        ax.xaxis.set_major_locator(plt.MultipleLocator(750.0))  # 设置x主坐标间隔 1
        ax.xaxis.set_minor_locator(plt.MultipleLocator(150.0))  # 设置x从坐标间隔 0.1
    ax.yaxis.set_major_locator(plt.MultipleLocator(0.5))  # 设置y主坐标间隔 1
    ax.yaxis.set_minor_locator(plt.MultipleLocator(0.1))  # 设置y从坐标间隔 0.1

    # ax.spines['top'].set_visible(False)  # 去掉上边框
    #  ax.spines['bottom'].set_visible(False)  # 去掉下边框
    #  ax.spines['left'].set_visible(False)  # 去掉左边框
    #  ax.spines['right'].set_visible(False)  # 去掉右边框

    ax.spines['top'].set_color('#f08689')
    ax.spines['bottom'].set_color('#f08689')
    ax.spines['left'].set_color('#f08689')
    ax.spines['right'].set_color('#f08689')
    ax.spines['top'].set_linewidth(0.2)
    ax.spines['bottom'].set_linewidth(0.2)
    ax.spines['left'].set_linewidth(0.2)
    ax.spines['right'].set_linewidth(0.2)
    #
    ax.grid(which='major', linewidth=0.6, linestyle='-', color='#f08689')
    ax.grid(which='minor', linewidth=0.3, linestyle='-', color='#f08689')
    # ax.set_xticklabels([])#标记x轴主坐标的值,在这里设为空值，则表示坐标无数值标定；其他情况如
    # ax.set_yticklabels([])

    ax.tick_params(axis='both', which='both', length=0, bottom=False, left=False, labelbottom=False, labelleft=False)



    if is_multi_plot:
        plt.xlim(0, 2500)
        plt.ylim(-1.5, 2.5)
    else:
        plt.ylim(-1, 1.5)
