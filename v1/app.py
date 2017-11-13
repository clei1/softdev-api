from flask import Flask, render_template
import urllib2, json

my_app = Flask(__name__)

@my_app.route('/', methods=['GET', 'POST'])
def root():
    u = urllib2.urlopen("https://api.nasa.gov/planetary/apod?api_key=TppvUAP35fD957Rj53aPtiwP1TaY29Z6mHa25b2Y")
    d = json.loads(u.read())
    return render_template("index.html", hdurl = d["hdurl"], explanation = d["explanation"])

if __name__ == '__main__':
    my_app.debug = True
    my_app.run()
