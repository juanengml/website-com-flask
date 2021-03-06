
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/',methods=["GET","POST"])
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact',methods=["GET","POST"])
def contact():
    if request.method == "POST":
        dados = "%s %s %s" % (request.form["email"], request.form["assunto"], request.form["mensagem"])
        return(dados)

    return render_template("contact.html")

@app.route('/portifolio')
def portifolio():
    return render_template("portifolio.html")

@app.route("/search",methods=["GET","POST"])
def busca():
   if request.method == "POST":
           return request.form['busca']
