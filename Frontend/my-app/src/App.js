import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [items, setItems] = useState([]);
  const PROXY_URL = 'http://cors-anywhere.herokuapp.com/';
  //remember to change ngrok every restart
  const NGROK_URL = 'http://cb57bb83bbdb.ngrok.io/';
  useEffect(() => {
    fetch(PROXY_URL+NGROK_URL+"files/1")
      .then(res => res.json())
      .then((result) => {
        console.log(result);
        setItems(result);
      },
      (error) => {
        console.log(error);
      })

  }, []);

  return (
    <div style={{ flex: 1, padding: 24 }}>
    </div>
  );
}


export default App;
