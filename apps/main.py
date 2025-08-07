import requests
import json
from datetime import datetime, timedelta

BASE_URL = "https://kglw.net/api/v2"
METHOD   = "setlists"

def fetch_setlists_for_artist_last_year(artist_id=1):
    today        = datetime.now()
    one_year_ago = today - timedelta(days=365)
    results      = []

    for year in range(one_year_ago.year, today.year + 1):
        # insert artist_id filter before the year filter
        url    = f"{BASE_URL}/{METHOD}/artist_id/{artist_id}/showyear/{year}.json"
        params = {
            "order_by": "showdate",
            "direction": "asc"
        }
        resp = requests.get(url, params=params)
        resp.raise_for_status()
        payload = resp.json()
        if payload.get("error") != 0:
            raise RuntimeError(f"API error: {payload.get('error_message')}")

        for sl in payload["data"]:
            show_date = datetime.strptime(sl["showdate"], "%Y-%m-%d")
            if one_year_ago <= show_date <= today:
                results.append(sl)

    return results

if __name__ == "__main__":
    setlists = fetch_setlists_for_artist_last_year(artist_id=1)
    print(f"Retrieved {len(setlists)} setlists for artist 1 from the past year.")

    out_filename = f"setlists_artist_{artist_id}_last_year.json"
    with open(out_filename, "w", encoding="utf-8") as f:
        json.dump(setlists, f, ensure_ascii=False, indent=2)

    print(f"Wrote {len(setlists)} setlists to {out_filename}")