import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import spline
import numpy as np
import setupaxis


class PreProcess(object):

    def __init__(self, file_path):
        f = open(file_path)
        self.__data = pd.read_csv(f, names=['kst', 'seconds', 'value'])

        print(self.__data.columns)

        print(self.__data.get('seconds'))

    def process(self):
        # sample_id = np.arange(1000, 20000, 5000)

        # sample_val = spline(self.__data.get('kst'), self.__data.get('value'), sample_id)

        # plt.plot(sample_id, sample_val, 'ro')
        # plt.plot(self.__data.get('kst'), self.__data.get('value'))

        sample_idx_7 = [36600, 42200, 47400, 52600, 57800, 114600, 120200, 143000, 158000, 163400, 197400, 202400,
                        207400, 212600, 220000, 244800, 250000, 255200, 260800, 279800, 325600, 340800, 368600, 394400,
                        415600]

        sample_idx_2 = [87400, 92800, 99200, 105200, 119400, 254400, 259800, 265000, 270400, 275200, 312000, 318800,
                        324000, 328400, 333800, 492200, 497200, 502200, 507600, 513000, 647400, 653000, 658400, 665800,
                        689400]
        sample_idx_3 = [16600, 22800, 27800, 33200, 38400, 225400, 231000, 236200, 241400, 293200, 337400, 342800,
                        348000, 565000, 570200, 618000, 711600, 717200, 857000, 864000, 735400, 740800, 746000, 874400,
                        897400]
        sample_idx = sample_idx_7
        true_val_7 = [99, 99, 99, 99, 99, 89, 90, 91, 94, 95, 88, 89, 90, 88, 87, 81, 83, 86, 86, 66, 71, 82, 68, 80,
                      64]
        true_val_2 = [98, 98, 98, 98, 98, 93, 92, 92, 91, 91, 92, 88, 88, 87, 86, 83, 81, 79, 81, 80, 74, 73, 72, 65,
                      71]
        true_val_3 = [97, 98, 98, 98, 98, 91, 90, 90, 89, 93, 87, 85, 84, 92, 92, 78, 81, 81, 81, 82, 79, 76, 76, 78,
                      90]

        true_val = true_val_7

        plt.plot(sample_idx, true_val, 'rx')
        setupaxis.setup_axis()
        plt.show()

        return self.__data


if __name__ == '__main__':
    rawData = '''D:\githome\spo2analysistech\SPO2Analysis\SPo2Data_8.csv'''
    print(rawData)
    my_data = PreProcess(rawData)
    my_data.process()
