import React from 'react';
import './footer.css';

function Footer() {
  return (
    <div className='contact'>
      <h3>Contact Us</h3>
      <div className="footer">
        <div className='Mike'>
          <h4>Michael George</h4>
          <p>michael.george@holbertonschool.com</p>
          <a href='https://github.com/mag389'>https://github.com/mag389</a>
        </div>
        <div className='Carter'>
          <h4>Carter Clements</h4>
          <p>cclements3150@gmail.com</p>
          <a href='https://github.com/JavaPhish'>https://github.com/JavaPhish</a>
        </div>
        <div className='Kevin'>
          <h4>Kevin Smith</h4>
          <p>kevin.smith@holbertonschool.com</p>
          <a href='https://github.com/95ktsmith'>https://github.com/95ktsmith</a>
        </div>
      </div>
    </div>
  );
}

export default Footer;
