from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route("/")
def home():
    #return redirect("/profile")
    return render_template("index.html")

@app.route("/profile")
def profile():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug = True, host = "0.0.0.0", port = 3000)