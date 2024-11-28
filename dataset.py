import pandas as pd
from matplotlib import pyplot as plt
from sklearn import *
from sklearn import preprocessing
import seaborn as sns
import tensorflow as tf
import torch


class Dataset:
    def __init__(self, df):
        self.df = df

    def info(self):
        return {
            'Type': self.df.dtypes,
            'Missing values': self.df.isnull().sum()
        }

    def check_categorical(self, threshold_of_num_cat: int = None):
        threshold_of_num_cat = threshold_of_num_cat or self.df.shape[0]

        def _is_categorical(column):
            if column.dtype in ('category', 'bool'):
                return True
            elif column.dtype == 'object':
                return len(column.astype(str).unique()) <= threshold_of_num_cat
            elif column.dtype == 'float64':
                return len(column.round(10).unique()) <= threshold_of_num_cat
            # other datatypes: 'int64', 'float64', 'timedelta[ns]'
            return len(column.unique()) <= threshold_of_num_cat

        return [column for column in self.df.columns if _is_categorical(column)]

    def eval_categorical(self, categorical_names, strategy='Onehot'):
        if strategy == 'Onehot':
            encoder = preprocessing.OneHotEncoder()
            for col in categorical_names:
                sub = encoder.fit_transform(self.df[col].to_numpy().reshape(-1, 1))
                df_encoded = pd.DataFrame(sub, columns=encoder.get_feature_names_out([col]))
                self.df = pd.concat([self.df, df_encoded], axis=1)

        elif strategy == 'Label':
            encoder = preprocessing.LabelEncoder()
            for col in categorical_names:
                self.df[col + '_labeled'] = encoder.fit_transform(self.df[col].to_numpy().reshape(-1, 1))

        else:
            raise ValueError("strategy must be 'Onehot' or 'Label'")

    def preparation(self, threshold_of_num_cat: int = None, strategy='Onehot'):
        self.fill_missing(strategy="mean")
        categorical = self.check_categorical(threshold_of_num_cat=threshold_of_num_cat)
        self.eval_categorical(categorical, strategy)

    def fill_missing(self, strategy='mean', value=None):
        for column in self.df.select_dtypes(include=['float64', 'int64']).columns:
            if self.df[column].isnull().sum() > 0:
                match strategy:
                    case "mean":
                        self.df[column].fillna(self.df[column].mean(), inplace=True)
                    case "median":
                        self.df[column].fillna(self.df[column].median(), inplace=True)
                    case "constant":
                        if value is not None:
                            self.df[column].fillna(value, inplace=True)

    def display(self, plot_type="Hist", column=None):
        if column:
            self._display_column_plot(plot_type, column)
        else:
            self._display_all_columns_plot(plot_type)
        plt.show()

    def _display_column_plot(self, plot_type, column):
        match plot_type:
            case "Hist":
                self.df[column].plot(kind='hist', title=f'Histogram of {column}')
            case "Box":
                sns.boxplot(x=self.df[column])
            case _:
                raise ValueError

    def _display_all_columns_plot(self, plot_type):
        match plot_type:
            case "Hist":
                self.df.hist(figsize=(10, 8))
            case "Box":
                sns.boxplot(data=self.df.select_dtypes(include=['float64', 'int64']))
            case _:
                raise ValueError

    def transform(self, library='tensorflow'):
        if library == 'tensorflow':
            return tf.convert_to_tensor(self.df.values)
        elif library == 'pytorch':
            return torch.tensor(self.df.values)
        elif library == 'numpy':
            return self.df.values

        raise ValueError("Wrong library! Choose from 'tensorflow', 'pytorch', or 'numpy'")
