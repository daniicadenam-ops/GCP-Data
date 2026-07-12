from google.cloud import bigquery

def query_public_dataset():
    client = bigquery.Client()

    query = """
    SELECT
        CONCAT(first_name, " ", last_name) AS Name_user,
        products.id,
        category,
        products.name as product_name,
        distribution_center_id,
        status,
        sale_price
    FROM `bigquery-public-data.thelook_ecommerce.products` AS products
    LEFT JOIN `bigquery-public-data.thelook_ecommerce.order_items` AS order_items
        ON products.id = order_items.product_id
    LEFT JOIN `bigquery-public-data.thelook_ecommerce.users` AS users
        ON users.id = order_items.user_id
    LIMIT 10
    """

    results = client.query(query).to_dataframe()[:8]


    print(results)
    #for row in results:
    #    print(row.Name_user, row.id, row.category, row.product_name, row.sale_price)

if __name__ == "__main__":
    query_public_dataset()