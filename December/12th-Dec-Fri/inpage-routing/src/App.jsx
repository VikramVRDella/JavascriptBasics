import React from 'react'
import Home from './components/Home'
import About from './components/About'
import Content from './components/Content'
import {Routes,Route} from 'react-router-dom'
const App = () => {
  return (
    <div>
      <Routes>
        <Route path="/" element={<Home></Home>}/>
        <Route path="/content" element={<Content></Content>}/>
        <Route path="/about" element={<About></About>}/>
      </Routes>
    </div>
  )
}

export default App
