import datetime
from os import system
import os
import subprocess
import sys
import time


if len(sys.argv) == 4:
    year = sys.argv[1]
    day = sys.argv[2]
    day_padded = day.zfill(2)
    part = sys.argv[3]
elif len(sys.argv) == 1:
    today = datetime.date.today()
    year = today.year
    day = today.day
    day_padded = str(day).zfill(2)
    part = 1
else:
    print("Usage: python run.py 2023 1 1")
    print("Usage: python run.py (current day)")
    exit()

file = f"{year}/{day_padded}/part{part}.py"

if not os.path.isfile(file):
    subprocess.run(["python", "create_day.py", str(year), str(day)])

while True:
    system('cls')
    subprocess.run(["python", f"{year}/{day_padded}/part{part}.py"])
    time.sleep(0.25)