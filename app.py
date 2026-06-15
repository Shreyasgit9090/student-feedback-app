from flask import Flask, render_template, request

app = Flask(__name__)

feedbacks = []

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form["name"]
        subject = request.form["subject"]
        feedback = request.form["feedback"]

        feedbacks.append({
            "name": name,
            "subject": subject,
            "feedback": feedback
        })

    return render_template("index.html", feedbacks=feedbacks)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)