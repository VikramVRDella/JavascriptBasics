import React from 'react'
import Home from './components/Home.jsx'
import About from './components/About.jsx'
import Content from './components/Content.jsx'
import {Routes, Route} from 'react-router-dom'
import Navbar from './components/Navbar.jsx'

const App = () => {
  return (
    <div>
      <Navbar></Navbar>
      <Routes>
        <Route path="/" element={<Home></Home>}/>
        <Route path="/content" element={<Content></Content>}/>
        <Route path="/about" element={<About></About>}/>
      </Routes>
    </div>
  )
}

export default App
