import praw
import requests
import os

# Replace client_id, client_secret and folder_path with your own values
client_id = 'icuiw6HNK21QoQ'
client_secret = 'pzdmKpdnB_JBO0eVkL1IZoxu3vdpug'

# Use the Reddit API to authenticate the client and obtain an access token
auth = requests.auth.HTTPBasicAuth(client_id, client_secret)
headers = {'User-Agent': 'my_app/1.0'}
data = {'grant_type': 'client_credentials'}
response = requests.post('https://www.reddit.com/api/v1/access_token', auth=auth, data=data, headers=headers)
access_token = response.json()['access_token']

# Use the access token to authenticate the client
reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, user_agent='my_app/1.0', access_token=access_token)

# List of subreddits to download from
subreddit_names = ['memes', 'funny', 'dankmemes']

# Iterate through each subreddit
for subreddit_name in subreddit_names:
  # Retrieve the last 25 videos and images from the subreddit
  subreddit = reddit.subreddit(subreddit_name)
  posts = subreddit.hot(limit=5)

  # Create the folders for the subreddit if it doesn't already exist
  video_path = f'{subreddit_name}/videos/'
  post_path = f'{subreddit_name}/images/'
  if not os.path.exists(video_path): os.makedirs(video_path)
  if not os.path.exists(post_path): os.makedirs(post_path)

  # Download and save the videos and images
  for post in posts:
    url = post.url
    title = post.title
    upvotes = post.ups

    # Modify the title to make it a valid file name
    if not os.path.isabs(title):
      title = title.replace(' ', '_')
      title = title.replace('/', '_')
      title = title.replace('\\', '_')
      title = title.replace(':', '_')
      title = title.replace('*', '_')
      title = title.replace('?', '_')
      title = title.replace('"', '_')
      title = title.replace('<', '_')
      title = title.replace('>', '_')
      title = title.replace('|', '_')
      
    # Check the file extension to determine if it's an image or a video
    if url.endswith('.jpg') or url.endswith('.png'):
      response = requests.get(url)
      # Specify the path to the file in the folder
      file_path = os.path.join(post_path, f'{upvotes}_{title}.jpg')
      # Save the file to the specified path
      open(file_path, 'wb').write(response.content)

    if post.is_video:
      video_url = post.media['reddit_video']['fallback_url']
      response = requests.get(video_url)

      # Specify the path to the file in the folder
      file_path = os.path.join(video_path, f'{upvotes}_{title}.mp4')
      # Save the file to the specified path
      open(file_path, 'wb').write(response.content)