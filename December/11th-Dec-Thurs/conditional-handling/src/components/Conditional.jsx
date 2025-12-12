import React from 'react'
import { useState } from 'react'
const Conditional = () => {
    const [admin,setAdmin]=useState(true)
    let result = admin ===true? <h1>You are Admin User</h1>:<h2>Normal User</h2>
  return (
    <div>
      {
        result
      }
      <button onClick={()=>setAdmin(!admin)}>click me</button>
    </div>
  )
}

export default Conditional
