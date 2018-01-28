import wave
from contextlib import closing

def join_audio(infiles, outfile):

    if len(infiles) is 0:
        raise ValueError("input file list empty")

    with closing(wave.open(outfile, "wb")) as output:

        #Set the parameters of the output file to the parameters of the first input file
        with closing(wave.open(infiles[0])) as w:
            output.setparams(w.getparams())

        #Combine the files
        for file in infiles:
            with closing(wave.open(file)) as f:
                output.writeframes(f.readframes(f.getnframes()))
