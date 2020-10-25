import React from 'react';
import './App.css';


function SemiTrustedSrc(props) {
    return (
        <div className='source'>
            <div className='semi'>
                <h4>Semi-trusted</h4>
                <h5>Info: This link is run by an organization (.org)</h5>
                <h5>Click here to learn more about .org links</h5>
                <h5>Source Found: <a href={props.url}>{props.url}</a></h5>                
            </div>

        </div>

    );
}

export default SemiTrustedSrc;
