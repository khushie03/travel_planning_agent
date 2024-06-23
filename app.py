from flask import redirect , url_for
from flask import Flask , render_template
from main import chat_app
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/chatbot")
def chatbot():
    return redirect(url_for(chat_app))


if __name__ == "__main__":
    app.run(debug= "True")
