import React from 'react'

const Title = ({framework,language,children}) => {
  return (
    <div>
      {framework} Application using {language} and this is {children}
    </div>
  )
}

export default Title
