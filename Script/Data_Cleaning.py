import pandas as pd

# Load CSV files
orders = pd.read_csv('data/olist_orders_dataset.csv')
order_items = pd.read_csv('data/olist_order_items_dataset.csv')
customers = pd.read_csv('data/olist_customers_dataset.csv')
products = pd.read_csv('data/olist_products_dataset.csv')
payments = pd.read_csv('data/olist_order_payments_dataset.csv')
sellers = pd.read_csv('data/olist_sellers_dataset.csv')
category_translation = pd.read_csv('data/product_category_name_translation.csv')

# Merge datasets
merged = orders.merge(order_items, on='order_id', how='left') \
               .merge(customers, on='customer_id', how='left') \
               .merge(products, on='product_id', how='left') \
               .merge(payments, on='order_id', how='left') \
               .merge(sellers, on='seller_id', how='left') \
               .merge(category_translation, on='product_category_name', how='left')

# Clean columns
merged['order_purchase_timestamp'] = pd.to_datetime(merged['order_purchase_timestamp'])
merged['order_delivered_customer_date'] = pd.to_datetime(merged['order_delivered_customer_date'])

# Feature Engineering
merged['delivery_time_days'] = (merged['order_delivered_customer_date'] - merged['order_purchase_timestamp']).dt.days

# Save clean version
merged.to_csv('data/olist_merged_clean.csv', index=False)
