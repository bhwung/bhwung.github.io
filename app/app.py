from flask import Flask, render_template, request, redirect

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about", methods=["GET", "POST"])
def about():
    if request.method == "POST":
        ...
        return redirect("/")
    return render_template("about.html")

@app.route("/menu", methods=["GET", "POST"])
def menu():
    if request.method == "POST":
        ...
        return redirect("/")
    return render_template("menu.html")

@app.route("/how", methods=["GET", "POST"])
def how():
    if request.method == "POST":
        ...
        return redirect("/")
    return render_template("how.html")

@app.route("/social", methods=["GET", "POST"])
def social():
    if request.method == "POST":
        ...
        return redirect("/")
    return render_template("social.html")