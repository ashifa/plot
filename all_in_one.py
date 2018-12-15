import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

import setupaxis
from PreProcess import PreProcess


def my_plot(layout, data):
    print(layout)
    plt.subplot(4, 1, layout)
    plt.plot(data.get_values()  , color='black', linewidth=0.5)
    setupaxis.setup_axis()


def genPdf(fullpath_name):
    my_data = PreProcess(fullpath_name).process()

    with PdfPages(fullpath_name.replace('xlsx', 'pdf'), keep_empty=True) as pdf:

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
                # each page contains 4 plotting
                pdf.savefig(papertype='a4')

                # start a new page to plot
                plt.figure(figsize=(10, 7))
                plt.subplots_adjust(bottom=0.05, top=0.95, left=0.05, right=0.95, hspace=0.05)

        # save the rest plotting
        if subplot_index != 3:
            pdf.savefig(papertype='a4')

if __name__ == '__main__':

    path = 'C:\\Users\\user\\Downloads\\'
    filename = 'processed_ecg.xlsx'
    #filename = '29.xlsx'

    #path = r'C:\Users\user\Desktop\整机\典型927\朱媛媛\\'
    #filename = r'16：57.xlsx'

    fullpath_name = path + filename
    genPdf(fullpath_name)
