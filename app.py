from flask import Flask, render_template, request, redirect, url_for, flash
import urllib2, json

my_app = Flask(__name__)
my_app.secret_key = "notsosecret"
#RuntimeError: The session is unavailable because no secret key was set. Set the secret_key on the application to something unique and secret.

key = "e6aa067ea41a844458f5aaba21ad2ebd"

@my_app.route('/', methods=['GET', 'POST'])
def root():
    if(request.method == "POST"):
        search = "https://api.themoviedb.org/3/search/movie?api_key=%s&query=${%s}" % (key, request.form["keyword"])
        u = urllib2.urlopen(search)
        d = json.loads(u.read())
        display = {};
        if(d["total_results"] == 0):
            flash("No matching results");
        else:
            movieNum = 0;
            while(len(d["results"]) > movieNum & movieNum < 10):
                title = d["results"][movieNum]["title"]
                overview = d["results"][movieNum]["overview"]
                display[title] = overview
                movieNum += 1;
            print display
        return render_template("index.html", display = display)
    else:
        return render_template("index.html")
    

if __name__ == '__main__':
    my_app.debug = True
    my_app.run()
