import pysrt

def find_subtitle_in_srt(path_to_srt_file, subtitle_slice):
	subs = pysrt.open(path_to_srt_file)

	len(subs)

	i = 0
	while (subtitle_slice.lower() not in subs[i].text.lower()):
		i += 1

	print "Subtitle is in position: " + i
	print subs[i].text
	print subs[i].start.seconds
	print subs[i].end.seconds

find_subtitle_in_srt ('subtitles/taxi_driver.srt', "I once had a horse")
