#!/usr/bin/env python

import os.path
from flask import Flask
from flask.ext.autoindex import AutoIndex

directory_root="/home/jherr/projects/motionout"

app = Flask(__name__)
idx = AutoIndex(app, directory_root, add_url_rules=False)

@app.route('/motionfiles/')
@app.route('/motionfiles/<path:path>')
def motionfiles(path='.'):
    #return "["+path+"]"
    #return idx.render_autoindex('motionrecording', browse_root='/motionfiles', endpoint = '.motionfiles')
    return idx.render_autoindex(path, endpoint = '.motionfiles')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8083, debug=True)

