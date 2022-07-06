import os
import configparser
#날짜 관리
import datetime


libdir = os.path.dirname(__file__)

config = configparser.ConfigParser()
config.read(libdir + '/config.ini')

name=config['SERVER']['name']
server_ip=config['SERVER']['server_ip']
database_name=config['SERVER']['database_name']
user_name =config['SERVER']['user_name']
user_password=config['SERVER']['user_password']
char=config['SERVER']['char']

my_sql_user=config['my-sql-db-server']['my_sql_user']
my_sql_password=config['my-sql-db-server']['my_sql_password']
my_sql_host=config['my-sql-db-server']['my_sql_host']
my_sql_db=config['my-sql-db-server']['my_sql_db']
my_sql_charset=config['my-sql-db-server']['my_sql_charset']

today_now = datetime.datetime.now()
xml_today=today_now.strftime("%Y%m%d")
xml_month=today_now.strftime("%Y%m")+"01"

DB_ym=today_now.strftime("%Y%m")

xml_password='ka22fslfod1vid'

# 메세지 발송
protocol = config['solapi']['protocol']
domain = config['solapi']['domain']
prefix = config['solapi']['prefix']
api_key = config['solapi']['api_key']
api_secret = config['solapi']['api_secret']


# 카카오 연동(회원 로그인)
api_name=config['kakao']['api_name']
api_site=config['kakao']['api_site_name']
api_code=config['kakao']['api_code']
api_site_address=config['kakao']['api_site_address']
api_site_url=config['kakao']['api_site_url']
api_1_key=config['kakao']['api_1_key']
api_2_key=config['kakao']['api_2_key']
api_3_key=config['kakao']['api_3_key']
api_4_key=config['kakao']['api_4_key']
api_5_key=config['kakao']['api_5_key']