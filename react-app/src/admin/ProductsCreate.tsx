import React, {SyntheticEvent, useState} from 'react';
import Wrapper from "./Wrapper";
import {Redirect} from 'react-router-dom';

const ProductsCreate = () => {
    const [title, setTitle] = useState('');
    const [image, setImage] = useState('');
    const [redirect, setRedirect] = useState(false);

    const submit = async (e: SyntheticEvent) => {
        e.preventDefault();

        await fetch('http://20.219.112.96:10000/creation-page/api/create-item', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({
                title,
                image
            })
        });
        
        setRedirect(true);
    }

    if (redirect) {
        return <Redirect to={'/products-panel'}/>
    }

    return (
        <Wrapper>
            <form onSubmit={submit}>
                <div className="form-group">
                    <label>Title</label>
                    <input type="text" className="form-control" name="title" required
                           onChange={e => setTitle(e.target.value)}
                    />
                </div>
                <div className="form-group">
                    <label>Image</label>
                    <input type="text" className="form-control" name="image" required
                           onChange={e => setImage(e.target.value)}
                    />
                </div>
                <div style={{display: "flex", flexDirection: "row"}}>
                    <button className="submitButton btn btn-outline-secondary" >Save</button>
                </div>
            </form>
        </Wrapper>
    );
};

export default ProductsCreate;
