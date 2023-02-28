const baseURL = 'http://localhost:8000/filmes'
let filmes = []


function atualizar_tela(){
    const ul_filmes = document.getElementById('list-filmes')
    ul_filmes.innerHTML = ''

    filmes.forEach(filme => ul_filmes.appendChild(item_filme(filme)))
}

function item_filme(filme){
    const li_filme = document.createElement('li')
    li_filme.innerText = filme.nome
    return li_filme
}

async function carregar_filmes(){
    try {
        const response = await fetch(baseURL)
        const dados = await response.json()
        filmes = []
        dados.forEach(filme => {
            filmes.push(filme)
        });

        console.log(`Filmes carregados ${filmes.length}`)
        atualizar_tela()
    } catch (error) {
        console.error(`Não foi possível carregar os filmes: ${error}`)
    }
}

function configurar_componentes(){
    const form_filme = document.getElementById('form-filme')
    

    form_filme.onsubmit = async function(event){
        event.preventDefault()
        const inputs = event.target.children
        const nome = inputs[0].value
        const genero = inputs[1].value
        const ano = Number(inputs[2].value)
        const duracao = Number(inputs[3].value)

        const filme = {nome, genero, ano, duracao}

        // Salvar na API
        // console.log('Salvar filme...')
        // console.log(filme)
        try {
            const config = {
                body: JSON.stringify(filme), 
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                }
            }

            const response = await fetch(baseURL, config)
            
            console.log(`Status: ${response.status}`)
            if (response.ok){
                alert('Filme salvo com sucesso!')
                const novo_filme = await response.json()
                filmes.push(novo_filme)
                atualizar_tela()
            }else{
                console.log(`Resposta: ${await response.json()}`)
            }
        } catch (error) {
            console.log(`Não foi possível salvar: ${error}`)
        }
    }
}

function app(){
    console.log('Hello...')
    configurar_componentes()
    carregar_filmes()
}

app()