import { useCallback, useEffect, useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Navbar from './Navbar'
import { useAuth, useUser } from '@clerk/clerk-react'

function App() {
  const [count, setCount] = useState(0)
  const {user} = useUser()
  const {userId, getToken} = useAuth()

  const handleSendUserDataToTheBackend = useCallback(async ()=>{
    const token = await getToken()
    const requestHeaders = {
      "Authorization": `Bearer ${token}`
    }
    console.log(user, userId)
    // call Django / FastAPI backend
    const response = await fetch("http://localhost:8888/api/hello/", {
      headers: requestHeaders
    })
    if (response.ok) {
      const data = await response.json()
      console.log(data)
    } else {
      const text = await response.text()
      console.log(text)
    }
  }, [user, userId, getToken])



  

  return (
    <>
      <Navbar />
      <div>
        <a href="https://vite.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>Vite + React + Clerk</h1>
      <button onClick={handleSendUserDataToTheBackend}>Trigger Backend</button>
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button>
        <p>
          Edit <code>src/App.jsx</code> and save to test HMR
        </p>
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
    </>
  )
}

export default App
