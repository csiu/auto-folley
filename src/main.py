import argparse
import spacy
import pysrt
import nltk
import mix


usage = """
"""

spacy_model = 'en'
sound_track = "data/sound/sad-trombone-73581_634166-lq.wav"
subtitle_track = 'data/casablanca-rEWaqUVac3M.srt'
video = "data/casablanca-rEWaqUVac3M.mp4"
target_word = u'sad'
resulting_mkv_video = "out.mp4"
threshold = 0.58

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
        if score > threshold:
            # print(sub.text, score)
            cues.append(parse_cue(sub))

    # print(cues)
    mix.add_wavs(cues, video, resulting_mkv_video)

if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description=usage,
        formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument(
        '-m', '--model', dest='spacy_model',
        default = 'en',
        help = "spaCy model to use. Default = 'en'.\n"
        "More information at https://spacy.io/docs/usage/models")
    parser.add_argument(
        '-t', '--threshold', dest='threshold',
        default = 0.58,
        help = "Threshold for sound effect")
    parser.add_argument(
        '-w', '--target_word', dest='target_word',
        default = u'sad',
        help = "Word used for modelling")

    parser.add_argument(
        '--video', dest='video',
        default = "data/casablanca-rEWaqUVac3M.mp4",
        help = "mp4 video clip")
    parser.add_argument(
        '--sub', dest='subtitle_track',
        default = 'data/casablanca-rEWaqUVac3M.srt',
        help = "srt subtitle track of the video clip")
    parser.add_argument(
        '--sound', dest='sound_track',
        default = "data/sound/sad-trombone-73581_634166-lq.wav",
        help = "wav file containing a sound effect to add.")

    parser.add_argument(
        '-o', '--output', dest='output_video',
        default = "out.mp4",
        help = "Output mp4 video")

    ## get at the arguments
    args = parser.parse_args()

    # do something...
    main()
