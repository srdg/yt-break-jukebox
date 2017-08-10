from pydub import AudioSegment
audio_track=AudioSegment.from_file("sample_track.mp3")					#open audio track file

song_length,song_name=[],[]												#store details of song (could be done in a single list)
for i in range(int(input("Enter number of songs, and then duration(in seconds) and name of each song \n"))):
	song_length.append(int(input())*1000)		
	song_name.append(str(input()+".mp3"))

start_song=song_length[0]												#initialise counter for durations
for j in range(len(song_length)):
	if j==0:															#for first song
		song=audio_track[:song_length[0]]								#crop audio track
	else:
		song=audio_track[start_song:start_song+song_length[j]]
		start_song+=song_length[j]										#update counter
	song.export(song_name[j])											#save and close file with user-entered details (default:MP3 format)

"""
INITIAL VERSION OF THE CODE
=============================
song1=audio_track[:320000]
song2=audio_track[320001:545000]
song3=audio_track[545000:len(audio_track)]
song1.export("Amar Hiyar Majhe.mp3",format="mp3")
song2.export("Jini Sokol Kajer Kaji.mp3")
song3.export("Pinakete Lage Tonkar.mp3")

"""