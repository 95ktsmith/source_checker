import React from 'react';
import './App.css';
import './sources.css';

function IrreleventSrc(props) {
    return (
        <div className='source'>
            <div className='irrelevent'>
                <h4>(likely) Irrelevent</h4>
                <h5>Info: This goes back the same domain</h5>
                <h5>Source Found: <a href={props.url}>{props.url}</a></h5>                
            </div>

        </div>

    );
}

export default IrreleventSrc;
