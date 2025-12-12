import React from 'react'
import {useNavigate} from 'react-router-dom' 



const Login = () => {
    const navigate = useNavigate()
    return (
    <div id='login-card'> 
        <form>
            <h1>Login</h1>
            {/* <label>Username :</label> */}
            <div>
                <input type="text" name="username" id="username-input" placeholder='Enter Username' required/>
            </div>
            {/* <label>Password :</label> */}
            <div>
                <input type="password" name="password" id="password-input" placeholder='Enter Password' required/>
            </div>
            <button id= "login-button" onClick={()=> navigate("/home")}>Login</button>
            <div id="anchor-field">
                <p id="reset-id">Forgot Password ? <a href="#">Reset Password</a></p>
                <p id = "create-id">Create Account ? <a href="#">Sign up</a></p>
            </div>

        </form>
    </div>
  )
}

export default Login
