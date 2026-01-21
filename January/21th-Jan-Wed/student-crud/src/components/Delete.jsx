import axios from 'axios'
import React from 'react'
import { useState } from 'react'
import { useNavigate } from 'react-router-dom'

const Delete = () => {
    const navigate = useNavigate()
    const [roll,setRoll] = useState(0)
    const deleteStudent = (event) =>{
        event.preventDefault();
        axios.delete(`http://localhost:8000/students/delete/${roll}`)
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
        <h3>Deleting Students</h3>
        <form onSubmit={(event)=>deleteStudent(event)}>
            <div>
                <label>Roll No : <input type="text" id='todo-id' onChange={(e)=>setRoll(e.target.value)}required/></label>
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
