import React from 'react'
import {useState,useEffect} from 'react'
import axios from 'axios'
import { useNavigate } from 'react-router-dom'

const Get = () => {
  const navigate = useNavigate()
    const[data,setData] = useState([])
    useEffect(()=>{
        axios.get("http://localhost:8000/todo/fetch")
        .then(res =>{
            setData(res.data)
        })
        .catch(err =>{
            console.log(err)
        })
    },[])
  return (
    <div>
      <h3>Fetching Todo</h3>
      <table>
        <thead>
          <tr>
            <th>id</th>
            <th>title</th>
            <th>description</th>
            <th>Completed</th>
          </tr>         
        </thead>
        <tbody>
            {
              data.map((todo)=>(
                <tr key={todo.id}>
                  <td>{todo.id}</td>
                  <td>{todo.title}</td>
                  <td>{todo.description}</td>
                  <td><input type="checkbox" checked={todo.completed}/></td>
                </tr>
              ))
            }
        </tbody>
      </table>
      <button id = "forward-todo"onClick={()=>navigate("/create")}>Create Todo</button>
    </div>
  )
}

export default Get
