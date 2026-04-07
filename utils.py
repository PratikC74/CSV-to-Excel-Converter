import pandas as pd

def clean_data(df):
    # Handle missing values
    df.fillna("N/A", inplace=True)

    # Example: Convert date column (if exists)
    for col in df.columns:
        if "date" in col.lower():
            try:
                df[col] = pd.to_datetime(df[col])
            except:
                pass

    # Rename columns (example)
    df.columns = [col.strip().replace(" ", "_").title() for col in df.columns]

    return df