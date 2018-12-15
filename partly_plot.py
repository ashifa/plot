import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

import setupaxis
from PreProcess import PreProcess


def my_plot(layout, data):
    print(layout)
    plt.subplot(4, 1, layout)
    plt.plot(data.get_values(), color='black', linewidth=0.5)
    setupaxis.setup_axis()


if __name__ == '__main__':
    path = 'C:\\Users\\user\\Downloads\\'
    filename = 'processed_ecg.xlsx'
    # filename = '29.xlsx'

    # path = r'C:\Users\user\Desktop\整机\典型927\朱媛媛\\'
    # filename = r'16：57.xlsx'

    fullpath_name = path + filename

    my_data = PreProcess(fullpath_name).process(False)

    plt.figure(figsize=(20, 4))
    plt.subplots_adjust(bottom=0, top=1, left=0, right=1, hspace=0)

    plt.plot(my_data.get_values(), color='black', linewidth=0.5)
    setupaxis.setup_axis(False)

    plt.show()
    plt.savefig(filename.replace('xlsx', 'png'))
