"use client"

import PostCreateForm from "@/components/postsCreateForm";
import useClerkSWR from "@/hooks/useClerkSWR";

const DJANGO_API_BACKEND = "http://localhost:8888/api/posts/"
export default function PostsPage(){
    const {data, isLoading, error, mutate} = useClerkSWR(DJANGO_API_BACKEND)
    if (isLoading) {
        return <h1>Loading...</h1>
    }
    if (error) {
        return <div>Error happend</div>
    }
    const results = data && data.results || []

    return <>
        <h1>Hello World</h1>
        <PostCreateForm mutate={mutate} />
        <div className='space-y-4'>
        {results.map((data,idx)=>{

            return <div className='border px-2 py-4 rounded' key={`key-${idx}`}>
                {data.content}
            </div>
        })}
        </div>
    </>
}