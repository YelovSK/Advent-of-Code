import requests
import sys
import os
import datetime
from dotenv import load_dotenv

# Usage: python create_day.py 1
day = sys.argv[1]
day_padded = day.zfill(2)

# Check if day is not in the future
today = datetime.date.today()
if day_padded > today.strftime("%d"):
    print("Day is in the future")
    exit()

# Check if folder already exists
if os.path.exists(day_padded):
    print("Day already exists")
    exit()

# Create folder and files
os.mkdir(day_padded)
with open(f"{day_padded}/part1.py", "w") as f:
    f.write(f'with open("{day_padded}/input.txt") as f:\n    data = f.read()')
with open(f"{day_padded}/part2.py", "w") as f:
    f.write(f'with open("{day_padded}/input.txt") as f:\n    data = f.read()')

# Get input
url = f"https://adventofcode.com/2022/day/{day}/input"
load_dotenv()
r = requests.get(url, cookies={"session": os.getenv("AOC_SESSION")})

with open(f"{day_padded}/input.txt", "w") as f:
    f.write(r.text)

with open(f"{day_padded}/test_input.txt", "w") as f:
    pass