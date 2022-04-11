from dataclasses import dataclass
from flask import Flask, jsonify, abort
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint
from flask_migrate import Migrate
import requests
from producer import publish

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@db/main'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)

db = SQLAlchemy(app)

migrate = Migrate(app, db)


@dataclass
class Product(db.Model):
    id: int
    title: str
    image: str
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    title = db.Column(db.String(200))
    image = db.Column(db.String(200))


@dataclass
class ProductUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)

    UniqueConstraint('user_id', 'product_id', name='user_product_unique')


@app.route('/api/health')
def check():
    return jsonify({"ok": "ok"})


# GET http://172.24.0.3:5000/api/products
@app.route('/api/products')
def index():
    return jsonify(Product.query.all())
    # if you don't use dataclasses and redeclared properties use this
    # products = Product.query.all()
    # return jsonify([
    #     {
    #         '_id': product.id,
    #         'title': product.title,
    #         'image': product.image
    #     } for product in products
    # ])


# GET http://172.24.0.3:5000/api/products/3
@app.route('/api/products/<id>')
def get_product(id):
    return jsonify(Product.query.filter_by(id=id).first_or_404())
    # if you don't use dataclasses and redeclared properties use this
    # product = Product.query.filter_by(id=id).first_or_404()
    # return jsonify({
    #     'id': product.id,
    #     'title': product.title,
    #     'image': product.image
    # })


# GET http://172.24.0.3:5000/api/products/3
@app.route('/api/products/<id>/like')
def like(id):
    req = requests.get('http://host.docker.internal/api/user')
    json = req.json()

    try:
        productUser = ProductUser(user_id=json['id'], product_id=id)
        db.session.add(productUser)
        db.session.commit()

        publish('product_liked', id)
    except:
        abort(400, 'You already liked')



    return jsonify({
        'message': 'success'
    })
