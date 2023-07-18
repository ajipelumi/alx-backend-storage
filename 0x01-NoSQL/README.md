## NoSQL

This repository contains the code and resources for the NoSQL project.
NoSQL is a project that is part of the ALX Software Engineering Web Stack curriculum.
The project is designed to help us understand how to understand NoSQL databases and how to use them.

**NoSQL** is a term that is used to refer to non-relational databases.
NoSQL databases are databases that do not use the SQL language to query data.
NoSQL databases are also called non-relational databases because they do not use the relational model that is used by relational databases.
NoSQL databases are also called non-SQL databases because they do not use the SQL language to query data.

Examples of NoSQL databases include MongoDB, CouchDB, Redis, Cassandra, etc.

### Topics Covered

- **NoSQL Databases**: We learned about NoSQL databases and how they differ from SQL databases. We also learned about the different types of NoSQL databases.

- **MongoDB**: We learned how to install MongoDB and how to use it from the command line. We also learned how to use MongoDB from a NodeJS application.

- **MongoDB Shell**: We learned how to use the MongoDB shell to interact with MongoDB.

- **MongoDB Aggregation**: We learned how to use the MongoDB aggregation framework to perform complex queries.

- **Pymongo**: We learned how to use Pymongo to interact with MongoDB from a Python application.

### Code Snippets

```mongo
db.users.insertOne({
    name: "Pelumi",
    age: 25,
    hobbies: ["reading", "coding", "swimming"],
    address: {
        street: "123 Main St",
        city: "Lagos",
        state: "Nigeria",
        zip: "12345"
    }
})
```
```mongo
db.users.find({name: "Pelumi"})
```
```mongo
db.users.find({age: {$gt: 20}})
```
```mongo
db.users.find({hobbies: "coding"})
```
```mongo
db.users.find({hobbies: {$in: ["coding", "swimming"]}})
```

### Resources

- [MongoDB Manual](https://docs.mongodb.com/manual/)
- [MongoDB CRUD Operations](https://docs.mongodb.com/manual/crud/)
- [MongoDB Aggregation](https://docs.mongodb.com/manual/aggregation/)