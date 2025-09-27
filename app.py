import mysql.connector
from mysql.connector import Error
import os

def connect_to_db():
         try:
             # Use environment variables for credentials (secure practice)
             connection = mysql.connector.connect(
                 host=os.getenv("DB_HOST", "127.0.0.1"),  # Use 'my-mysql' if Dockerized
                 port=3306,
                 user=os.getenv("DB_USER", "alx_client"),
                 password=os.getenv("DB_PASSWORD", "alx_pass"),
                 database=os.getenv("DB_NAME", "alx_book_store")
             )
             if connection.is_connected():
                 print("Connected to MySQL database")
                 return connection
         except Error as e:
             print(f"Error connecting to MySQL: {e}")
             return None

def get_subscribers(connection):
         try:
             cursor = connection.cursor()
             cursor.execute("SELECT * FROM subscribers")
             rows = cursor.fetchall()
             print("Subscribers:")
             for row in rows:
                 print(row)
             cursor.close()
         except Error as e:
             print(f"Error querying subscribers: {e}")

def add_subscriber(connection, first_name, last_name, email, subscription_date, plan, status):
         try:
             cursor = connection.cursor()
             insert_query = """
             INSERT INTO subscribers (first_name, last_name, email, subscription_date, plan, status)
             VALUES (%s, %s, %s, %s, %s, %s)
             """
             values = (first_name, last_name, email, subscription_date, plan, status)
             cursor.execute(insert_query, values)
             connection.commit()
             print(f"Added subscriber: {email}")
             cursor.close()
         except Error as e:
             print(f"Error adding subscriber: {e}")

def main():
         connection = connect_to_db()
         if connection:
             # Query existing subscribers
             get_subscribers(connection)
             
             # Add a new subscriber
             add_subscriber(
                 connection,
                 first_name="Mike",
                 last_name="Lee",
                 email="mike.lee@example.com",
                 subscription_date="2025-09-26",
                 plan="premium",
                 status="active"
             )
             
             # Query again to verify insertion
             get_subscribers(connection)
             
             connection.close()
             print("MySQL connection closed")

if __name__ == "__main__":
         main()
