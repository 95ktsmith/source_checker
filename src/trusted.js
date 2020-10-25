import React from 'react';
import './App.css';

function TrustedSrc(props) {
    return (
        <div className='source'>
            <div className='trusted'>
                <h4>Likely Trusted</h4>
                <h5>This is either a .gov or .edu url which means that this link is backed by goverment or educational resources</h5>
                <h5>Source Found: <a href={props.url}>{props.url}</a></h5>
            </div>
        </div>

    );
}

export default TrustedSrc;
