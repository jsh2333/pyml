from time import localtime

t = localtime()
start_day = '%d-01-01' %t.tm_year
elapsed_day = t.tm_yday

print('오늘은 [%s]이후 [%d]일째 되는 날입니다.' %(start_day, elapsed_day))
