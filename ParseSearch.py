from search import youtube_search as searcher
from apiclient.errors import HttpError
from oauth2client.tools import argparser



quary = input("Enter a song to search for")


argparser.add_argument("--q", help="Search term", default = quary)
argparser.add_argument("--max-results", help="Max results", default=1)
argparser.add_argument("--closedCaption", help = "closed caption", default = "true")
args = argparser.parse_args()

    
try:
    result = searcher(args)
except HttpError:
    print ("An HTTP error %d occurred:")

print ("get results")
print (args)

print (result)