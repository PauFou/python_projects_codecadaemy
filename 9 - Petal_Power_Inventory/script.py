import pandas as pd

inventory = pd.read_csv('inventory.csv')

staten_island = inventory.head(10)
product_request = staten_island["product_description"]

seed_request = inventory[(inventory.location == "Brooklyn") & (inventory.product_type == "seeds")]

inventory["total_value"] = inventory.apply(lambda row: round(row.quantity * row.price, 2), axis = 1)

combine_lambda = combine_lambda = lambda row: f'{row.product_type} - {row.product_description}'

inventory["full_description"] = inventory.apply(combine_lambda, axis = 1)

print(inventory)
