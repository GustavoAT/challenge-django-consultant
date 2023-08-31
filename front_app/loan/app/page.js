'use client'
import React, { useState } from "react"

export default function Page() {
  const [formData, setFormData] = useState({
    name: "",
    document: "",
    extra_fields: [],
  });

  const [formSuccess, setFormSuccess] = useState(false)
  const [formSuccessMessage, setFormSuccessMessage] = useState("")

  const handleInput = (e) => {
    const fieldName = e.target.name;
    const fieldValue = e.target.value;

    setFormData((prevState) => ({
      ...prevState,
      [fieldName]: fieldValue
    }));
  }

  const submitForm = (e) => {
    e.preventDefault()

    const formURL = process.env.NEXT_PUBLIC_API_URL;

    fetch(formURL + "request/", {
      method: "POST",
      body: JSON.stringify(formData),
      headers: {
        "accept": "application/json",
        "Content-Type": "application/json",
      },
    }).then((response) => response.json())
    .then((data) => {
      setFormData({ 
        name: "", 
        document: "", 
        extra_fields: [],
      })
      setFormSuccess(true)
      setFormSuccessMessage(data.message)
    })
  }

  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      <div>
        <h1>Solicitar empréstimo</h1>
        {formSuccess ? 
          <div>{formSuccessMessage}</div> 
          : 
          <form method="POST" onSubmit={submitForm}>
            <div>
              <label>Nome</label>
              <input type="text" name="name" onChange={handleInput} value={formData.name} />
            </div>

            <div>
              <label>Documento</label>
              <input type="text" name="document" onChange={handleInput} value={formData.email} />
            </div>
            <button type="submit">Solicitar</button>
          </form>
        }
      </div>
    </main>
  )
}