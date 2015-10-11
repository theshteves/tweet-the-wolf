import requests

class Wolf(object):
    ''' Wolfram|Alpha response handler '''

    def __init__(self, app_id, query):
        ''' Initializes Wolf object '''
        self.query = str(query)
        self.url = "http://api.wolframalpha.com/v2/query?&appid={0}&input=({1})&output=json".format(str(app_id), self.query).replace("#tweetthewolf","")
        #self.url = "http://api.wolframalpha.com/v2/query?input=12*12&appid=PG9HJR-3JT67J7J3E&output=json"

    def request(self):
        ''' Make request to Wolfram|Alpha '''
        return requests.get(self.url).json()

    def result(self):
        ''' Returns human-readable response '''
        return self.url
