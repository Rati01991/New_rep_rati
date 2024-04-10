# თუ არ გაქვთ შექმნილი, შექმენით მონაცემთა ბაზა სახელად IT_STEP  და შეასრულეთ შემდეგი დავალებები:
#mysql> create database if not exists IT_STEP_db;

#1. დაწერეთ SQL რომელიც შექმნის Author ცხრილს, რომელსაც ექნება პირველადი გასაღები
CREATE TABLE author (
    author_id INT AUTO_INCREMENT PRIMARY KEY,
    author_name VARCHAR(50),
    author_lastname VARCHAR(50)
);


#2. დაწერეთ SQL რომელიც შექმნის Books ცხრილს, სადაც გექნებათ მეორადი გასაღები AuthorID
CREATE TABLE Books (
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    author_id INT,
    FOREIGN KEY (author_id) REFERENCES author(author_id)
);

#3. დაწერეთ SQL Author და Books ცხრილებისთვის სადაც შექმნით მინიმუმ 5 ჩანაწერს
INSERT INTO author (author_name, author_lastname) VALUES
('Rati1', 'B1'),
('Rati2', 'B2'),
('Rati3', 'B3'),
('Rati4', 'B4'),
('Rati5', 'B5');

INSERT INTO Books (title, author_id) VALUES
('A1', 1),
('A2', 1),
('A3', 2),
('A4', 3),
('A5', 4);

-- 4. დაწერეთ SQL Books ცხრილისთვის სადაც გამოიყენებთ update ბრძანებას და გაანახლებთ კონკრეტულ ჩანაწერის ერთ-ერთ ველის მნიშვნელობას
UPDATE Books
SET title = 'New'
WHERE book_id = 1;

-- 5. წაშალეთ ყველა ჩანაწერი Author და Books ცხრილიდან
DELETE FROM Books;
DELETE FROM author;

-- 6. წაშალეთ Author და Books ცხრილები

DROP TABLE IF EXISTS Books;

DROP TABLE IF EXISTS author;