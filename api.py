#!/usr/bin/env python
import requests
import json


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
    # catagory: (min, max) where min, max in ['NC', '4', '3', '2', '1', 'HC']
    def get_segment_explore(self,
                            bounds,
                            activity_type='riding',
                            category=('NC', 'HC')):
        return self.get(
            f'segments/explore',
            bounds=f'[{bounds[0][0]}, {bounds[0][1]}, {bounds[1][0]}, {bounds[1][1]}]',
            activity_type=activity_type,
            min_cat=category[0],
            max_cat=category[1])


def main():
    api = StravaAPI()
    # print(api.get_segment_detail(229781))
    # print(api.get_segment_leaderboard(229781))
    print(api.get_segment_explore(bounds=((40, 116), (41, 117))))


if __name__ == '__main__':
    main()
