from youtube_transcript_api import YouTubeTranscriptApi

video_id='x2nzzuQwbs4&t=43s'
list_of_dicts=YouTubeTranscriptApi.get_transcript(video_id)
# Extract 'text' values into a new list
transcript = [item["text"] for item in list_of_dicts]

print(transcript)