import sys, os
from shutil import copyfile
import subprocess
import tempfile

def add_wav(time, wav, video, out="out.mkv"):
    """Mix audio file onto video at timestamp and write out"""
    cmd = ("ffmpeg -y -i \"{video}\" -i \"{wav}\" -c:v copy "
           "-filter_complex '[1:a] adelay={time}|{time} [delayed]; "
           "[0:a] [delayed] amix [out]' -map 0:v -map '[out]' "
           "\"{out}\"".format(video=video, wav=wav, time=time, out=out))
    subprocess.call(cmd, shell=True)

def add_wavs(cues, video, out="out.mkv"):
    i = 0
    v = video
    prev = None 
    l = len(cues)
    for time, wav in cues:
        if prev is None:
            v = video
        else:
            v = prev
        tmp = tempfile.NamedTemporaryFile(suffix=".mkv").name
        print(tmp)
        add_wav(time, wav, v, out=tmp)
        if prev is not None:
            os.unlink(prev)
        prev = tmp
    copyfile(tmp, out) 
    return(v)

if __name__ == "__main__":
    sound = sys.argv[1]
    movie = sys.argv[2]
    out = "out.mkv"
    add_wav(60000, sound, movie, out="0_out.mkv")
    add_wav(120000, sound, "0_out.mkv", out="1_out.mkv")
    add_wavs([(30000, sound), (40000, sound)], movie, out="out.mkv")
