#!/usr/bin/python3
"""all cities from the database hbtn_0e_4_usa are listed"""

if __name__ == '__main__':
    from sys import argv
    import MySQLdb as mysql

    if (len(argv) != 4):
        print('Use: username, password, database name')
        exit(1)

    try:
        db = mysql.connect(host='localhost', port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3])
    except Exception:
        print('connection error')
        exit(0)

    cursor = db.cursor()

    cursor.execute("""SELECT c.id, c.name, s.name FROM cities as c
                      INNER JOIN states as s
                      ON c.state_id = s.id
                      ORDER BY c.id ASC;""")

    result = cursor.fetchall()

    for row in result:
        print(row)

    cursor.close()
    db.close()
