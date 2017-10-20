import spacy
import numpy as np
import nltk
import pysrt
import matplotlib.pyplot
import collections


class MovieMoodAnalyzer:
    def __init__(self):
        self.model = spacy.load('en')
        self.subtitles = None
        self.emotions = ["joy", "sadness", "anger", "fear"]
        # line_score = {"start":, "end":, "emotions":}
        #self.emotions = [self.model(e) for e in self.emotions]
        self.emotions_dict = {}
        self.line_scores = []
        
        for e in self.emotions:
            self.emotions_dict[e] = self.model(e)

#         self.emotions_dict = {"joy":["happy", "cheerful", "satisfied", "joy", "delight"],
#                               "sadness": ["depressed", "sad", "heartbroken", "mounrful", "sorry"],
#                               "anger": ["anger", "fury", "hatred", "rage", "outrage"],
#                               "disgust": ["dislike", "disgust", "revulsion", "disgust", "distaste"],
#                               "fear": ["fear", "horror", "dread", "terror", "scare"]
#                              }

    def get_emotion_score(self, sub):
        start = sub.start.seconds+sub.start.minutes*60+sub.start.hours*60*60
        end = sub.end.seconds+sub.end.minutes*60+sub.end.hours*60*60
        score = {"start": start, "end": end, "text": sub.text}
        item_vector = self.model(sub.text)
        for e in self.emotions:
            score[e] = self.emotions_dict[e].similarity(item_vector)
        return score

    def load_srt(self, srt):
        self.srt = srt
    
    def analyze_srt(self):
        line = 0
        total = len(self.srt)
        for sub in self.srt:
            line+=1
            print("%d/%d"%(line, total))
            
            score = self.get_emotion_score(sub)
            self.line_scores.append(score)
            print(sub.text)
            print(score)
    
    def get_top_emotion(self, word):
        return
    
    def plot_score(self):
        colours = {"joy":"y-", "sadness":"b-", "anger":"r-", "fear":"g-"}
        start_times = []
        end_times = []
        emotional_score_lists = collections.defaultdict(list)
        means = {}
        stdev = {}
        
        
        for score in self.line_scores:
            start_times.append(score["start"])
            end_times.append(score["end"])
            for e in self.emotions:
                #s = score[e]
                emotional_score_lists[e].append(score[e])
       
        for e in self.emotions:
            means[e]=sum(emotional_score_lists[e])/len(emotional_score_lists[e])
            stdev[e]=np.std(emotional_score_lists[e])
        
        for e in self.emotions:
            emotional_score_lists[e] = (emotional_score_lists[e]-means[e])/stdev[e]
        
        print(emotional_score_lists)
        for i in range(0, len(self.line_scores)):
            for e in self.emotions:
                if  emotional_score_lists[e][i] > 1.5:
                    print("==",e, emotional_score_lists[e][i])
                    print(self.line_scores[i])
            
        for e in self.emotions:
            matplotlib.pyplot.plot(end_times, emotional_score_lists[e], colours[e], lw=1)
        matplotlib.pyplot.show()
        return
    
def main():
    srt = pysrt.open('../subtitles/taxi_driver.srt')
    mma = MovieMoodAnalyzer()
    #mma.get_word_emotion_score(["joyness", "in", "sad"])
    mma.load_srt(srt)
    mma.analyze_srt()
    mma.plot_score()
    
    
main()