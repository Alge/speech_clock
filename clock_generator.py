from os import path, makedirs
from audio_joiner import join_audio


#Folder containing the recorded files (0-59 etc)
folder = "Johan"

#The file name of the first number recording (of "0"). Assuming continuous file names with recordings from
#0 to 59
starting_number = 1

#recording containing "nollnoll" (zero zero)
zerozero = "69.wav"

#recording containing "klockan är"
watchis = "61.wav"

#Create output dir if it doesn't already exist
if not path.exists("output/%s" %(folder)):
    makedirs("output/%s" %(folder))

#List of files to be combined
files = []

for hour in range(0,24):
    print("starting on hour: {}".format(hour))

    for minute in range(0,60):

        files.append("%s/%s"%(folder, watchis)) #"Klockan är:"

        if(hour == 0):
            files.append("%s/%s"%(folder, zerozero))
        else:
            if(hour < 10):
                files.append("%s/1.wav"%(folder))

            files.append("%s/%i.wav" %(folder, hour+starting_number))

        if(minute == 0):
            files.append("%s/%s"%(folder, zerozero))
        else:
            if(minute < 10):
                files.append("%s/1.wav"%(folder))
            files.append("%s/%i.wav" %(folder, minute+starting_number))

        join_audio(files, "output/%s/%i_%i.wav" %(folder, hour, minute))
        files = []
print("done")