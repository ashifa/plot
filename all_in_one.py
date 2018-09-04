import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

import setupaxis
from PreProcess import PreProcess


def my_plot(layout, data):
    print(layout)
    plt.subplot(4, 1, layout)
    plt.plot(data.get_values(), color='black', linewidth=0.2)
    setupaxis.setup_axis()


if __name__ == '__main__':

    path = 'C:\\Users\\user\\Downloads\\'
    filename = '845.xlsx'

    my_data = PreProcess(path + filename).process()

    with PdfPages('all_in_one.pdf', keep_empty=True) as pdf:

        plt.figure(figsize=(10, 7))
        plt.subplots_adjust(bottom=0.05, top=0.95, left=0.05, right=0.95, hspace=0.05)

        subplot_index = -1
        slice_data_len = 2500

        while my_data.size > 0:
            print(my_data.size)
            subplot_index += 1
            subplot_index %= 4
            my_plot(subplot_index + 1, my_data.head(slice_data_len))

            my_data = my_data.slice_shift(-slice_data_len)
            if subplot_index == 3:
                pdf.savefig(papertype='a4')

                plt.figure(figsize=(10, 7))
                plt.subplots_adjust(bottom=0.05, top=0.95, left=0.05, right=0.95, hspace=0.05)

        if subplot_index != 3:
            pdf.savefig(papertype='a4')
