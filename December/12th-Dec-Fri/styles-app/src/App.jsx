import React from 'react'
import Home from './components/Home'
import Login from './components/Login'
import {Routes, Route} from 'react-router-dom'

const App = () => {
  return (
    <div>
      <Routes>
        <Route path='/' element={<Login></Login>}/>
        <Route path='/home' element={<Home></Home>}/>
      </Routes>
    </div>
  )
}

export default App
