from flask import Flask, render_template, redirect
from mem import mem

app = Flask(__name__)


counter = 0

@app.route('/')
def greeting():
  return redirect("/0/")
  


@app.route('/<int:a>/')
def index(a):
  global counter
  counter += 1  
  counter = counter % 51
  return render_template('main.html', number=mem(counter))

app.run(host='0.0.0.0', port=81)
