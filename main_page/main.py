from flask import Flask, jsonify, abort, request
from dataclasses import dataclass
from flask_cors import CORS
import requests
import json
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.inspection import inspect
from flask_marshmallow import Marshmallow
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from server.producer import publish


app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://admin:admin@db_host1:3306/main_db'

mash = Marshmallow(app)
db = SQLAlchemy(app)

class ProductDisplay(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    image = db.Column(db.Text(), nullable=False)
    likes = db.Column(db.Integer)

    def __repr__(self):
        return f'<product named {self.title}> is created'

class ProductSerializer(mash.SQLAlchemyAutoSchema): 
    class Meta: 
        model = ProductDisplay
        

@app.route("/main-page/api/items", methods = ["GET"])
def items(): 
    try: 
        products = ProductDisplay.query.all()
        product_serializer = ProductSerializer(many=True)
        products = product_serializer.dump(products)
        return jsonify({"result": products}), 200
    
    except Exception as err: 
        return jsonify({"result": "failure"}), 500


@app.route("/main-page/api/item/<int:id>/like", methods = ["POST"])
def like(id): 
    try: 
        product = ProductDisplay.query.filter_by(id=id).first()
        product.likes += 1 
        publish("product-liked", id)
        db.session.commit()
        db.session.close()
        return jsonify({"likes": "success"}), 200
    
    except Exception as err: 
        return jsonify({"likes": "failure"}), 500


if __name__ == "__main__": 
    db.create_all()
    app.run(port = 10001, debug = True, host = "0.0.0.0")