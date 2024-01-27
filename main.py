from flask import Flask, render_template, request, flash

from SQLAgent import SQLAgent

app = Flask(__name__)
app.secret_key = '123'
DB_NAME = "items.db"



@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")



@app.route("/interesting_articles")
def interesting_articles():
    sql_agent = SQLAgent(DB_NAME)
    items = sql_agent.get_interesting_articles()
    return render_template("interesting_articles.html", items=items)

@app.route("/about_author")
def about_author():
    return render_template("about_author.html")


if __name__ == '__main__':
    app.run(debug=True)

"""
vanv/Scripts\activate
python app.py
"""