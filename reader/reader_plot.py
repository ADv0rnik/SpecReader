import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

from . import DATA_DIR

CURRENT_DATE = datetime.strftime(datetime.now(), '%Y-%m-%d')


class Plot:
    def __init__(self):
        self.df = None

    def make_plot(self):
        try:
            self.df = pd.read_csv(DATA_DIR + "/spec_data.csv")
            x = self.df['Energy']
            y = self.df['CPS']
            fig, ax = plt.subplots(figsize=(12, 8), dpi=300)
            ax.fill_between(x, y, color='blue')
            ax.set_xlabel(
                'Energy, kev',
                fontsize=14,
                color='black'
            )
            ax.set_ylabel(
                'Counts per seconds',
                fontsize=14,
                color='black'
            )
            ax.set_xlim(xmin=0)
            ax.set_ylim(ymin=0)
            ax.grid(axis='x')
        except FileNotFoundError as err:
            print(err)

    @staticmethod
    def show_plot():
        plt.show()

    @staticmethod
    def save_plot():
        plt.savefig(DATA_DIR + f"/spectrum_{CURRENT_DATE}.png", dpi=300)




