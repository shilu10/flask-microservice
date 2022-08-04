import React, {useEffect, useState} from 'react';
import Wrapper from "./Wrapper";
import {Product} from "../interfaces/product";
import {Link} from "react-router-dom";

const Products = () => {
    const [products, setProducts] = useState([]);

    useEffect(() => {
        (
            async () => {
                const response = await fetch('http://20.219.112.96:10000/creation-page/api/items');

                const data = await response.json();

                setProducts(data["result"]);
            }
        )();
    }, []);

    const del = async (id: number) => {
        if (window.confirm('Are you sure you want to delete this product?')) {
            await fetch(`http://20.219.112.96:10000/creation-page/api/items/delete/${id}`, {
                method: 'DELETE'
            });

            setProducts(products.filter((p: Product) => p.id !== id));
        }
    }

    return (
        <Wrapper>
            <div className="pt-3 pb-2 mb-3 border-bottom">
                <div className="btn-toolbar mb-2 mb-md-0">
                    <Link to='/products-panel/create' className="btn btn-sm btn-outline-secondary">Add</Link>
                </div>
            </div>

            <div className="table-responsive">
                <table className="table table-striped table-sm">
                    <thead>
                    <tr>
                        <th>#</th>
                        <th>Image</th>
                        <th>Title</th>
                        <th>Likes</th>
                        <th>Action</th>
                    </tr>
                    </thead>
                    <tbody>
                    {products.map(
                        (p: Product) => {
                            return (
                                <tr key={p.id} className="tr">
                                    <td>{p.id}</td>
                                    <td><img src={p.image} height="40" object-fit="cover" width="40px"/></td>
                                    <td>{p.title}</td>
                                    <td>{p.likes}</td>
                                    <td>
                                        <div className="btn-group mr-2">
                                            <Link to={`/products-panel/${p.id}/edit`}
                                                  className="editButton btn btn-sm btn-outline-secondary">Edit</Link>
                                            <a href="#" className="deleteButton btn btn-sm btn-outline-secondary"
                                               onClick={() => del(p.id)}
                                            >Delete</a>
                                        </div>
                                    </td>
                                </tr>
                            )
                        })}

                    </tbody>
                </table>
            </div>
        </Wrapper>
    );
};

export default Products;
