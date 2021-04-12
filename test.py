import datetime
date1 = datetime.datetime(1945, 7, 14)
current_time = 8812800000
print((date1 + datetime.timedelta(milliseconds=current_time)).date())