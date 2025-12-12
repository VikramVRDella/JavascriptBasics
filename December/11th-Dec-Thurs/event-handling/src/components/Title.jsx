import React from 'react'

const Title = ({framework,language,children}) => {
  return (
    <div>
        <h1>Sample App</h1>
      {framework} Application using {language} and this is {children}
    </div>
  )
}

export default Title
