months = {'Enero': 1, 'Febrero': 2, 'Marzo': 3}

sdate = '07 de Febrero del 2020'
day = int(sdate[0:2])
year = int(sdate[-4:])
month = months[sdate.split(' ')[2]]
print(day)
print(year)
print(month)
