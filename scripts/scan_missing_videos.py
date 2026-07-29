# -*- coding: utf-8 -*-
"""
DRY RUN: Cadbim Teknik Destek kanalındaki TÜM videoları tarar (uploads playlist
üzerinden sayfalama ile), assets/data/blog-posts.json'daki mevcut videoId'lerle
karşılaştırır, hiçbir dosyayı DEĞİŞTİRMEDEN eksik videoların listesini yazdırır.
"""
import json
import os
import urllib.parse
import urllib.request

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
POSTS_JSON = os.path.join(BASE, "assets", "data", "blog-posts.json")

API_KEY = os.environ.get("YOUTUBE_API_KEY")
CHANNEL_ID = os.environ.get("YOUTUBE_CHANNEL_ID", "UCGLIaycdAkSFM3Q54d3zVQg")
UPLOADS_PLAYLIST_ID = "UU" + CHANNEL_ID[2:]

def api_get(url, params):
    qs = urllib.parse.urlencode(params)
    with urllib.request.urlopen(f"{url}?{qs}", timeout=30) as r:
        return json.loads(r.read().decode("utf-8"))

def fetch_all_uploads():
    videos = []
    page_token = None
    while True:
        params = {
            "key": API_KEY,
            "playlistId": UPLOADS_PLAYLIST_ID,
            "part": "snippet",
            "maxResults": 50,
        }
        if page_token:
            params["pageToken"] = page_token
        data = api_get("https://www.googleapis.com/youtube/v3/playlistItems", params)
        for item in data.get("items", []):
            sn = item["snippet"]
            vid = sn["resourceId"]["videoId"]
            videos.append({
                "videoId": vid,
                "title": sn["title"],
                "description": (sn.get("description") or "").strip().split("\n")[0][:300],
                "publishedAt": sn["publishedAt"][:10],
            })
        page_token = data.get("nextPageToken")
        if not page_token:
            break
    return videos

def main():
    if not API_KEY:
        print("YOUTUBE_API_KEY tanımlı değil.")
        return

    with open(POSTS_JSON, encoding="utf-8") as f:
        data = json.load(f)
    existing_video_ids = {p.get("videoId") for p in data if p.get("videoId")}

    videos = fetch_all_uploads()
    print(f"Kanalda toplam video: {len(videos)}")
    print(f"Blog'da kayıtlı video: {len(existing_video_ids)}")

    missing = [v for v in videos if v["videoId"] not in existing_video_ids]
    print(f"EKSIK video sayisi: {len(missing)}")

    out_path = os.path.join(BASE, "missing_videos.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(missing, f, ensure_ascii=False, indent=2)
    print(f"Liste yazildi: missing_videos.json")

    print("\n--- Ilk 20 eksik video (ornek) ---")
    for v in missing[:20]:
        print(f"{v['publishedAt']}  {v['title']}  ({v['videoId']})")

if __name__ == "__main__":
    main()
