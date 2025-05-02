
import {
    SignedIn,
    SignedOut,
    UserButton,
  } from '@clerk/nextjs'
import Link from 'next/link'

export default function Navbar () { 


    return  <header className="flex justify-end items-center p-4 gap-4 h-16">
    <SignedOut>
      <Link href='/login'>Login</Link>
      <Link href='/register'>Register</Link>
    </SignedOut>
    <SignedIn>
      <UserButton />
    </SignedIn>
  </header>
}