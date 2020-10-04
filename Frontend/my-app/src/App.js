import React, { useState, useEffect } from 'react';
import './App.css';

  //needed to avoid "Access-Control-Allow-Origin" error in browser
  const PROXY_URL = 'http://cors-anywhere.herokuapp.com/';
  //remember to change ngrok every backend restart
  const NGROK_URL = 'http://d8c3ee7e4864.ngrok.io';


const ListOfAvaibleItems = () => {
  const [error, setError] = useState(null);
  const [items, setItems] = useState([]);
  const [isDataFetched, setFetched] = useState(false);

  useEffect(() => {
    fetch(PROXY_URL+NGROK_URL+"/files")
      .then(res => res.json())
      .then((result) => {
        setItems(result.filelist);
        setFetched(true);
      },
      (error) => {
        setError(error);
        setFetched(true);
      })
  }, []);

  if (error){
    return <div>Error: {error.message}</div>
  } else if (!isDataFetched) {
    return <div>Fetching data...</div>
  } else {
    return (
      <ul>
        {items.map(item => (
          <li key={item.name}>
            {item.name}
          </li>
        ))}
      </ul>
    );
  }
}

const SendFile = () => {
   const data = {
     name: "fromfrontend",
     path: "testpath/testpath2"
   }
   
    fetch(PROXY_URL+NGROK_URL+"/upload", {
      method: "POST",
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    })
}

const ShowListButton = () => {
  const handleClick = () => {
    console.log("click");
  }

  return (
    <button className="Buttons" onClick={handleClick}>Show file list</button>
  )

}

const App = () => {
  const [list, setList] = useState([]);

  const showItems = () => {
    setList(<ListOfAvaibleItems />);
  }

  return (
    <div className="App-header">
      <div className="List">
        {list}
      </div>
      <div>
        <ShowListButton className="Buttons" />
        <button className="Buttons" onClick={showItems}>Show list</button>
        <button className="Buttons" onClick>Add file</button>
      </div>
    </div>
  )
}


export default App;
