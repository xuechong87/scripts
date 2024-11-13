# coding: utf-8

# generate a  python script to print current date time in chinese

import datetime

print(datetime.datetime.now().strftime("%Y年%m月%d日 %H时%M分%S秒"))

def print_fridays_of_year():
    # 获取当前年份
    current_year = datetime.datetime.now().year
    
    # 遍历当年每一天
    start_date = datetime.datetime(current_year, 1, 1)
    end_date = datetime.datetime(current_year, 12, 31)
    current_date = start_date
    
    while current_date <= end_date:
        # 判断是否为星期五 (weekday() 返回 0-6, 其中 4 代表星期五)
        if current_date.weekday() == 4:
            print(current_date.strftime("%Y年%m月%d日 星期五"))
        current_date += datetime.timedelta(days=1)

# 调用函数
print_fridays_of_year()

