import React from 'react'

const Title = ({framework,language,children}) => {
  return (
    <div>
      {framework} Appplication using {language} and this is {children}
    </div>
  )
}

export default Title
