#!/usr/bin/env python

import os.path
from flask import Flask
from flask.ext.autoindex import AutoIndex

directory_root="/home/jherr/projects/motionout"

app = Flask(__name__)
idx = AutoIndex(app, directory_root, add_url_rules=False)

@app.route('/<path:path>')
def app_root(path = ''):
    print "test 2"+"["+path+"]"
    return "test 2"+"["+path+"]"

@app.route('/motionfiles')
@app.route('/motionfiles/')
@app.route('/motionfiles/<path:path>')
def motionfiles(path=''):
    print "test 1"+"["+path+"]"
#    return "test 1"+"["+path+"]"
    return idx.render_autoindex(path, endpoint = '.motionfiles')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8083, debug=True)

