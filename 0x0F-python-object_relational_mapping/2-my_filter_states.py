#!/usr/bin/python3
"""
All values in the states table of
hbtn_0e_0_usa where name matches the argument are displayed.
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

    searched = argv[4]

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE name = BINARY '{:s}' \
                    ORDER BY id ASC;".format(searched))

    result = cursor.fetchall()

    for row in result:
        print(row)

    cursor.close()
    db.close()
