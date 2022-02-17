from datetime import date, timedelta

print((date(int(input('Year: ')), 1, 1) + timedelta(int(input('Day: ')) - 1)).strftime('%d %B'))
