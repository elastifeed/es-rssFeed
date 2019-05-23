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
            payload = {
                'title': channelTitle,
                'description': channelDescription,
                'link': channelLink
                #'published': channelPublished
            }
            for entry in entries:
                payload['entryId'] = entry.id
                payload['entryTitle'] = entry.title
                payload['entryDescription'] = entry.description
                payload['entryLink'] = entry.link
                payload['entryPublished'] = entry.published

            print("building response")
            response = requests.request('POST', url, data=json.dumps(payload), headers=headers)
        except Exception as e:
            logging.error(traceback.format_exc())
            logging.error(str(e))

        return json.dumps(payload)
    return 202


if __name__=='__main__':
    app.run(host='0.0.0.0', debug=True, port=8050)