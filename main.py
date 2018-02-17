# Craig Tomkow
# February 17, 2018
# Main web app file

import logging

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def calc():
    return render_template('calc.html')

@app.route('/result', methods=['POST'])
def result():
    ip_address = request.index['ip_address']
    subnet_mask = request.index['subnet_mask']
   
    ### DO IPv6 Calc Magic Here!

    return render_template(
         'calc_result.html',
	 ip_address = ip_address,
	 subnet_mask = subnet_mask)
