from moviepy.editor import *

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

    composite_clip.write_videofile(f".mp4", threads=8, codec="libx264")
