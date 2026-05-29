import { useState } from 'react'
import './App.css'

function App() {
  const [file, setFile] = useState(null);

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  return (
    <>
      <h1>Logo Processor</h1>

      <input type="file" accept=".png,.jpg,.jpeg" onChange={handleFileChange} />

      <button>Process Image</button>

      {file && <p>Selected file: {file.name}</p>}
    </>
  )
}

export default App
