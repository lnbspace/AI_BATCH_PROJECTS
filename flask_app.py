import numpy as np
from flask import Flask, render_template, request
import pandas as pd
#import pickle

model = pd.read_pickle('/home/saurdrokr/mysite/Salary_mdl.pkl')
#model = pickle.load(open('/home/saurdrokr/mysite/Salary_mdl.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('LnB.html')

@app.route('/hello')
def hello_world():
    return 'Hello from Flask!'

@app.route('/just')
def index_page():
    return '''<html>
<title>
testing server with flask
</title>
<body>
<br>
<h1>
Hello i am just testing it for the very first time
</h1>
</body>
'''

@app.route('/prediction',methods=['POST'])
def predict():

    int_f = [int(x) for x in request.form.values()]
    final_f = [np.array(int_f)]
    p = model.predict(final_f)
    op = round(p[0], 2)
    return render_template('LnB.html', prediction_text='Expected Salary should be INR {}'.format(op))


if __name__ == "__main__":
    app.run(debug=True) #,port=5001
