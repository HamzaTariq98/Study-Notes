import React, { useState, useEffect } from 'react';
import ReactDOM from 'react-dom';
import 'bootstrap/dist/css/bootstrap.min.css';
import Header from './Header/Header';
import './index.css';
import reportWebVitals from './reportWebVitals';
import Cards from './Cards/Cards';

function Root() {


  const fetchEmailData = async (email) => {
    try {
      const response = await fetch(`http://127.0.0.1:3005/add/${email}`);
      if (response.ok) {
        const data = await response.json();
        setUserData(data);
      } else {
        console.error('Failed to fetch data');
      }
    } catch (error) {
      console.error(error);
    }
  }

  const [email, setEmail] = useState('user1');
  const [userData, setUserData] = useState(null);

  useEffect(() => {
    fetch('http://127.0.0.1:3005/get/ip/address')
      .then((response) => response.text())
      .then((userIp) => {
        console.log('b4 fetch',userIp)
        setEmail(userIp);
        fetchData(userIp)
      })
  }, []);
  



  const fetchData = async (userIp) => {
    
    console.log(userIp)
    console.log('fetching yr data')
    await fetchEmailData(userIp);
  }

  

 

  const addNewCard = async ()=> {
    setUserData(null);
    await fetch(`http://127.0.0.1:3005/addNewCard/${email}`)
    .then(response => response.json)
    .then(() => fetchData(email))
  }

   
  const removeCard = async (event)=> {
    setUserData(null);
    let index = parseInt(event.target.className)
    await fetch(`http://127.0.0.1:3005/removeCard/${email}/${index}`)
    .then(response => response.json)
    .then(() => fetchData(email))
  }


  const changeLocation = async (event)=> {
    setUserData(null);
    const newLocationName = prompt('Enter new city, country, ip',event.target.innerText);
    const index = event.target.className
    await fetch(`http://127.0.0.1:3005/removeCard/${email}/${index}/${newLocationName}`)
    .then(response => response.json)
    .then(() => fetchData(email))
  }

  return (
    <React.StrictMode>
      <div className='container'>
        <div className='row'>
          <div className='col header'>
            <Header email = {email}/>
          </div>
        </div>
        <hr />
        <div className="row">
          <div>
            <Cards userData = {userData} addNewCard= {addNewCard} removeCard={removeCard} changeLocation ={changeLocation}/>
          </div>
        </div>
      </div>
    </React.StrictMode>
  );
}

const rootElement = document.getElementById('root');
ReactDOM.createRoot(rootElement).render(<Root />);

reportWebVitals();
