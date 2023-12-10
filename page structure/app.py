from flask import Flask, render_template


app = Flask(__name__)

class Jay:
    def __init__(self, first, second, third):
        self.first = first
        self.second = secomd
        self.third = third


@app.route('/data-structures')
def home():

    movie = [
        'paid in full',
        'big short',
        'the beautiful mind'
    ]

    car = {
        'brand': 'Mercedes',
        'model': 'Roadster',
        'year': '2023',

    }

    me = Jay('jabu', 'Jeff', 'Jaden', 'James', 'Jordan')


    # shorter code:

    kwargs = {
        'movie': movie,
        'car': car,
        'jay': jay,
    }
    return render_template('data-structure.html', **kwargs)

    return render_template('data-structure.html', movies=movie)

@app.route('/conditionals-basics')
def con():
    company = 'Jay'
    return render_template('conditional.html', company=company)

@app.route('/conditionals-basics')
def con():
    planets = [
        'mercuary',
        'mercuary',
        'mercuary',
        'mercuary',
        'mercuary',
        'mercuary',
    ]


@app.route('/conditionals-basics')
def con():
    user_os = {
    'jay': 'linux'
    'jay': 'debian',
    'jay': 'Ubuntu',
    'jay': 'arch'
    }
