import pysftp

host = '112.196.76.14'
port = 9090
username = 'root'
password = 'dvnsv!1$6^5'

try:
    conn = pysftp.Connection(host=host, port=port, username=username, password=password)
    print("Connection established successfully")
    
    conn.close()
except Exception as e:
    print(f'Failed to establish connection to the targeted server: {e}')
