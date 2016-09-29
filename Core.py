#!/usr/bin/python
from urllib.parse import urlparse, parse_qs
import requests
# Extracts the video id of from youtube video URL
"""
    Examples:
    - http://youtu.be/SA2iWivDJiE
    - http://www.youtube.com/watch?v=_oPAwA_Udwc&feature=feedu
    - http://www.youtube.com/embed/SA2iWivDJiE
    - http://www.youtube.com/v/SA2iWivDJiE?version=3&amp;hl=en_US
    - http://stackoverflow.com/a/7936523/6809114
    """


def get_video_id(youtube_url):
    query = urlparse(youtube_url)
    if query.hostname == 'youtu.be':
        return query.path[1:]
    if query.hostname in ('www.youtube.com', 'youtube.com'):
        if query.path == '/watch':
            p = parse_qs(query.query)
            return p['v'][0]
        if query.path[:7] == '/embed/':
            return query.path.split('/')[2]
        if query.path[:3] == '/v/':
            return query.path.split('/')[2]
            # fail?
    return None


# This code creates a new, private playlist in the authorized user's channel.
# Returns the playlist id of newly created playlist
def create_playlist(name, info, privacy):
    playlists_insert_response = youtube.playlists().insert(
        part="snippet,status",
        body=dict(
            snippet=dict(
                title=name,  # playlist name
                description=info  # playlist description
            ),
            status=dict(
                privacyStatus=privacy  # public/private/unlisted
            )
        )
    ).execute()
    return playlists_insert_response["id"]


# This module adds youtube videos with links to youtube playlist
def add_videos2playlist(playlist_id, video_id):
    add_video_response = youtube.playlistItems().insert(
        part="snippet",
        body={
            'snippet': {
                'playlistId': playlist_id,
                'resourceId': {
                    'kind': 'youtube#video',
                    'videoId': video_id
                }
                # 'position': 0 https://www.youtube.com/watch?v=1sIdXDorVtk
            }
        }
    ).execute()
    print(add_video_response['id'])


#This method returns the source page of the URL
def get_page_source(theurl):
    thepage = requests.get(theurl)
    return thepage.content
