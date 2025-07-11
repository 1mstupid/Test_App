import requests
import yagmail
from datetime import *
from time import sleep


Urls = ["https://api.sunrise-sunset.org/json", "http://api.open-notify.org/iss-now.json"]

MY_LAT = -2.529450
MY_LNG = -44.296951
CORDS = (MY_LAT,MY_LNG)
Prms = {
    "lat":MY_LAT,
    "lng":MY_LNG,
    "formatted":0
}

response = requests.get(Urls[0],params=Prms)
response.raise_for_status()
data = response.json()


def isslocation():
    response = requests.get(Urls[1])
    data = response.json()
    return (data["iss_position"]["latitude"], data["iss_position"]["longitude"])

def main():
    #

    hour_sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
    
    hour_sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

    while True:
        current_hour = datetime.now().strftime('%H')
        if int(current_hour) > int(hour_sunset) or int(hour_sunrise) < 9:
            cords = isslocation()
            if (CORDS[0]- 5 <= cords[0] <= CORDS[0] + 5) and  (CORDS[1]- 5 <= cords[1] <= CORDS[1] + 5):
                yag = yagmail.SMTP("whatli3swithin@gmail.com", "mscq iaej waoz eugj")
                yag.send("italolv20@gmail.com", "KYS", "You Dirty little fag-boy, you dispicaple piece of trash, today you were blessed by the heavens and didn't even realise, too blind to notice and too scared to seek. Yes that right, today you missed a golden opportunity, to gaze into the start and watching one that we placed there. Anyway, you didn't remeber to check inbox and see the iss, peace.")
                break
        else:
            sleep(30)
            yag = yagmail.SMTP("whatli3swithin@gmail.com", "mscq iaej waoz eugj")
            yag.send("italolv20@gmail.com", "KYS", "It's working bro")
            
    
if __name__ == "__main__":
    main()
