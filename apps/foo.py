import requests
import json


def fetch_setlists_for_year(year: int):
    base_url = "https://kglw.net/api/v2"
    
    path = f"/setlists/showyear/{year}.json"
    
    url = base_url + path
    params = {
        "order_by": "showdate",
        "direction": "asc", 
    }
    resp = requests.get(url, params=params)
    data = (resp.json())
    data = data.get("data")
    show_ids = []
    for show in data: 
        show_ids.append(show.get("show_id"))
    print(set(show_ids))
    print(len(set(show_ids)))

if __name__ == "__main__":
    year = 2024
    setlists = fetch_setlists_for_year(year)