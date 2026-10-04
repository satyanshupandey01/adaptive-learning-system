import psycopg

connection = psycopg.connect(
    "dbname=adaptive_learning"
)

print("Database connection successful!")

connection.close()