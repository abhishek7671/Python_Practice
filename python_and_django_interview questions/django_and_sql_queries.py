Django SQL Queries & Database-related Questions

1. Django ORM Basics
What is Django ORM, and how does it interact with a relational database?
How does Django map models to tables in a database?
How do you retrieve all records from a model in Django?
How do you retrieve a single object by its primary key (ID) in Django?
How do you filter records in Django using filter() method?
What are exclude() and filter() methods in Django ORM? How do they differ?
Explain the get() method in Django ORM. What happens if no results are found or multiple results are returned?
What is values() in Django ORM, and how does it work?
What is the difference between values() and values_list() in Django?
How do you handle NULL values in Django ORM?
What are Django's annotate() and aggregate() methods, and how do you use them?
How do you perform joins in Django using select_related() and prefetch_related()?
How does Django handle one-to-one, one-to-many, and many-to-many relationships in the ORM?
Explain the purpose of distinct() method in Django ORM queries.
How do you handle database transactions in Django?


2. Raw SQL Queries in Django

How do you execute raw SQL queries in Django?
Explain the difference between cursor.execute() and Model.objects.raw() for running raw SQL in Django.
How do you fetch results from a raw SQL query using Django’s connection?
What are the advantages of using Django's ORM over raw SQL queries? When would you use raw SQL?
Can you use SELECT, INSERT, UPDATE, and DELETE statements in Django’s raw SQL queries?
How do you perform a JOIN operation using raw SQL in Django?
What is a GROUP BY operation in SQL? How can you use it in Django ORM or raw SQL queries?
How do you use LIMIT and OFFSET in Django raw SQL queries?
How do you handle database parameterization (avoiding SQL injection) in Django raw SQL queries?
How do you handle transactions when executing raw SQL queries in Django?
Explain how to execute bulk updates or bulk inserts using raw SQL in Django.


3. Complex Queries and Optimization

How would you write a query to retrieve records where a field’s value is greater than a certain number in Django?
What is a subquery, and how can you perform a subquery in Django?
How do you perform aggregation in Django to calculate sums, averages, or counts across a group of records?
What is the difference between F() expressions and raw SQL in Django queries?
Explain how you can optimize database queries in Django.
How do you filter based on related models in Django? For example, how would you retrieve all books by a specific author using Django ORM?
How do you write a query in Django to count records across multiple related models (e.g., counting the number of orders for each customer)?
What is the purpose of select_related() and prefetch_related() in Django, and how do they affect database performance?
What is a CASE WHEN SQL statement, and how do you use it in Django queries?
How can you implement pagination with Django’s ORM for a large set of results?


4. Django and SQL Database Relationships

How does Django handle many-to-many relationships in the database?
How do you use ForeignKey and OneToOneField in Django models to define relationships?
Explain the purpose of ManyToManyField in Django models.
How do you access related models in Django using reverse relationships (e.g., accessing all books from an author)?
How would you retrieve the latest record in a table based on a timestamp or date field in Django?
How would you write a query to get records that match a pattern (similar to SQL LIKE) in Django?
What is a self-referential relationship in Django models, and how would you define it?


5. Django Migrations and Schema Changes

What are migrations in Django, and how do they work?
How do you handle schema changes in a Django project without losing data?
What is the purpose of makemigrations and migrate commands in Django?
How do you undo a migration in Django?
What is the difference between alter and drop migrations in Django?
How do you handle database schema changes manually (e.g., adding a column or modifying a field) in Django?


6. Django Database Indexing and Performance

What is database indexing, and how does it improve performance in Django?
How do you create and manage database indexes in Django?
Explain the difference between unique constraints and database indexes in Django.
How can you optimize a Django query to reduce database load for large datasets?
What are database query plans, and how do you analyze and optimize slow Django queries?


7. Database and Query Debugging in Django

How do you debug SQL queries generated by Django ORM?
How can you view the actual SQL query generated by a Django ORM call?
How do you enable SQL query logging in Django?
How would you profile database queries to identify performance bottlenecks in a Django application?
Additional SQL Interview Questions:
What are the differences between INNER JOIN, LEFT JOIN, and RIGHT JOIN in SQL?
What is normalization and denormalization in databases?
What is ACID in the context of SQL databases?
Explain how you would create and use database triggers in Django.
How would you write a SQL query to find duplicate records in a table?
What is a database transaction, and how do you handle it in Django?
How would you write a query to update multiple records at once based on a condition in Django?
How do you use a JOIN to combine data from two tables, and can you write the SQL equivalent for Django ORM queries?