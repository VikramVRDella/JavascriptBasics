import React from 'react'
import {NavLink} from 'react-router-dom'
const Navbar = () => {
  return (
    <nav>
        <ul>
            <li>
                <NavLink to={"/"}>Home</NavLink>
                <NavLink to={"/content"}>Content</NavLink>
                <NavLink to={"/about"}>About</NavLink>
            </li>
        </ul>
    </nav>
  )
}

export default Navbar
