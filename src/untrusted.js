import React from 'react';
import './App.css';

function SemiTrustedSrc(props) {
    return (
        <div className='source'>
            <h3>Semi-trusted</h3>
            <h4>Info: This link is run by an organization (.org)</h4>
            <h4>Click here to learn more about .org links</h4>
            <h4>URL: <a href={props.url}>{props.url}</a></h4>
        </div>

    );
}

export default SemiTrustedSrc;
