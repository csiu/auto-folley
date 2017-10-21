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

# Usage/Example

```
python src/main.py --video data/casablanca-rEWaqUVac3M.mp4 --sub data/casablanca-rEWaqUVac3M.srt --sound data/sad-trombone-73581_634166-lq.wav --w sad
```

# Acknowledgements

Team: Celia, Scott, Albertina, Jacky, Casey, Jeff, Nomoyun, Michael
