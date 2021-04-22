#help from https://medium.com/@MAbdElRaouf/simple-content-based-recommendation-engine-flask-api-heroku-dd27760dfe8e

import pandas as pd
import numpy as np

def most_similar(ref, df, pairwise_similarities):

   
    try:

        def get_ix(ref):
            ref = ref.replace(' ', '\u2009')
            return df[df['ref'] == ref].index[0]

        doc_ix = get_ix(ref)

    except:
        
        return 'Sutta reference not found. Try another.'


    similar_ix = np.argsort(pairwise_similarities[doc_ix])[::-1][1:]

    response = {'Result': [{'Title':df.iloc[ix]["title"], 'URL': df.iloc[ix]["title_url"]} for ix in similar_ix[1:6]]}

    return response