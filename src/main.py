import spacy
import pysrt
import nltk
import mix

nlp = spacy.load('en_core_web_md')
subs = pysrt.open('subtitles/taxi_driver.srt')

len(subs)

#first_sub = subs[0]

#print first_sub.text;
#print str(first_sub.start.minutes) + " minutes and " + str(first_sub.start.seconds);
#print str(first_sub.end.minutes) + " minutes and " + str(first_sub.end.seconds);

#print subs.slice(starts_after={'minutes': 2, 'seconds': 30}, ends_before={'minutes': 2, 'seconds': 40}).text;

cues = []

target = nlp(u'funny')

def parse_cue(sub):
    hours = sub.end.hours * 3600000
    minutes = sub.end.minutes * 60000
    seconds = sub.end.seconds * 1000
    cue = (hours + minutes + seconds, "laugh.wav")
    print("event: {}:{}:{}".format(sub.end.hours,sub.end.minutes,sub.end.seconds))
    return cue

for sub in subs:
#    if "porno" in sub.text or "organezized" in sub.text:

    score = target.similarity(nlp(sub.text))
    if score > 0.70:
        print(sub.text, score)
        cues.append(parse_cue(sub))

print(cues)
#ts, wav = cues[0]
video = "taxi_driver.mkv"


mix.add_wavs(cues, video)
