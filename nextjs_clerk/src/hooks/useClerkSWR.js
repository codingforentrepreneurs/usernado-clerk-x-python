"use client"

import { useAuth } from "@clerk/nextjs";
import useSWR from 'swr'
 

export default function useClerkSWR(url) {
    const { getToken } = useAuth();

    const fetcher = async (...args) => {

        const token = await getToken()
        const headers = {
            "Authorization": `Bearer ${token}`,
            "Content-Type": "application/json"
        }
        return fetch(...args, {headers: headers}).then(res => res.json())
    }
    return useSWR(url, fetcher)
}