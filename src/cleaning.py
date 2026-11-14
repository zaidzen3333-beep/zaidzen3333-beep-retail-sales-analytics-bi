"""
Data Cleaning & Transformation Pipeline
Transforms raw retail data into conformed dimensions and the analytical master.
"""

from pathlib import Path
import numpy as np
import pandas as pd

RAW_DIR = Path("data/raw")
PROCESSED_DIR = Path("data/processed")


def clean_customers(raw_dir: Path = RAW_DIR) -> pd.DataFrame:
  df = pd.read_csv(raw_dir / "Customers.csv")
  df["Birthday"] = pd.to_datetime(df["Birthday"], errors="coerce")
  df["State Code"] = df["State Code"].fillna("Unknown")
  return df


def clean_products(raw_dir: Path = RAW_DIR) -> pd.DataFrame:
  df = pd.read_csv(raw_dir / "Products.csv")
  # Strip currency symbols and whitespace
  for col in ["Unit Cost USD", "Unit Price USD"]:
    df[col] = (
        df[col]
        .astype(str)
        .str.replace("$", "", regex=False)
        .str.replace(",", "", regex=False)
        .str.strip()
    )
    df[col] = pd.to_numeric(df[col], errors="coerce")
  return df


def clean_stores(raw_dir: Path = RAW_DIR) -> pd.DataFrame:
  df = pd.read_csv(raw_dir / "Stores.csv")
  df["Open Date"] = pd.to_datetime(df["Open Date"], errors="coerce")

  # Conformed Online dimension for StoreKey = 0
  if 0 not in df["StoreKey"].values:
    online_row = pd.DataFrame([{
        "StoreKey": 0,
        "Country": "Online",
        "State": "Online",
        "Square Meters": np.nan,
        "Open Date": pd.to_datetime("2014-01-01"),
    }])
    df = pd.concat([online_row, df], ignore_index=True)

  df["StoreKey"] = df["StoreKey"].astype(int)
  return df


def clean_exchange_rates(raw_dir: Path = RAW_DIR) -> pd.DataFrame:
  df = pd.read_csv(raw_dir / "Exchange_Rates.csv")
  df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
  return df


def clean_sales(raw_dir: Path = RAW_DIR) -> pd.DataFrame:
  df = pd.read_csv(raw_dir / "Sales.csv")
  df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")
  df["Delivery Date"] = pd.to_datetime(df["Delivery Date"], errors="coerce")
  df["Order Number"] = df["Order Number"].astype(int)
  df["Line Item"] = df["Line Item"].astype(int)
  df["StoreKey"] = df["StoreKey"].astype(int)
  df["Quantity"] = df["Quantity"].astype(int)
  return df


def build_analytical_master(
    sales: pd.DataFrame,
    products: pd.DataFrame,
    stores: pd.DataFrame,
    customers: pd.DataFrame,
) -> pd.DataFrame:
  # Merge dimensional context into sales transactions
  df = sales.merge(products, on="ProductKey", how="left")
  df = df.merge(stores, on="StoreKey", how="left")
  df = df.merge(customers, on="CustomerKey", how="left")

  # Financial metrics
  df["Revenue_USD"] = df["Quantity"] * df["Unit Price USD"]
  df["Cost_USD"] = df["Quantity"] * df["Unit Cost USD"]
  df["Profit_USD"] = df["Revenue_USD"] - df["Cost_USD"]
  df["Profit_Margin_Pct"] = (df["Profit_USD"] / df["Revenue_USD"]) * 100
  df["Channel"] = np.where(df["StoreKey"] == 0, "Online", "In-Store")

  return df


def run_pipeline():
  PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

  customers = clean_customers()
  products = clean_products()
  stores = clean_stores()
  exchange_rates = clean_exchange_rates()
  sales = clean_sales()

  customers.to_csv(PROCESSED_DIR / "customers_cleaned.csv", index=False)
  products.to_csv(PROCESSED_DIR / "products_cleaned.csv", index=False)
  stores.to_csv(PROCESSED_DIR / "stores_cleaned.csv", index=False)
  exchange_rates.to_csv(
      PROCESSED_DIR / "exchange_rates_cleaned.csv", index=False
  )
  sales.to_csv(PROCESSED_DIR / "sales_cleaned.csv", index=False)

  master = build_analytical_master(sales, products, stores, customers)
  master.to_csv(PROCESSED_DIR / "sales_master_analytical.csv", index=False)
  print(" Pipeline executed successfully: files written to data/processed/")


if __name__ == "__main__":
  run_pipeline()