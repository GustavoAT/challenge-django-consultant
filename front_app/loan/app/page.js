import FormPage from "./formcomponent"

async function getData() {
  const res = await fetch(process.env.NEXT_PUBLIC_API_URL + "fields/")
  if (!res.ok) {
    throw new Error('Failed to fetch data')
  }
  return res.json()
}

export default async function Page() {
  const extraFields = await getData()

  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      <FormPage extraFields={extraFields}/>
    </main>
  )
}