"use client"

import { useAuth } from "@clerk/nextjs";
import { useRef, useState } from "react"

const DJANGO_API_BACKEND = "http://localhost:8888/api/posts/"
const FASTAPI_API_BACKEND = "http://localhost:8002/api/posts/"

export default function PostCreateForm({mutate}) {
    const { getToken } = useAuth();
    const [data, setData] = useState('')
    const formRef = useRef(null)

    const handleSubmit = async event => {
        event.preventDefault()
        const token = await getToken()
        const myFormData = new FormData(formRef.current)
        const myFormDataObject = Object.fromEntries(myFormData)
        const myFormDataAsJson = JSON.stringify(myFormDataObject)
        const headers = {
            "Authorization": `Bearer ${token}`,
            "Content-Type": "application/json"
        }
        const httpOptions = {
            method: "POST",
            headers: headers,
            body: myFormDataAsJson
        }
        const response = await fetch(DJANGO_API_BACKEND, httpOptions)
        if (response.ok) {
            const responseData = await response.json()
            setData(responseData)
            formRef.current.reset()
            if (mutate) {
                mutate()
            }
        } else {
            const rText = await response.text()
            console.log(rText)
        }
        

    }


    return <>
        {data && JSON.stringify(data)}
        <form ref={formRef} onSubmit={handleSubmit}>
            <textarea name='content' required placeholder="Your content"
            className='border rounded w-full border-gray-300 p-3'
            >

            </textarea>
            <button type='submit'>Send</button>
        </form>
    
    </>

}