from flask import Flask
from apis._api import api

from ENV import *
from apis.case_design_api import *
from pylab import *

mpl.rcParams['font.sans-serif'] = ['SimHei']

app = Flask(__name__)
app.register_blueprint(api, url_prefix='/api')
app.config['JSON_AS_ASCII'] = False

if __name__ == '__main__':
    app.run(host=HOST, port=PORT, debug=True)
