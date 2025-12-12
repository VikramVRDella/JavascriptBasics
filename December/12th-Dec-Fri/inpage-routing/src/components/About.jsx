import React from 'react'
import { useNavigate } from 'react-router-dom'
const About = () => {
    const navigate = useNavigate();
  return (
    <div>
      <h2>About Page</h2>
      <p>This is a About Page</p>
      <button onClick={()=> navigate("/content")}>Go Back</button>
    </div>
  )
}

export default About
