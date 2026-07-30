import pandas as pd


def transform_sales(df):

    # Remove blank rows
    df = df.dropna()

    # Remove duplicate Order IDs
    df = df.drop_duplicates(subset=["OrderID"])

    # Calculate Total Amount
    df["TotalAmount"] = df["Quantity"] * df["Price"]

    print(df)
    
    return df