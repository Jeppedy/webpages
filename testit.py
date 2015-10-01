#!/usr/bin/env python

import os.path
from flask import Flask
from flask.ext.autoindex import AutoIndex

app = Flask(__name__)

@app.route('/testit')
@app.route('/testit/<path:onepath>')
def testit( onepath='' ):
    return '['+onepath+']'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8083, debug=True)

