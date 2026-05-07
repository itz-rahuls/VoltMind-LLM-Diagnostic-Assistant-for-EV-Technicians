from youtubesearchpython import VideosSearch

def get_youtube_videos(query):
    videos = []

    try:
        search = VideosSearch(query, limit=2)
        results = search.result()

        if "result" in results and len(results["result"]) > 0:
            for v in results["result"]:
                link = v.get("link", "")
                
                # Only accept valid YouTube watch links
                if "watch?v=" in link:
                    videos.append({
                        "title": v.get("title", "No title"),
                        "link": link
                    })

    except Exception as e:
        print("YouTube API failed:", e)

    # 🔥 FORCE FALLBACK IF EMPTY
    if not videos:
        search_query = query.replace(" ", "+")
        return [{
            "title": "Open YouTube Results",
            "link": f"https://www.youtube.com/results?search_query={search_query}"
        }]

    return videos