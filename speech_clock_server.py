from flask import Flask, send_file
from datetime import datetime

app = Flask(__name__, static_url_path='')

@app.route('/')
def root():

    time = datetime.now()

    folder = "output/Johan"
    hours = time.hour
    minutes = time.minute
    seconds = time.second
    print("%i:%i:%i" %(hours, minutes, seconds))


    return send_file("%s/%i_%i.wav" %(folder, hours, minutes))

if __name__ == "__main__":
    app.run(host="0.0.0.0")