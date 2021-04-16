from flask import Flask, render_template, request, jsonify, make_response
from sutta_model_3 import most_similar #Importing engine function
import json
import pandas as pd
import numpy as np
from werkzeug.datastructures import CombinedMultiDict

app = Flask(__name__)

#Avoid switching the order of 'title' and 'confidence' keys
app.config['JSON_SORT_KEYS'] = False

df = pd.read_csv('./data/df_all_clean.csv')

with open('./data/pairwise_similarities.npy', 'rb') as f:
        pairwise_similarities = np.load(f)

@app.route('/')
def hello_world():
    return render_template('sutta.html')


#API endpoint
@app.route('/api', methods=['POST','GET'])
def process_request():

    #Parse received JSON request
    user_input = request.form
  
    ref = user_input["ref"]

    #Call recommendation engine
    recommended = most_similar(ref, df, pairwise_similarities)

    return render_template('sutta.html', out= most_similar(ref, df, pairwise_similarities))


if __name__ == '__main__':

    app.run()