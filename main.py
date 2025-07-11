import os
import requests
import yagmail
from datetime import datetime

MY_LAT = -2.529450
MY_LNG = -44.296951
CORDS = (MY_LAT, MY_LNG)
Prms = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}
Urls = ["https://api.sunrise-sunset.org/json", "http://api.open-notify.org/iss-now.json"]

def isslocation():
    response = requests.get(Urls[1])
    data = response.json()
    return (float(data["iss_position"]["latitude"]), float(data["iss_position"]["longitude"]))

def main():
    response = requests.get(Urls[0], params=Prms)
    response.raise_for_status()
    data = response.json()

    hour_sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    hour_sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    current_hour = datetime.utcnow().hour  # API times are UTC, so use UTC time

    if current_hour > hour_sunset or current_hour < hour_sunrise:
        cords = isslocation()
        if (CORDS[0] - 5 <= cords[0] <= CORDS[0] + 5) and (CORDS[1] - 5 <= cords[1] <= CORDS[1] + 5):
            yag = yagmail.SMTP(os.environ["YAGMAIL_USER"], os.environ["YAGMAIL_PASS"])
            yag.send(os.environ["EMAIL_TO"], "ISS Alert", "The ISS is near your location!")
        else:
            print("ISS not near, no email sent.")
    else:
        print("It is daytime, no email sent.")

if __name__ == "__main__":
    main()

