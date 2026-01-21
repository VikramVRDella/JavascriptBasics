import React from 'react'
import {useState,useEffect} from 'react'
import axios from 'axios'
import { useNavigate } from 'react-router-dom'

const Get = () => {
  const navigate = useNavigate()
    const[data,setData] = useState([])
    useEffect(()=>{
        axios.get("http://localhost:8000/students/get")
        .then(res =>{
            setData(res.data)
        })
        .catch(err =>{
            console.log(err)
        })
    },[])
  return (
    <div id='Get-Container'>
      <h3>Fetching Students</h3>
      <table>
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
              data.map((student)=>(
                <tr key={student.id}>
                  <td>{student.id}</td>
                  <td>{student.roll}</td>
                  <td>{student.name}</td>
                  <td>{student.age}</td>
                </tr>
              ))
            }
        </tbody>
      </table>
      <button id = "forward-todo"onClick={()=>navigate("/create")}>Create Student</button>
    </div>
  )
}

export default Get
