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
        # Инициализация датасета
        self.df = df

    def __clear_empty_rows(self):
        # Чистим все пустые строки
        self.df = self.df.dropna(how='all')

    def __clear_outliers(self):
        # Чистим все выбросы из датасета по z оценке
        for column in self.df.select_dtypes(include=["int64", "float64"]).columns:
            z_scores = np.abs(stats.zscore(self.df[column]))
            self.df = self.df[(z_scores < 3)]

    def __encode_categorical_features(self, encoding_type='Onehot'):    # кодируем категориальные признаки
        # определяем столбцы, содержащие категориальные признаки
        categorical_features = self.df.select_dtypes(include=['object']).columns.tolist()
        # если есть
        if categorical_features:
            # проверяем каким способом кодируем кат. признаков
            match encoding_type:
                case 'Onehot':      # Onehot кодирует данные в бинарные векторы
                    encoder = OneHotEncoder(sparse_output=False)
                    self.encoded_data = pd.DataFrame(encoder.fit_transform(self.df[categorical_features]),
                                                     columns=encoder.get_feature_names_out(categorical_features))
                case 'Label':   # Label присваивает каждому кат. признаку номер
                    encoder = LabelEncoder()
                    self.encoded_data = self.df[categorical_features].apply(encoder.fit_transform)
                case _:
                    raise ValueError("Wrong encoding type! Choose from 'Onehot' or 'Label")

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

    def preparing(self, strategy='mean', encoding_type='Onehot'):
        self.__clear_empty_rows()
        self.__fill_missing(strategy)
        self.__clear_outliers()
        self.__encode_categorical_features(encoding_type)

    def prepare_for_cross_validation(self, n_splits=5, stratify_by=None):   # Подготавливаем данные для кроссвалидирования (разбиение на n)
        if stratify_by is not None:
            if stratify_by in self.df.columns:
                if self.df[stratify_by].dtype in ('category', 'object', 'bool'):
                    # Стратификация по категориальному признаку
                    kf = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=42)
                    return [(self.df.iloc[train_index], self.df.iloc[test_index])
                            for train_index, test_index in kf.split(self.df, self.df[stratify_by])]
                else:
                    # Стратификация по непрерывному признаку
                    kf = KFold(n_splits=n_splits, shuffle=True, random_state=42)
                    return [(self.df.iloc[train_index], self.df.iloc[test_index]) for train_index, test_index in kf.split(self.df)]
            else:
                raise ValueError(f"Column '{stratify_by}' not found in DataFrame.")
        else:
            # Без стратификации
            kf = KFold(n_splits=n_splits, shuffle=True, random_state=42)
            return [(self.df.iloc[train_index], self.df.iloc[test_index])
                    for train_index, test_index in kf.split(self.df)]

    def display(self, column=None):
        if column:
            self.df[column].plot(kind='hist', title=f'Histogram of {column}')
            plt.title(f'Histogram of {column}')
        else:
            self.df.hist(figsize=(10, 8))
            plt.title(f'Histogram of all columns')
        plt.show()

    def transform(self, library='tensorflow'):
        data = self.df.values
        match library:
            case 'tensorflow':
                return tf.convert_to_tensor(data)
            case 'pytorch':
                return torch.tensor(data)
            case 'numpy':
                return data
            case _:
                raise ValueError("Wrong library! Choose from 'tensorflow', 'pytorch', or 'numpy'")
