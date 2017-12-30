from pydub import AudioSegment
#open audio track file
audio_track=AudioSegment.from_file("sample_track.mp3")					

song_length,song_name=[],[]												
#store details of song (could be done in a single list)
for i in range(int(input("Enter number of songs, and then duration(in seconds) and name of each song \n"))):
	song_length.append(int(input())*1000)		
	song_name.append(str(input()+".mp3"))

#initialise counter for durations
start_song=song_length[0]												
for j in range(len(song_length)):
	#for first song
	if j==0:															
		#crop audio track
		song=audio_track[:song_length[0]]								
	else:
		song=audio_track[start_song:start_song+song_length[j]]
		start_song+=song_length[j]	
	#save and close file with user-entered details (default:MP3 format)
	song.export(song_name[j])											
