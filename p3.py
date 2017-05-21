# make random CODE and save into MySQL database.

import uuid
import pymysql


def generate_activation_code(num):
    code_list = []
    for i in range(num):
        code = str(uuid.uuid4()).replace('-', '').upper()
        while code in code_list:
            code = str(uuid.uuid4()).replace('-', '').upper()
        code_list.append(code)

    return code_list


def store_in_mysql(code_list):
    try:
        conn = pymysql.connect(host='127.0.0.1',user='root',passwd='cyh921122', db='p3')
        cur = conn.cursor()
    except BaseException as e:
        print(e)
    else:
        try:
            cur.execute('''CREATE TABLE IF NOT EXISTS code6(
                            id INT NOT NULL AUTO_INCREMENT,
                            code VARCHAR(32) NOT NULL,
                            PRIMARY KEY(id)
                        )''')
            for code in code_list:
                cur.execute('INSERT INTO code6(code) VALUES(%s)',(code))
                cur.connection.commit()
        except BaseException as e:
            print(e)
    finally:
        cur.close()
        conn.close()

if __name__ == '__main__':
    store_in_mysql(generate_activation_code(200))
    print('OK!')