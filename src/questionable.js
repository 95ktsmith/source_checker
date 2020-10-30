import React from 'react';
import './App.css';
import './sources.css';

function UnknownSrc(props) {
    return (
        <div className='source'>
            <div className='unknown'>
                <h4>Unknown</h4>
                <p>Info: We couldnt find enough information to make unbiased claims about this link</p>
                <h5>Source Found: <a href={props.url}>{props.url}</a></h5>                
            </div>

        </div>

    );
}

export default UnknownSrc;
