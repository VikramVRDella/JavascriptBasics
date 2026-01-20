import {useState,useEffect} from 'react'
import axios from 'axios'

const Get = () => {
    const [data,setData] = useState([])

    useEffect(()=>{
        axios.get("http://localhost:8000/todo/fetch")
        .then((response)=>{
            setData(response.data)
        })
        .catch((err)=>{
            console.log(err)
        })
    },[])

  return (
    <div>
     <table>
        <thead>
            <th>
                id
            </th>
            <th>
                title
            </th>
            <th>
                description
            </th>
            <th>
                Completed
            </th>
        </thead>
        <tbody>
            {data.map((todo)=>(
                <tr key={todo.id}>
                    <td>{todo.id}</td>
                    <td>{todo.title}</td>
                    <td>{todo.description}</td>
                    <td>{todo.completed == 0  ? "Not Done" : "Done"}</td>
                </tr>
            ))}
        </tbody>
        
     </table>
    </div>
  )
}

export default Get
