import re

youtube_url = "https://www.youtube.com/watch?v=RgJvZER-qwA&t=3s"

# Extract video ID using regular expression
match = re.search(r"v=([A-Za-z0-9_-]+)", youtube_url)
if match:
    video_id = match.group(1)
    print("Video ID:", video_id)
else:
    print("Video ID not found in the URL.")
