import pymysql

def check_if_account_exists(username,password):
    conn = pymysql.connect(host='10.221.137.167',
                           user='root',
                           db='supermarket',
                           passwd='a887400',
                           port=3306,
                           charset="utf8"
                           )

    cursor = conn.cursor()
    sql = "SELECT * FROM staffacc WHERE empl_id='%s' AND staff_psw='%s'"
    data = (username, password)
    cursor.execute(sql % data)
    values = cursor.fetchall()
    if values:
        return True
    else:
        return False
