"""
1. Реализовать вывод информации о промежутках времени в зависимости от его продолжительности
duration в секундах
а до минуты <sek>
б. до часа <min> <sek>
в. до суток <h> <m> <all_ent_profit>
г* остальных <d> <h> <m> <all_ent_profit>

duration = 53
53 сек
duration = 153
2 мин 33 сек
duration = 4153
1 час 9 мин 13 сек
duration = 400153
4 дн 15 час 9 мин 13 сек
"""
duration_sek = 567789
if duration_sek < 60:
    print(duration_sek, 'сек')
elif 60 <= duration_sek < 3600:
    min_time = duration_sek//60
    sek_time = duration_sek%60
    print(min_time, 'min', sek_time , 'sek')
elif 3600 <= duration_sek < 86400:
    hour_time = duration_sek//3600
    min_time = duration_sek//60%60
    sek_time = duration_sek%60
    print(hour_time, 'h', min_time, 'min', sek_time , 'sek')
#elif 86400 <= duration_sek:
else:
    days_time = duration_sek//86400
    hour_time = duration_sek//3600%24
    min_time = duration_sek//60%60
    sek_time = duration_sek%60
    print(days_time, 'days', hour_time, 'h', min_time, 'min', sek_time , 'sek')

