import pyodbc
import os

# Function to send statistics to zabbix via zabbix sender 
def zabbix(zabbix_host, key, message):
    # Here you must enter the IP of your Zabbix Server
    zabbix_server = '192.168.x.x'
    os.system(f'C:\zabbix_sender.exe -z {zabbix_server} -s {zabbix_host} -k {key} -o "{message}"')  

# Function to query the database and, in case of errors, report to zabbix 
def sql(bd, query, type_result = 0, zabbix_hostname = None, zabbix_key):
    zabbix_host, key = zabbix_hostname, zabbix_key
    try:
        # Here you must enter the name of your ODBC Driver
        # The database user and password were defined as environment variables (DB_User and DB_Pass, respectively) 
        conn = pyodbc.connect('DRIVER={ODBC Driver};'
                          'Server=192.168.x.y;'
                          f'Database={bd};'
                          f"UID={os.environ.get('DB_User')};"
                          f"PWD={os.environ.get('DB_Pass')}")
        conn.autocommit = True
        cursor = conn.cursor()
        
        cursor.execute(query)
        
        if zabbix_hostname != None:
            zabbix(zabbix_host, key, 'normal')
        
        # 0 = Only first row
        # Any other value = multiple rows
        if type_result == 0:
            return cursor.fetchone()
        else:
            return cursor.fetchall()
        
    except Exception as e:
        if zabbix_hostname != None:
            zabbix(zabbix_host, key, f"BD ERROR: {e}")
        else:
            pass
        
#Example with zabbix monitoring:
query = sql('bd_123', 'SELECT * FROM TABLE_123', type_result = 1, zabbix_hostname = 'BD_SERVER', 'bd.check')

for row in query:
    print(row)

#Example without zabbix monitoring:
sql('bd_123', 'TRUNCATE TABLE TABLE_123', type_result = 0)
    