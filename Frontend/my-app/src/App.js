import React, { useState, useEffect } from 'react';
import './App.css';

  //needed to avoid "Access-Control-Allow-Origin" error in browser
  const PROXY_URL = 'http://cors-anywhere.herokuapp.com/';
  //remember to change ngrok every backend restart
  const NGROK_URL = 'http://d8c3ee7e4864.ngrok.io';


const ListOfAvaibleItems = (props) => {
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
  }, [props.refresh]);

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

const SendFile = (props) => {
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

const SendF = () => {
  const fileInput = React.createRef();

  const handleSubmit = (event) =>{
    event.preventDefault();
    const formData = new FormData();
    formData.append('file', fileInput.current.files[0]);
    fetch(PROXY_URL+NGROK_URL+"/fileupload", {
      method: "POST",
      body: formData
    })
  }

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Send file:
        <input type="file" ref={fileInput} />
      </label>
      <br />
      <button type="submit">Send</button>
    </form>
  )
}


const App = () => {
  const [list, setList] = useState([]);
  const [refreshAction, setRefreshToggle] = useState(true);

  const showItems = () => {
    console.log(refreshAction);
    setList(<ListOfAvaibleItems refresh={refreshAction}/>);
    setRefreshToggle(!refreshAction);
  }

  return (
    <div className="App-header">
      <div className="List">
        {list}
      </div>
      <div>
        <button className="Buttons" onClick={showItems}>Show list</button>
        <button className="Buttons" onClick={SendFile}>Add file</button>
        <SendF />
      </div>
    </div>
  )
}


export default App;
