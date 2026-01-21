import React from 'react'
import axios from 'axios'
import {useState} from 'react'
import { useNavigate } from 'react-router-dom'

const Create = () => {
    const navigate = useNavigate()
    const [roll,setRoll] = useState(0)
    const [name,setName] = useState('')
    const [age,setAge] = useState(0)
   
    const postData = (event) =>{
        event.preventDefault();
        const data ={
            roll:roll,
            name:name,
            age:age
        };
        axios.post("http://localhost:8000/students/create",data)
        .then((res)=>{
            console.log(res.data)
            alert("Student Created")
            navigate("/")
        }
        )
        .catch((err)=>{
            console.log(err)
        })
    
    };
   
  return (
    <div>
      <h3>Creating Student</h3>
      <form onSubmit={(event)=>postData(event)}>
        <div>
            <label>Roll No: <input type="text" id="title" onChange={(event)=>setRoll(event.target.value)}/></label>
        </div>
        <div>
            <label>Name: <input type="text" id="desc" onChange={(event)=>setName(event.target.value)}/></label>
        </div>
        <div>
            <label>Age: <input type="text" id="desc" onChange={(event)=>setAge(event.target.value)}/></label>
            
        </div>
        <div>
            <input type="submit" id='submit'/>
        </div>
      </form>
      <div id='button-div'>
        <button id="back-todo" onClick={()=>navigate('/')}>Back</button>
        <button id="forward-todo" onClick={()=>navigate('/update')}>Update Students</button>
      </div>
    </div>
  )
}

export default Create
