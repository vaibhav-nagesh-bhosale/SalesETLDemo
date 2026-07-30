from sqlalchemy import text
from database.db import engine


def load_sales(df):

    print("Loading records into PostgreSQL...")

    with engine.begin() as conn:
        print("Current Database:",
              conn.execute(text("SELECT current_database()")).scalar())

        print("Sales Before:",
              conn.execute(text("SELECT COUNT(*) FROM sales")).scalar())
        
        for _, row in df.iterrows():

            print(row.to_dict())

            conn.execute(
                text("""
                INSERT INTO sales
                (
                    orderid,
                    product,
                    quantity,
                    price,
                    totalamount
                )

                VALUES
                (
                    :orderid,
                    :product,
                    :quantity,
                    :price,
                    :totalamount
                )

                ON CONFLICT (orderid)
                DO UPDATE SET

                    product=EXCLUDED.product,
                    quantity=EXCLUDED.quantity,
                    price=EXCLUDED.price,
                    totalamount=EXCLUDED.totalamount
                """),

                {
                    "orderid": int(row["OrderID"]),
                    "product": row["Product"],
                    "quantity": int(row["Quantity"]),
                    "price": float(row["Price"]),
                    "totalamount": float(row["TotalAmount"])
                }
            )

        print("Sales After:",conn.execute(text("SELECT COUNT(*) FROM sales")).scalar())
    
    print("Finished loading.")