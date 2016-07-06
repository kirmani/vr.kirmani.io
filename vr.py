#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 Sean Kirmani <sean@kirmani.io>
#
# Distributed under terms of the MIT license.

import json
import os

from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)
app.secret_key = 'kirmani_io_secret_key'


@app.route('/')
def home():
  return render_template('index.html')

if __name__ == '__main__':
  port = int(os.environ.get('PORT', 33507))
  app.run(host='0.0.0.0', port=port, debug=True)
