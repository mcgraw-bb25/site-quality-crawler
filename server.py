import os
from flask import Flask
from flask import render_template
from flask import send_from_directory
from app.get_report_list import get_report_list

app = Flask(__name__)
reports_directory = '/reports/'


@app.route('/')
def index():
    return render_template('index.html', site_reports=get_report_list())


@app.route('/site_report/<filename>')
def site_report(filename):
    report_filename = reports_directory + filename
    return render_template('site_report.html', site_report=report_filename)


@app.route('/reports/<path:filename>')
def send_json(filename):
    return send_from_directory(os.getcwd() + reports_directory, filename)

if __name__ == "__main__":
    app.run()
