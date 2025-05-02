import Link from 'next/link'


export default function DashboardLayout({ children }) {
  return (
    <div className="flex h-screen">
    {/* Sidebar */}
    <aside className="w-64 bg-gray-800 text-white p-4">
      <nav>
        <ul className="space-y-2">
          <li>
            <Link href="/dashboard" className="block py-2 px-4 hover:bg-gray-700 rounded">
              Dashboard
            </Link>
          </li>
          <li>
            <Link href="/posts" className="block py-2 px-4 hover:bg-gray-700 rounded">
              Posts
            </Link>
          </li>
          <li>
            <Link href="/contact" className="block py-2 px-4 hover:bg-gray-700 rounded">
              Contact
            </Link>
          </li>
        
        </ul>
      </nav>
    </aside>

    {/* Main Content */}
    <main className="flex-1 p-8 bg-gray-100">
      {children}
    </main>
  </div>
  )
}