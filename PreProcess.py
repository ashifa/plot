import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.backends.backend_pdf import PdfPages

import setupaxis


class PreProcess(object):

    def __init__(self, file_path):
        self.__data = pd.read_excel(file_path, names=['volt'])
        print(self.__data.columns)

    def process(self):
        clip_len = 100

        tmp = self.__data.head(clip_len)

        while tmp.max().volt < 0.1:
            self.__data = self.__data.slice_shift(-clip_len)
            tmp = self.__data.head(clip_len)

        self.add_step_signal()
        return self.__data

    def add_step_signal(self):
        my_list = []

        for i in range(0, 40):
            my_list.append(None)

        for i in range(0, 10):
            my_list.append(0)

        for i in range(0, 50):
            my_list.append(1)

        for i in range(0, 10):
            my_list.append(0)

        for i in range(0, 40):
            my_list.append(None)

        step_sig = pd.DataFrame({"volt": my_list})
        self.__data = step_sig.append(self.__data, ignore_index=True)
        print(self.__data)


if __name__ == '__main__':
    my_data = PreProcess('/Users/zyy/Desktop/607.xlsx')
    my_data.process()
