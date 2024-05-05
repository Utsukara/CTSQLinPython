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

def add_member():
    """
    Adds a new member to the gym database.
    Prompts the user for name and age.
    """
    print("Enter the following details: ")
    name = input("Name: ")
    age = int(input("Age: "))
    query = "INSERT INTO members (name, age) VALUES (%s, %s)"
    values = (name, age)
    execute_query(query, values)

def add_workout_session():
    """
    Records a new workout session for a gym member.
    Prompts the user for session details.
    """
    print("Enter the following details: ")
    member_id = int(input("Member ID: "))
    workout_time = input("Workout Time: ")
    workout_duration = int(input("Workout Duration: "))
    calories_burned = int(input("Calories Burned: "))
    query = "INSERT INTO workout_sessions (member_id, workout_time, workout_duration, calories_burned) VALUES (%s, %s, %s, %s)"
    values = (member_id, workout_time, workout_duration, calories_burned)
    execute_query(query, values)

def update_member_info():
    """
    Updates information (name or age) for an existing gym member.
    Prompts the user for member ID, attribute to update, and new value.
    """
    print("Enter the following details: ")
    member_id = int(input("Member ID: "))
    change = input("What would you like to change? (name, age): ")
    if change == 'name':
        new_name = input("New Name: ")
        query = "UPDATE members SET name = %s WHERE member_id = %s"
        values = (new_name, member_id)
        execute_query(query, values)
    elif change == 'age':
        new_age = int(input("New Age: "))
        query = "UPDATE members SET age = %s WHERE member_id = %s"
        values = (new_age, member_id)
        execute_query(query, values)
    else:
        print("Invalid input")

def delete_workout_session():
    """
    Deletes a workout session for a gym member.
    Prompts the user for session details.
    """
    print("Enter the following details: ")
    member_id = int(input("Member ID: "))
    workout_time = input("Workout Time: ")
    query = "DELETE FROM workout_sessions WHERE member_id = %s AND workout_time = %s"
    values = (member_id, workout_time)
    execute_query(query, values)