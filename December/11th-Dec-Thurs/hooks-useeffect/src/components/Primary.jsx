import React from 'react'
import { useState,useEffect } from 'react'
import Secondary from './Secondary'

const Primary = () => {
    const [admin,setAdmin] = useState(true)
    const [greeting,setGreeting]=useState('Hello')
    const result = admin === true ? <h1>{greeting} You are Admin</h1> : <h2>{greeting} You are a Normal User</h2>
    const ChangeValue=()=>{
        setAdmin(!admin)
        setGreeting(greeting==="Hello"?"Hi":"Hello")
    }
    useEffect(()=>{
        console.log("React App")
    },[])
    useEffect(()=>{
        console.log("Hello User")
    },[admin])
  return (
    <div>
      {result}
      <Secondary></Secondary> <br />
      <button onClick={ChangeValue}>Click Me</button>
    </div>
  )
}

export default Primary
