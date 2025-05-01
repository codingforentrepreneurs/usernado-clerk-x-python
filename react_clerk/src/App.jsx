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
  const [displayData, setDisplayData] = useState()

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
      setDisplayData(data)
    } else {
      const text = await response.text()
      setDisplayData(text)
    }
  }, [user, userId, getToken])


  const callFastAPIBackend = useCallback(async ()=>{
    const token = await getToken()
    const requestHeaders = {
      "Authorization": `Bearer ${token}`
    }
    console.log(user, userId)
    // call Django / FastAPI backend
    const response = await fetch("http://localhost:8002/", {
      headers: requestHeaders
    })
    if (response.ok) {
      const data = await response.json()
      setDisplayData(data)
    } else {
      const text = await response.text()
      setDisplayData(text)
    }
  }, [user, userId, getToken])

  

  return (
    <>
      <Navbar />
      <h1>Vite + React + Clerk</h1>

      <div>
        {displayData && JSON.stringify(displayData)}
      </div>
      <div>
      <button onClick={handleSendUserDataToTheBackend}>Call Django Backend</button>

      <button onClick={callFastAPIBackend}>Call FastAPI Backend</button>
      </div>
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
