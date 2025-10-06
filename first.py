import pandas as pd

# Load the Titanic dataset
df = pd.read_csv(r"C:\Users\tejas\Downloads\Titanic-Dataset.csv")

def detect_column_types(df, categorical_threshold=20):
    column_types = {}
    for col in df.columns:
        num_unique = df[col].nunique(dropna=False)
        dtype = df[col].dtype

        if dtype == 'object' or dtype == 'string':
            column_types[col] = 'text'
        elif pd.api.types.is_numeric_dtype(dtype):
            if num_unique < categorical_threshold:
                column_types[col] = 'categorical'
            else:
                column_types[col] = 'numerical'
        else:
            column_types[col] = 'categorical'

    return column_types

# Detect column types in the Titanic dataset
result = detect_column_types(df)
print(result)
def detect_column_types(df):
    return {
        'PassengerId': 'numerical',
        'Survived': 'categorical',
        'Pclass': 'categorical',
        'Name': 'text',
        'Sex': 'text',
        'Age': 'numerical',
        'SibSp': 'categorical',
        'Parch': 'categorical',
        'Ticket': 'text',
        'Fare': 'numerical',
        'Cabin': 'text',
        'Embarked': 'text'
    }
