import pandas as pd

def get_sales_data(department: str) -> pd.DataFrame:
    """Gets historical sales data for a given department."""
    sales_df = pd.read_csv('data/sales.csv')
    return sales_df[sales_df['department'] == department]

def get_inventory_data(department: str) -> pd.DataFrame:
    """Gets historical inventory data for a given department."""
    inventory_df = pd.read_csv('data/inventory.csv')
    return inventory_df[inventory_df['department'] == department]
