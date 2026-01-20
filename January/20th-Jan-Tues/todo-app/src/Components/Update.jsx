import axios from 'axios'
import React, { useEffect, useState } from 'react'
import { useNavigate, useParams } from 'react-router-dom'

const Update = () => {
    const navigate = useNavigate()
    const [id,setId] = useState(null)
    const [tit,setTit] = useState('')
    const [desc,setDesc] = useState('')
    const [com,setCom] = useState(false)
    
    const getinfo=(event)=>{
        event.preventDefault();
        axios
        .get(`http://localhost:8000/todo/fetch/${id}`)
        .then((res)=>{
            setTit(res.data.title)
            setDesc(res.data.description)
            setCom(res.data.completed == 0 ? false : true)
        })
        .catch((err)=>{
            console.log(err)
        })
    }
    const updateTodo=(event)=>{
        event.preventDefault();
        const data ={
            title : tit,
            description : desc,
            completed : com
        }
        axios.put(`http://localhost:8000/todo/update/${id}`,data)
        .then((res)=>{
            console.log(res.data)
            navigate('/')
        })
        .catch((err)=>{
            console.log(err)
        })
    }
  return (
    <div>
        <h3>Updating Todo</h3>
        <form onSubmit={(event)=>updateTodo(event)}>
            <div>
                <label>ID : <input type="text" id='todo-id' onChange={(e)=>setId(e.target.value)}/> <button id="submit" onClick={(e)=>getinfo(e)}>fetch</button></label>
            </div>
            <div>
                <label>Title : <input type="text" value={tit} id= 'title'onChange={(e)=>setTit(e.target.value)} /></label>
            </div>
            <div>
                <label>Description : <input type="text" id = 'desc' value={desc} onChange={(e)=>setDesc(e.target.value)} /></label>
            </div>
            <div>
                <label>Completed : <input type="checkbox" value={com == 0 ? false:true} onChange={(e)=>setCom(e.target.checked)} /></label>
            </div>
            <div>
                <button id='submit'>Update</button>
            </div>
        </form>
      <div id='button-div'>
        <button id="back-todo" onClick={()=>navigate('/create')}>Back</button>
        <button id="forward-todo" onClick={()=>navigate('/delete')}>Delete Todo</button>
      </div>
    </div>
  )
}

export default Update
