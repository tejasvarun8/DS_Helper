# auto_visualizer.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from collections import Counter

# --- Function to detect column types ---
def detect_column_types(df):
    """
    Detects column types based on data types and known patterns.
    Returns a dictionary with column name as key and type as value.
    """
    column_types = {}
    for col in df.columns:
        if df[col].dtype in ['int64', 'float64']:
            column_types[col] = 'numerical'
        elif df[col].dtype == 'object':
            # Treat categorical if unique values < 20
            if df[col].nunique() < 20:
                column_types[col] = 'categorical'
            else:
                column_types[col] = 'text'
        else:
            column_types[col] = 'text'
    return column_types

# --- Main visualization function ---
def visualize(df):
    """
    Auto visualizer: Generates plots for numerical, categorical, and text columns.
    """
    column_types = detect_column_types(df)

    num_cols = [col for col, t in column_types.items() if t == 'numerical']
    cat_cols = [col for col, t in column_types.items() if t == 'categorical']
    text_cols = [col for col, t in column_types.items() if t == 'text']

    print("\nDetected column types:")
    for col, t in column_types.items():
        print(f"{col}: {t}")

    # --- Numerical columns ---
    for col in num_cols:
        plt.figure(figsize=(12, 4))

        plt.subplot(1, 2, 1)
        sns.histplot(df[col].dropna(), kde=True, bins=30)
        plt.title(f"Histogram of {col}")

        plt.subplot(1, 2, 2)
        sns.boxplot(x=df[col])
        plt.title(f"Boxplot of {col}")

        plt.tight_layout()
        plt.show()

    # Scatter plots for numerical columns (if ≥2)
    if len(num_cols) >= 2:
        sns.pairplot(df[num_cols].dropna())
        plt.suptitle("Scatter Matrix for Numerical Columns", y=1.02)
        plt.show()

    # --- Categorical columns ---
    for col in cat_cols:
        plt.figure(figsize=(8, 4))
        sns.countplot(x=col, data=df)
        plt.title(f"Count Plot of {col}")
        plt.xticks(rotation=45)
        plt.show()

    # --- Text columns ---
    for col in text_cols:
        text_data = " ".join(df[col].dropna().astype(str))

        # Word Cloud
        plt.figure(figsize=(10, 6))
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text_data)
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.title(f"Word Cloud for {col}")
        plt.show()

        # Top 20 frequent words
        words = text_data.split()
        common_words = Counter(words).most_common(20)
        word_df = pd.DataFrame(common_words, columns=['Word', 'Frequency'])

        plt.figure(figsize=(10, 6))
        sns.barplot(x='Frequency', y='Word', data=word_df)
        plt.title(f"Top 20 Words in {col}")
        plt.show()
import pandas as pd
from auto_visualizer import visualize

# Load your dataset
df = pd.read_csv(r"C:\Users\tejas\Downloads\Titanic-Dataset.csv")

# Run auto visualizer
visualize(df)
