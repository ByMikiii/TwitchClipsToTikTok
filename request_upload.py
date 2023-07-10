import download
import fullscreen
import facecam
import upload
import random
import os

def request_upload(clip_url, video_style):
    download.main('clip', clip_url)

    if(video_style == "1"):
        facecam.edit('clip')
    else:
        fullscreen.edit('clip')

    hashtags = ['#foryou','#foryoupage', '#fyp', '#fy']

    tag1 = random.choice(hashtags)
    hashtags.remove(tag1)
    tag2 = random.choice(hashtags)
    print(f"tags:{tag1} {tag2}")

    while True:
        try:
            upload.upload_video('.mp4', f"{tag1} {tag2} ", cookies='cookies.txt', headless=True, comment=True, stitch=True, duet=True)
            file_name = '.mp4'
            file_path = os.path.join(os.getcwd(), file_name)
            if not os.path.isfile(file_path):
                break
        except Exception as e:
            print(f"An error occurred: {e}")
            
request_upload('https://clips.twitch.tv/AttractiveIgnorantHamAsianGlow-pbf5QLZeomZID8Ws', 1)