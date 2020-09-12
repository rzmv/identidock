#!/usr/bin/env python
from flask import Flask, Response, request
from flask_script import Manager
import requests
import hashlib
import redis

app = Flask(__name__)
manager = Manager(app)
cache = redis.StrictRedis(host="redis", port=6379, db=0)
default_name = "Max Razumov"
salt = "asdfdasfdslkjtioejwtiogrhgdr"


@app.route('/', methods=['GET', 'POST'])
def mainpage():
    name = default_name

    if request.method == "POST":
        name = request.form['name']
    salted_name = salt + name
    name_hash = hashlib.sha256(salted_name.encode()).hexdigest()
    
    header = "<html><head><title>Identidock</title></head><body>"
    body = '''<form method="POST">
              Hello <input type="text" name="name" value="{}">
              <button>Sumbit</button>
              </form>
              <p> You look like a: </p>
              <img src="/monster/{}"/>
           '''.format(name, name_hash)
    footer = "</body></html>"

    return header + body + footer

@app.route("/monster/<name>")
def get_identicon(name):
    image = cache.get(name)

    if image is None:
        print("Cache miss", flush=True)
        r = requests.get("http://dnmonster:8080/monster/" + name + "?size=80")
        image = r.content
        cache.set(name, image)

    return Response(image, mimetype="image/png")

if __name__ == "__main__":
    #manager.run()
    app.run(debug=True, host="0.0.0.0")
