currentTime = int(input("Input required number of seconds: "))

seconds = currentTime

minutes = (currentTime / 60)  

hours = (currentTime / 3600 ) 

days = currentTime / 86400

print(f"days:  {int(days)} \n hours: {int(hours)} \n minutes: {int(minutes)} \n seconds: {int(seconds)}")
input("Press Enter to close program")
exit()