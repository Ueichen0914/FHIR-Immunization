from datetime import datetime

value = "20200505"
svalue = value[:4] + "-" + value[4:6] + "-" + value[6:8]
print(svalue)
try:
    d_format = datetime.strptime(svalue, "%Y-%m-%d")
except:
    print("hello world")
print(d_format.strftime("%Y-%m-%d"))