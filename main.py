from flask import Flask
from flask import request

# testing
from modules.spider.spider import Spider
app = Flask(__name__)


@app.route("/search", methods=['POST'])
def search():
    query = request.form.get("Q")
    # call search api
    return {"count": 12132, "query": query}


@app.route("/test_spider", methods=['POST'])
def test_spider():
    query = request.form.get("url")
    # call search api
    res = Spider(url=query).run()
    return {"res": res}


if __name__ == "__main__":
    app.run()
