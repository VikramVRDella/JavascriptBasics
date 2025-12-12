import React from 'react'
import Secondary from './Secondary'
const Primary = () => {
    const Person = ()=>{
        console.log("Hello this is Primary Function")
    }
  return (
    <div>
      <Secondary NamePerson={Person}></Secondary>
    </div>
  )
}

export default Primary
