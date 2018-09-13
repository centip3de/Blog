import markdown
import sys

from flask import Flask
from flask import render_template
from flask import Markup

from os import listdir
from os.path import isfile, join

app = Flask(__name__)
POST_DIR = 'posts'

def getPosts():
    return [join(POST_DIR, f) for f in listdir(POST_DIR) if isfile(join(POST_DIR, f))]

@app.route("/")
def root():
    posts = getPosts()[:3]
    nums = {
        0: "first",
        1: "second",
        2: "third"
    }
    replacements = {}
    for i, post in enumerate(posts):
        with open(post) as file:
            replacements[nums[i]] = Markup(markdown.markdown(file.read()))

    return render_template('index.html', **replacements)




if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] == "-d":
        app.run(debug=True, host='0.0.0.0', port=28080)
    app.run(debug=False, port=80)