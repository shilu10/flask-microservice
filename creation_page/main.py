from flask import Flask, jsonify, abort, request
from dataclasses import dataclass
import requests
import os, sys
import json
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from server.producer import publish
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from server.image_accessability_checker import is_image_accessable


app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://admin:admin@db_host:3306/product_db'

mash = Marshmallow(app)
db = SQLAlchemy(app)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(100), nullable=False)
    likes = db.Column(db.Integer)

    def __repr__(self):
        return f'<product named {self.title}> is created'

class ProductSerializer(mash.SQLAlchemyAutoSchema): 
    class Meta: 
        model = Product


@app.route("/creation-page/api/items", methods = ["GET"])
def list_item(): 
    try: 
        products = Product.query.all()
        product_serializer = ProductSerializer(many=True)
        products = product_serializer.dump(products)
        print(products)
        return jsonify({"result": products}), 200
    
    except Exception as err: 
        return jsonify({"result": "error"}), 500


@app.route("/creation-page/api/create-item", methods = ["POST"])
def create(): 
    try:
        if request.content_type == "application/json":  
            data = json.loads(request.data)
            image = data.get("image")
            if not is_image_accessable(image):
                image = "" 
            new_product = Product(title = data.get("title"), image=data.get("image"), likes=0)
            db.session.add(new_product)
            product_serializer = ProductSerializer()
            new_product = product_serializer.dump(new_product)
            publish("product-created", new_product)
            db.session.commit()
            db.session.close()
            return jsonify({"create": "success"}), 200

    except Exception as err:
        return jsonify({"create": "failure"}), 400


# id is the route parameter.
@app.route("/creation-page/api/items/<int:id>", methods = ["GET"])
def retrieve(id):
    try: 
        product = Product.query.get(id)
        product_serializer = ProductSerializer()
        product = product_serializer.dump(product)
        return jsonify({"retrieve": product}), 200 
    
    except Exception as err: 
        return jsonify({"retrieve": "failure"}), 500


@app.route("/creation-page/api/items/delete/<int:id>", methods = ["DELETE"])
def delete(id): 
    try: 
        product = Product.query.get(id)
        db.session.delete(instance = product)
        publish("product-deleted", id)
        db.session.commit()
        db.session.close()
        return jsonify({"delete": "success"}), 200
    
    except Exception as err:
        return jsonify({"delete": "failure"}), 500


@app.route("/creation-page/api/items/update/<int:id>", methods = ["PUT"])
def update(id): 
    try: 
        data = json.loads(request.data)
        product = Product.query.get(id)
        product.title = data.get("title") if data.get("title") else product.title
        product.image = data.get("image") if data.get("image") else product.image
        product.likes = data.get("likes") if data.get("likes") else product.likes
        product_serializer = ProductSerializer()
        product = product_serializer.dump(product)
        publish("product-updated", product)
        db.session.commit()
        db.session.close()
        return jsonify({"update": "success"}), 200
    
    except Exception as err:
        return jsonify({"update": "failure"}), 500


if __name__ == "__main__": 
    db.create_all()
    app.run(debug=True, host="0.0.0.0", port=10000)
   
    