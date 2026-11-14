"""
Data Quality Validation Suite
Asserts primary key uniqueness, referential integrity, and business logic rules.
"""

from pathlib import Path
import pandas as pd

PROCESSED_DIR = Path("data/processed")


def validate_processed_data():
  customers = pd.read_csv(PROCESSED_DIR / "customers_cleaned.csv")
  products = pd.read_csv(PROCESSED_DIR / "products_cleaned.csv")
  stores = pd.read_csv(PROCESSED_DIR / "stores_cleaned.csv")
  sales = pd.read_csv(PROCESSED_DIR / "sales_cleaned.csv")
  master = pd.read_csv(PROCESSED_DIR / "sales_master_analytical.csv")

  # 1. Primary Key Uniqueness
  assert (
      customers["CustomerKey"].is_unique
  ), "Duplicate CustomerKey found in customers"
  assert (
      products["ProductKey"].is_unique
  ), "Duplicate ProductKey found in products"
  assert stores["StoreKey"].is_unique, "Duplicate StoreKey found in stores"

  # 2. Referential Integrity
  assert set(sales["CustomerKey"]).issubset(
      set(customers["CustomerKey"])
  ), "Orphan CustomerKey in sales"
  assert set(sales["ProductKey"]).issubset(
      set(products["ProductKey"])
  ), "Orphan ProductKey in sales"
  assert set(sales["StoreKey"]).issubset(
      set(stores["StoreKey"])
  ), "Orphan StoreKey in sales"

  # 3. Business Logic Asserts
  assert (products["Unit Price USD"] > 0).all(), "Non-positive Unit Price found"
  assert (
      products["Unit Cost USD"] > 0
  ).all(), "Non-positive Unit Cost found"
  assert (sales["Quantity"] > 0).all(), "Non-positive Quantity found in sales"
  assert (
      master["Revenue_USD"] >= master["Cost_USD"]
  ).all(), "Negative gross margin detected"

  print(" All data quality assertions passed (0 integrity violations).")


if __name__ == "__main__":
  validate_processed_data()