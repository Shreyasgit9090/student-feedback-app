from flask import Flask, render_template, request

app = Flask(__name__)

feedbacks = []

def validate_feedback(name, subject, feedback):
    if len(name.strip()) < 2:
        return False

    if len(subject.strip()) < 2:
        return False

    if len(feedback.strip()) < 5:
        return False

    return True

@app.route("/", methods=["GET", "POST"])
def home():
    message = ""

    if request.method == "POST":
        name = request.form["name"]
        subject = request.form["subject"]
        feedback = request.form["feedback"]

        if validate_feedback(name, subject, feedback):
            feedbacks.append({
                "name": name,
                "subject": subject,
                "feedback": feedback
            })
            message = "Feedback submitted successfully"
        else:
            message = "Invalid feedback data"

    return render_template(
        "index.html",
        feedbacks=feedbacks,
        message=message
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)