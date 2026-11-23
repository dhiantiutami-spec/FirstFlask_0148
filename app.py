from flask import Flask, request, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World</p>! <img src='https://www.pixelstalk.net/wp-content/uploads/2016/08/Disney-Tangled-Backgrounds-1240x654.jpg' />"

@app.route("/about")
def about():
    return "About us"

@app.route("/user/<name>")
def profile(name):
    return f"Hello, {escape(name)}!"

@app.route("/post/<int:post_id>")
def post(post_id):
    return f"Post #{post_id}"

# Route dengan method POST
@app.route("/submit", methods=["GET", "POST"])
def submit():
    if request.method == "POST":
        nama = request.form.get("nama")
        nama = escape(nama)
        return f"<h1>Halo, {nama}!</h1><a href='/submit'>Kembali</a>"

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)