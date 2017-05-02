#!/usr/bin/python

from apiclient.discovery import build
#from apiclient.errors import HttpError
#from oauth2client.tools import argparser


# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = "AIzaSyDWH0e3ZQs8bBAYrVleXJsSUhDxMS7EXC0"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def youtube_search(options):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

    # Call the search.list method to retrieve results matching the specified
    # query term.
    search_response = youtube.search().list(
        q=options.q,
        part="id,snippet",
        maxResults=options.max_results
        ).execute()

    #videoID = search_response.get("items")
    #captions = youtube.caption().list(
    #    part ="snippet",
    #    id = videoID
    #    ).execute()
    
    #print (captions)
    
    
    videos = []
    #channels = []
    #playlists = []

# Add each result to the appropriate list, and then display the lists of
# matching videos, channels, and playlists.
    x = 0
    for search_result in search_response.get("items", []):
        
        if search_result["id"]["kind"] == "youtube#video":
            videos.append("%s (%s)" % (search_result["snippet"]["title"], search_result["id"]["videoId"]))
            #videos.append("%s %s" % ( x, search_result["snippet"]["title"]))
            x += 1
           
        #elif search_result["id"]["kind"] == "youtube#channel":
        #   channels.append("%s (%s)" % (search_result["snippet"]["title"], search_result["id"]["channelId"]))
        #elif search_result["id"]["kind"] == "youtube#playlist":
        #    playlists.append("%s (%s)" % (search_result["snippet"]["title"],search_result["id"]["playlistId"]))
            
    
    #return search_result        
    #print "Videos:\n", "\n".join(videos), "\n"
    #print "Channels:\n", "\n".join(channels), "\n"
    #print "Playlists:\n", "\n".join(playlists), "\n"
    
    #print("results found: " + x)
    return videos

#if __name__ == "__main__":
#
#    argparser.add_argument("--q", help="Search term", default = "cat")
#    argparser.add_argument("--max-results", help="Max results", default=25)
#    args = argparser.parse_args()
#   
#  
#    try:
#        youtube_search(args)
#    except HttpError, e:
#        print "An HTTP error %d occurred:\n%s" % (e.resp.status, e.content)
