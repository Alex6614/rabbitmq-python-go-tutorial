from flask import Flask
from flask import request
from flask import jsonify
from redis import Redis
from services.product_event_handler import emit_product_order

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/create', methods=['POST'])
def create():
	pass