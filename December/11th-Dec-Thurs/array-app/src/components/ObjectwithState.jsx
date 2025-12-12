import React from 'react'
import { useState } from 'react'

const ObjectwithState = () => {
    const [data,setData] = useState({
        firstname:"",
        lastname:""
    })
  return (
    <div>
      {JSON.stringify(data)}
      <form>
        <label htmlFor="">First Name</label>
        <input type="text" value={data.firstname} onChange={(event)=>setData({...data,firstname:event.target.value})}/>
        <label htmlFor="">Last Name</label>
        <input type="text" value={data.lastname} onChange={(event)=>setData({...data,lastname:event.target.value})}/>
        <button onSubmit={()=>setData(...data,firstname,lastname)}>submit</button>
      </form>
    </div>
  )
}

export default ObjectwithState
