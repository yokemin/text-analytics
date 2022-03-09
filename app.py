#!/usr/bin/env python
# coding: utf-8

# In[1]:


from textblob import TextBlob


# In[2]:


from flask import Flask


# In[3]:


app = Flask(__name__)


# In[4]:


from flask import render_template, request

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form.get("text")
        print(text)
        r = TextBlob(text).sentiment
        return(render_template("index.html", result=r))
    else:
        return(render_template("index.html", result="2"))


# In[ ]:


if __name__ == "__main__":
    app.run()


# In[ ]:




