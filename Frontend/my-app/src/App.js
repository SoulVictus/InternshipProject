import React, { useState, useEffect } from 'react';
import './App.css';

  //needed to avoid "CORS" error in browsers
  const PROXY_URL = 'http://cors-anywhere.herokuapp.com/';
  
  // CHANGE NGROK URL //
  const NGROK_URL = 'http://8a2c462b252c.ngrok.io';
  //                  //

const ListOfAvaibleItems = (props) => {
  const [error, setError] = useState(null);
  const [items, setItems] = useState([]);
  const [isDataFetched, setFetched] = useState(false);

  //fetchinng data and rendering as list
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
  } else if (items.length === 0){ 
    return <div>No files in database</div>
  } else {
    return (
      <ul>
        {items.map(item => (
          <li key={item.toString()}>
            {item}
          </li>
        ))}
      </ul>
    );
  }
}

const SendFile = () => {
  const fileInput = React.createRef();

  //sending  file to server
  const handleSubmit = (event) =>{
    event.preventDefault();
    const formData = new FormData();
    formData.append('file', fileInput.current.files[0]);
    fetch(PROXY_URL+NGROK_URL+"/upload", {
      method: "POST",
      body: formData
    })
  }

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Send file:
        <br />
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
    //rerendering list onclick
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
      </div>
      <div>
        <SendFile />
      </div>
    </div>
  )
}


export default App;
