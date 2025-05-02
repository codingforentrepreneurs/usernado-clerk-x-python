/** @type {import('next').NextConfig} */
const nextConfig = {
    async redirects() {
    return [
        {
            source: '/console(.*)',
            destination: '/dashboard',
            permanent: true,
            },
        {
        source: '/signin',
        destination: '/login',
        permanent: true,
        },
        {
        source: '/sign-in',
        destination: '/login',
        permanent: true,
        },
        {
        source: '/sign-up',
        destination: '/register',
        permanent: true,
        },
        {
        source: '/signup',
        destination: '/register',
        permanent: true,
        },
    ]
    },
};

export default nextConfig;
