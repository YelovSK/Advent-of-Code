import requests
import sys
import os
import datetime
from dotenv import load_dotenv

# Usage: python create_day.py 2023 1
year = sys.argv[1]
day = sys.argv[2]
day_padded = day.zfill(2)

# Check if day is not in the future
today = datetime.date.today()
new_date = datetime.date(int(year), 12, int(day))
if new_date > today:
    print("Day is in the future")
    exit()

base_path = f"{year}/{day_padded}"

# Check if folder already exists
if os.path.exists(base_path):
    print("Day already exists")
    exit()

# Create folder and files
os.mkdir(base_path)
with open(f"{base_path}/part1.py", "w") as f:
    f.write(f'with open("{base_path}/input.txt") as f:\n    data = f.read().strip()')
with open(f"{base_path}/part2.py", "w") as f:
    f.write(f'with open("{base_path}/input.txt") as f:\n    data = f.read().strip()')

# Get input
url = f"https://adventofcode.com/{year}/day/{day}/input"
load_dotenv()
r = requests.get(url, cookies={"session": os.getenv("AOC_SESSION")})

with open(f"{base_path}/input.txt", "w") as f:
    f.write(r.text)

with open(f"{base_path}/test_input.txt", "w") as f:
    pass