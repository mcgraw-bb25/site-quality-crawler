from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/site_report.json")
def polls_json():
    with open("reports/site_report.json", 'r') as report_file:
        return report_file.read()


if __name__ == "__main__":
    app.run()
