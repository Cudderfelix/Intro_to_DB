#!/bin/bash
DB_NAME="alx_book_store"
DB_USER="alx_client"
DB_PASS="alx_pass"
CONTAINER="my-mysql"

for sql_file in *.sql; do
    echo "Loading $sql_file..."
    docker exec -i $CONTAINER mysql -u$alx_client -p$alx_pass alx_book_store < "$subscribers.sql"
done
