# For Date and playing sound
from datetime import datetime 
from playsound import playsound


# For checking if the input time format given by the user is correct or not
def Validate_time(alarm_time):
    if len(alarm_time)!=11:
        return "Invalid time format, Please try again"
    else:
        if int(alarm_time[0:2]) > 12:
            return "Invalid Hour Format!,Please Try again"
        elif int(alarm_time[3:5]) > 59:
            return 'Invalid Minute Format!,Please Try again'
        elif int(alarm_time[6:8])>59:
            return "Invalid Seconds Format!,Please Try again"
        else:
            return "Ok"
# we keep on asking untill the user gives the correct format
while True:
    alarm_time = input("Enter the time to be set :HH:MM:SS AM/PM\n ")
    validate = Validate_time(alarm_time)
    if validate !="Ok":
        print(validate)
    else:
        print(f"Setting alarm for {alarm_time}")
        break
#
alarm_hour = alarm_time[0:2]
alarm_min = alarm_time[3:5]
alarm_sec = alarm_time[6:8]
alarm_period = alarm_time[9:].upper()

#keep on iterating untill it hits the time
while True:

    now = datetime.now()

    current_hour = now.strftime("%I")
    current_min = now.strftime("%M")
    current_sec = now.strftime("%S")
    current_period = now.strftime("%p")


    if alarm_period == current_period:
            if alarm_hour == current_hour:
                if alarm_min == current_min:
                    if alarm_sec == current_sec:
                        print("Wake Up!")
                        playsound('audio.mp3')
                        break







