import React from 'react'
import axios from 'axios'
import {useState} from 'react'
import { useNavigate } from 'react-router-dom'

const Create = () => {
    const navigate = useNavigate()
    const [tit,setTit] = useState('')
    const [desc,setDesc] = useState('')
    const [com,setCom] = useState(false)
   
    const postData = (event) =>{
        event.preventDefault();
        const data ={
            title:tit,
            description:desc,
            completed:com
        };
        axios.post("http://localhost:8000/todo/create",data)
        .then((res)=>{
            console.log(res.data)
        }
        )
        .catch((err)=>{
            console.log(err)
        })
    
    };
   
  return (
    <div>
      <h3>Creating Todo</h3>
      <form onSubmit={(event)=>postData(event)}>
        <div>
            <label>Title: <input type="text" id="title" onChange={(event)=>setTit(event.target.value)}/></label>
        </div>
        <div>
            <label>Description: <input type="text" id="desc" onChange={(event)=>setDesc(event.target.value)}/></label>
        </div>
        <div>
            <label>Completed: <input type="checkbox" id= 'checkbox'onChange={(event)=>setCom(event.target.checked)}/></label>
            
        </div>
        <div>
            <input type="submit" id='submit'/>
        </div>
      </form>
      <div id='button-div'>
        <button id="back-todo" onClick={()=>navigate('/')}>Back</button>
        <button id="forward-todo" onClick={()=>navigate('/update')}>Update Todo</button>
      </div>
    </div>
  )
}

export default Create
