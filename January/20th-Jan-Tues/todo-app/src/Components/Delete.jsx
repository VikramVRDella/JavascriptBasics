import axios from 'axios'
import React from 'react'
import { useState } from 'react'
import { useNavigate } from 'react-router-dom'

const Delete = () => {
    const navigate = useNavigate()
    const [id,setId] = useState(0)
    const deleteTodo = (event) =>{
        event.preventDefault();
        axios.delete(`http://localhost:8000/todo/delete/${id}`)
        .then((res)=>{
            alert(res.data)
            navigate('/')
        })
        .catch((err)=>{
            console.log(err)
        })
    }
  return (
    <div>
        <h3>Delete Todo</h3>
        <form onSubmit={(event)=>deleteTodo(event)}>
            <div>
                <label>ID : <input type="text" id='todo-id' onChange={(e)=>setId(e.target.value)}/></label>
                <button id="submit">Delete</button>
            </div>
        </form>
      <div id='button-div'>
        <button id="back-todo" onClick={()=>navigate('/update')}>Back</button>
        <button id="forward-todo" onClick={()=>navigate('/')}>Home</button>
      </div>
    </div>
  )
}

export default Delete
