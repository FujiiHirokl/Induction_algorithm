import mysql.connector
from mysql.connector import Error
from mysql.connector.pooling import MySQLConnectionPool

# Database configuration
db_config = {
    "user": "root",
    "password": "wlcm2T4",
    "host": "localhost",
    "database": "root",
    "charset": "utf8mb4"
}

# Create a connection pool
connection_pool = MySQLConnectionPool(pool_name="mypool", pool_size=5, **db_config)

def get_coordinates_database():
    """
    Retrieve coordinates from the database.

    Returns:
        tuple: Coordinates (x, y).
    """
    try:
        # Get a connection from the pool
        connection = connection_pool.get_connection()
        cursor = connection.cursor()

        # Use parameterized query to prevent SQL injection
        select_query = "SELECT x, y FROM coordinates WHERE id = %s;"
        cursor.execute(select_query, (1,))

        # Get the result
        result = cursor.fetchone()

        # Release resources
        cursor.close()
        connection.close()

        return result

    except Error as e:
        return {"error": str(e)}

def get_geomagnetism_database():
    """
    Retrieve geomagnetism information from the database.

    Returns:
        float: Geomagnetism information.
    """
    try:
        # Get a connection from the pool
        connection = connection_pool.get_connection()
        cursor = connection.cursor()

        # Use parameterized query to prevent SQL injection
        select_query = "SELECT direction FROM geomagnetism WHERE ID = %s;"
        cursor.execute(select_query, (1,))

        # Get the result
        result = cursor.fetchone()

        # Release resources
        cursor.close()
        connection.close()

        return result

    except Error as e:
        return {"error": str(e)}
    
def get_route_information():
    try:
        # Get a connection from the pool
        connection = connection_pool.get_connection()
        cursor = connection.cursor()

        # Use parameterized query to prevent SQL injection
        select_query = "SELECT direction FROM geomagnetism WHERE ID = %s;"
        cursor.execute(select_query, (1,))

        # Get the result
        result = cursor.fetchone()

        # Release resources
        cursor.close()
        connection.close()

        return result

    except Error as e:
        return {"error": str(e)}
    

def __main__():
    print(get_coordinates_database())
    print(get_geomagnetism_database())

if __name__ == "__main__":
    __main__()
