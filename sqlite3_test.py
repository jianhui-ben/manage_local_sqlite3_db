import sqlite3
from datetime import date
import sys

## test git branch feature1
## passed args: .csv name; db name; table name

def write_csv_to_local_db(csv_name, db_name, table_name):
    connection = sqlite3.connect(db_name) #'test.db'
    cursor = connection.cursor()
    today = date.today()

    ## table creation
    ## this needs to be mannually set up at the first time
    command1 = """CREATE TABLE IF NOT EXISTS
    test_table(year INTEGER, company_name TEXT, revenue FLOAT, date TEXT)"""
    cursor.execute(command1)


    with open(csv_name, 'r') as file:
        next(file) ## depends on if csv has header
        for row in file:
            cursor.execute("INSERT INTO {} VALUES(?,?,?,?)".format(table_name), row.split(',')+[""+today.strftime("%m/%d/%Y")])

    # custom query
    # cursor.execute("select * from test_table where year = 2018")
    # print(cursor.fetchall())
    connection.commit()
    connection.close()


## passed args: .csv name; db name; table name
if __name__=="__main__":
    csv_name, db_name, table_name= sys.argv[1:]
    write_csv_to_local_db(csv_name, db_name, table_name)
    print('All data from '+ csv_name + ' are loaded into ' + db_name +' Table:' + table_name)



