import mysql.connector
from mysql.connector import Error

def add_member():
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='fitness_center_db',
                                             user='root',
                                             password='Kelly')
        cursor = connection.cursor()
        print("Enter the following details: ")
        name = input("Name: ")
        age = int(input("Age: "))
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.execute("INSERT INTO members (name, age) VALUES (%s, %s)", (name, age))
            connection.commit()
            cursor.close()
            connection.close()
            print("Member added successfully")

def add_workout_session():
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='fitness_center_db',
                                             user='root',
                                             password='Kelly')
        cursor = connection.cursor()
        print("Enter the following details: ")
        member_id = int(input("Member ID: "))
        workout_time = input("Workout Time: ")
        workout_duration = int(input("Workout Duration: "))
        calories_burned = int(input("Calories Burned: "))
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.execute("INSERT INTO workout_sessions (member_id, workout_time, workout_duration, calories_burned) VALUES (%s, %s, %s, %s)", (member_id, workout_time, workout_duration, calories_burned))
            connection.commit()
            cursor.close()
            connection.close()
            print("Workout session added successfully")

def update_member_info():
    try:
        connection = mysql.connector.connect(host='localhost',
                                                database='fitness_center_db',
                                                user='root',
                                                password='Kelly')
        cursor = connection.cursor()
        print("Enter the following details: ")
        member_id = int(input("Member ID: "))
        change = input("What would you like to change? (name, age): ")
        if change == 'name':
            new_name = input("New Name: ")
            cursor.execute("UPDATE members SET name = %s WHERE member_id = %s", (new_name, member_id))
        elif change == 'age':
            new_age = int(input("New Age: "))
            cursor.execute("UPDATE members SET age = %s WHERE member_id = %s", (new_age, member_id))
        else:
            print("Invalid input")
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            connection.commit()
            cursor.close()
            connection.close()
            print("Member info updated successfully")

def delete_workout_session():
    pass