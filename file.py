# import pysftp

# host = '112.196.76.14'
# port = 9090
# username = 'root'
# password = 'dvnsv!1$6^5'

# try:
#     conn = pysftp.Connection(host=host, port=port, username=username, password=password)
#     print("Connection established successfully")
    
#     conn.close()
# except Exception as e:
#     print(f'Failed to establish connection to the targeted server: {e}')



import csv
import mysql.connector

mydb = mysql.connector.connect(
    host="",
    user="root",
    password="",
    database="s"
)

# Open the CSV file and read content
with open('dnd.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        mobail_no = row[0]
        first_three_letters_mobail_no = mobail_no[:3] if len(mobail_no) >= 3 else mobail_no 

        query = "SELECT COUNT(*) FROM `insert_new` WHERE `mobail_no` = %s"
        mycursor = mydb.cursor()
        mycursor.execute(query, (mobail_no,))
        result = mycursor.fetchone()

        if result[0] == 0:
            F1 = '1'
            F4 = '4'
            F5 = '5'
            F3 = '6'

            # Insert data into the database
            insert_query = "INSERT INTO `insert_new` (`F1`, `mobail_no`, `F3`, `F4`,`prefix`, `F5`) VALUES (%s, %s, %s, %s, %s, %s)"
            insert = (F1, mobail_no,  F3, F4, first_three_letters_mobail_no, F5)
            mycursor.execute(insert_query, insert)
            mydb.commit()

# Close the database connection
mydb.close()



