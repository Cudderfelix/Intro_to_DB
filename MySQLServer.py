import mysql.connector
from mysql.connector import Error

try:
    # Establish connection to MySQL server
    connection = mysql.connector.connect(
        host="localhost",
        user="cudder_felix",  
        password="admin_pass"  
    )
    
    if connection.is_connected():
        cursor = connection.cursor()
        # Create database if it doesn't exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")
        
except Error as e:
    if e.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
        print("Error: Invalid username or password. Please check your credentials.")
    elif e.errno == mysql.connector.errorcode.ER_HOST_NOT_FOUND:
        print("Error: Could not connect to MySQL server. Please check the host.")
    else:
        print(f"Error: Failed to connect or create database: {e}")
        
finally:
    # Close database connection
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("Database connection closed.")