# -*- coding: utf-8 -*-
"""home_ex.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yM22xeS6LFnU7J4vi1N6wFimi_gas6Uc
"""

!pip install PyVimeo

import vimeo
import requests
import json

# Initial settings
vClient = vimeo.VimeoClient(
    token="950146123d6a62ddbbcf68b097e34256",
    key="72370b62bc26c7e8a3f21ce772a2dba0956d7444",
    secret="4pqSW/W2gAPaaX7B1etvT+AVCVyIX9J1Ad6+p7B3TMGnClgQNdWA90QNwBB6swX8hPrA9k34ZFF1Rx9QAX++TKtaFE88y+TxYQ79a6GD31ogYrZ8LagTvdJylM1Xbiti"
)

OK = 200
CREATED = 201
ERROR = "HTTP status error: "

# Comment on a video
video_id = "708566342"
action = "comments"
uri = "https://api.vimeo.com/videos/{}/{}".format(video_id, action)

comment_video = vClient.post("https://api.vimeo.com/videos/" + video_id + "/comments",
                             data={"text": "Well done!"})

# Make sure we got back a successful response.
assert comment_video.status_code == CREATED, ERROR + str(comment_video.status_code)

# Get number of video likes
action = "likes"
uri = "https://api.vimeo.com/videos/{}/{}".format(video_id, action)
count_likes = vClient.get(uri)

# Make sure we got back a successful response.
assert count_likes.status_code == OK, ERROR + str(count_likes.status_code)

# Serialize response data
likes_data = count_likes.json()

# Search dictionary for likes counter
for key, value in likes_data.items():
  if key == "total":
    print("Video id {} number of likes is:{}".format(video_id, value))

# Get number of video views and serialize response data
uri = "https://api.vimeo.com/videos/{}".format(video_id)
client_response = vClient.get(uri)

# Make sure we got back a successful response.
assert client_response.status_code == OK, ERROR + str(client_response.status_code)

# Serialize response data
video_data = client_response.json()

# Search dictionary for views counter
for key, value in video_data.items():
  if key == "stats":
    print("Video id {} number of views is:{}".format(video_id, value.get("plays")))