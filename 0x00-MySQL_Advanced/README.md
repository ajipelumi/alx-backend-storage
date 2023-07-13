## Advanced MySQL

This repository contains the code and resources for the Advanced MySQL project.
Advanced MySQL is a project that is part of the ALX Software Engineering Web Stack curriculum.
The project is designed to help us understand how to use MySQL in a more advanced way.

### Topics Covered

- **Stored Procedures**: We learned how to create stored procedures in MySQL and how to call them from the command line.

- **Triggers**: We learned how to create triggers in MySQL and how to call them from the command line.

- **Views**: We learned how to create views in MySQL and how to call them from the command line.

- **Functions**: We learned how to create functions in MySQL and how to call them from the command line.

- **Indexes**: We learned how to create indexes in MySQL and how to call them from the command line.

### Code Snippets
```sql
DELIMITER $$
CREATE PROCEDURE `sp_get_users`()
BEGIN
    SELECT * FROM users;
END$$
DELIMITER ;
```
```sql
DELIMITER $$
CREATE TRIGGER `trg_update_user` BEFORE UPDATE ON `users`
FOR EACH ROW
BEGIN
    SET NEW.updated_at = NOW();
END$$
DELIMITER ;
```
```sql
CREATE VIEW `v_users` AS
SELECT * FROM users;
```
```sql
DELIMITER $$
CREATE FUNCTION `fn_get_user`(`id` INT) RETURNS varchar(255)
BEGIN
    DECLARE name varchar(255);
    SELECT name INTO name FROM users WHERE id = id;
    RETURN name;
END$$
DELIMITER ;
```
```sql
CREATE INDEX `idx_users_name` ON users (name);
```

### Resources

- [MySQL 5.7 Reference Manual](https://dev.mysql.com/doc/refman/5.7/en/)
- [MySQL 5.7 SQL Statement Syntax](https://dev.mysql.com/doc/refman/5.7/en/sql-statements.html)
- [MySQL 5.7 Stored Programs and Views](https://dev.mysql.com/doc/refman/5.7/en/stored-programs-views.html)
- [MySQL 5.7 Triggers](https://dev.mysql.com/doc/refman/5.7/en/triggers.html)
- [MySQL 5.7 Functions and Operators](https://dev.mysql.com/doc/refman/5.7/en/functions.html)