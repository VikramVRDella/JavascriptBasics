import React from 'react'
import { cloneElement } from 'react'
import { useState } from 'react'
const User = () => {
    const [username,setusername] = useState('')
    const [password,setpassword] = useState('')

    const UserData = (event)=>{
        event.preventDefault()

        const collected_data ={
            name:username,
            user_pass:password
        }

        console.log(collected_data)
    }
  return (
    <div>
      <form onSubmit={event => UserData(event)}>
        <label htmlFor="">Username: </label>
        <input type="text" name="username" id="username" value={username} onChange={event => setusername(event.target.value)}/><br />
        <label htmlFor="">Password: </label>
        <input type="password" name="password" id="password" value={password} onChange={event => setpassword(event.target.value)}/><br />
        <input type="submit" name="submit" id="submit"/>
      </form>
    </div>
  )
}

export default User
