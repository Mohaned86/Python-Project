


import sqlite3
# importing sqlite3 module 


conn = sqlite3.connect('test.db')
# create variable and connected to database file

with conn:
    # create table into the database file
    # ctrate variable and assigined it to the cuesor
    # create coloms in the table
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tb1_persons( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fname TEXT, \
        col_lname TEXT, \
        col_email TEXT \
        )")
    conn.commit()
    # commit the update
conn.close()
# close the file



conn = sqlite3.connect('test.db')

with conn:
    cur = conn.cursor()
    # insert values to the coloms in the table
    cur.execute("INSERT INTO tb1_persons(col_fname, col_lname, col_email) VALUES (?,?,?)", \
                ('nadia', 'salih', 'nadiasalih@gmail.com'))
    # insert values to the coloms in the table
    cur.execute("INSERT INTO tb1_persons(col_fname, col_lname, col_email) VALUES (?,?,?)", \
                ('hassan', 'taj', 'hassantaj@gmail.com'))
    # insert values to the coloms in the table
    cur.execute("INSERT INTO tb1_persons(col_fname, col_lname, col_email) VALUES (?,?,?)", \
                ('amna', 'adan', 'amnaadam@gmail.com'))
    conn.commit()
    # commit the update
conn.close()
# close the file

conn = sqlite3.connect('test.db')

with conn:
    cur = conn.cursor()
    # quering value from the table in spacifice condition
    cur.execute("SELECT col_fname, col_lname, col_email FROM tb1_persons WHERE col_fname = 'nadia'")
    varPerson = cur.fetchall()
    # create variable and assigned it to the cursor and make it itrate through the values in the table
    for item in varPerson:
        # vreate a loop to itrate through the table
        msg = "First Name: {}\nLast Name: {}\nEmail: {}".format(item[0], item[1], item[2])
        # create variable and assign it to output formation 
    print(msg)
    # print the resulte



def readList():
    # create a function and use loop through the file in same directory and give it permission to read only
    with open('list.txt', 'r') as l:
        # craete variable and assign it to reading the list
        data = l.read()
        # print the resulte
        print(data)
        # close the file
        l.close()

if __name__ == "__main__":
    readList()
