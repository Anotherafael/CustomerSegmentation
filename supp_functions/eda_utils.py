import sys
from warnings import filterwarnings

filterwarnings("ignore")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

from supp_functions.exception import CustomException


def sns_plots(
    data,
    features,
    target=None,
    histplot=False,
    countplot=False,
    barplot=False,
    barplot_y=None,
    various_barplots=False,
    barplot_x=None,
    boxplot=False,
    boxplot_x=None,
    outliers=False,
    kde=False,
    hue=None,
    palette=None,
    style="whitegrid",
):
    try:
        sns.set_theme(style=style)
        num_features = len(features)
        num_rows = num_features // 3 + (num_features % 3 > 0)

        fig, axes = plt.subplots(num_rows, 3, figsize=(20, 5 * num_rows))

        for i, feature in enumerate(features):
            row = i // 3
            col = i % 3

            ax = axes[row, col] if num_rows > 1 else axes[col]

            if countplot:
                sns.countplot(data=data, x=feature, hue=hue, ax=ax, palette=palette)
                for container in ax.containers:
                    ax.bar_label(container)

            elif barplot:
                ax = sns.barplot(
                    data=data,
                    x=barplot_x,
                    y=feature,
                    hue=hue,
                    ax=ax,
                    ci=None,
                    palette=palette,
                )
                ax.set_ylabel(f'{feature} (mean)')
                for container in ax.containers:
                    ax.bar_label(container)

            elif various_barplots:
                ax = sns.barplot(
                    data=data,
                    x=barplot_x,
                    y=feature,
                    hue=hue,
                    ax=ax,
                    ci=None,
                    palette=palette,
                )
                for container in ax.containers:
                    ax.bar_label(container)

            elif boxplot:
                sns.boxplot(
                    data=data,
                    x=boxplot_x,
                    y=feature,
                    showfliers=outliers,
                    ax=ax,
                    palette=palette,
                )

            elif outliers:
                sns.boxplot(data=data, x=feature, ax=ax, palette=palette)

            else:
                sns.histplot(
                    data=data, x=feature, hue=hue, kde=kde, ax=ax, palette=palette
                )

            ax.set_title(feature)
            ax.set_xlabel("")

        if num_features < len(axes.flat):
            for j in range(num_features, len(axes.flat)):
                fig.delaxes(axes.flat[j])

        plt.tight_layout()

    except Exception as e:
        raise CustomException(e, sys)

def check_outliers(data, features, verbose=True):
    try:
        outlier_counts = {}
        outlier_indexes = {}
        total_outliers = 0

        for feature in features:
            Q1 = data[feature].quantile(0.25)
            Q3 = data[feature].quantile(0.75)

            IQR = Q3 - Q1

            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR

            feature_outliers = data[
                (data[feature] < lower_bound) | (data[feature] > upper_bound)
            ]
            outlier_indexes[feature] = feature_outliers.index.tolist()
            outlier_count = len(feature_outliers)
            outlier_counts[feature] = outlier_count
            total_outliers += outlier_count

        if verbose:
            print(f"There are {total_outliers} outliers in the dataset.")
            print()
            print(f"Number (percentage) of outliers per feature: ")
            print()
            for feature, count in outlier_counts.items():
                print(f"{feature}: {count} ({round(count/len(data)*100, 2)})%")

        return outlier_indexes, outlier_counts, total_outliers

    except Exception as e:
        raise CustomException(e, sys)