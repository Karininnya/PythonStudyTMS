import psycopg2

DB_CONFIG = {
    "dbname": "inventory",
    "user": "postgres",
    "password": "postgres",
    "host": "localhost",
    "port": "5432"
}


def connect_db():
    return psycopg2.connect(**DB_CONFIG)


def init_db():
    with connect_db() as conn, conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS categories
            (
                   id SERIAL PRIMARY KEY,
                    name VARCHAR(255) NOT NULL
            );
        """)

        cur.execute("""
            CREATE TABLE IF NOT EXISTS suppliers
            (
                 id SERIAL PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                address VARCHAR(255)
            );
        """)

        cur.execute("""
            CREATE TABLE IF NOT EXISTS products
            (
                d SERIAL PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                price DECIMAL(10, 2) NOT NULL,
                stock_quantity INTEGER NOT NULL,
                category_id INTEGER REFERENCES categories(id),
                supplier_id INTEGER REFERENCES suppliers(id)
            );
        """)

        cur.execute("""
            CREATE TABLE IF NOT EXISTS supply_orders
            (
                id SERIAL PRIMARY KEY,
                product_id INTEGER REFERENCES products(id),
                supplier_id INTEGER REFERENCES suppliers(id),
                quantity INTEGER NOT NULL
            );
        """)


def get_all_products():
    with connect_db() as conn, conn.cursor() as cur:
        cur.execute("SELECT * FROM products")

        products = cur.fetchall()
        return products


def get_all_suppliers():
    with connect_db() as conn, conn.cursor() as cur:
        cur.execute("SELECT * FROM suppliers")

        suppliers = cur.fetchall()
        return suppliers


def get_all_categories():
    with connect_db() as conn, conn.cursor() as cur:
        cur.execute("SELECT * FROM categories")

        categories = cur.fetchall()
        return categories


def get_product_full_info_by_id(product_id):
    with connect_db() as conn, conn.cursor() as cur:

        cur.execute("SELECT * FROM products WHERE id = %s", (product_id,))
        product_info = cur.fetchone()

def get_all_supply_orders(product_id):
    with connect_db() as conn, conn.cursor() as cur:

        cur.execute("SELECT * FROM supply_orders WHERE id = %s", (product_id,))
        product_info = cur.fetchone()


        cur.execute("""
                    SELECT s.full_name
            FROM products_suppliers ps
                     JOIN suppliers a ON ps.suppliers_id = s.id
            WHERE ps.product_id = %s""", (product_id,))

        products = cur.fetchall()



        return {
            "product_info": product_info,

        }


def create_product(full_name):
    with connect_db() as conn, conn.cursor() as cur:
        cur.execute("INSERT INTO product (full_name) VALUES (%s)", (full_name,))


def search_product(query):
    with connect_db() as conn, conn.cursor() as cur:
        cur.execute("SELECT * FROM products WHERE name ILIKE %s;", (f"%{query}%",))

        products = cur.fetchall()
        return products


