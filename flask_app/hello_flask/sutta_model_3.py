import pandas as pd
import numpy as np

def most_similar(ref, df, pairwise_similarities):
    '''
  doc_id: (str) unique document identifier
  similarity_matrix: (ndarray) cosine similarity or euclidean difference matrix
  matrix_type: (str) 'cosine' or 'euclidean'
  number: (int) n of similar suttas to display
    '''

    df['ref'] = df['ref'].str.replace('\u2009', ' ')


    try:

        def get_ix(ref):
            return df[df['ref'] == ref].index[0]

        doc_ix = get_ix(ref)

    except:
        
        return 'Sutta reference not found. Try another.'


    similar_ix = np.argsort(pairwise_similarities[doc_ix])[::-1][1:]
    nl = "\n"

    #https://stackoverflow.com/questions/44780357/how-to-use-newline-n-in-f-string-to-format-output-in-python-3-6 
    rec_list = []
    for ix in similar_ix[1:6]:
        rec_list += f'Title: {df.iloc[ix]["title"]} ----------------------------------------- URL: {df.iloc[ix]["title_url"]}    ****************************************************************************************************************************   '
    
    ref_string = f"{''.join(rec_list)}"
    return ref_string