import './globals.css'


export const metadata = {
  title: 'Loan App',
  description: 'LFG Challenge Django Consultant',
}

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  )
}
