time_sec = int(input("Укажите время в секундах : "))
hour = time_sec // 3600
min = (time_sec - (hour * 3600)) // 60
sec = time_sec - ((hour * 3600) + (min * 60))
print(f" Время чч:мм:сек  {hour} : {min} : {sec}")
