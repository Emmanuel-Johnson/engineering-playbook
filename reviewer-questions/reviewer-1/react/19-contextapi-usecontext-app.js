import React, { useContext, createContext } from 'react'

const NameContext = createContext()

function Child() {
  const name = useContext(NameContext)

  console.log(name)

  return <h1>{name}</h1>
}

function App() {
  return (
    <NameContext.Provider value="Emmanuel">
      <Child />
    </NameContext.Provider>
  )
}

export default App