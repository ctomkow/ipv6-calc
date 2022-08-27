# Craig Tomkow
# February 17, 2018
# Main web app file

import ipaddress

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def calc():
    return render_template('calc.html')

@app.route('/result', methods=['POST'])
def result():
    ip_addr = request.form['ip_address']

    # If form is blank, set ip_address to placeholder text
    if ip_addr == '':
    	ip_addr = 'a634:57b4:573f:5d34::1/39'

    # ipv6 address
    ipv6_net = ipaddress.IPv6Interface(ip_addr)

    return render_template(
        'calc_result.html',
	    original_ip = ipv6_net.with_prefixlen,
	    ip_network = ipv6_net.network.with_netmask)
