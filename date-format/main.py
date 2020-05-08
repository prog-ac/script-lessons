import datetime
import locale

locale.setlocale(locale.LC_TIME, 'ja_JP.UTF-8')

now = datetime.datetime.now()

year = now.strftime("%Y")
month = now.strftime("%m")
day = now.strftime("%d")

day_of_the_week = now.strftime("%a")

print("{0}年{1}月{2}日({3})".format(year, month, day, day_of_the_week))
