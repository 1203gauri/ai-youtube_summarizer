# import re
# from urllib.parse import urlparse, parse_qs

# def extract_video_id(url):
#     """Extract YouTube video ID from a given URL."""
#     query = urlparse(url)
#     if query.hostname == 'youtu.be':
#         return query.path[1:]
#     if query.hostname in ('www.youtube.com', 'youtube.com'):
#         if query.path == '/watch':
#             return parse_qs(query.query)['v'][0]
#         if query.path[:7] == '/embed/':
#             return query.path.split('/')[2]
#         if query.path[:3] == '/v/':
#             return query.path.split('/')[2]
#     raise ValueError("Invalid YouTube URL")

import re
from urllib.parse import urlparse, parse_qs

def extract_video_id(url):
    """Extract YouTube video ID from a given URL."""
    query = urlparse(url)
    if query.hostname == 'youtu.be':
        return query.path[1:]
    if query.hostname in ('www.youtube.com', 'youtube.com'):
        if query.path == '/watch':
            return parse_qs(query.query)['v'][0]
        if query.path[:7] == '/embed/':
            return query.path.split('/')[2]
        if query.path[:3] == '/v/':
            return query.path.split('/')[2]
    raise ValueError("Invalid YouTube URL")