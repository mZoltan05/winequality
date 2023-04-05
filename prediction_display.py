import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd


class PredictionDisplay:
    @staticmethod
    def save_result(predicted_data: pd.DataFrame, actual_data: pd.DataFrame, path: str ):
        sns.set_theme()
        ax1 = sns.kdeplot(actual_data,color='r',label='actual_data')
        sns.kdeplot(predicted_data,color='b',ax=ax1,label='predicted_data')

        plt.legend()
        plt.xlabel('Level')
        plt.ylabel('Density')
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        if len(path) > 0:
            plt.savefig(path+f"plot_{timestamp}.png")
        else:
            plt.savefig(f"plot_{timestamp}.png")