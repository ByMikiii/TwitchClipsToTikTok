import cv2
from moviepy.editor import VideoFileClip, ImageClip, CompositeVideoClip

def edit(filename):
    # Define the input video file path
    input_file = f"{filename}.mp4"

    # Define the output video file path
    output_file = f".mp4"

    # Load the input video clip
    video_clip = VideoFileClip(input_file)

    # Initialize the face detection classifier
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    # Process frames to detect the webcam region
    zoom_x, zoom_y, zoom_w, zoom_h = None, None, None, None

    for frame in video_clip.iter_frames():
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.7, minNeighbors=6)

        if len(faces) > 0:
            x, y, w, h = faces[0]
            face_width = w
            offset_x = int(face_width * 0.9)  # Adjust the horizontal offset as needed for more width
            offset_y = int((h + 1.05 * offset_x) * 0.2)  # Adjust the vertical offset as needed

            zoom_x = max(0, x - offset_x)
            zoom_y = max(0, y - offset_y)
            zoom_w = min(video_clip.size[0], w + 2 * offset_x)
            zoom_h = min(video_clip.size[1], h + 2 * offset_y)
            
            break  # Exit the loop after the first frame with a detected face

    if zoom_x is None or zoom_y is None or zoom_w is None or zoom_h is None:
        raise ValueError("No face detected. Unable to find the webcam region.")

    # Crop the video to the zoomed-out region around the webcam
    cropped_clip = video_clip.crop(x1=zoom_x, y1=zoom_y, x2=zoom_x + zoom_w, y2=zoom_y + zoom_h)

    # Calculate new width and height for the resized clip
    new_width = 1080
    new_height = int(new_width * cropped_clip.h / cropped_clip.w)

    # Resize the cropped clip to the new dimensions
    resized_facecam = cropped_clip.resize(width=new_width, height=new_height)

    # # Write the resized clip to the output video file
    # resized_clip.write_videofile(output_file, codec="libx264", audio_codec="aac")


    #GAMEPLAY 

    # Resize the video to the desired resolution
    resized_clip = video_clip.resize(height=1365)

    # Set the output video resolution to 1080x1240
    final_clip = resized_clip.crop(x1=650, y1=0, x2=1730, y2=1365)

    # # Export the final video
    # final_clip.write_videofile("output_gameplay.mp4", fps=clip.fps)

    #340 740
    #JOIN
    template = ImageClip("template.png")

    # # Load the first video
    # facecam = VideoFileClip("output_video.mp4",audio=True)

    # # Load the second video
    # gameplay = VideoFileClip("output_gameplay.mp4",audio=False)

    final_clip = CompositeVideoClip([template.set_duration(resized_facecam.duration), final_clip.set_pos((0, 0)), resized_facecam.set_pos((0, 1300))])

    final_clip.write_videofile(output_file, threads=2, codec="libx264")