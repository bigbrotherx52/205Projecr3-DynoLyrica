#from search import youtube_search as searcher
from apiclient.errors import HttpError
from oauth2client.tools import argparser

from apiclient.discovery import build
from youtube_dl import downloader 
#from apiclient.errors import HttpError
#from oauth2client.tools import argparser


# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = "AIzaSyDWH0e3ZQs8bBAYrVleXJsSUhDxMS7EXC0"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"



def getCaption(vID):
    CapsFound = caption(vID)
    
    #get a good caption track for Video id
    for item in CapsFound:
        cID = item["id"]
        if (cID):
            break

    tfmt = "sbv"
    
    return download_caption(cID, tfmt)
    
    
    
def caption(vID):

    #results = youtube.captions().list(
    #    part="snippet",
    #    videoId=vID
    #).execute()

    return " results"
    #for item in results["items"]:
    #cid = item["id"]
    #name = item["snippet"]["name"]
    #language = item["snippet"]["language"]
    #print ("Caption track '%s(%s)' in '%s' language." )% (name, cid, language)

    #return results["items"]


    
def download_caption(caption_id, tfmt):
    #subtitle = youtube.captions().download( id=caption_id, tfmt=tfmt).execute()
    
    return ""




def youtube_Caption(quary):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

    # Call the search.list method to retrieve results matching the specified
    # query term.
    
    argparser.add_argument("--q", default = quary)
    argparser.add_argument("--max-results", help="Max results", default=10)
    argparser.add_argument("--closedCaption", help = "closed caption", default = "true")
    args = argparser.parse_args()
    
    search_response = youtube.search().list(
        q=args.q,
        part="id,snippet",
        maxResults=args.max_results
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
        
        #tell you
        if search_result["id"]["kind"] == "youtube#caption":
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