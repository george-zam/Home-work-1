
time = int(input('Please input time in seconds '))
h = time//3600
m = (time//60)%60
s = time%60
if h<10:
    h = str('0' + str(h))
else:
    h = str(h)
if m<10:
    m = str('0' + str(m))
else:
    m = str(m)
if s<10:
    s = str('0' + str(s))
else:
    s = str(s)
print('The duration is', h,'h', m,'m', s,'s')
