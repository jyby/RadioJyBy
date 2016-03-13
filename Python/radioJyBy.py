"""Radio JyBy
Plays your local music (music player like) while interleaving it with recorded personal comments (DJ like) to simulate the feel of a radio. 

Prototype in Python for desktop.
"""

import time, wave, pymedia.audio.sound as sound

MusicFolder = '../Music/'
RadioCommentsFolder = '../RadioComments/'

f= wave.open( RadioCommentsFolder+'5mnBreak-HoYouHaveBeenWorkingGreatNoItSTimeForAFiveMinuteBreak.wav', 'rb' )

sampleRate= f.getframerate()
channels= f.getnchannels()
format= sound.AFMT_S16_LE
snd= sound.Output( sampleRate, channels, format )
s= f.readframes( 300000 )

snd.play( s )
while snd.isPlaying(): time.sleep( 0.05 )
