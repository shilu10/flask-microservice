import React, {useEffect, useState} from 'react';
import {Product} from "../interfaces/product";
import "./main.css"
import {Link} from "react-router-dom";

const Main = () => {
    const [products, setProducts] = useState([] as Product[]);

    useEffect(() => {
        (
            async () => {
                const response = await fetch('http://20.219.112.96:10001/main-page/api/items');

                const data = await response.json();

                setProducts(data["result"]);
            }
        )();
    }, []);

    const like = async (id: number) => {
        await fetch(`http://20.219.112.96:10001/main-page/api/item/${id}/like`, {
            method: 'POST',
            headers: {'Content-Type': 'application/json'}
        });

        setProducts(products.map(
            (p: Product) => {
                if (p.id === id) {
                    p.likes++;
                }

                return p;
            }
        ));
    }
    console.log(products)

    return (
        <main role="main">
            <nav className="navbar navbar-dark sticky-top bg-dark flex-md-nowrap p-0 shadow">
                <Link to={`/products-panel`}>
                    <a className="navbar-brand col-md-3 col-lg-2 mr-0 px-3" href="#">Add Product</a>
                </Link>
                <button className="navbar-toggler position-absolute d-md-none collapsed" type="button"
                        data-toggle="collapse"
                        data-target="#sidebarMenu" aria-controls="sidebarMenu" aria-expanded="false"
                        aria-label="Toggle navigation">
                    <span className="navbar-toggler-icon"></span>
                </button>
                
                
                </nav>
            <div className="album py-5 bg-light">
                <div className="container">
                    <div className="row">
                        {products.map(
                            (p: Product) => {
                                return (
                                    <div className="col-md-4" key={p.id}>
                                        <div className="card mb-4 shadow-sm">
                                            <img src={p.image} style={{height: "300px", objectFit: "cover"}}/>
                                            <div className="card-body">
                                                <p className="card-text">{p.title}</p>
                                                <div className="d-flex justify-content-between align-items-center">
                                                    <div className="btn-group">
                                                        <button type="button"
                                                                className="likeButton btn btn-sm btn-outline-secondary"
                                                                onClick={() => like(p.id)}
                                                        >
                                                            Like
                                                        </button>
                                                    </div>
                                                    <small className="text-muted">{p.likes} likes</small>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                )
                            }
                        )}
                    </div>
                </div>
            </div>

        </main>
    );
};

export default Main;
