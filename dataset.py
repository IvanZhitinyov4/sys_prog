import pandas as pd
from matplotlib import pyplot as plt
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.model_selection import KFold, StratifiedKFold
import tensorflow as tf
import torch
import numpy as np
from scipy import stats


class Dataset:
    def __init__(self, df):
        self.df = df

    def __clear_empty_rows(self):
        self.df = self.df.dropna(how='all')

    def __clear_outliers(self):
        for column in self.df.select_dtypes(include=["int64", "float64"]).columns:
            z_scores = np.abs(stats.zscore(self.df[column]))
            self.df = self.df[(z_scores < 3)]

    def __encode_categorical_features(self, encoding_type='Onehot'):
        categorical_features = self.df.select_dtypes(include=['object']).columns.tolist()
        if categorical_features:
            match encoding_type:
                case 'Onehot':
                    encoder = OneHotEncoder(sparse_output=False)
                    self.encoded_data = pd.DataFrame(encoder.fit_transform(self.df[categorical_features]),
                                                     columns=encoder.get_feature_names_out(categorical_features))
                case 'Label':
                    encoder = LabelEncoder()
                    self.encoded_data = self.df[categorical_features].apply(encoder.fit_transform)
                case _:
                    raise ValueError

        else:
            print('Categorical features not found')

    def __fill_missing(self, strategy='mean', value=None):
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

    def preparing(self, clear_type="z", strategy='Onehot'):
        self.__clear_empty_rows()
        self.__fill_missing(clear_type)
        self.__clear_outliers()
        self.__encode_categorical_features(strategy)

    def prepare_for_cross_validation(self, n_splits=5, stratify_by=None):
        if stratify_by and stratify_by in self.df.columns:
            skf = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=42)
            splits = skf.split(self.df, self.df[stratify_by])
        else:
            kf = KFold(n_splits=n_splits, shuffle=True, random_state=42)
            splits = kf.split(self.df)
        return [(self.df.iloc[train_idx], self.df.iloc[test_idx]) for train_idx, test_idx in splits]

    def display(self, column=None):
        if column:
            self.df[column].plot(kind='hist', title=f'Histogram of {column}')
            plt.title(f'Histogram of {column}')
        else:
            self.df.hist(figsize=(10, 8))
        plt.show()

    def transform(self, library='tensorflow'):
        if library == 'tensorflow':
            return tf.convert_to_tensor(self.df.values)
        elif library == 'pytorch':
            return torch.tensor(self.df.values)
        elif library == 'numpy':
            return self.df.values

        raise ValueError("Wrong library! Choose from 'tensorflow', 'pytorch', or 'numpy'")
