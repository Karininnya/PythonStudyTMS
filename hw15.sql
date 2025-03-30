CREATE TABLE authors
(
    id SERIAL PRIMARY KEY,
    first_name VARCHAR NOT NULL,
    last_name VARCHAR NOT NULL
);

CREATE TABLE books
(
    id SERIAL PRIMARY KEY,
    title VARCHAR NOT NULL,
    author_id INT,
    publication_year INT,
    FOREIGN KEY (author_id) REFERENCES authors (id) ON DELETE SET NULL
);

CREATE TABLE sales
(
    id SERIAL PRIMARY KEY,
    book_id INT,
    quantity INT,
    FOREIGN KEY (book_id) REFERENCES books (id) ON DELETE CASCADE
);
INSERT INTO authors (first_name, last_name)
VALUES ('Николай', 'Карамзин'),
        ('Михаил', 'Салтыков-Щедрин'),
        ('Максим', 'Горький');

INSERT INTO books (title, author_id, publication_year)
VALUES ('Бедная Лиза', 1, 1792),
        ('Конек-Горбунок', 2, 1960),
        ('Старуха Изергиль', 3, 1895);

INSERT INTO sales (book_id, quantity)
VALUES (1, 10),
        (2, 7),
        (3, 37);

SELECT books.title, authors.first_name, authors.last_name
FROM books
        INNER JOIN authors ON books.author_id = authors.id;

SELECT authors.first_name, authors.last_name, books.title
FROM authors
        LEFT JOIN books ON authors.id = books.author_id

SELECT books.title, authors.first_name, authors.last_name
FROM books
        RIGHT JOIN authors ON books.author_id = authors.id;

SELECT books.title, authors.first_name, authors.last_name, sales.quantity
FROM books
        INNER JOIN authors ON books.author_id = authors.id;
        INNER JOIN sales ON books.id = sales.book_id;

SELECT authors.first_name, authors.last_name, books.title, sales.quantity
FROM authors
        LEFT JOIN books ON authors.id = books.author_id

        CREATE TABLE IF NOT EXISTS categories
(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS suppliers
            (
                 id SERIAL PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                address VARCHAR(255)
            );
CREATE TABLE IF NOT EXISTS products
            (
                id SERIAL PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                price DECIMAL(10, 2) NOT NULL,
                stock_quantity INTEGER NOT NULL,
                category_id INTEGER REFERENCES categories(id),
                supplier_id INTEGER REFERENCES suppliers(id)
            );

CREATE TABLE IF NOT EXISTS supply_orders
            (
                id SERIAL PRIMARY KEY, -- serial = int + autoincrement,
                supplier_id INTEGER REFERENCES suppliers(id),
                quantity INTEGER NOT NULL
            );

INSERT INTO categories (name)
VALUES ('для мытья'),
        ('для подметания'),
        ('спортивный инвентарь');


INSERT INTO products (name, price, stock_quantity)
VALUES ('ведро', 5, 170),
        ('щетка', 2, 200),
        ('гантели', 30, 100);

INSERT INTO suppliers (name, address)
VALUES ('Большой магазин', 'ул. Столетова 17'),
        ('Триовист', 'ул. Шишкина 14'),
        ('Спортмастер', 'ул. Свердлова 11');

 INSERT INTO supply_orders (quantity)
VALUES (14),
        (3),
        (7);

