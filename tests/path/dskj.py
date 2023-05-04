from datetime import datetime
from re import sub
var='06-APR-2023'
d=str(datetime.now()).split()[0]
d1=sub(r"-","/",d)

date_obj = datetime.strptime(var,'%d-%b-%Y')
d2=date_obj.strftime('%Y/%m/%d')
d3 = datetime.strptime(d1, "%Y/%m/%d")
d4 = datetime.strptime(d2, "%Y/%m/%d")
delta = d3 - d4
print(f'Difference is {delta.days} days')