import React, { useState, useEffect } from 'react'
import axios from 'axios'
import { useNavigate } from 'react-router-dom'

const Home = () => {
  const [student, setStudent] = useState(null)
  const navigate = useNavigate()

  useEffect(() => {
    axios.get("http://127.0.0.1:8000/student/get")
      .then(res => setStudent(res.data))
      .catch(err => console.log(err))
  }, [])

  return (
    <div id='get-div'>
      <table id='get_table' border='5'>
        <thead>
          <tr>
            <th>ID</th>
            <th>Roll No</th>
            <th>Name</th>
            <th>Age</th>
          </tr>
        </thead>
        <tbody>
          {
            student && student.map((item)=>
              <tr>
                <td>{item.id}</td>
                <td>{item.roll_no}</td>
                <td>{item.name}</td>
                <td>{item.age}</td>
              </tr>
            )
          }
        </tbody>
      </table>
    </div>
  )
}

export default Home
