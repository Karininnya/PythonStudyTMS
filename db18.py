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


def create_categories(name):
    with connect_db() as conn, conn.cursor() as cur:
        cur.execute("INSERT INTO categories (name) VALUES (%s, %s)", (name,))


def get_all_categories():
    with connect_db() as conn, conn.cursor() as cur:
        cur.execute("SELECT id, name created_at FROM categories WHERE deleted_at IS NULL;")

        categories_from_db = cur.fetchall()
        categories = list()
        for categories in categories_from_db:
            categories.append({
                "id": categories[0],
                "name": categories[1],

            })
        return categories


def get_categories_by_id(post_id):
    with connect_db() as conn, conn.cursor() as cur:
        cur.execute("SELECT id, name created_at FROM categories WHERE id = %s AND deleted_at IS NULL;",
                    (categories_id,))

        categories_from_db = cur.fetchone()
        if categories_from_db is None:
            return None

        categories = {
            "id": categories_from_db[0],
            "name": categories_from_db[1],

        }
        return categories


def update_categories(categories_id, name):
    with connect_db() as conn, conn.cursor() as cur:
        cur.execute("UPDATE posts SET title = %s, description = %s WHERE id = %s AND deleted_at IS NULL;",
                    (name, categories_id))


def delete_categories(categories_id):
    with connect_db() as conn, conn.cursor() as cur:
        cur.execute("UPDATE categories SET deleted_at = CURRENT_TIMESTAMP WHERE id = %s;",
                    (categories_id,))