import pafy
import urllib.request
import urllib.parse
import re

print("Enter name of video: ")
query_string = urllib.parse.urlencode({"search_query" : input()})
html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
print("http://www.youtube.com/watch?v=" + search_results[0])

url = "http://www.youtube.com/watch?v=" + search_results[0]
video = pafy.new(url)
#print(video.title)
duration = video.duration
#print(video.streams)
audiostreams = video.audiostreams
print(audiostreams)
m4a = video.getbestaudio(preftype="m4a")
print(m4a)
audiostreams[0].download("music")

print(duration)