from flask import Flask, render_template, request
from werkzeug.contrib.cache import SimpleCache
import dbhelper

app = Flask(__name__)
simplecache = SimpleCache()

@app.route("/")
def init():
    return render_template("index.html")

@app.route("/create")
def create():
    return render_template("create.html")

@app.route("/update")
def update():
	rows = dbhelper.read_all()
	return render_template("update.html", rows=rows)

@app.route("/delete")
def delete():
	rows = dbhelper.read_all()
	return render_template("delete.html", rows=rows)

@app.route("/insert", methods=['POST'])
def insert():
	if request.method == 'POST':
		id = request.form['id']
		name = request.form['name']
		return dbhelper.insert(id, name)

@app.route('/read')
def read():
	rows = dbhelper.read_all()
	return render_template("read.html", rows=rows)

@app.route('/upd', methods=['POST'])
def upd():
	if request.method == 'POST':
		id = request.form['id']
		name = request.form['name']
		return dbhelper.update(id, name)

@app.route("/cache")
def cache():
	topdog = simplecache.get('topdog')
	if topdog is None:
		print("nothing cached")
		rows = dbhelper.read_one()
		topdog = {"id": rows[0], "name": rows[1]}
		
		simplecache.set('topdog', topdog, timeout = 1.5*60)
	return render_template("cache.html", id=topdog["id"], name = topdog["name"])

@app.route("/remove", methods=['POST'])
def remove():
	if request.method == 'POST':
		id = request.form['id']
		return dbhelper.delete(id)

if __name__ == '__main__':
	app.run(debug=True)
	dbhelper.init_db()
