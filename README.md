# Linear Ordering of NBA Players from the Los Angeles Lakers Based on Selected Statistical Features

## Summary

This project performs a linear ordering of Los Angeles Lakers players based on selected basketball statistics. The primary goal is to objectively rank players by analyzing a variety of performance metrics. The analysis includes nine diagnostic features, such as points, assists, rebounds, and shooting percentages. The methodology involves data preprocessing, statistical analysis, and visualization to draw insightful conclusions.

## Objectives

The main objectives of this project are:

* To rank players of the Los Angeles Lakers based on their statistical performance.
* To handle missing data in a robust and statistically sound manner.
* To visualize the results and provide intuitive insights.
* To develop a flexible and reproducible framework for ranking NBA players using diverse statistics.

## Background

Linear ordering is a technique used in sports analytics to establish a ranking order among players based on multiple criteria. In basketball, this can be particularly challenging due to the diversity of performance metrics, from scoring and shooting efficiency to defensive contributions. This project aims to address this challenge by integrating various metrics into a cohesive ranking system.

## Data

The dataset used in this project is sourced from a CSV file named `players1.csv`. The data includes statistics of Lakers players, such as:

* Player Name
* Years of Experience (Yrs)
* Minutes Played (MP)
* Offensive Rebounds (ORB)
* Assists (AST)
* Steals (STL)
* Blocks (BLK)
* Turnovers (TOV)
* Points (PTS)
* Field Goal Percentage (FG%)
* Three-Point Percentage (3P%)
* Free Throw Percentage (FT%)

### Data Preprocessing

Missing data was handled by replacing missing values with the median of the respective feature. The median, being less sensitive to outliers compared to the mean, ensures the stability of the ranking process. Additionally, data normalization was applied to bring all features to a comparable scale. Data transformations, such as scaling and encoding, were conducted where necessary to improve the performance of the ranking algorithm.

## Analysis

The project implements the following steps:

1. **Data Cleaning:** Handling missing values, normalizing the features, and performing exploratory data analysis (EDA) to understand data distributions.
2. **Feature Selection:** Identifying relevant metrics using statistical methods and domain knowledge to ensure accurate player ranking.
3. **Ranking Algorithm:** Applying linear ordering techniques, including ranking by composite scores derived from weighted averages and multi-criteria decision-making methods.
4. **Visualization:** Generating plots to illustrate player performance and the relative differences among the top-ranked players. Plots include bar charts, scatter plots, and ranking histograms.

### Details of `analyze_lakers.py`

This Python script is the main analysis tool in the project. It performs the following tasks:

* Loads and preprocesses the player data from `players1.csv`.
* Applies imputation methods for missing data.
* Normalizes the data to a uniform scale.
* Calculates a composite score for each player based on selected metrics.
* Ranks the players according to their scores.
* Visualizes the ranking results using matplotlib and seaborn.

The script is modular and can be extended to include additional metrics or alternative ranking methods as needed.

## Installation

To run this project, you need Python 3 and the following packages:

```
pip install pandas numpy matplotlib seaborn
```

## Usage

Run the following command to execute the analysis:

```
python analyze_lakers.py
```

### Example Output

The program outputs a ranked list of players based on their calculated scores, along with visualizations highlighting key statistics and comparisons between top performers with visual charts for further inspection.

## Performance Metrics

The primary metrics used for ranking include:

* **Efficiency Metrics:** Points per game, field goal percentage, free throw percentage.
* **Defensive Metrics:** Steals, blocks, defensive rebounds.
* **Playmaking Metrics:** Assists and turnovers.
* **Consistency Metrics:** Shooting percentages to evaluate scoring reliability.

## Contribution

Contributions are welcome! You can contribute by submitting new ranking algorithms, improving data preprocessing, or adding more comprehensive visualizations. Please open issues or submit pull requests on GitHub for any enhancements.
