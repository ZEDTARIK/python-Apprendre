# This Python code snippet is taking an input value for a timestamp in seconds, then converting it
# into hours, minutes, and seconds. Here's a breakdown of what each line does:
TimeStamp = int(input("Put the value of timestamp : "))
Hour = TimeStamp // 3600 
Reste = TimeStamp % 3600
Minute = Reste // 60
Second = Reste % 60

print(Hour, "h: ", Minute, "m: ", Second, "s")