import csv
import psycopg2

def insertSQL(csv):
    #Classes for coloured text
    class txtcolour:
        RED = "\033[1;31;40m"
        GREEN = "\033[1;32;40m"
        YELLOW = "\033[1;33;40m"
        DEFAULT = "\033[0m"
        
        try:
            print(txtcolour.YELLOW + "Input SQL connection details" + txtcolour.DEFAULT)
            
            host = str(input("host"))
            dbname = str(input("dbname"))
            user = str(input("user"))
            
            conn = psycopg2.connect("host={} dbname={} user={}".format(host, dbname, user))
            cur = conn.cursor()
            
            with open(csv, 'r') as f:
                reader = csv.reader(f)
                columns = next(reader)
                query = "INSERT INTO 
                for row in reader:
                    cur.execute(
                        
        except:
            
        else:
    
    return
    
