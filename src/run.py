import datetime
print(datetime.datetime.now())

with open("./result/time.txt", mode='w') as f:
    f.write(str(datetime.datetime.now()))
