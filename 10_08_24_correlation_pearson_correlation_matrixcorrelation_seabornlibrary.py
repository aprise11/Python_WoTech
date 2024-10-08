# -*- coding: utf-8 -*-
"""10.08.24_Correlation_Pearson_Correlation_MatrixCorrelation_SeabornLibrary.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1RUUJALkIk4ia9ZKU0EjSQrXmiXJo4hLf
"""

import pandas as pd
import matplotlib.pyplot as plt

pokemon_df = pd.read_csv('/content/Pokemon.csv')

pokemon_df.head(n=5)

# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html

### Create a histogram of column 'Speed'
plt.hist(pokemon_df['Speed'], color = 'green', edgecolor = 'black')
plt.xlabel('Total')
plt.ylabel('Frequency')
plt.title('Histogram of Pokemon Speeds')

### Add to your histogram min, max, mean (average) lines
plt.axvline(pokemon_df["Speed"].mean(), color='red', linestyle='dashdot', linewidth=1)
plt.axvline(pokemon_df["Speed"].max(), color='blue', linestyle='dashed', linewidth=1)
plt.axvline(pokemon_df["Speed"].min(), color='blue', linestyle='dashed', linewidth=1)

"""###CORRELATION"""

# scatter plot between variables : Attack and Defense

plt.scatter(pokemon_df['Attack'], pokemon_df['Defense'], color = 'blue', alpha=0.5)
plt.xlabel('Attack')
plt.ylabel('Defense')
plt.title('Attack vs. Defense')

### Create scatter plot for variables(columns): Speed and Defense

plt.scatter(pokemon_df['Speed'], pokemon_df['Defense'], color = 'turquoise', alpha=0.5)
plt.xlabel('Speed')
plt.ylabel('Defense')
plt.title('Speed vs. Defense')

### Create a scatterplot for variables : HP and Defense

plt.scatter(pokemon_df['HP'], pokemon_df['Defense'], color = 'purple', alpha=0.5)
plt.xlabel('HP')
plt.ylabel('Defense')
plt.title('HP vs. Defense')

"""##Pearson correlation

###The correlation coefficient indicates the strength and direction of the statistical relationship between two variables. The coefficient ranges from -1 to 1, with a value of 0.43 signifying a positive but moderately strong relationship between the two variables.

-A positive correlation coefficient means that the variables increase together. Therefore, as one variable increases, the other also tends to increase, and vice versa.

-The closer the correlation coefficient is to 1, the stronger the positive relationship.

-A correlation coefficient of 0.43 is not very high, but it indicates a moderately positive relationship.

-If the correlation coefficient were negative, it would suggest that as one variable increases, the other variable decreases.

-A correlation coefficient of -1 indicates a perfect negative relationship.
Thus, a correlation coefficient of 0.43 might suggest that, for example, as Pokémon's Attack values increase, their Defense values tend to increase as well, but the relationship is not very strong.
"""

# Result of this correlation calculation is between -1 and 1.
# -1 means perfect negative relationship
# 1 means perfect positive relationship

# Pearson correlation between Attack/Defense
correlation1 = pokemon_df['Attack'].corr(pokemon_df['Defense'])
print(correlation1)

# Pearson correlation between Speed/Defense
correlation2 = pokemon_df['Speed'].corr(pokemon_df['Defense'])
print(correlation2)

### Select only numeric columns
numeric_columns = pokemon_df.select_dtypes(include=['number'])
numeric_columns = numeric_columns.drop('#', axis=1)
numeric_columns

# compare relation between Attack to each other column of this data frame and save this results in a dictionary, where key is the column and values is pearson_correlation
target_column = 'Attack'
correlation_results = {} #key = column, val=pearson_correlation

#  for loop comparing target column and all other columns in the DataFrame

for col in numeric_columns.columns:
  if col == 'Attack':
    continue
  correlation = pokemon_df[target_column].corr(pokemon_df[col])
  correlation_results[col] = correlation

correlation_results

"""##Correlation matrix

######A correlation matrix is a table that shows the correlation coefficients between many variables. Each cell in the table represents the correlation between two variables. The correlation coefficient measures the strength and direction of the relationship between two variables.
"""

correlation_matrix = numeric_columns.corr() # all columns are numeric
correlation_matrix

"""###Visualizing with Seaborn library

######https://www.tylervigen.com/spurious-correlations
"""

import seaborn as sns

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='cividis') # annot means - to add values #https://r02b.github.io/seaborn_palettes/
plt.title('Correlation Matrix')

"""###Linear regression (predict one value based on the other)

#####Linear regression is one of the simplest and most commonly used algorithms in machine learning and statistics. It is used to model the relationship between a dependent variable (also called the target or outcome) and one or more independent variables (also called features or predictors). Documentation :https://seaborn.pydata.org/generated/seaborn.regplot.html
"""

#sns.regplot(x='Attack', y='Defense', data=pokemon_df)

sns.regplot(
    data=pokemon_df, x='Attack',y='Defense',
    ci=99, marker="x", color=".3", line_kws=dict(color="r"),
)

sns.regplot(
    data=pokemon_df, x='Speed', y="Defense",
    ci=99, marker="x", color=".3", line_kws=dict(color="r"),
)

correlation2 = pokemon_df['Speed'].corr(pokemon_df['Defense'])
print('Pearson correlation coefficient:', correlation2)

