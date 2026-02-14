# PYTHON Script Approach

import pandas as pd
import sqlite3

db_con= sqlite3.connect("sales.db")

df_cust= pd.read_sql("SELECT * FROM Customer", db_con)
df_sales= pd.read_sql("SELECT * FROM Sales",db_con)
df_orders = pd.read_sql("SELECT * FROM Orders",db_con)
df_items = pd.read_sql("SELECT * FROM Items",db_con)


df_joined1 = df_cust.merge(df_sales, on="customer_id",how="inner")
df_joined2 = df_joined1.merge(df_orders, on="sales_id", how="inner")
df_joined3 = df_joined2.merge(df_items, on="item_id", how="inner")

df_filter = df_joined3[(df_joined3["age"]) >= 18 & (df_joined3["age"]<=35)]

df_joined3["quantity"] = df_joined3["quantity"].fillna(0)

final = df.groupBy(["customer_id", "age", "item"]).agg({"quantity": "sum"}).reset_index()

final = final[final["quantity"]>0]

final["quantity"]= final["quantity"].astype(int)

final.to_csv("final.csv",sep=";",index=False)

print("testing")
