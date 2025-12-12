import React from 'react'
import Title from './Title'


const Home = () => {
    const mesage =()=>{
        alert("button click")
        console.log("button clicked")
    }
    const LogData=(a,b)=>{
        console.log(a)
        console.log(b)
    }
  return (
    <div>
      <Title framework={"React"} language={"Javascript"}>testing</Title>
      <button onClick={mesage}>Click Me</button>
      <button onClick={()=>LogData(20,30)}>Click</button>
    </div>
  )
}

export default Home
