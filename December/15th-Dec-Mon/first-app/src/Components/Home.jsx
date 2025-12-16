import React from 'react'
import { useState } from 'react'


const Home = () => {
    const [color,setcolor] = useState("Red")
  return (
    <div>
      <h1>My Favorite Color is {color}!</h1>
      <button onClick={()=>setcolor("Pink")}>Pink</button>
      <button onClick={()=>setcolor("Blue")}>blue</button>
      <button onClick={()=>setcolor("Yellow")}>Yellow</button>
      <button onClick={()=>setcolor("Red")}>Red</button>
    </div> 
  )
}

export default Home
