function main() {
  const form_signup = document.getElementById("form-signup")

  form_signup.onsubmit = async (event) => {
    event.preventDefault()
    const nome = get_element_value("nome")
    const email = get_element_value("email")
    const usuario = get_element_value("usuario")
    const senha = get_element_value("senha")
    const confirmacao_senha = get_element_value("confirmacao_senha")

    const data = { nome, email, usuario, senha, confirmacao_senha }

    const url = "http://localhost:8000/auth/signup2"
    const opcoes = {
      method: "POST",
      body: JSON.stringify(data),
      headers: {
        "Content-Type": "application/json"
      }
    }

    const response = await fetch(url, opcoes)

    if (!response.ok) {
      const result_data = await response.json()
      console.error(result_data)
      alert(`Error: ${result_data["detail"]}`)
    } else {
      alert("Cadastro realizado com sucesso!\nFavor faça login!")
      window.location.replace("/login.html")
    }
  }
}

function get_element_value(id) {
  return document.getElementById(id).value
}

main()
