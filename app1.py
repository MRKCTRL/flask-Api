from flask import Flask, render_template
import time
from pymongo import MongoClient
from dotenv import load_dotenv
import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

load_dotenv()

def create_app():

    cliwnt = MongoClient(os.environ.get('MONGODB_URI'))
    db = client.TheCuriousMind
    app = Flask(__name__)


    entries = []


    @app.route('/' methods=['GET', 'POST'])
    def home():

        if request.method == 'POST':
            entry_content = request.form.get('name')
            format_date = date.datetime.today().strftime(%Y-%m-%d)
            app.db.entries.insert({'content': entry_content, 'date':format_date})


        entries_with_date = [
            (
            entry['content'],
            entry['date'],
            date.date.strptime(entry['date'], '%Y-%m-%d').strftime('%b %d')
            )
            for entry in app.db.entries.find({})
        ]
        return render('index.html', entries=entries_with_date)

        return app
