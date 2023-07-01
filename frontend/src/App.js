import React, { useState } from 'react';
import axios from 'axios';

const MyPage = () => {
  const [data, setData] = useState([]);
  const [csvFile, setCsvFile] = useState(null);

  const fetchData = async () => {
    try {
      const response = await axios.get('http://localhost:8000/api/data');
      setData(response.data);
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };

  const handleFileUpload = async (event) => {
    const file = event.target.files[0];
    setCsvFile(file);
  };

  const submitFile = async () => {

    try {
      const formData = new FormData();
      formData.append('file', csvFile);
      console.log(csvFile.type)
      const headers={'Content-Type': csvFile.type}
      await axios.post('http://localhost:8000/api/data', formData, headers);

      // Handle successful file upload
    } catch (error) {
      console.error('Error uploading file:', error);
    }
  };

  return (
    <div >
      
      <button style = {{margin: 10 + 'px'}} onClick={fetchData}>Fetch Data</button>
      <div  >
        <label htmlFor="file-upload">Upload CSV: </label>
        <input
          id="file-upload"
          type="file"
          accept=".csv"
          onChange={handleFileUpload}
        />
        <button onClick={submitFile}>Submit</button>
      </div>
      <br>
      </br>
      <table>
        <thead>
          <tr>
            <th>Date Time</th>
            <th>Close</th>
            <th>High</th>
            <th>Low</th>
            <th>Open</th>
            <th>Volume</th>
            <th>Instrument</th>
          </tr>
        </thead>
        <tbody>
          {data.map((item, index) => (
            <tr key={index}>
              <td>{item.datetime}</td>
              <td>{item.close}</td>
              <td>{item.high}</td>
              <td>{item.low}</td>
              <td>{item.open}</td>
              <td>{item.volume}</td>
              <td>{item.instrument}</td>
            </tr>
          ))}
        </tbody>
      </table>

      <style jsx>{`
        table {
          border-collapse: collapse;
          width: 100%;
        }

        th,
        td {
          border: 1px solid #ddd;
          padding: 8px;
          text-align: left;
        }

        th {
          background-color: #f2f2f2;
        }

        tr:nth-child(even) {
          background-color: #f9f9f9;
        }
      `}</style>
    </div>
  );
};

export default MyPage;
