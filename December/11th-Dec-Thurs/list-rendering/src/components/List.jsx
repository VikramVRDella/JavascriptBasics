import React from 'react'

const List = () => {
    // let numbers = [43,23,45,67]
    // let res=numbers.map(number=><h2>{number}</h2>)
    let fruits=['Apple','Orange','Grapes']
    let result = fruits.map((fruit,index)=> {
        return (
            <div key={index}>
                <h2>{fruit}</h2> 
                <p>This is a Fruit</p>
            </div>
        )
    })
    let students=[
        {
            id:1,
            name:"Student1"
        },
        {
            id:2,
            name:"Student2"
        }
    ]
    let Students = students.map(student=><h1 key={student.id}>{student.name}</h1>)
  return (
    <div>
      {Students}
      {result}
    </div>
  )
}

export default List
