from moviepy.editor import *
import os
import shutil

def copy_video_file(original_path, new_name):
    try:
        # Extract the directory and filename from the original path
        directory, filename = os.path.split(original_path)
        
        # Create the new path with the new name in the same directory
        new_path = os.path.join(directory, new_name)
        
        # Copy the file
        shutil.copy2(original_path, new_path)
        print(f"File '{original_path}' copied to '{new_path}' successfully.")
    except FileNotFoundError:
        print(f"Error: File '{original_path}' not found.")
    except PermissionError:
        print(f"Error: Permission denied to copy file '{original_path}'.")

def edit(filename):
    clip = VideoFileClip(f"{filename}.mp4")

    template = ImageClip("template.png")

    duration = clip.duration

    new_width = 1080
    new_height = int(clip.size[1] * (new_width / clip.size[0]))

    resized_clip = clip.resize((new_width, new_height))

    x_pos = (template.size[0] - resized_clip.size[0]) // 2
    y_pos = (template.size[1] - resized_clip.size[1]) // 2

    composite_clip = CompositeVideoClip([template.set_duration(duration), resized_clip.set_pos((x_pos, y_pos)).set_duration(duration)])

    composite_clip.write_videofile(f".mp4", threads=6, codec="libx264")

    # composite_clip = composite_clip.set_duration(2).without_audio()

    # composite_clip.write_videofile('cliptest.mp4', threads=6, codec="libx264")
    original_file_path = ".mp4"
    new_file_name = "v.mp4"
    copy_video_file(original_file_path, new_file_name)
