import datetime
from flask import Flask, render_template

"""
gcloud projects create PROJECT_ID
gcloud projects create localflask

Project name personalflask
Project number 351370458645
Project ID personalflask
"""
app = Flask(__name__)

@app.route('/')
def root():
    # For the sake of example, use static information to inflate the template.
    # This will be replaced with real information in later steps.
    dummy_times = [datetime.datetime(2018, 1, 1, 10, 0, 0),
                   datetime.datetime(2018, 1, 2, 10, 30, 0),
                   datetime.datetime(2018, 1, 3, 11, 0, 0),
                   ]
    dummy_times={"employee": [{"id": "04", "name": "sunil", "department": "HR"}, {"id": "03", "name": "Charlie", "department": "CEO"}, {"id": "007", "name": "james", "department": "HR"}]}

    #return render_template('index.html', times=dummy_times)
    #dict(dummy_times['employee'])
    out = dict(dummy_times['employee'][0]).items()
    return render_template('recds.html', times=out )

@app.route("/docs")
def docs():

    return render_template("index.html", title="docs page testing an update re-deploy")

@app.route("/about")
def about():
    return render_template("index.html", title="about page")

if __name__ == "__main__":
    app.run(debug=True)