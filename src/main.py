import argparse
import spacy
import pysrt
import nltk
# import sys; sys.path.append("/Users/csiu/repo/auto-folley/src")
import mix


usage = """
"""

spacy_model = 'en'
sound_track = "data/sound/sad-trombone-73581_634166-lq.wav"
subtitle_track = 'data/subtitles/taxi_driver.srt'
video = "data/videos/taxi_driver_tp_clip.mkv"
target_word = u'funny'
resulting_mkv_video = "out.mkv"

def parse_cue(sub):
    hours = sub.end.hours * 3600000
    minutes = sub.end.minutes * 60000
    seconds = sub.end.seconds * 1000
    cue = (hours + minutes + seconds, sound_track)
    print("event: {}:{}:{}".format(sub.end.hours,sub.end.minutes,sub.end.seconds))
    return cue

def main():
    nlp = spacy.load(spacy_model)
    subs = pysrt.open(subtitle_track)
    target = nlp(target_word)

    cues = []
    for sub in subs:
        score = target.similarity(nlp(sub.text))
        if score > 0.70:
            # print(sub.text, score)
            cues.append(parse_cue(sub))

    # print(cues)
    mix.add_wavs(cues, video, resulting_mkv_video)

if __name__ == '__main__':
    # parser = argparse.ArgumentParser(
    #     description=usage,
    #     formatter_class=argparse.RawTextHelpFormatter)
    #
    # parser.add_argument(
    #     '-i', '--infile', dest='infile',
    #     action='store',
    #     default=None,
    #     type=str,
    #     #choices=['','',''],
    #     required=True,
    #     help='path to input file')
    #
    # ## get at the arguments
    # args = parser.parse_args()

    ## do something...
    main()
