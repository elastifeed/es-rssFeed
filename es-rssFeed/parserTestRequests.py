import requests
import json
import logging
import traceback


class RequestCalls():

    def request1(self):
        url = 'http://127.0.0.1:8050/rssParser'
        data = None
        try:
            headers = {
                'Content-Type': 'application/json'
            }
            payload = {
                'url': "https://www.reddit.com/.rss"
            }

            response = requests.request('POST', url, data=json.dumps(payload), headers=headers)
            print(response)
        except Exception as e:
            logging.error(traceback.format_exc())
            logging.error(str(e))

        return 'Request done. Answer get : ' + str(data)

    def request2(self):
        url = 'http://127.0.0.1:8050/rssParser'
        data = None
        try:
            headers = {
                'Content-Type': 'application/json'
            }
            payload = {
                'url': "https://www.reddit.com/r/ProgrammerHumor/.rss"
            }

            response = requests.request('POST', url, data=json.dumps(payload), headers=headers)
            print(response)
        except Exception as e:
            logging.error(traceback.format_exc())
            logging.error(str(e))

        return 'Request done. Answer get : ' + str(data)

    def request3(self):
        url = 'http://127.0.0.1:8050/rssParser'
        data = None
        try:
            headers = {
                'Content-Type': 'application/json'
            }
            payload = {
                'url': "https://www.reddit.com/r/askReddit/.rss"
            }

            response = requests.request('POST', url, data=json.dumps(payload), headers=headers)
            print(response.json())
        except Exception as e:
            logging.error(traceback.format_exc())
            logging.error(str(e))

        return 'Request done. Answer get : ' + str(data)

if __name__ == '__main__':
    for x in range(0,100):
        RequestCalls.request1(RequestCalls)
        RequestCalls.request2(RequestCalls)
        RequestCalls.request3(RequestCalls)


