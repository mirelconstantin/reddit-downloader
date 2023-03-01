<h1 align="center">Reddit Video and Image Downloader</h1>

<div align="center">

This script uses the praw library to access the Reddit API and **download videos and images from a list of subreddit names**.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/mirelconstantin) [![Freelancer](https://img.shields.io/badge/Freelancer-29B2FE?style=for-the-badge&logo=Freelancer&logoColor=white)](https://www.freelancer.com/u/mirelconstantin) [![Upwork](https://img.shields.io/badge/UpWork-6FDA44?style=for-the-badge&logo=Upwork&logoColor=white)](https://www.upwork.com/freelancers/~018dd0ecda291358f9)

</div>

## ➕ Dependencies
The following libraries are required to run this script:
- `praw:` Used to access the Reddit API and retrieve posts from subreddits.
- `requests:` Used to send HTTP requests to the Reddit API and download content from URLs.
- `os:` Used to create directories and manipulate file paths.

## 📙 Downloading Videos and Images
The script iterates through each subreddit in the **subreddit_names** list and retrieves the **last 25 hot posts** from the subreddit. It creates a folder for the subreddit if it doesn't already exist, and then **downloads and saves the videos and images from the posts**.
> For each post, the script checks the file extension of the url to determine if it's an image or a video. If it's an image, it downloads the content and saves it to the images folder for the subreddit. If it's a video, it retrieves the fallback_url from the media attribute and downloads the content, saving it to the videos folder for the subreddit. The file names are constructed using the post's upvotes and title, with any invalid characters in the title replaced with an underscore.

## ⚙️ Configuration
To customize the behavior of the script, you can modify the following variables:
- `client_id:` The client ID provided to you by Reddit.
- `client_secret:` The client secret provided to you by Reddit.
- `subreddit_names:` A list of subreddit names that the script should download content from.

## Running the Script
To run the script, **ensure that the required dependencies are installed** and then execute the script using a command line interface or a Python interpreter. 
> **The downloaded videos and images will be saved to the appropriate folders in the current working directory.**
```
pip install -m requirements.txt
python reddit.py
```

## 📝 License

**The MIT License (MIT)**

Copyright © 2023 Mirel Constantin
