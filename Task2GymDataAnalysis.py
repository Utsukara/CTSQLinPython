import mysql.connector
from mysql.connector import Error

def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='fitness_center_db',
            user='root',
            password='Kelly'
        )
        return connection
    except Error as e:
        print("Error while connecting to MySQL:", e)
        return None

def execute_query(query, values=None):
    """
    Executes an SQL query on the connected database.

    Args:
    - query: The SQL query to execute.
    - values: Optional parameter values for a parameterized query.

    Returns:
    - results: The result set obtained after executing the query.
    """
    connection = connect_to_database()
    if connection is None:
        return
    
    try:
        cursor = connection.cursor()
        if values:
            cursor.execute(query, values)
        else:
            cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
        results = cursor.fetchall()
        return results
    except Error as e:
        print("Error while executing query:", e)
        return None
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def list_distinct_trainers():
    """
    Retrieves unique trainer IDs from the Members table.

    Returns:
    - trainers: A list of unique trainer IDs.
    """
    query = "SELECT DISTINCT trainer_id FROM Members"
    results = execute_query(query)
    if results:
        return [result[0] for result in results]
    else:
        return []

def count_members_per_trainer():
    """
    Counts the total number of members assigned to each trainer.

    Returns:
    - member_counts: A list of tuples containing trainer ID and member count.
    """
    query = "SELECT trainer_id, COUNT(*) AS member_count FROM Members GROUP BY trainer_id"
    results = execute_query(query)
    if results:
        return results
    else:
        return []

def get_members_in_age_range(start_age, end_age):
    """
    Retrieves details of members whose ages fall within a specified range.

    Args:
    - start_age: The lower bound of the age range.
    - end_age: The upper bound of the age range.

    Returns:
    - members: A list of tuples containing member name, age, and trainer ID.
    """
    query = "SELECT name, age, trainer_id FROM Members WHERE age BETWEEN %s AND %s"
    values = (start_age, end_age)
    results = execute_query(query, values)
    if results:
        return results
    else:
        return []

# Example usage:
# trainers = list_distinct_trainers()
# print("Distinct Trainers:", trainers)
# member_counts = count_members_per_trainer()
# print("Member Counts per Trainer:", member_counts)
# members_in_age_range = get_members_in_age_range(25, 30)
# print("Members in Age Range 25-30:", members_in_age_range)