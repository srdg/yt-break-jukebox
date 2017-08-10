YOUTUBE JUKEBOX SEPARATOR
=========================================

The batch script (file with a .BAT extension) will prompt you to enter the youtube link
you want to download the video from and then convert your .MP4 file (here configured 
to convert "sample_track.MP4") to a .MP3 file and save it with a same name in the same directory.
NOTE: In case the file is already present, you might be prompted to authorize an overwrite.
      Delete the "sample_track.MP3" file to resolve this, or simply authorize the overwrite
      by entering "y" at the terminal.
--------------------------------------------------------------------------------------------
 After that, the script will automatically call a python script ("audiocrop.py") which will 
prompt you for entering number of songs you want to extract from "sample_track.MP4". You'd 
then be asked to enter the duration of each song (IN SECONDS) and the name you want to save
each individual file with. Once you've completed the input procedure, the script will auto-
matically crop the track for you and save each file with the name you specified. Don't worry,
unless you screwed up during the input process, there's nothing to panick about!!!!!!!!!!!!!

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Here are a few issues that could go wrong:
1. The program might not work :/ If this is the case, maybe, just maybe, ACCIDENTALLY, you 
   screwed up the script by entering unpermitted characters in the script. The easiest way
   to resolve this is deleting your entire copy of the directory (I mean only the one you 
   downloaded) and re-download it again.
 
2. In case you want to pinpoint the error, open the COMMAND LINE INTERFACE, navigate to the
   working directory (this means the one you downloaded) and type in "audiocrop.py" and hit
   ENTER. If you see a "[Err No 2]:File Not Found" error, it essentially means that the file
   name is either incorrect in the script, or is not present at all in the directory. To
   resolve, change the "sample_track.mp3" in line number 2 in "audiocrop.py" to <your_audio_
   track_filename>. For e.g. if your song's name is "I Remain", you should change "sample_
   track.mp3" to "I Remain.mp3". Else, redownload it, and save to this directory.

3. However, an error might also be flagged if you have broken requirements. Requirements mean
   essentially the environment that is needed for the script to execute successfully. The next
   section deals with how you would be able to resolve this error.

***********************************************************************************************
 
In order to fix the broken requirements error, you need to follow the steps mentioned below. 
Here are the steps:

Our script needs Python 3.6x to run. So if you haven't got python installed on your local machine,
head over to "https://www.python.org/downloads" and download and install it (the version 3.6x, mind you).
It's pretty straightforward, so you need not worry much. In case you have any doubts, look it up on 
Youtube - there are plenty of video tutorials available.
NOTE: Make sure you install python with "pip", we'll need it later on.

Once you've got python installed, verify it by opening your CLI and entering "python". If all is well,
the command line should change to a python CLI, each command preceding with a ">>>" tag.

Next, you need to install "pydub".
You can install "pydub" by opening your CLI and entering "pip install pydub".

What we need to do next is install a codec converter called "FFMPEG".
You need to download a static build from "https://ffmpeg.zeranoe.com/builds/".
Next, Unzip the file in a location (for convenience let's say it's "path\to\ffmpeg").
Open CLI with administrator rights (Right click on CLI icon, click "Run as Administrator", on prompt, 
authorize) and type in "" setx /M PATH "path\to\ffmpeg\bin;%PATH%" "" (skip the spaces and "" at the
beginning and end) and hit ENTER.
Once the command executes successfully, you are all set up to use the script at par.