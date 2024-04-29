# import lib
from flask import *
import pandas as pd
from nltk import word_tokenize
from nltk.corpus import stopwords
from string import punctuation
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from pickle import *

# Initialize Porter Stemmer
ps = PorterStemmer()

# Text cleaning function
def clean_data(txt):
    txt = txt.lower()
    txt = word_tokenize(txt)
    txt = [t for t in txt if t not in punctuation]
    txt = [t for t in txt if t not in stopwords.words("english")]
    txt = [ps.stem(t) for t in txt]
    txt = " ".join(txt)
    return txt

#restore the model and restore the vector
f=open("vector.pkl","rb")
tv=load(f)
f.close()

f=open("model.pkl","rb")
model=load(f)
f.close()



app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        txt = request.form["txt"]
        ctxt = clean_data(txt)
        vtxt = tv.transform([txt])
        res = model.predict(vtxt)
        return render_template("home.html", msg=res[0])
    else:
        return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
