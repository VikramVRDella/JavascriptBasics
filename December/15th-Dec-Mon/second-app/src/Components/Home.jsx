import React, { useState } from 'react'
import { useEffect } from 'react'

const Home = () => {
    const [counter,setCounter]=useState(0)
    useEffect(()=>{
        setTimeout(()=>{
            setCounter((counter)=>counter+1)
        },1000)
    })
  return (
    <div>
      <h1>I've rendered {counter}! times</h1>
    </div>
  )
}

export default Home
