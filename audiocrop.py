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

