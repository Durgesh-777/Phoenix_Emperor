import sqlite3
import time
from sqlite3 import Error

#Creating a connection

def database_connection():
    try:
        connection = sqlite3.connect("to_do_app.db")
        return connection
    except Error:
        print(Error)

#Creating a table to store values

def create_table(conn):
    cus = conn.cursor()
    cus.execute("CREATE TABLE IF NOT EXISTS details(id INTEGER PRIMARY KEY AUTOINCREMENT, task TEXT NOT NULL, status TEXT NOT NULL, task_time TEXT)")
    conn.commit()
    cus.close()

#Inserting new task in the table

def insert_task(conn, values):
    cus = conn.cursor()
    cus.execute("INSERT INTO details(id,task,status,task_time) VALUES(null,?,'Incomplete',?)", values)
    conn.commit()
    print("Task added")
    cus.close()

#Updating status of task that already exists in the table

def update_status(conn, values):
    cus = conn.cursor()
    cus.execute("UPDATE details SET status = ?, task_time = ? where id = ?", values)
    conn.commit()
    print("Status Updated")
    cus.close()
    
#Updating task which already exisits in the table
    
def update_task(conn, values):
    cus = conn.cursor()
    cus.execute("UPDATE details SET task = ?, task_time = ? where id = ?", values)
    conn.commit()
    print("Task Updated")
    cus.close()

#Deleteing a task from the table

def delete_task(conn, values):
    cus = conn.cursor()
    cus.execute("DELETE FROM details WHERE id = ?", values)
    conn.commit()
    print("Task Removed")
    cus.close()

#Displying the task, status and the time from the table

def view_all_tasks(conn):
    cus = conn.cursor()
    cus.execute("SELECT task,status,task_time FROM details")
    rows = cus.fetchall()
    for row in rows:
        print(row)
    cus.close()
    
#Showing only id and task from the table

def view_update_delete_task(conn):
    cus = conn.cursor()
    cus.execute("SELECT id,task FROM details")
    rows = cus.fetchall()
    for row in rows:
        print(row)
    cus.close()

#The Main fucntion

def main():
    conn = database_connection()
    create_table(conn)

    print("**************** Menu *******************")
    print("\n 1.Create a new task\n 2.Update existing task\n 3.Remove a task\n 4.View all tasks\n 5.Exit\n")

    while True:

        choice = int(input("What do you want to do: "))
        t_time = time.asctime(time.localtime(time.time()))

        #Calling fucntion to insert task
        
        if choice == 1:
            user_task = input("New Task :")
            values = (user_task, t_time)
            insert_task(conn, values)
            print(15*"*")

        #Calling fucntion to update task/status
        
        elif choice == 2:
            view_update_delete_task(conn)
            print("\n1. Update the task \n2. Update the status of task\n")
            choice1 = int(input("Enter your choice: "))
            if choice1 == 1:
                user_id = int(input("Id of task: "))
                user_task = input("Updated Task: ")
                values = (user_task, t_time, user_id)
                update_task(conn, values)
                print(15*"*")
            elif choice1 == 2:
                user_id = int(input("Id of the task: "))
                user_status = input("New Status: ")
                values = (user_status, t_time, user_id)
                update_status(conn, values)
                print(15*"*")
            else:
                print("Invalid Choice")
                print(15*"*")

        #Calling fucntion to remove a task
        
        elif choice == 3:
            view_update_delete_task(conn)
            user_id = int(input("Id of the task: "))
            values = (user_id,)
            delete_task(conn, values)
            print(15*"*")

        #Calling a fuctntion to show all tasks
        
        elif choice == 4:
            view_all_tasks(conn)
            print(15*"*")

        elif choice == 5:
            break
        
        else:
            print("Please choose one of the above tasks mentioned only")

    conn.close()
print("See you again !!!")    
if __name__ == '__main__':
    main()
