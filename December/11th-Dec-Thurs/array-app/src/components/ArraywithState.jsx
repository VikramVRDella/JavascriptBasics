import React from 'react'
import { useState } from 'react'
const ArraywithState = () => {
    const [language,setLanguage]=useState("Python")
    const [fruits_one,setFruits_one]=useState('')
    const [fruits,setFruits] =useState(["Apple", "Orange"])
    let fruits_data = fruits.map((fruit,index)=><h1 key ={index}>{fruit}</h1>)
  return (
    <div>
      {language}
      <br />
      <button onClick={()=>setLanguage(language==="Python"?"JavaScript":"Python")}>Click Me</button>
      {fruits_data}
      <input type="text" name="fruit" value={fruits_one} onChange={(event)=>setFruits_one(event.target.value)}/> <br /> <br />
      <button onClick={()=>setFruits([...fruits,fruits_one])}>Add fruit</button>
    </div>
  )
}

export default ArraywithState
