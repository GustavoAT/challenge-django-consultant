'use client'
import React, { useState } from "react"

export default function FormPage({extraFields}) {
  const [formData, setFormData] = useState({
    name: "",
    document: "",
    extra_fields: extraFields.map((field) => {
      return {loan_request_field: field.id, value: ""}
    }),
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

  const handleInputExtra = (value, index, fieldId) => {
    const fieldName = "extra_fields";
    let extra_fields2 = formData[fieldName];
    extra_fields2[index] = {loan_request_field: fieldId, value: value}

    setFormData((prevState) => ({
      ...prevState,
      [fieldName]: extra_fields2
    }));
  }

  const submitForm = (e) => {
    e.preventDefault()

    const formURL = process.env.NEXT_PUBLIC_API_URL

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
    <div>
      {!formSuccess && <h1>Solicitar empréstimo</h1>}
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
          {extraFields.map((field, index) => {
            return (
              <ExtraInput 
                key={field.id}
                field={field}
                value={formData[index]?.value}
                index={index}
                onChange={handleInputExtra}
              />
            )
          })}

          <button type="submit">Solicitar</button>
        </form>
      }
    </div>
  )
}

function ExtraInput({field, value, index, onChange}){
  const handlechange = (e) => {
    onChange(e.target.value, index, field.id)
  }
  return (
    <div>
      <label>{field.name}</label>
      <input type="text" onChange={handlechange} name={field.name} value={value} />
    </div>
  )
}