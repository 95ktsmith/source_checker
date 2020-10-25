import React from "react";
import TrustedSrc from "./trusted";
import SemiTrustedSrc from "./semi";
import UnknownSrc from "./questionable";

import "./sources.css";

export default class search extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            value: '',
            loaded: '',
            error: false,
            data: ''
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
        this.setState({loaded: true, data: data})
        console.log(data);
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
                    {this.state.data['trusted'].map(src => (
                        <TrustedSrc url = {src} />
                    ))}
                    {this.state.data['semi-trusted'].map(src => (
                        <SemiTrustedSrc url = {src} />
                    ))}
                    {this.state.data['questionable'].map(src => (
                        <UnknownSrc url = {src} />
                    ))}

                </div> : <div><h5>Search an article to discover what sources its using</h5></div>}
            </div>
        );
  }  
}