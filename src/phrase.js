import React from 'react';

//import './phrase.css';

function Phrase() {

  var phrases = ["Check your sources.", "The onion is not a credible news source"]

  return (
    <div className="Phrase">
        <h5>{phrases[Math.floor(Math.random() * phrases.length)]}</h5>
    </div>
  );
}

export default Phrase;
