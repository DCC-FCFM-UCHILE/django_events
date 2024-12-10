function showMessage(message, level, auto_dismiss=true) {
    const messagesDiv = document.getElementById('messages');
    if (!messagesDiv) {
        console.error('Incluye un div con id "messages" y class "alert-container" en el DOM.');
        return;
    }

    let alertClass = '';
    let iconClass = '';

    switch (level) {
        case 'success':
            alertClass = 'alert alert-success';
            iconClass = 'bi-check-circle-fill';
            break;
        case 'warning':
            alertClass = 'alert alert-warning';
            iconClass = 'bi-exclamation-circle-fill';
            break;
        case 'info':
            alertClass = 'alert alert-info';
            iconClass = 'bi-info-circle-fill';
            break;
        case 'danger':
            alertClass = 'alert alert-danger';
            iconClass = 'bi-x-circle-fill';
            break;
        default:
            alertClass = 'alert alert-info';
            iconClass = 'bi-info-circle-fill';
    }

    const alertDiv = document.createElement('div');
    alertDiv.className = `alert ${alertClass} fade show text-center alert-dismissible`;
    alertDiv.role = 'alert';

    const icon = document.createElement('i');
    icon.className = `${iconClass} pe-1`;
    alertDiv.appendChild(icon);

    const messageText = document.createTextNode(message);
    alertDiv.innerHTML += message;

    const closeButton = document.createElement('button');
    closeButton.type = 'button';
    closeButton.className = 'btn-close';
    closeButton.setAttribute('data-bs-dismiss', 'alert');
    closeButton.setAttribute('aria-label', 'Close');
    alertDiv.appendChild(closeButton);

    messagesDiv.appendChild(alertDiv);

    if(auto_dismiss == true) {
        setTimeout(() => {
            $(alertDiv).slideUp(450, function() {
                $(this).alert('close');
            });
        }, 3500);
    }
}