__title__ = "api-tmdb"
__version__ = "1.0.0"
__author__ = "German Sosa Goy, Micael Gomez"
__license__ = "AGPL-3"

from datetime import datetime
import requests
from requests import request
import base64


"""
Endpoint
/movie/{movie_id}
https://api.themoviedb.org/3/movie/550?api_key=511f7d4c0cad0f61cb9e7037eae11ff2
"""


class APITMDB(object):
    """ APITMDB Class """

    def __init__(self, api_key):
        self.url = 'https://api.themoviedb.org/3'
        self.api_key = api_key
        self.timeout = 3600
        

    def __get_url(self, endpoint):
        """ Get URL for requests """
        url = self.url
        return "{}/{}?api_key={}" % (url, endpoint, self.api_key)

    def __request(self, endpoint, raw=False):
        """ Do requests """
        url = self.__get_url(endpoint)
        res = request(
            method='GET',
            url=url,
            timeout=self.timeout,
        )
        if raw:
            return res
        else:
            if res.status_code == 404:
                print('404 Not Found')
                return {'success': False, 'statuscode': res.status_code, 'message':res.content and res.content}
            if res.status_code not in [200, 201]:
                message = res.content and res.content
                print(message)
                return {'success': False, 'statuscode': res.status_code, 'message':res.content and res.content}
            return res.json()
    
    def get(self, endpoint):
        """ GET requests """
        return self.__request("GET", endpoint)