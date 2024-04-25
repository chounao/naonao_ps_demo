import time
import pymysql


timestamp = int(time.time())
createTime = ''
wlbCode = "433377758724714"
orderId = "1947701858270704297"
logisticsTime = "1"
acceptTime = ""
transportTime = ""
signTime = "2"
logisticsStatus = ''
selct_data  = "UPDATE logistics_chargetime_cn_part SET logisticsTime = {},logisticsStatus = {},createTime = {},WHERE wlbCode = {}".format(logisticsTime,logisticsStatus,createTime,wlbCode)
print(selct_data)
conn = pymysql.connect(host="192.168.16.200", port=3307, user='root', passwd='123456qqq', db='qnjy_cluster_01', charset='utf8mb4')
cursor = conn.cursor()
# cursor.execute('SELECT  *FROM logistics_chargetime_cn_part  WHERE wlbCode = "433377758724714"')
# #待揽收状态
# cursor.execute("UPDATE logistics_chargetime_cn_part SET logisticsTime = '1691480100',logisticsStatus = '',createTime = '',WHERE wlbCode = '433377758724714'")
# #揽收超时状态
# cursor.execute("UPDATE logistics_chargetime_cn_part SET logisticsTime = '1691480100',logisticsStatus = '',createTime = '',WHERE wlbCode = '433377758724714'")
# #运输中状态
# cursor.execute("UPDATE logistics_chargetime_cn_part SET logisticsTime = '1691480100',logisticsStatus = '',createTime = '',WHERE wlbCode = '433377758724714'")
#
# #物流停滞状态
#
# #派送中状态
#
# #签收超时状态
#
#
#
#
# row = cursor.fetchall()
# cursor.close()
# conn.close()
# print(row)
