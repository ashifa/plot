import matplotlib.pyplot as plt


def setup_axis():
    ax = plt.gca()

    # ax.xaxis.set_major_locator(plt.MultipleLocator(50.0))  # 设置x主坐标间隔 1
    # ax.xaxis.set_minor_locator(plt.MultipleLocator(10.0))  # 设置x从坐标间隔 0.1
    ax.yaxis.set_major_locator(plt.FixedLocator([70, 77, 78, 84, 85, 92, 97, 100, ]))  # 设置y主坐标间隔 1
    ax.yaxis.set_minor_locator(plt.MultipleLocator(1))  # 设置y从坐标间隔 0.1

    ax.spines['top'].set_linewidth(0.2)
    ax.spines['bottom'].set_linewidth(0.2)
    ax.spines['left'].set_linewidth(0.2)
    ax.spines['right'].set_linewidth(0.2)
    #
    ax.grid(which='major', linewidth=0.2, linestyle='-')
    ax.grid(which='minor', linewidth=0.1, linestyle='-')
    # ax.set_xticklabels([])#标记x轴主坐标的值,在这里设为空值，则表示坐标无数值标定；其他情况如
    # ax.set_yticklabels([])

#  ax.tick_params(axis='both', which='both', length=0, bottom=False, left=False, labelbottom=False, labelleft=False)

# plt.ylim(-1.5, 2.5)
# plt.xlim(0, 2500)
