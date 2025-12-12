import React from 'react'
import {useNavigate} from 'react-router-dom'
const Home = () => {
const navigate = useNavigate();

  return (
    <div>
      <h2>Home Page</h2>
      <p>This is a home page</p>
      <button onClick={()=> navigate("/content")}>Next Page</button>
    </div>
  )
}

export default Home
