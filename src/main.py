#!/usr/bin/env python3
import datetime
from mail import send_email

def get_prompt():
    with open("./prompts.txt", "r") as file:
        prompts = file.readlines()
    doy = datetime.datetime.now().timetuple().tm_yday
    return prompts[doy - 1].strip()

def get_season():
    doy = datetime.datetime.now().timetuple().tm_yday

    if doy not in [1, 92, 184, 278,341]:
        return None

    if doy == 1:
        season = "1.txt"
    elif doy == 92:
        season = "2.txt"
    elif doy == 184:
        season = "3.txt"
    elif doy == 278:
        season = "4.txt"
    elif doy == 341:
        season = "1.txt"
    with open(f"./seasons/{season}", "r") as file:
        return file.readlines()

def send_season_email():
    season = get_season()
    if season is None:
        return
    print(season)
    send_email(f"✨ Prompt Of The Day - A New Season: {season[0]}✨", season[2])

def send_prompt_email():
    prompt_of_the_day = get_prompt()
    print(prompt_of_the_day)
    send_email("📝 Prompt of the day 📝", prompt_of_the_day)

if __name__ == "__main__":
    send_prompt_email()
    send_season_email()