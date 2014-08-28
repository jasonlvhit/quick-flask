### quick-flask: simple script to create a general flask project prototype.

usage:
```
	~: python quick-flask.py app_name
```

this script will generate some python files,
and the file structrue will be like this:
```
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
```


@dir: app_pac: app_pac is the name of application package.
@dir: app_pac/static: dir for static files.
@dir: app_pac/templates: dir for templates files

@file: app_pac/__init__.py:

``` py
	from flask import Flask
	from flask.ext.sqlalchemy import SQLAlchemy

	app = Flask(__name__)
	app.config.from_object('config')

	db = SQLAlchemy(app)

	from app_pac import views
```

@file: app_pac/views.py

``` py
	from flask import render_template
	from app_pac import app, db
	from models import *

	@app.route('/')
	def index():
		return render_template('index.html')
```

@file: app_pac/models.py

``` py
	from app_pac import db

	class Data(db.Model):
		__tablename__ = ''
		id = db.Column(db.Integer, primary_key = True)

		def __init__():
			pass

		def __repr__():
			pass
```

@file: config.py

``` py
	DEBUG = True
	SECRET_KEY = 'quick-flask'
	SQLALCHEMY_DATABASE_URI = 'database://user:password@server/database'

```

@file: run.py

``` py
	from app_pac import app

	app.run(debug = True)
```

to launch a flask app, simply run file run.py

```
	~: python run.py

```

copyright: (c) 2014 by Jason Lyu.

Have fun!

