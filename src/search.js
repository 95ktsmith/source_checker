import React from "react";
import TrustedSrc from "./trusted";
import SemiTrustedSrc from "./semi";
import UnknownSrc from "./questionable";
import RateFtr from "./rateFtr"

import "./sources.css";

export default class search extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            value: '',
            loaded: '',
            error: false,
            url: '',
            sources: '',
            rating: ''
        };

        this.handleSubmit = this.handleSubmit.bind(this)
        this.handleChange = this.handleChange.bind(this)
    }


    handleChange(event) {
        this.setState({value: event.target.value});
    }

    async handleSubmit(event) {
        event.preventDefault();

        const req_options = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json'},
            body: JSON.stringify({url: this.state.value})
        };

        const response = await fetch('/sourcecheck', req_options)
            .catch(error => {
                console.log(error)
            }) 
        const data = await response.json();
        this.setState({loaded: true, sources: data['sources'], url: this.state.value, rating: data['rating']})
    }

    render () {
        return (
            <div className='Search'>
                <form onSubmit={this.handleSubmit} >
                    <input type="text" id='url' value={this.state.value} onChange={this.handleChange}></input>
                    <button type="submit" className="button">Go</button>
                </form>
                {this.state.loaded ? 
                <div>
                    <h4>Sources from {this.state.url}</h4>
                    <h5>Average user trust rating: {this.state.rating}/5</h5>
                    {this.state.sources['trusted'].map(src => (
                        <TrustedSrc url = {src} />
                    ))}
                    {this.state.sources['semi-trusted'].map(src => (
                        <SemiTrustedSrc url = {src} />
                    ))}
                    {this.state.sources['questionable'].map(src => (
                        <UnknownSrc url = {src} />
                    ))}
                    <RateFtr url = {this.state.value} />


                </div> : <div><h5>Search an article to discover what sources its using</h5></div>}
            </div>
        );
  }  
}