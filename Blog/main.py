import markdown
import sys

from flask import Flask
from flask import render_template
from flask import Markup

from os import listdir
from os.path import isfile, join

app = Flask(__name__)
POST_DIR = 'posts'

@app.route("/")
def root():
    filenames = [join(POST_DIR, f) for f in listdir(POST_DIR) if isfile(join(POST_DIR, f))]
    first_three = filenames[:3]
    posts = []
    for filename in first_three:
        with open(filename) as file:
            posts.append(Markup(markdown.markdown(file.read())))

    return render_template('index.html', posts=posts)

if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] == "-d":
        app.run(debug=True, host='0.0.0.0', port=28080)

    app.run(debug=False, port=80)