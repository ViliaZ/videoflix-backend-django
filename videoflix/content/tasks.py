
import subprocess

def convert_videoformat(path_sourcefile, target_format): # e.g. 480, 720, 1080
    new_filename = get_filename_converted_video(path_sourcefile, target_format)
    
    #cmd = 'ffmpeg -i {} -s hd720 -c:v libx264 -crf 23 -c:a aac -strict -2 {}'.format(source, new_file)
    cmd = ['ffmpeg', '-i', str(path_sourcefile), '-s', 'hd' + target_format, '-c:v', 'libx264', '-crf', '23', '-c:a', 'aac', '-strict', '-2', new_filename]
    run = subprocess.run(cmd)

    if run.returncode != 0:
        print(f"An error occured: Convert {path_sourcefile} to {target_format}")


def get_filename_converted_video(filename, target_format): 
    splitted = filename.split('.')[0]  # cut original 'mp4' 
    new_filename = f'{splitted}_{target_format}p.mp4' # e.g. originalvideo_720p.mp4
    return new_filename
