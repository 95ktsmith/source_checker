import React from 'react';

import Search from "./search";
import Footer from "./footer";
import Phrase from "./phrase";
import Header from "./header";
import LandingPageContent from "./landingPage";

import './App.css';

function App() {

  var page = (
    <div className="App">
      <header className="App-header">
        <Header />
        <Phrase />
        <Search />
      </header>
      <LandingPageContent />
      <Footer />
    </div>
  );

  return page
}

export default App;
