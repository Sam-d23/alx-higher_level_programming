#!/usr/bin/python3
"""All states from the database hbtn_0e_0_usa are listed"""

if __name__ == '__main__':
    from sys import argv
    import MySQLdb as mysql

    try:
        db = mysql.connect(host='localhost', port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3])
    except Exception:
        print('Failed connecting to the database')
        exit(0)

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states ORDER BY id ASC;")

    result = cursor.fetchall()

    for row in result:
        print(row)

    cursor.close()
    db.close()
