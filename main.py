import download
import fullscreen
import facecam
import upload

download.main('clip')
videoStyle = input('Choose a video style. (1 - facecam, 2 - fullscreen)')

if(videoStyle == "1"):
    facecam.edit('clip')
else:
    fullscreen.edit('clip')

upload.upload()