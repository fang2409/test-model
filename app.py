#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, request, render_template

app = Flask(__name__)

import joblib

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        rates = request.form.get("rates")
        print(rates)
        model = joblib.load("DBS_Reg")
        pred = model.predict([[rates]])
        return(render_template("index.html", results=pred))
    else:
        return(render_template("index.html", results="2"))

if __name__=="__main__":
    app.run()


# In[ ]:




