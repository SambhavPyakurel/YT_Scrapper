import googleapiclient.discovery
import googleapiclient.errors

# Set your API key
API_KEY = 'YOUR_API_KEY'

# Set the channel ID
channel_id = 'CHANNEL_ID'

# Create a YouTube API client
youtube = googleapiclient.discovery.build('youtube', 'v3', developerKey=API_KEY)




def extract_video_urls(channel_id, youtube):
    request = youtube.search().list(
        part='id',
        channelId=channel_id,
        maxResults=5,
        order='date',
        type='video'
    )
    response = request.execute()

    video_urls = []
    for item in response['items']:
        video_id = item['id']['videoId']
        video_url = f'https://www.youtube.com/watch?v={video_id}'
        video_urls.append(video_url)

    return video_urls

video_urls = extract_video_urls(channel_id, youtube)
print(video_urls)



def extract_thumbnail_urls(channel_id, youtube):
    request = youtube.search().list(
        part='snippet',
        channelId=channel_id,
        maxResults=5,
        order='date',
        type='video'
    )
    response = request.execute()

    thumbnail_urls = []
    for item in response['items']:
        thumbnail_url = item['snippet']['thumbnails']['default']['url']
        thumbnail_urls.append(thumbnail_url)

    return thumbnail_urls

thumbnail_urls = extract_thumbnail_urls(channel_id, youtube)
print(thumbnail_urls)


def extract_video_titles(channel_id, youtube):
    request = youtube.search().list(
        part='snippet',
        channelId=channel_id,
        maxResults=5,
        order='date',
        type='video'
    )
    response = request.execute()

    video_titles = []
    for item in response['items']:
        video_title = item['snippet']['title']
        video_titles.append(video_title)

    return video_titles

video_titles = extract_video_titles(channel_id, youtube)
print(video_titles)



def extract_video_views(channel_id, youtube):
    request = youtube.search().list(
        part='id',
        channelId=channel_id,
        maxResults=5,
        order='date',
        type='video'
    )
    response = request.execute()

    video_ids = [item['id']['videoId'] for item in response['items']]
    video_stats = youtube.videos().list(
        part='statistics',
        id=','.join(video_ids)
    ).execute()

    video_views = []
    for item in video_stats['items']:
        video_view_count = item['statistics']['viewCount']
        video_views.append(video_view_count)

    return video_views

video_views = extract_video_views(channel_id, youtube)
print(video_views)



def extract_upload_times(channel_id, youtube):
    request = youtube.search().list(
        part='snippet',
        channelId=channel_id,
        maxResults=5,
        order='date',
        type='video'
    )
    response = request.execute()

    upload_times = []
    for item in response['items']:
        video_id = item['id']['videoId']
        video_request = youtube.videos().list(
            part='snippet',
            id=video_id
        )
        video_response = video_request.execute()
        video_time = video_response['items'][0]['snippet']['publishedAt']
        upload_times.append(video_time)

    return upload_times

upload_times = extract_upload_times(channel_id, youtube)
print(upload_times)




import csv

# Ensure all data is processed correctly as strings
data = ['Video', 'Thumbnail', 'Title', 'Views', 'Time']
data_rows = zip(video_urls, thumbnail_urls, video_titles, video_views, upload_times)

# Open the file with utf-8 encoding
with open('storage.csv', 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(data)  # Write headers
    writer.writerows(data_rows)  # Write rows

"""
import csv


data=[['Video','Thumbnail','Title','views','time'],
      [video_urls,thumbnail_urls,video_titles,video_views,upload_times]
]





with open('storage.csv','w') as f:
    w=csv.writer(f)
    w.writerow(data[0])
    for i in data[1:]:
        if type(i)==list:
            for j in i:
                w.writerow(j) 
            




data=['Video','Thumbnail','Title','views','time']
data1=zip(video_urls,thumbnail_urls,video_titles,video_views,upload_times)


with open('storage.csv','w') as f1:
    w=csv.writer(f1)
    w.writerow(data)
    w.writerows(data1)

"""