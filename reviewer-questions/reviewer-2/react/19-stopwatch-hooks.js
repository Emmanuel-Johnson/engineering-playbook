import React, { useState, useEffect } from 'react';

function App() {
  
  const [flag, setFlag] = useState(false)

  const [count, setCount] = useState(0)

  useEffect(() => {
    let interval

    if (flag) {
      interval = setInterval(() => {
        setCount((prev) => prev + 1)
      }, 1000)
    }
    
    return () => clearInterval(interval)

  }, [flag])

  return (
    <div>
      <h1>{count}</h1>
      <button onClick={() => setFlag(prev => !prev)}>{flag ? "Stop" : "Start"}</button>
    </div>
  );
}

export default App;