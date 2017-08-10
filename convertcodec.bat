@echo off
set /p file_url= Enter youtube link 
youtube-dl --output "sample_track" -k %file_url%
ffmpeg -i sample_track.mp4 sample_track.mp3
del /f /s /q *.f136 *.f140
audiocrop.py