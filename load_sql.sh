#!/bin/bash
# Load environment variables from .env
if [ -f .env ]; then 
   source .env
fi

# Use defaults pr environment variables
DB_NAME=${DB_NAME:-"intro_db"}
DB_USER=${DB_USER:-"alx_client"}
DB_PASS=${DB_PASS:-"alx_pass"}
CONTAINER=${CONTAINER:-"my-mysql"}

#Check if required variables are set
if [ -z "$DB_NAME" ] || [ -z "$DB_USER" ] || [ -z "$DB_PASS" ]; then
    echo "Error: DB_NAME, DB_USER, and DB_PASS must be set in .env or environment"
    exit 1
fi

for sql_file in * .sql; do
    echo "Loading $sql_file..."
    docker exec -i $CONTAINER mysql -u$DB_USER -p$DB_PASS $DB_NAME < "$sql_file"
done
