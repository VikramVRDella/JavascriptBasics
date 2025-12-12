import React from 'react'
import Title from './Title'
import { useState } from 'react'
const Home = () => {
    const[frame,setframe]=useState("React")
    const[lang, setLang]=useState("Javascript")

    const ChangeValue = ()=>{
        setframe("Angular")
        setLang("TypeScript")
        alert("Value Changed")
    }
    
  return (
    <div>
      <h1>Sample App</h1>
      <Title framework={frame} language={lang}>testing</Title>
      <br />
      <button onClick={()=>setframe("Django")}>Change Framework</button>&ensp;
      <button onClick={()=> setLang("Python")}>Change Language</button>&ensp;
      <button onClick={ChangeValue}>Click me</button>&ensp;
    </div>
  )
}

export default Home
