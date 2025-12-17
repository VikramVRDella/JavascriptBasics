import React from 'react'
import Home from './Components/Home.jsx'
import Create from './Components/Create.jsx'
import {Routes,Route} from 'react-router-dom'
import Navigate from './Components/Navigate.jsx'
const App = () => {
  return (
    <div>
        <Navigate></Navigate>
      <nav>
        <Routes>
        <Route path='/student/get' element={<Home/>}/>
        <Route path='/student/create' element={<Create/>}/>
        </Routes>
      </nav>
    </div>
  )
}

export default App
