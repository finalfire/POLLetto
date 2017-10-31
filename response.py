from collections import namedtuple

ResponseNT = namedtuple('Response', ['descr', 'count'])

class Response(ResponseNT):
    def add_count(count=1):
        self.count = self.count + count
    
    def remove_count(count=1):
        if (self.count > 0 and self.count - count >= 0):
            self.count = self.count - count
        else:
            self.count = 0
    
    def __str__(self):
        return 'Response: {}.\nVotes: {}.'.format(self.descr, self.count)

class Pool():
    def __init__(self, name, descr):
        self.name = name
        self.descr = descr
        self.responses = []

    def get_responses(self):
        return {index: response for index, response in enumerate(self.responses)}

    def get_response(self, response):
        for i, r in enumerate(self.responses):
            if r.descr == response.descr:
                return i, r
        return -1, None
    
    def add_response(self, response):
        i, resp = self.get_response(response)
        if i == -1:
            self.responses.append(response)
    
    def remove_response(self, index):
        if index >= 0 and index < len(self.responses):
            del self.responses[index]


