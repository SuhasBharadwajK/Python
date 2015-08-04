from flask import Flask

#app = Flask("First World App")

app = Flask(__name__)
app.debug = True

@app.route("/")
def index():    
    return "Index"

'''@app.route("/hello")
def hello():
    return "Hello"'''

@app.route("/<string:nam>")
def gener(nam):
    #return render_template('/var/www/html/index.html')
    return nam

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'






if __name__ == "__main__":
    app.run()
