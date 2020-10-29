import React from 'react';
import './App.css';
import './sources.css';

function TrustedSrc(props) {
    return (
        <div className='source'>
            <div className='trusted'>
                <h4>Likely Trusted</h4>
                <p>Info: This is a .gov or .edu url which means that this link is backed by goverment or educational resources</p>
                <h5>Click me to learn about .edu (or me for .gov links)</h5>
                <h5>Source Found: <a href={props.url}>{props.url}</a></h5>
            </div>
        </div>

    );
}

export default TrustedSrc;
