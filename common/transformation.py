import pandas as pd


class Transformation:
    def __init__(self, df):
        """
        This is a constructor
        :param df: pd.DataFrame
        """
        self.df = df
        self.cond_dict = {1: 'Very_Bad', 2: 'Bad', 3: 'Good', 4: 'Very_Good', 5: 'Excellent'}

    def change_col_names(self, col_name_list):
        """
        This method is used to tranform........
        :param col_name_list: list: list of all the column names
        :return: dict:

        For Example:
            if the list contAINS ['a', 'b'], then the output will be {'a': 'A', 'b': 'B'}
        """
        col_name_dict = {}
        for col_name in col_name_list:
            if len(col_name) == 2:
                col_name_dict[col_name] = col_name.upper()
            elif col_name.count('_') == 0:
                col_name_dict[col_name] = col_name.capitalize()
            else:
                col_name_dict[col_name] = '_'.join([word.capitalize() for word in col_name.split('_')])

        return col_name_dict

    def convert_date(self, date_column):
        """

        :param date_column:
        :return:
        """
        return pd.to_datetime(date_column)

    def convert_condition(self):
        self.df['Condition'] = self.df['Condition'].apply(lambda col: self.cond_dict[col])

    def run(self):
        self.df.rename(columns=self.change_col_names(self.df.columns), inplace=True)
        self.df['Date'] = self.convert_date(self.df['Date'])
        self.convert_condition()

        self.df.to_csv('Transformed_Data.csv')
        return self.df

