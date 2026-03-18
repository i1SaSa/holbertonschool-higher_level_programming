my First database
=================
In this tutorial, we will create a simple database to manage a library. We will create tables for books, authors, and borrowers, and we will learn how to insert data into these tables and query the data.
Creating the Database
To create a database, we can use the following SQL command:
```sqlCREATE DATABASE library;
```This command creates a new database called "library". We can then switch to this database using the following command:
```sqlUSE library;
```Creating Tables
Next, we will create tables for authors, books, and borrowers. We can use the following SQL commands to create these tables:
```sqlCREATE TABLE authors (
	id INT PRIMARY KEY AUTO_INCREMENT,
	name VARCHAR(255) NOT NULL
);
CREATE TABLE books (
	id INT PRIMARY KEY AUTO_INCREMENT,
	title VARCHAR(255) NOT NULL,
	author_id INT,
	FOREIGN KEY (author_id) REFERENCES authors(id)
);
CREATE TABLE borrowers (
	id INT PRIMARY KEY AUTO_INCREMENT,
	name VARCHAR(255) NOT NULL
);
```In this code, we create three tables: "authors", "books", and "borrowers". The "authors" table has an auto-incrementing primary key called "id" and a "name" column. The "books" table has an auto-incrementing primary key called "id", a "title" column, and a foreign key called "author_id" that references the "id" column in the "authors" table. The "borrowers" table has an auto-incrementing primary key called "id" and a "name" column.Inserting Data
Now that we have created our tables, we can insert data into them. We can use the following SQL commands to insert data into the "authors" and "books" tables:
```sqlINSERT INTO authors (name) VALUES ('J.K. Rowling');
INSERT INTO authors (name) VALUES ('George R.R. Martin');
INSERT INTO books (title, author_id) VALUES ('Harry Potter and the Sorcerer''s Stone', 1);
INSERT INTO books (title, author_id) VALUES ('A Game of Thrones', 2);
```In this code, we insert two authors into the "authors" table and two books into the "books" table. The "author_id" in the "books" table corresponds to the "id" of the authors we inserted earlier.Querying Data
Finally, we can query the data in our tables. For example, we can use the following SQL command to retrieve all books along with their authors:
```sqlSELECT books.title, authors.name	FROM booksJOIN authors ON books.author_id = authors.id;
```This command retrieves the title of each book and the name of its author by joining the "books" and "authors" tables on the "author_id" foreign key. The result will show the titles of the books along with the corresponding authors' names.
Conclusion
In this tutorial, we have created a simple database for managing a library. We created tables for authors, books, and borrowers, inserted data into these tables, and queried the data to retrieve information about the books and their authors. This is just the beginning of what you can do with SQL and databases, and there are many more features and functionalities to explore as you continue learning!
