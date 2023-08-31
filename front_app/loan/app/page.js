import FormPage from "./formcomponent"

async function getData() {
  try {
    const res = await fetch(
      process.env.NEXT_PUBLIC_API_URL + "fields/",
      { next: { revalidate: 30 }}
    )
    if (!res.ok) {
      return []
    }
    return res.json()
  } catch (error) {
    return []
  }
}

export default async function Page() {
  const extraFields = await getData()

  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      <FormPage extraFields={extraFields}/>
    </main>
  )
}