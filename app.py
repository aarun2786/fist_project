from flask import Flask, render_template, jsonify
app = Flask(__name__)
job = [
  {
    "id": 1,
    'title': "Data Analyst",
    'location':'Bangalore',
    'Package': '10,00,000'
  }
  ,
  {
    "id": 2,
    'title': "Accountant",
    'location':'Tumkur'
  }
  ,
  {
    "id": 3,
    'title': "HR",
    'location':'Mysore',
    'Package': '11,00,000'
  }
]



@app.route('/')
def hello():
  return render_template("home.html",jobs=job)
@app.route("/jobs")
def list_jobs():
  return jsonify(job)
if __name__ == '__main__':
  app.run(host= '0.0.0.0',debug=True)