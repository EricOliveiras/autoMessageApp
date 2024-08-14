let modal = document.getElementById('loadingModal');

let form = document.querySelector('form');

form.addEventListener('submit', function () {
    modal.style.display = 'block';
});

setTimeout(function () {
    modal.style.display = 'none';
}, 5000);

function confirmReset() {
    return confirm("Tem certeza de que deseja resetar as mensagens enviadas?");
}

function showMessage() {
    let selectContacts = document.getElementById('num_contacts');
    let numContacts = selectContacts.value;
    let message = "A mensagem será enviada para " + numContacts + " contatos.\nDeseja continuar?";
    return confirm(message);
}