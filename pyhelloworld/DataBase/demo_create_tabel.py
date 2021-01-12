CREATE TABLE runoob_tbl(
    runoob_id INT NOT NULL AUTO_INCREMENT,
    runoob_title VARCHAR(100) NOT NULL,
    runoob_author VARCHAR(40) NOT NULL,
    submission_date DATE,
    PRIMARY KEY ( runoob_id ));

INSERT INTO runoob_tbl 
(runoob_title, runoob_author, submission_date)
VALUES
("学习 PHP", "菜鸟教程", NOW());

INSERT INTO runoob_tbl
(runoob_title, runoob_author, submission_date)
VALUES
("学习 MySQL", "菜鸟教程", NOW());

INSERT INTO runoob_tbl
(runoob_title, runoob_author, submission_date)
VALUES
("JAVA 教程", "RUNOOB.COM", '2016-05-06');

INSERT INTO runoob_tbl
(runoob_title, runoob_author, submission_date)
VALUES
("学习c", "FK", '2016-05-06');

INSERT INTO tcount_tbl 
(runoob_author, runoob_count)
VALUES
("Google", 22);