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