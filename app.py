import json
from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():

    with open('./data/home.json') as f:
        data = json.load(f)

    return render_template('home.html', route='', banner='banner9.jpg',data=data)


@app.route("/about")
def about():
    return render_template('about.html', route='About', banner='banner9.jpg')

@app.route("/teaching")
def teaching():
    with open('./data/teaching.json') as f:
        data = json.load(f)

    return render_template('teaching.html', route='Teaching', banner='banner9.jpg', data=data)

@app.route("/research")
def research():
    with open('./data/research.json') as f:
        data = json.load(f)

    return render_template('research.html', route='Research', banner='banner9.jpg', data=data)

@app.route("/publications")
def publications():
    with open('./data/publications.json') as f:
        data = json.load(f)
    
    return render_template('publications.html', route='Pubications', banner='banner9.jpg', data=data)

@app.route("/team")
def team():
    with open('./data/members.json') as f:
        data = json.load(f)
        
    return render_template('team.html', route='Team', banner='banner9.jpg', data=data)

@app.route("/professionalactivities")
def professionalactivities():
    with open('./data/activities.json') as f:
        data = json.load(f)

    return render_template('professionalactivities.html', route='Activities', banner='banner9.jpg', data=data)


if __name__ == '__main__':
    app.run(debug=True)
