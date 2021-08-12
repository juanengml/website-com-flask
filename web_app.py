
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, request
import os

# Set environment variables
db = os.getenv('DATABASE')

app = Flask(__name__)

@app.route('/',methods=["GET","POST"])
def index():
    return render_template("index.html")

@app.route('/database',methods=["GET","POST"])
def index():
    html = """
     <center>
     <h1>url database</h1>
     <br> 
     <h2>{}</h2>
     </center>
     """.format(db)
    return html


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
           
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=80,debug=True)