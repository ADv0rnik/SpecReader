import pandas as pd


class DfConstructor:
    def __init__(self):
        pass

    def get_dataframe(self, list1, list2, time):
        df = pd.Series(list1, list2).to_frame().reset_index()
        df.columns = ['Energy', 'Counts']
        df['CPS'] = df['Counts'] / int(time)
        return df
