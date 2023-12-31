# import paramiko

# # Server credentials
# host = '112.196.76.14'
# port = 9090
# username = 'root'
# password = 'dvnsv!1$6^5'
# remote_file_path = '/home/PutAllFiveServerDndFile/MergedDndNoOfFiveServer_2023-12-18.xls'  
# local_file_path = 'D:/SFTP/localfile.xls'  

# # Create an SSH client
# ssh_client = paramiko.SSHClient()


# ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# try:
#     # Connect to  server
#     ssh_client.connect(hostname=host, port=port, username=username, password=password)

#     # Create an SFTP client from the SSH client
#     sftp_client = ssh_client.open_sftp()

#     # Download the remote file
#     sftp_client.get(remote_file_path, local_file_path)
#     print(f"File downloaded successfully to {local_file_path}")

#     # Close the SFTP session and the SSH connection
#     sftp_client.close()
#     ssh_client.close()

# except paramiko.AuthenticationException:
#     print("Authentication failed. Please check your credentials.")
# except paramiko.SSHException as ssh_err:
#     print(f"Unable to establish SSH connection: {ssh_err}")
# except Exception as e:
#     print(f"An error occurred: {e}")



















# import csv
# import mysql.connector

# mydb = mysql.connector.connect(
#     host="",
#     user="root",
#     password="",
#     database="s"
# )

# # Open the CSV file and read content
# with open('dndfinal.csv') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     for row in csv_reader:
#         mobail_no = row[0]
#         first_three_letters = mobail_no[:3] if len(mobail_no) >= 3 else mobail_no 

#         query = "SELECT COUNT(*) FROM `insert_new` WHERE `mobail_no` = %s"
#         mycursor = mydb.cursor()
#         mycursor.execute(query, (mobail_no,))
#         result = mycursor.fetchone()

#         if result[0] == 0:
#             F1 = '1'
#             F4 = '4'
#             F5 = '5'
#             F3 = '6'

#             # Insert data into the database
#             insert_query = "INSERT INTO `insert_new` (`F1`, `mobail_no`, `F3`, `F4`,`prefix`, `F5`) VALUES (%s, %s, %s, %s, %s, %s)"
#             insert = (F1, mobail_no,  F3, F4, first_three_letters, F5)
#             mycursor.execute(insert_query, insert)
#             mydb.commit()

# # Close the database connection
# mydb.close()
















# import csv
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/s'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)

# class Insert_new(db.Model):
#     __tablename__ = 'insert_new'
#     id = db.Column(db.Integer, primary_key=True)
#     F1 = db.Column(db.String(100), nullable=False)
#     mobail_no = db.Column(db.String(100), nullable=False)
#     F3= db.Column(db.String(100), nullable=False)
#     F4 = db.Column(db.String(100), nullable=False)
#     prefix = db.Column(db.String(200), nullable=False)
#     F5 = db.Column(db.String(200), nullable=False)

# # Read the CSV file and insert data into the database
# def read_csv_and_insert():
#     with open('dndfinal.csv') as csv_file:
#         csv_reader = csv.reader(csv_file, delimiter=',')
        
#         for row in csv_reader:
#             mobail_no = row[0]
#             first_three_letters_mobail_no = mobail_no[:3] if len(mobail_no) >= 3 else mobail_no

#             existing_entry = Insert_new.query.filter_by(mobail_no=mobail_no).first()

#             if not existing_entry:
#                 F1 = '1'
#                 F4 = '4'
#                 F5 = '5'
#                 F3 = '6'

#                 new_data = Insert_new(F1=F1, mobail_no=mobail_no, F3=F3, F4=F4, 
#                                       prefix=first_three_letters_mobail_no, F5=F5)
#                 db.session.add(new_data)
#                 db.session.commit()


# with app.app_context():
#     read_csv_and_insert()












# import pandas as pd
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)

# # Configure the database connection
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/s'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)

# class Sdm(db.Model):
#     __tablename__ = 'sdm'
#     id = db.Column(db.Integer, primary_key=True)
#     F1 = db.Column(db.String(100), nullable=False)
#     mobail_no = db.Column(db.String(100), nullable=False)
#     F3 = db.Column(db.String(100), nullable=False)
#     F4 = db.Column(db.String(100), nullable=False)
#     prefix = db.Column(db.String(200), nullable=False)
#     F5 = db.Column(db.String(200), nullable=False)

# def read_excel_and_insert():
#     excel_data = pd.read_excel('dndrai.xlsx', header=None)
        
#     for index, row in excel_data.iterrows():
#         mobail_no = str(row[0])
#         first_three_letters_mobail_no = mobail_no[:3] if len(mobail_no) >= 3 else mobail_no

#         existing_entry = Sdm.query.filter_by(mobail_no=mobail_no).first()

#         if not existing_entry:
#             F1 = '1'
#             F3 = '6'
#             F4 = '4'
#             F5 = '5'

#             new_data = Sdm(F1=F1,mobail_no=mobail_no,F3=F3,F4=F4,
#                                      prefix=first_three_letters_mobail_no,F5=F5
#                 )
#             db.session.add(new_data)
#             db.session.commit()

# with app.app_context():
#     result = read_excel_and_insert()
#     print(result) 










# import pandas as pd
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# import concurrent.futures

# app = Flask(__name__)

# # Configure the database connection
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/s'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)

# class Insert_new(db.Model):
#     __tablename__ = 'insert_new'
#     id = db.Column(db.Integer, primary_key=True)
#     F1 = db.Column(db.String(100), nullable=False)
#     mobail_no = db.Column(db.String(100), nullable=False)
#     F3 = db.Column(db.String(100), nullable=False)
#     F4 = db.Column(db.String(100), nullable=False)
#     prefix = db.Column(db.String(200), nullable=False)
#     F5 = db.Column(db.String(200), nullable=False)

# def read_and_insert(data):
#     with app.app_context():
#         for data, row in data.iterrows():
#             mobail_no = str(row[0])
#             three_letters_mobail_no = mobail_no[:3] if len(mobail_no) >= 3 else mobail_no

#             entry = Insert_new.query.filter_by(mobail_no=mobail_no).first()

#             if not entry:
#                 F1 = '1'
#                 F3 = '6'
#                 F4 = '4'
#                 F5 = '5'

#                 new_data = Insert_new(F1=F1, mobail_no=mobail_no, F3=F3, F4=F4,
#                                prefix=three_letters_mobail_no, F5=F5)
#                 db.session.add(new_data)
#                 db.session.commit()

# def read_excel_insert():
#     excel_data = pd.read_excel('dndrai.xlsx', header=None)

    

#     with concurrent.futures.ThreadPoolExecutor(max_workers=400) as executor:
#         data_size = 1000  
#         data = [excel_data[i:i + data_size] for i in range(0, excel_data.shape[0], data_size)]

#         executor.map(read_and_insert, data)


   

# if __name__ == "__main__":
#     read_excel_insert()


# db.session.close()







# import pandas as pd
# import pymysql

# # Connect to database
# connection = pymysql.connect(host='localhost',user='root',password='',database='s',
#                              cursorclass=pymysql.cursors.DictCursor)

# def data_insert(data):
#     entries = []

#     for _, row in data.iterrows():
#         mobail_no = str(row[0])
#         three_letters_mobail_no = mobail_no[:3] if len(mobail_no) >= 3 else mobail_no

#         entry = {'F1': '1','mobail_no': mobail_no,'F3': '6','F4': '4',
#                  'prefix': three_letters_mobail_no,'F5': '5'
#         }
#         entries.append(entry)

#     with connection.cursor() as cursor:
#         insert_query = "INSERT INTO insert_new (F1, mobail_no, F3, F4, prefix, F5) VALUES (%(F1)s, %(mobail_no)s, %(F3)s, %(F4)s, %(prefix)s, %(F5)s)"
#         cursor.executemany(insert_query, entries)
#         connection.commit()

# def read_excel_insert():
#     excel_data = pd.read_excel('dndrai.xlsx', header=None)

#     data_size = 100000  
#     data = [excel_data[i:i + data_size] for i in range(0, excel_data.shape[0], data_size)]

#     for chunk in data:
#         data_insert(chunk)

# if __name__ == "__main__":
#     read_excel_insert()
#     connection.close()






import datetime
import openpyxl
import pandas as pd
import pymysql
from concurrent.futures import ThreadPoolExecutor

# Connect to the MySQL database
try:
    connection = pymysql.connect(host='localhost', user='root', password='', database='s',
                                 cursorclass=pymysql.cursors.DictCursor)
    print("DB connection successful")
except:
    print("DB connection failed")

def data_insert(data):
    duplicate_data = set()
    duplicate = 0 

    try:
        with connection.cursor() as cursor:
            select_query = "SELECT F2 FROM insert_new"
            cursor.execute(select_query)
            sdm = cursor.fetchall()

            for row in sdm:
                duplicate_data.add(row['F2'])  
    except :
        print("Duplicate data error")

    list_data = []

    for _, row in data.iterrows():
        mobail_no = str(row[0])
        three_letters_mobail_no = mobail_no[:3] if len(mobail_no) >= 3 else mobail_no

        if mobail_no not in duplicate_data:
            entry = {
                'F1': '1',
                'F2': mobail_no,
                'F3': '6',
                'F4': '4',
                'prefix': three_letters_mobail_no,
                'F5': '5'
            }
            list_data.append(entry)
        else:
            duplicate += 1


    try:
        if list_data:
            with connection.cursor() as cursor:
                insert_query = "INSERT INTO insert_new (F1, F2, F3, F4, prefix, F5) VALUES (%(F1)s, %(F2)s, %(F3)s, %(F4)s, %(prefix)s, %(F5)s)"
                cursor.executemany(insert_query, list_data)
                connection.commit()
                print("Data inserted successfully")

                for data in list_data:
                    print(data)
                
    except:
        print("Error Insert ")

    print(f"Total duplicate found: {duplicate}")

def read_csv_insert():
    current_date = datetime.datetime.now().strftime("%Y_%m_%d")
    file_path = f'MergedDndNoOfFiveServer_{current_date}.csv'
    csv_data = pd.read_csv(file_path, header=None)
    
    
    print(file_path)
    
    data_size = 100000  
    data = [csv_data[i:i + data_size] for i in range(0, csv_data.shape[0], data_size)]

    with ThreadPoolExecutor(max_workers=1) as executor:
        executor.map(data_insert, data)

read_csv_insert()
connection.close()
