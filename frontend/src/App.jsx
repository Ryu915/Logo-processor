import { useState } from 'react'
import './App.css'

function App() {
  const [file, setFile] = useState(null);
  const [results, setResults] = useState(null);

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  const handleSubmit = async () => {
    if (!file) {
      alert("Please select a file");
      return;
    }

    const formData = new FormData();
    formData.append("image", file);

    try {
      const response = await fetch("http://127.0.0.1:5000/process", {
        method : "POST",
        body : formData
      });

      const data = await response.json();

      setResults(data);
      alert("Upload successful");
    } catch(error) {
        console.error(error);
        alert("Upload failed");
    }
  };

  return (
    <>
      <h1>Logo Processor</h1>

      <input type="file" accept=".png,.jpg,.jpeg" onChange={handleFileChange} />

      <button onClick={handleSubmit}>Process Image</button>

      {results && (
        <div>

          <h2>Processed Outputs</h2>

          <div>
            <h3>Grayscale</h3>
            <img src={results.grayscale} width="200" />
          </div>

          <div>
            <h3>Border</h3>
            <img src={results.border} width="200" />
          </div>

          <div>
            <h3>Silhouette</h3>
            <img src={results.silhouette} width="200" />
          </div>

        </div>
      )}

      {file && <p>Selected file: {file.name}</p>}
    </>
  )
}

export default App
