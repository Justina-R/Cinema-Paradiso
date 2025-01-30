document.addEventListener('DOMContentLoaded', () => {
    // Selecciona ambos formularios
    const forms = document.querySelectorAll('form');

    // Agrega el manejador de eventos a cada formulario
    forms.forEach((form) => {
        form.addEventListener('submit', validateInformation);
    });
});

const validateInformation = (e) => {
    e.preventDefault(); // Prevents that the formulary is sent

    const form = e.target; // Form that triggered the event

    const name = form.querySelector("[name='name']").value.trim();
    const surname = form.querySelector("[name='surname']").value.trim();
    const email = form.querySelector("[name='mail']").value.trim();
    const message = form.querySelector("[name='message']").value.trim();


    const validCharactersText = /^[a-zA-Z\s]+$/;

    // Validations
    const validName = verifyName(name, validCharactersText, form);
    const validSurname = verifySurname(surname, validCharactersText, form);
    const validMail = verifyMail(email, form);
    const validMessage = verifyMessage(message, form);

    if (validName && validSurname && validMail && validMessage) {
        Swal.fire({
            icon: 'success',
            title: 'Thank you!',
            text: 'Your message has been sent.',
            confirmButtonText: 'Accept'
        }).then((result) => {
            if (result.isConfirmed) {
                form.submit(); //Sends the form
            }
        });
    }
};

// Field Validations
const verifyName = (name, validCh, form) => {
    if (name.length < 2 || !validCh.test(name)) {
        errorMessage(form, 'nameError', 'Your name must have at least 2 characters and consist only of letters.');
        return false;
    }
    hideError(form, 'nameError');
    return true;
};

const verifySurname = (surname, validCh, form) => {
    if (surname.length < 2 || !validCh.test(surname)) {
        errorMessage(form, 'surnameError', 'Your surname must have at least 2 characters and consist only of letters.');
        return false;
    }
    hideError(form, 'surnameError');
    return true;
};

const verifyMail = (email, form) => {
    if (!email.includes('@') || !email.includes('.com')) {
        errorMessage(form, 'emailError', 'Enter a valid email.');
        return false;
    }
    hideError(form, 'emailError');
    return true;
};

const verifyMessage = (message, form) => {
    if (message.length < 10) {
        errorMessage(form, 'messageError', 'The message must have at least 10 characters.');
        return false;
    }
    hideError(form, 'messageError');
    return true;
};

// Error Messages
function errorMessage(form, id, message) {
    const element = form.querySelector(`#${id}`);
    if (element) {
        element.textContent = message;
    }
}

function hideError(form, id) {
    const element = form.querySelector(`#${id}`);
    if (element) {
        element.textContent = '';
    }
}