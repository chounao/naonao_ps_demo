import pymysql

select_data = "SELECT * FROM jd_cluster_01.jd_order_part WHERE orderSn = '280304973547'"
select_data1 = "SELECT * FROM jd_cluster_01.jdp_order_part WHERE orderSn = '280304973547'"

conn = pymysql.connect(host="192.168.16.200", port=3307, user='root', passwd='123456qqq', db='qnjy_cluster_01', charset='utf8mb4')
cursor = conn.cursor()
def s_1():

    cursor.execute(select_data)
    res = cursor.fetchall()
    str_new = ','.join(map(str,res))
    lis = str_new.split(',')
    print(lis)
    print(res)
    return res
def s_2():

    cursor.execute(select_data1)
    res1 =cursor.fetchall()

    print(res1)

    return res1
def s_3():
    set1 = set(s_1())
    set2 = set(s_2())
    value = set1.symmetric_difference(set2)
    print(value)
    cursor.close()
    conn.close()


if __name__ == '__main__':
    s_1()