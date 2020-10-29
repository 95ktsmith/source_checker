import React from 'react';

import './landing.css';

function LandingPageContent() {

  var page = (
    <div className="Landing">
 
        <div className="Goal">
            <h3>Our goal</  h3>
            <p>
            With the glut of new and often unreliable sources seemingly popping up daily we aimed to create a tool that could enable users to better evaluate sources so that we can be better informed about the news, articles, and information we consume and the sources they originate from.  We didn’t want to create a tool that will judge articles or information, there is too much to be able to effectively determine authenticity, rather we want to help users educate themselves.
            </p>
        </div>
 
        <div className="What">
            <h3>What is Source Checker</h3>
            <p>
            Source Checker is a web application tool made to help you easily identify what an article, blog, or any publication is listing as sources. Sources that are found are categorized in an objective, unbiased manner, and displayed in an easily digestible way.
            </p>
        </div>

        <div className="Why">
            <h3>Why should you use Source Checker</h3>
            <p>
            There aren’t viable alternatives that help the user determine the credibility of a source in an unbiased manner and allow the user to decide for themselves. Most similar tools use proprietary methods for determining credibility that are often biased, but more importantly are unknown to the user so they would have no way of knowing if they are getting accurate information.  Source Checker allows gives the user all the information and therefore all the power to decide for themselves.
            </p>
        </div>

        <div className="How">
            <h3>How Source Checker should be used</h3>
            <p>
            To use the tool simply input the url of a website or article you’d like to check in the bar and press go.  If the url is valid it will display results below the search bar and you can enter a rating below the results.  The rating is simply a number between one and five.
            </p>
        </div>
    </div>
  );

  return page
}

export default LandingPageContent;
