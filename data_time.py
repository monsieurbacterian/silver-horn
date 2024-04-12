from datetime import datetime

cur_time = datetime.now()
#print(cur_time)
h_end_as = [1, 21]
h_end_sa = [2, 3, 4, 22, 23, 24]
m_end_ta = [1, 21, 31, 41, 51]
m_end_t = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20,]

h = cur_time.hour
m = cur_time.minute

h = 5
m = 36


if h in h_end_as:
    h_w = 'час'
elif h in h_end_sa:
    h_w = 'часа'
else:
    h_w = 'часов'
if m in m_end_ta:
    m_w = 'минута'
elif m in m_end_t:
    m_w = 'минут'
else:
    m_w = 'минуты'
print(f'Сейчас {h} {h_w} {m} {m_w}')




#print(cur_time.hour)
#print(cur_time.minute)
