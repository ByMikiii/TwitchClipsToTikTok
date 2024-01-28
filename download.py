import subprocess
import streamlink
import requests

def download_clip(url, filename):
    if 'twitch' in url:
        quality='best'
        streams = streamlink.streams(url)

        if quality not in streams:
            print(f"Error: Quality '{quality}' not available for the given URL.")
            return

        stream_url = streams[quality].url
        subprocess.run(['ffmpeg', '-i', stream_url, '-c', 'copy', filename+'.mp4'])
    
    elif 'kick' in url:
        response = requests.get(url)

        if response.status_code == 200:
            with open(filename+'.mp4', 'wb') as f:
                f.write(response.content)
            print(f"Video downloaded and saved as {filename+'.mp4'}")
        else:
            print(f"Failed to download the video. Status code: {response.status_code}")

    return("Download complete!")