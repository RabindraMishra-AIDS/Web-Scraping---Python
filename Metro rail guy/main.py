import requests
url="https://themetrorailguy.com/2024/05/25/rvnl-wins-nagpur-metro-phase-2-c-08s-contract-for-6-stations/"
r=requests.get(url)
print(r.text)