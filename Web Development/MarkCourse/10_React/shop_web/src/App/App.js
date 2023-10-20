import React from 'react';
import logo from './logo.svg';
import './App.css';
import HttpService from '../services/http-service';

const httpService = new HttpService();

class App extends React.Component {
  constructor(props) {
    super(props);
    httpService.getProducts();
  }

  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <p>
            Edit <code>src/App.js</code> and save to reload.
          </p>
          <button className="btn btn-primary">Click me</button>
          <a
            className="App-link"
            href="https://reactjs.org"
            target="_blank"
            rel="noopener noreferrer"
          >
            Learn React
          </a>
        </header>
      </div>
    );
  }
}

export default App;
