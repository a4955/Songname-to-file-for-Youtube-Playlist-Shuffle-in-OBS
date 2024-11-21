# Songname-to-file-for-Youtube-Playlist-Shuffle-in-OBS
Export the current song name from a tab on the website https://youtube-playlist-randomizer.bitbucket.io/ 
Can be used elsewhere, will write any window name to a file in the same directory, but it specifically truncates everything but the song name for YTPLR.

To setup: Download [this](https://github.com/a4955/Songname-to-file-for-Youtube-Playlist-Shuffle-in-OBS/blob/main/WindowTitleToFile.exe), place it in a folder (or don't, I'm not your dad). Run it once and select any window so that it generates the text file in the same directory as the exe, then add a text source in OBS and check "Read from file", and select that text file. 

To use: Get the YTPLR tab in its own separate window, run the WindowTitleToFile.exe you downloaded during setup, and select that YTPLR window. OBS will automatically detect that the file is being updated, so you only need to set that up once.
