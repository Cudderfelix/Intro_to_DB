USE alx_book_store;

CREATE TABLE Authors (
    author_id INT PRIMARY KEY AUTO_INCREMENT,
    author_name VARCHAR(215) NOT NULL
);

CREATE TABLE Customers (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_name VARCHAR(215) NOT NULL,
    email VARCHAR(215) NOT NULL UNIQUE,
    address TEXT NOT NULL
);

CREATE TABLE Books (
    book_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(130) NOT NULL,
    author_id INT NOT NULL,
    price_Double NOT NULL,
    publication_date_DATE DATE,
    FOREIGN KEY (author_id) REFERENCES AUTHORS(author_id) ON DELETE RESTRICT,
    INDEX idx_author_id (author_id)
);

CREATE TABLE Orders (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT NOT NULL,
    order_date DATE NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id) ON DELETE RESTRICT,
    INDEX idx_customer_id (customer_id)
);

CREATE TABLE Order_Details (
    order_Details_ID INT PRIMARY KEY AUTO_INCREMENT,
    order_id INT NOT NULL,
    book_id INT NOT NULL,
    quantity DOUBLE NOT NULL,
    FOREIGN KEY (order_id) REFERENCES Orders(order_id) ON DELETE RESTRICT,
    FOREIGN KEY (book_id) REFERENCES Books(book_id) ON DELETE RESTRICT,
    INDEX idx_order_id (order_id),
    INDEX idx_book_id (book_id)
);
