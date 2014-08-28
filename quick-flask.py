# -*- coding: utf-8 -*-

"""
quick-flask: simple script to create a general flask project prototype.

usage:

	~: python quick-flask.py app_name

this script will generate some python files,
and the file structrue will be like this:

	/application
		/app_pac
			/static
				/css
					...
				/js
					...
				/img
					...
			/templates
				index.html
				...

			__init__.py
			models.py
			views.py
			...

		config.py
		run.py
		...

@dir: app_pac: app_pac is the name of application package.
@dir: app_pac/static: dir for static files.
@dir: app_pac/templates: dir for templates files
@file: app_pac/__init__.py:

	from flask import Flask
	from flask.ext.sqlalchemy import SQLAlchemy

	app = Flask(__name__)
	app.config.from_object('config')

	db = SQLAlchemy(app)

	from app_pac import views

@file: app_pac/views.py

	from flask import render_template
	from app_pac import app, db
	from models import *

	@app.route('/')
	def index():
		return render_template('index.html')

@file: app_pac/models.py

	from app_pac import db

	class Data(db.Model):
		__tablename__ = ''
		id = db.Column(db.Integer, primary_key = True)

		def __init__():
			pass

		def __repr__():
			pass

@file: config.py

	DEBUG = True
	SECRET_KEY = 'quick-flask'
	SQLALCHEMY_DATABASE_URI = 'database://user:password@server/database'

@file: run.py

	from app_pac import app

	app.run(debug = True)

to launch a flask app, simply run file run.py

	~: python run.py


:copyright: (c) 2014 by Jason Lyu.
:license: Apache 2.0, see LICENSE for more details.
"""

import os
import sys

pac_name = "app_pac"


def mk_config():
    config_str = '''DEBUG = True
SECRET_KEY = 'quick-flask'
SQLALCHEMY_DATABASE_URI = 'database://user:password@server/database'
	'''
    with open('config.py', 'w') as f:
        f.write(config_str)


def mk_run():
    run_str = '''from pac_name import app

app.run(debug = True)
	'''.replace('pac_name', pac_name)
    with open('run.py', 'w') as f:
        f.write(run_str)


def mk_views():
    views_str = '''from flask import render_template
from pac_name import app, db
from models import *

@app.route('/')
def index():
	return render_template('index.html')
	'''.replace('pac_name', pac_name)
    with open('views.py', 'w') as f:
        f.write(views_str)


def mk_models():
    models_str = '''from pac_name import db

class Data(db.Model):
	__tablename__ = ''
	id = db.Column(db.Integer, primary_key = True)

	def __init__():
		pass

	def __repr__():
		pass
	'''.replace('pac_name', pac_name)
    with open('models.py', 'w') as f:
        f.write(models_str)


def mk___init__():
    __init__str = '''from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

from pac_name import views
	'''.replace('pac_name', pac_name)
    with open('__init__.py', 'w') as f:
        f.write(__init__str)


def mk_index():
    index_str = '''<html>
	<body>
		<a href = "http://github.com/jasonlvhit/quick-flask">http://github.com/jasonlvhit/quick-flask</a>
	</body>
</html>
	'''
    with open('index.html', 'w') as f:
        f.write(index_str)


def run():
    os.mkdir(pac_name)
    mk_config()
    mk_run()
    os.chdir(pac_name)
    os.mkdir('static')
    os.mkdir('templates')
    mk_views()
    mk_models()
    mk___init__()
    os.chdir('static')
    os.mkdir('css')
    os.mkdir('img')
    os.mkdir('js')
    os.chdir('../')
    os.chdir('templates')
    mk_index()

if __name__ == '__main__':
    assert sys.argv[1]
    pac_name = sys.argv[1]
    run()
