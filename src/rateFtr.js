import React from 'react';

import './rate.css';

export default class RateFtr extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            value: '',
            loaded: '',
            url: this.props.url,
            error: false
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
            body: JSON.stringify({url: this.state.url, rating: this.state.value})
        };

        const response = await fetch('/rate_article', req_options)
            .catch(error => {
                console.log(error)
            }) 
            if (response.status === 200) {
                this.setState({loaded: true})
            }
    }
    render () {
        return (
            <div className='Rate'>
            {!this.state.loaded ?
                <div>
                    <h3>Is this article trustworthy?</h3>
                    <p>Help us judge the trust rating for this article (1 - 5)</p>
                    <form onSubmit={this.handleSubmit}>
                        <input type="text" onChange={this.handleChange}></input>
                        <button type="submit" value='Go'>Submit</button>
                    </form>
                </div> : <div><h4>Thank you!</h4></div>
            }
            </div>
        );
    }

}
