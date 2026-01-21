import axios from 'axios'
import React, { useEffect, useState } from 'react'
import { useNavigate, useParams } from 'react-router-dom'

const Update = () => {
    const navigate = useNavigate()
    const [roll,setRoll] = useState(null)
    const [name,setName] = useState('')
    const [age,setAge] = useState(null)
    
    const getinfo=(event)=>{
        event.preventDefault();
        axios
        .get(`http://localhost:8000/students/get/${roll}`)
        .then((res)=>{
            setName(res.data.name)
            setAge(res.data.age)
            alert("Details Fetched")
        })
        .catch((err)=>{
            console.log(err)
        })
    }
    const updateStudents=(event)=>{
        event.preventDefault();
        const data ={
            roll:roll,
            name:name,
            age:age
        }
        axios.put(`http://localhost:8000/students/update/${roll}`,data)
        .then((res)=>{
            console.log(res.data)
            alert("Student Updated")
            navigate('/')
        })
        .catch((err)=>{
            console.log(err)
        })
    }
  return (
    <div>
        <h3>Updating Students</h3>
        <form onSubmit={(event)=>updateStudents(event)}>
            <div>
                <label>Roll No : <input type="text" id='todo-id' onChange={(e)=>setRoll(e.target.value)}/> <button id="submit" onClick={(e)=>getinfo(e)}>fetch</button></label>
            </div>
            <div>
                <label>Name : <input type="text" value={name} id= 'title'onChange={(e)=>setName(e.target.value)} /></label>
            </div>
            <div>
                <label>Age : <input type="text" id = 'desc' value={age} onChange={(e)=>setAge(e.target.value)} /></label>
            </div>
            <div>
                <button id='submit'>Update</button>
            </div>
        </form>
      <div id='button-div'>
        <button id="back-todo" onClick={()=>navigate('/create')}>Back</button>
        <button id="forward-todo" onClick={()=>navigate('/delete')}>Delete Students</button>
      </div>
    </div>
  )
}

export default Update
