#!/usr/bin/python3
"""
All states whose name start with
N (upper N) from the database hbtn_0e_0_usa are listed
"""

if __name__ == '__main__':
    from sys import argv
    import MySQLdb as mysql

    try:
        db = mysql.connect(host='localhost', port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3])
    except Exception:
        print('Connection to the database has failed')
        exit(0)

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states \
                    WHERE name LIKE BINARY 'N%' ORDER BY id ASC;")

    result = cursor.fetchall()

    for row in result:
        print(row)

    cursor.close()
    db.close()
