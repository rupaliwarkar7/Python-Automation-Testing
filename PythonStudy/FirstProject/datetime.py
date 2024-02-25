import datetime
x = datetime.datetime.now()
print(x)




import datetime
x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))


import datetime
tm = datetime.time(1, 30, 11, 22)
print(tm)

from datetime import datetime
print(datetime.strptime('15/11/2000', '%d/%m/%Y'))