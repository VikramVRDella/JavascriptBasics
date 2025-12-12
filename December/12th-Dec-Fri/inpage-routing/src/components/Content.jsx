import React from 'react'
import { useNavigate } from 'react-router-dom'
const Content = () => {
    const navigate = useNavigate();
  return (
    <div>
      <h2>Content Page</h2>
      <p>This is a Content Page</p>
      <button onClick={()=> navigate("/about")}>Next Page</button>
      <button onClick={()=> navigate("/")}>Go Back</button>
    </div>
  )
}

export default Content
