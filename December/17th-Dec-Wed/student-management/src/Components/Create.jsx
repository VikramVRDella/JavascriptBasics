import React, { useState } from 'react'
import axios from 'axios'

const Create = () => {
    const [roll_no, setRoll] = useState('')
    const [name, setName] = useState('')
    const[age , setAge]  =  useState('')

    const handleSubmit=()=>{
        const StudentData = {roll_no,name,age}
        axios.post("http://127.0.0.1:8000/student/create",StudentData)
        .then(alert("Student Created"))
        .catch(err => console.log(err))
    }

  return (
    <div id='create-container'>
      <form onSubmit={handleSubmit}>
        <h3>Create Student</h3>
        <label>
            Roll No
        </label>
        <input type="number" onChange={(e)=>setRoll(e.target.value)} required/>
        <label>
            Name
        </label>
        <input type="text" onChange={(e)=>setName(e.target.value)} required/>
        <label>
            Age
        </label>
        <input type="number" onChange={(e)=>setAge(e.target.value)} required/>
        <input type="submit" />
      </form>
    </div>
  )
}

export default Create
