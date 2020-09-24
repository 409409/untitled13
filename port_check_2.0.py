#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os

def check_port(port_dict):
    cmd='''''ss -tnlp|egrep -i "$1"|awk {'print $4'}|awk -F':' '{if ($NF~/^[0-9]*$/) print $NF}'|sort |uniq   2>/dev/null'''
    local_ports=os.popen(cmd).readlines()
    local_ports_new=[x.strip() for x in local_ports]
    local_ports_new=map(int,local_ports_new)
    for (k,v) in port_dict.items():
        if v in local_ports_new:
            print (k+':'+'\033[1;32;40m 启动成功。\033[0m')
        else:
            print (k+':'+'\033[1;31;40m 启动不成功。\033[0m')
    return

def Goldoffice_trade_api():
    Gta=os.popen("ps -ef | grep Goldoffice_trade_api | grep -v grep|awk {'print $2'}")
    Goldoffice_trade_api_pid=Gta.read()
    Gta.close()
    if Goldoffice_trade_api_pid != '':
        print ("Goldoffice_trade_api"+ ':' + '\033[1;32;40m 启动成功。\033[0m')
    else:
        print ("Goldoffice_trade_api" +':'+'\033[1;31;40m 启动不成功。\033[0m')
    return

server_middle_1={'Nginx':80, 'soul-admin':9009, 'soul-gateway':9010}
server_middle_2={'socketTradeServer':13021, 'socketVisitorServer':13022, 'account':9003}
server_middle_3={'kingQServer':1338}
server_middle_4={'appdb':9001, 'server-YzApi':9017}
server_middle_5={'MySQL':3306, 'RocketMQ':9876, 'ZooKeeper':2181}
server_middle_6={'ZooKeeper':2181}
server_middle_7={'Redis':6379, 'ZooKeeper':2181}
server_middle_8={'app-admin':8081, 'Dubbo-admin':9116, 'LTS-admin':8081}

server_bo_1={'kafka':10940, 'data_sync':10938, 'fastdfs_1':22122, 'fastdfs_2':2300, 'nginx':80}
server_bo_2={'redis_1':7000, 'redis_2':7001, '24k':10880, 'Gateway':10840, 'Goldoffice_web':10811, 'Goldoffice_api':8089, 'zookeeper_3':2181, 'frontoffice':10830, 'open_api':20180, 'nacos':10116, 'push_api':20195, 'chestbox1':10870, 'chestbox2':10870, 'Goldoffice_trade_api':Goldoffice_trade_api_pid}
server_bo_3={'redis_1':7000, 'redis_2':7001, 'Admin_web':10800, 'egpay-management':10970, 'egpay-interface':10960, 'zookeeper':2181}
server_bo_4={'redis_1':7000, 'redis_2':7001, 'rocketmq-server':9876, 'rocketmq-broker':10911, 'rocketmq-console':8858, 'scheduler-gw-deal':9898, 'scheduler-gw-message':9899, 'zookeeper':2181, 'postgresql':5432, 'elasticsearch':19300, 'mongodb':10910, 'influxDB':8086}

server_trade_t1={'ixforex_exchg':10202, 'ixpending':10030, 'ixpnl':10201, 'ixposition':10040, 'ix_access_bo_1':10018, 'ix_access_bo_2':10019, 'ixquote':10060, 'ixproxy':10000, 'ixsms':10190, 'ixemail':10290, 'ixhttp':10200, 'ixopenapi_quote':10450}
server_trade_t2={'ix_access_1':10010, 'ix_access_2':10011, 'ix_trade':10020, 'ixQuoteProxy_1':10052, 'ixQuoteProxy_2':10051, 'ixmarket_1':10053, 'ixmarket_2':10054, 'ixmarket_3':10055, 'ixmarket_4':10056, 'ixmarket_5':10057, 'ixmarket_6':10058, 'ixmarket_7':10059, 'simulated_quotation':5002, 'zk':2181}
server_trade_t3={'ix_access_1':10010, 'ix_access_2':10011, 'ix_trade':10020, 'ixQuoteProxy_1':10052, 'ixQuoteProxy_2':10051, 'ixmarket_1':10053, 'ixmarket_2':10054, 'ixmarket_3':10055, 'ixmarket_4':10056, 'ixmarket_5':10057, 'ixmarket_6':10058, 'ixmarket_7':10059, 'test_market_1':12347, 'test_market_2':23456, 'zk':2181}
server_trade_t4={'ixdb_account':10071, 'ixdb_acct_config':10076, 'ixdb_bo':10077, 'ixdb_config':10073, 'ixdb_http':10080, 'ixdb_id':10074, 'ixdb_market':10075, 'ixdb_session':10072, 'ixdb_user':10070, 'influxdb':8086, 'ssdb':10300, 'zk':2181, 'redis':6379, 'mysql_1':10306, 'mysql_2':10307, 'mysql_3':10308}

print ("a:中间层")
print ("b:业务层")
print ("c:交易层")
project_choose = raw_input("请选择你要检查的项目：")
if project_choose == 'a':
   print ("m1:middle_ip_1")
   print ("m2:middle_ip_2")
   print ("m3:middle_ip_3")
   print ("m4:middle_ip_4")
   print ("m5:middle_ip_5")
   print ("m6:middle_ip_6")
   print ("m7:middle_ip_7")
   print ("m8:middle_ip_8")
   server_middle = raw_input("请选择你要检查的服务器：")
   if server_middle == 'm1':
       check_port(server_middle_1)
       exit(0)
   elif server_middle == 'm2':
       check_port(server_middle_2)
       exit(0)
   elif server_middle == 'm3':
       check_port(server_middle_3)
       exit(0)
   elif server_middle == 'm4':
       check_port(server_middle_4)
       exit(0)
   elif server_middle == 'm5':
       check_port(server_middle_5)
       exit(0)
   elif server_middle == 'm6':
       check_port(server_middle_6)
       exit(0)
   elif server_middle == 'm7':
       check_port(server_middle_7)
       exit(0)
   elif server_middle == 'm8':
       check_port(server_middle_8)
       exit(0)
   else:
       print ("请在m1,m2,m3,m4,m5,m6,m7,m8中选择你要检查的服务器。")
       exit(1)
elif project_choose == 'b':
   print ("b1:bo_1")
   print ("b2:bo_2")
   print ("b3:bo_3")
   print ("b4:bo_4")
   server_bo=raw_input("请选择你要检查的服务器：")
   if server_bo == 'b1':
       check_port(server_bo_1)
       exit(0)
   elif server_bo == 'b2':
       check_port(server_bo_2)
       Goldoffice_trade_api()
       exit(0)
   elif server_bo == 'b3':
       check_port(server_bo_3)
       exit(0)
   elif server_bo == 'b4':
       check_port(server_bo_4)
       exit(0)
   else:
       print ("请在b1,b2,b3,b4中选择你要检查的服务器。")
       exit(1)
elif project_choose == 'c':
   print ("t1:trade_ip_1")
   print ("t2:trade_ip_2")
   print ("t3:trade_ip_3")
   print ("t4:trade_ip_4")
   t_server=raw_input("请选择你要检查的服务器：")
   if t_server == 't1':
       check_port(server_trade_t1)
       exit(0)
   elif t_server == 't2':
       check_port(server_trade_t2)
       exit(0)
   elif t_server == 't3':
       check_port(server_trade_t3)
       exit(0)
   elif t_server == 't4':
       check_port(server_trade_t4)
       exit(0)
   else:
       print ("请在t1,t2,t3,t4中选择你要检查的服务器。")
       exit(1)
else:
    print ("请在a,b,c中选择你要检查的项目。")
    exit(1)
