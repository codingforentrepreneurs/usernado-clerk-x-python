"use client"

import { SignUp, useUser } from '@clerk/nextjs'

export default function RegisterPage() {
  const {user} = useUser()
  if (!user) {
    return <SignUp />
  }
  return <h1>You are already signed up and logged in.</h1>
}