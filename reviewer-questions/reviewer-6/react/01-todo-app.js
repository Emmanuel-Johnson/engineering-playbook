import React from 'react';
import { useState } from 'react'

function App() {
  
  const [todos, setTodos] = useState([])

  const [todo, setTodo] = useState("")
 
  function handleSubmit() {
    setTodos([...todos, todo])
    setTodo("")
  }

  return (
    <>
      <input onChange={(e) => setTodo(e.target.value)} value={todo}></input>
      <button onClick={handleSubmit}>ADD</button>
      {todos.map((todo, id) => <p key={id}>{todo}</p>)}
    </>
  )
}

export default App
