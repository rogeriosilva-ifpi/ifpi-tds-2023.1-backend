// const baseURL = 'https://app-filmes-tds-366-2023-1.onrender.com/filmes'
const baseURL = "http://localhost:8000/filmes"

let filmes = []
let editing = false
let filme_id
const token = `Bearer ${localStorage.getItem("token_filmes")}`

function resetar_formulario() {
  const form_filme = document.getElementById("form-filme")
  form_filme.reset()

  const btn_confirmar = document.getElementById("btn-confirmar")
  btn_confirmar.value = "Adicionar Filme"

  editing = false
}

function atualizar_tela() {
  // Manipulacao de DOM
  const ul_filmes = document.getElementById("list-filme")
  ul_filmes.innerHTML = []

  for (let filme of filmes) {
    const item = document.createElement("li")
    // const label = '#'+filme.id+' - '+filme.nome + ' - ' + filme.genero
    const label = `#${filme.id} - ${filme.nome} -  ${filme.genero}  `

    const btn_editar = document.createElement("a") // <a></a>
    btn_editar.innerText = "Editar" // <a>Editar</a>
    btn_editar.href = "#"

    btn_editar.onclick = (event) => {
      event.preventDefault()

      // 1. Preencher o Formulário
      preencher_formulario(filme)

      // 2. Mudar o Label do Botão para Atualizar
      const btn_confirmar = document.getElementById("btn-confirmar")
      btn_confirmar.value = "Editar Filme"

      // 3. Salvar um Estado Global se está editando
      editing = true
      filme_id = filme.id
    }

    const btn_remover = document.createElement("a") // <a></a>
    btn_remover.innerText = "Remover" // <a>Editar</a>
    btn_remover.href = "#"
    const espaco = document.createElement("span")
    espaco.innerText = " "
    btn_remover.onclick = async (event) => {
      // alert(`Remover o Filme ${filme.nome}!!`)
      // chamar API método DELETE passando o ID URL
      event.preventDefault()
      const confirmou = confirm(`Deseja mesmo remover o Filme: ${filme.nome}`)

      if (!confirmou) {
        return
      }

      const opcoes = {
        method: "DELETE",
        headers: {
          Authorization: token
        }
      }

      const response = await fetch(baseURL + "/" + filme.id, opcoes)

      // se deu certo..
      if (response.ok) {
        alert("Filme removido com sucesso!")
        carregar_filmes()
      }
    }

    item.innerText = label
    item.appendChild(btn_editar)
    item.appendChild(espaco)
    item.appendChild(btn_remover)

    ul_filmes.appendChild(item)
  }
}

function preencher_formulario(filme) {
  const form_filme = document.getElementById("form-filme")

  const inputs = form_filme.children
  inputs[0].value = filme.nome
  inputs[1].value = filme.genero
  inputs[2].value = filme.ano
  inputs[3].value = filme.duracao
}

async function carregar_filmes() {
  console.log("API - Todos os filmes")

  const opcoes = {
    headers: {
      Authorization: token
    }
  }
  const response = await fetch(baseURL, opcoes)
  const status = response.status

  if (response.status === 200) {
    filmes = await response.json()
    atualizar_tela()
  } else {
    // const result = await response.json()
    alert(`Você não está autenticado!`)
    // redicionar para tela de login
    window.location.replace("login.html")
  }

  // console.log('Status', status)
  // console.log('Dados', dados)
}

function configurar_formulario() {
  const form_filme = document.getElementById("form-filme")
  const input_duracao = document.getElementById("duracao")

  const btn_cancelar = document.getElementById("btn-cancelar")

  btn_cancelar.onclick = () => {
    const btn_confirmar = document.getElementById("btn-confirmar")
    btn_confirmar.value = "Adicionar Filme"
  }

  form_filme.onsubmit = async function (event) {
    event.preventDefault()

    const dados = form_filme.children
    const nome = dados[0].value
    const genero = dados[1].value
    const ano = Number(dados[2].value)
    const duracao = Number(input_duracao.value)

    const filme = { nome, genero, ano, duracao }

    console.log("Submeteu!!!")
    // console.log(dados)
    // console.log('Filme: ', filme)
    let url = baseURL
    let method = "POST"
    let mensagem_ok = "Filme Adicionado com sucesso!"
    let mensagem_erro = "Não foi possível adicionar"
    let response_status = 201

    if (editing) {
      url = baseURL + "/" + filme_id
      method = "PUT"
      mensagem_ok = "Filme Atualizado com sucesso!"
      mensagem_erro = "Não foi possível editar"
      response_status = 200
    }

    const opcoes = {
      method: method,
      body: JSON.stringify(filme),
      headers: {
        "Content-Type": "application/json",
        Authorization: token
      }
    }

    const response = await fetch(url, opcoes)

    if (response.status === response_status) {
      alert(mensagem_ok)
      carregar_filmes()
      resetar_formulario()
    } else {
      const result_data = await response.json()
      alert(`Erro: ${result_data["detail"]}`)
    }
  }
}

function app() {
  console.log("Hello Filmes")
  show_current_user()
  configurar_formulario()
  carregar_filmes()
}

async function show_current_user() {
  const url = "http://localhost:8000/auth/me"
  const user_label = document.getElementById("user")

  const opcoes = {
    headers: {
      Authorization: token
    }
  }
  const response = await fetch(url, opcoes)

  if (response.ok) {
    const result_data = await response.json()
    const primeiro_nome = result_data["nome"].split(" ")[0]
    user_label.innerText = `Olá ${primeiro_nome}!`
  }
}

function logout() {
  alert("Tchau!")
  localStorage.clear()
  window.location.replace("login.html")
}

app()
