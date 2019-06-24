import feedparser
import requests
import json
import logging
import traceback
from flask import Flask, request



app = Flask(__name__)  # Declaring aplication

# port is 8050
@app.route('/rssParser', methods=['POST'])
def rssParser():

    #Extract URL, DATE, HEADING, FEEDCHANNEL"title"
    # Here will go the url coming from the JSON request


    url = request.json.get('url', 0)
    print("url " + url)
    if (url != 0):
        pfeed = feedparser.parse(url)
        print(pfeed)

    #DATA IN CHANNEL
        if 'title' in pfeed.feed:
            channelTitle = pfeed.feed.get('title', 'no title')
            print("title " + channelTitle)
        if 'link' in pfeed.feed:
            channelLink = pfeed.feed.get('link', 'no link')
            print("link " + channelLink)
        if 'description' in pfeed.feed:
            channelDescription = pfeed.feed.get('description', 'no description')
            print("Description " + channelDescription)
        if 'published' in pfeed.feed:
            channelPublished = pfeed.feed.get('published', 'published')
            print("Published " + channelPublished)

        entries = pfeed.entries


    #HERE DATE

    #HERE HEADING

    #HERE FEEDCHANNEL"title"


        data = None
        print("DEBUG: start to catch info")
        try:
            headers = {
                'Content-Type': 'application/json'
            }
            payload = {}
            try:
                payload['title'] = channelTitle
            except Exception:
                payload['title'] = 'none'
            try:
                payload['description'] = channelDescription
            except Exception:
                payload['description'] = 'none'
            try:
                payload['link'] = channelLink
            except:
                payload['link'] = 'none'
            try:
                payload['published'] = channelPublished
            except:
                payload['published'] = 'none'
            n = 0
            print ("DEBUG: Start to catch subEntries")
            for entry in entries:
                oneEntry = {}
                try:
                    oneEntry['entryId'] = entry.id
                except Exception:
                    oneEntry['entryId'] = 'no id'
                try:
                    oneEntry['entryTitle'] = entry.title
                except Exception:
                    oneEntry['entryTitle'] = 'no entryTitle'
                try:
                    oneEntry['entryDescription'] = entry.description
                except Exception:
                    oneEntry['entryDescription'] = 'no entryDescription'
                try:
                    oneEntry['entryLink'] = entry.link
                except Exception:
                    oneEntry['entryLink'] = 'no entryLink'
                try:
                    oneEntry['entryPublished'] = entry.published
                except Exception:
                    oneEntry['entryPublished'] = 'no entryPublished'
                payload['entry' + str(n)] = oneEntry

                n = n + 1

            print("building response")
            response = requests.request('POST', url, data=json.dumps(payload), headers=headers)
            print ("RESPONSE SENT")
        except Exception as e:
            logging.error(traceback.format_exc())
            logging.error(str(e))

        print(payload)
        print("DEBUG End of building")
        return json.dumps(payload)
    print("RETURNING 404")
    return 404


if __name__=='__main__':
    app.run(host='0.0.0.0', debug=True, port=8050)