import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns


def load_lakers_data(filepath):
    df = pd.read_csv(filepath, encoding='cp1250', sep=',')
    return df

def classify_features():
    return {
        'stimulants': ['ORB', 'AST', 'STL', 'BLK', 'PTS', 'FG%', '3P%', 'FT%'],
        'destimulants': ['TOV'],
        'nominals': []
    }

def min_max_scaling(df, features):
    return (df[features] - df[features].min()) / (df[features].max() - df[features].min())

def standardization(df, features):
    return (df[features] - df[features].mean()) / df[features].std()

def ratio_transformation(df, features):
    return df[features].div(df[features].mean())

def compute_synthetic_index(df, weights=None):
    if weights is None:
        weights = np.ones(df.shape[1]) / df.shape[1]
    return df.dot(weights)

def preprocess_data(df, all_features):
    df = df[df['Yrs'] > 1]

    df = df[df['MP'].notna()]
    df[all_features] = df[all_features].fillna(df[all_features].median())
    #df.loc[:, all_features] = df[all_features].fillna(df[all_features].median())
    
    per_minute_features = ['ORB', 'AST', 'STL', 'BLK', 'TOV', 'PTS']
    for feature in per_minute_features:
        df[feature] = df[feature] / df['MP']
        #df.loc[:, feature] = df[feature] / df['MP']

    return df
    
def impute_outliers_IQR(df, features):
    
    for feature in features:
        q1 = df[feature].quantile(0.25)
        q3 = df[feature].quantile(0.75)
        IQR = q3 - q1

        lower_bound = q1 - 1.5 * IQR
        upper_bound = q3 + 1.5 * IQR
        mean_val = df[feature].mean()

        df.loc[df[feature] > upper_bound, feature] = mean_val
        df.loc[df[feature] < lower_bound, feature] = mean_val

    return df

def transform_destimulants(df, destimulants):
    for feature in destimulants:
        df[feature] = df[feature].max() - df[feature]
    return df
    
def plot_histograms(df, features, output_dir):
    for feature in features:
        plt.figure(figsize=(6, 4))
        sns.histplot(df[feature], kde=True, bins=20)
        plt.title(f'Histogram: {feature}')
        plt.show()
        plt.close()
        
def generate_rankings(df, all_features, method_dict):
    for name, method in method_dict.items():
        df_norm = method(df.copy(), all_features)
        df["Synthetic_Index"] = compute_synthetic_index(df_norm[all_features])
        ranking = df[["Player", "Synthetic_Index"]].sort_values(by="Synthetic_Index", ascending=False)
        output_file = f"ranking_lakers_{name}.csv"
        ranking.to_csv(output_file, index=False)
        print(f"Top 5 players ({name}):")
        print(ranking.head(5), "\n")
        
def main():
    filepath = "players1.csv"
    df = load_lakers_data(filepath)
    df.head()

        
    features = classify_features()
    all_features = features['stimulants'] + features['destimulants']

    df = preprocess_data(df, all_features)
    df = impute_outliers_IQR(df, all_features)
    df = transform_destimulants(df, features['destimulants'])

    plot_histograms(df, all_features, output_dir="plots/histograms")

    transformations = {
        'unit normalization': min_max_scaling,
        'standardization': standardization,
        'ratio transformation': ratio_transformation
    }

    generate_rankings(df, all_features, transformations)


if __name__ == "__main__":
    main()