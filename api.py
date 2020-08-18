#!/usr/bin/env python
import requests
import json
from pprint import pprint


class StravaAPI:
    _BASE_URL = 'https://cdn-1.strava.com/api/v3/'

    def __init__(self):
        self.req = requests.Session()
        self.req.headers['User-Agent'] = 'Strava/152.12'
        self.req.headers['Client-Id'] = '2'
        self.req.headers['Client-Secret'] = \
            '3bf7cfbe375675dd9329e9de56d046b4f02a186f'

    def get(self, url: str, **params):
        response = self.req.get(StravaAPI._BASE_URL + url, params=params)
        try:
            return json.loads(response.text)
        except json.decoder.JSONDecodeError as e:
            print("ERROR: ", e)

    def get_segment_detail(self, id):
        return self.get(f'segments/{id}')

    def get_segment_leaderboard(self, id):
        return self.get(f'segments/{id}/leaderboard')

    # bounds: ((min_lat, min_lng), (max_lat, max_lng))
    # activity_type: 'cycling' or 'running'
    # category: (min, max) where min, max in [0, 1, 2, 3, 4, 5]
    def get_segment_explore(self,
                            bounds,
                            activity_type='cycling',
                            category=(0, 5)):
        return self.get(
            f'segments/explore',
            bounds=f'{bounds[0][0]}, {bounds[0][1]}, {bounds[1][0]}, {bounds[1][1]}',
            activity_type=activity_type,
            min_cat=category[0],
            max_cat=category[1])

# Example:
#   Segment: 229781
#   Bounding box: (40, 116), (41, 117)

def main():
    api = StravaAPI()
    from sys import argv

    if argv[1] == 'get_segment_detail':
        r = api.get_segment_detail(argv[2])
    elif argv[1] == 'get_segment_leaderboard':
        r = api.get_segment_detail(argv[2])
    elif argv[1] == 'get_segment_explore':
        r = api.get_segment_explore(bounds=((argv[2], argv[3]), (argv[4], argv[5])))
    else:
        print("unknown api!")
        return

    pprint(r)


if __name__ == '__main__':
    main()
