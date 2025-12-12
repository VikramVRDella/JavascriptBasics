import React from 'react'
import Title from './Title'

const Home = () => {
  return (
    <div>
      <h1>Sample App</h1>
      <Title framework={"React"} language={"Javascript"}>Testing</Title>
      <Title framework={"Angular"} language={"Typescript"}>Testing</Title>
    </div>
  )
}

export default Home
