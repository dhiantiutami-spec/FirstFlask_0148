from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    app.run(debug=True)

@app.route("/about")
def about():
    return "Tentang kami"

@app.route("/user/<name>")
def profile(name):
    return f"Halo, {name}!"

@app.route("/post/<int:post_id>")
def post(post_id):
    return f"Postingan #{post_id}"