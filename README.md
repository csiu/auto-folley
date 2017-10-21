# Hacking sound to video

Everyone watches movies and sound effects make movies better, more dramatic. The idea that our team had for the Global AI Hackathon is simple. We prototyped adding a sound effect to the evocative parts of a movie.

![](img/autofoley-head-smile.png)

Using artificial intelligence (AI), Auto-Foley watch movies by reading the subtitles, finds the funny parts, and add a given sound effect to these funny parts. We implement this AI by using `pysrt` to parse the subtitles, `spaCy` to do natural language processing and sentiment analysis, and `ffmpeg` to add the sound effect to the movie at the right times.

![Concept](img/concept.png)

# Dependencies

```
# Setup conda environment
conda create --name autofoley python=2.7

# Activate environment
source activate autofoley

# Install dependencies:
conda install spacy
python -m spacy download en
conda install nltk
pip install pysrt
brew install ffmpeg
```

# Usage

```
$ python src/main.py -h

usage: main.py [-h] [-m SPACY_MODEL] [-t THRESHOLD] [-w TARGET_WORD]
               [--video VIDEO] [--sub SUBTITLE_TRACK] [--sound SOUND_TRACK]
               [-o OUTPUT_VIDEO]

Hacking sound into video

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT_VIDEO, --output OUTPUT_VIDEO
                        Output mp4 video. Default = 'out.mp4'

Model arguments:
  -m SPACY_MODEL, --model SPACY_MODEL
                        spaCy model to use. Default = 'en'.
                        More information at https://spacy.io/docs/usage/models
  -t THRESHOLD, --threshold THRESHOLD
                        Threshold for sound effect. Default = 0.58.
  -w TARGET_WORD, --target_word TARGET_WORD
                        Word used for modelling. Default = 'sad'.

Path to file arguments:
  --video VIDEO         mp4 video clip
  --sub SUBTITLE_TRACK  srt subtitle track of the video clip
  --sound SOUND_TRACK   wav file containing a sound effect to add.
```

Example

```
python src/main.py --video data/casablanca-rEWaqUVac3M.mp4 --sub data/casablanca-rEWaqUVac3M.srt --sound data/sad-trombone-73581_634166-lq.wav --w sad
```

# Acknowledgements

Team: Celia, Scott, Albertina, Jacky, Casey, Jeff, Nomoyun, Michael
