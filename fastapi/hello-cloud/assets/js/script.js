function hello(){
    const input_name = document.getElementById('name')
    const name = input_name.value || 'Anônimo'

    alert(`Olá ${name}, seja bem vindo.`)
    input_name.value = ''
    input_name.focus()
}