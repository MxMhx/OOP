park_time = input().split()
hour_in = int(park_time[0])*60
min_in = hour_in + int(park_time[1])
hour_out = int(park_time[2])*60
min_out = hour_out + int(park_time[3])
deltatime = min_out - min_in

#calculate price
if deltatime <= 15:
    print('0')
elif deltatime <= 180:
    print(int((deltatime/60))*10 if deltatime%60 == 0 else int((deltatime/60)+1)*10)
elif deltatime <= 360:
    deltatime -= 180
    print((int(deltatime/60)*20) + 30 if deltatime%60 == 0 else (int((deltatime/60)+1)*20) + 30)
else:
    print('200')