import React from 'react'
import { Route,Routes } from 'react-router-dom'
import Get from './Components/Get'
import Create from './Components/Create'
import Update from './Components/Update'
import Delete from './Components/Delete.jsx'

const App = () => {
  return (
    <div>
      <h2>Student CRUD</h2>
      <Routes>
        <Route path='/' element={<Get/>}></Route>
        <Route path='/create' element={<Create/>}></Route>
        <Route path='/update' element={<Update/>}></Route>
        <Route path='/delete' element={<Delete/>}></Route> 2
      </Routes>
    </div>
  )
}

export default App
