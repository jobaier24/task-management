# from flask import Flask, render_template
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = ["Buy groceries", "Read a book", "Write code", "cong"]


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        new_task = request.form.get("task")
        if new_task:
            tasks.append(new_task)
        return redirect(url_for('index'))
    return render_template("index.html", tasks=tasks)

@app.route("/help")
def help():
    return render_template("help.html")