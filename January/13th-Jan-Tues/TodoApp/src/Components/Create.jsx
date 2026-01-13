import React from 'react'
import {useState} from 'react'

const Create = () => {
    const[title,setTitle] = useState('');
    const[description,setDescription] = useState('');
    const[completed,setCompleted] = useState(false);

    return (
    <div>
      <h2>Create Todo</h2>
        <form action="">
        <div>
            <label htmlFor="">Title: </label>
            <input type="text" />
        </div>
       <div>
            <label htmlFor="">Description: </label>
            <input type="text" name="" id="" />
       </div>
       <div>
        <label htmlFor="">Completed: </label>
        <input type="radio" name='Completed-yes'/>
        <label htmlFor="">yes</label>
        <input type="radio" name="Completed-no" id="" checked />
        <label htmlFor="">no</label>
       </div>
       <div>
        <button>submit</button>
       </div>
      </form>
    </div>
  )
}

export default Create
