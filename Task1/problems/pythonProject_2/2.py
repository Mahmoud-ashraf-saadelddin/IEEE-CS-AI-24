from datetime import datetime, timedelta

day, month, year = map(int, input().split())
today = datetime(year, month, day)

tomorrow = today + timedelta(days=1)
print(f"Day : {tomorrow.day}    Month: {tomorrow.month}   Year: {tomorrow.year}")
