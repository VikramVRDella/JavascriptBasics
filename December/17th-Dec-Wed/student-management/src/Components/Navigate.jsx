import React, { useState } from 'react'
import { useNavigate } from 'react-router-dom'
const Navigate = () => {
    const navigate = useNavigate()
    const [heading,setHeading] = useState('Student Management System')
  return (
    <div>
      <nav>
        <ul>
            <li>
                <h2>{heading}</h2>
            </li>
            <li>
             <button onClick={()=>{ navigate('/student/get');setHeading('Student Management System')}}>Home</button> 
  
            </li>
            <li>
                <button onClick={()=>{navigate("/student/create"),setHeading('Create Student')}}>Create</button>
            </li>
            <li>
                <button onClick={()=>{navigate("/student/update"),setHeading('Update Student')}}>Update</button>
            </li>
            <li>
                <button onClick={()=>{navigate("/student/delete"),setHeading('Delete Student')}}>Delete</button>
            </li>
        </ul>
      </nav>
    </div>
  )
}

export default Navigate
