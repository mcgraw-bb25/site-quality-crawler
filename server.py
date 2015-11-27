import os
from flask import Flask
from flask import render_template
from flask import send_from_directory
from app.get_report_list import get_report_list


app = Flask(__name__)


@app.route('/')
def index():
    reports = get_report_list()
    return render_template('index.html', reports=reports)


@app.route('/site_report/<site_report_file>')
def site_report(site_report_file):
    report_filename = '/reports/' + site_report_file
    return render_template('site_report.html', site_report_file=report_filename)


@app.route('/reports/<path:filename>')
def send_json(filename):
    curpath = os.getcwd()
    newpath = curpath + '/reports/'
    return send_from_directory(newpath, filename)


if __name__ == "__main__":
    app.run()
