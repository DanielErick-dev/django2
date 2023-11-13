

let container = document.getElementById('container');

toglle = () => {
    container.classList.toggle('entrar');
    container.classList.toggle('inscrever');
}

setTimeout(() => {
    container.classList.add('entrar');
})
