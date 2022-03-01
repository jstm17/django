console.log('hello world');

const socket = io('http://localhost:8000');

const alertBox = document.getElementById('alert-box');
const messagesBox = document.getElementById('messages-box');
const messageInput = document.getElementById('message-input');
const sendBtn = document.getElementById('send-btn');

const handleAlerts = (msg, type) => {
    alertBox.innerHTML = `
    <div class="alert alert-${type}" role="alert">
        ${msg}
    </div>
    `

    setTimeout(() => {
        alertBox.innerHTML = '';
    }, 5000);
};

socket.on("welcome2", (msg) => {
    handleAlerts(msg, 'primary');
});

socket.on("byebye", (msg) => {
    handleAlerts(msg, 'danger');
});

sendBtn.addEventListener('click', () => {
    const message = messageInput.value;
    messageInput.value = '';
    console.log(message);

    socket.emit('message', message);
});

socket.on("messageToClients", (msg) => {
    messagesBox.innerHTML += `<p>${msg}</p><hr>`;
});