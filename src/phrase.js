import React from 'react';

//import './phrase.css';

function Phrase() {

  var phrases = ["Check your sources."]

  return (
    <div className="Phrase">
        <h5>{phrases[Math.floor(Math.random() * phrases.length)]}</h5>
    </div>
  );
}

export default Phrase;
