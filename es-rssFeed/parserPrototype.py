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
        try:
            headers = {
                'Content-Type': 'application/json'
            }
            if channelTitle and channelDescription and channelLink != None :
                payload = {
                    'title': channelTitle,
                    'description': channelDescription,
                    'link': channelLink
                    #'published': channelPublished
                }
            else:
                payload = {
                'title': 'empty'
                }
            print(len(entries))
            for entry in entries:
                print("iteration check")
                try:
                    payload['entryId'] = entry.id
                except Exception:
                    payload['entryId'] = 'no id'
                try:
                    payload['entryTitle'] = entry.title
                except Exception:
                    payload['entryTitle'] = 'no entryTitle'
                try:
                    payload['entryDescription'] = entry.description
                except Exception:
                    payload['entryDescription'] = 'no entryDescription'
                try:
                    payload['entryLink'] = entry.link
                except Exception:
                    payload['entryLink'] = 'no entryLink'
                try:
                    payload['entryPublished'] = entry.published
                except Exception:
                    payload['entryPublished'] = 'no entryPublished'

            print("building response")
            response = requests.request('POST', url, data=json.dumps(payload), headers=headers)
        except Exception as e:
            logging.error(traceback.format_exc())
            logging.error(str(e))

        print(payload)

        return json.dumps(payload)
    return 202


if __name__=='__main__':
    app.run(host='0.0.0.0', debug=True, port=8050)