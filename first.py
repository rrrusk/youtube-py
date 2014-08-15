# -*- coding: utf-8 -*-

import gdata.youtube
import gdata.youtube.service

client = gdata.youtube.service.YouTubeService()
query = gdata.youtube.service.YouTubeVideoQuery()

query.vq = 'ミスチル'
query.max_results = 25
query.start_index = 1
query.racy = 'exclude'
query.orderby = 'relevance'

feed = client.YouTubeQuery(query)

print feed
for entry in feed.entry:
        print entry.media.player.url
