// sign in with passkey
document.getElementById('btn-passkey-signin').onclick = (event) => {
    event.preventDefault();

    // disable the button
    let passkey_login_button = document.getElementById('btn-passkey-signin');
    // change the text on submit button to the loading image
    passkey_login_button.disabled = true;
    passkey_login_button.innerHTML = `
        <span class="spinner-border spinner-border-sm" aria-hidden="true"></span>
        <span class="visually-hidden" role="status">Loading...</span>
        `;
    document.getElementById('email').disabled = true;
    document.getElementById('submit-btn').disabled = true;
    
    // TODO: finish below


    // if not success
    //     2_button_1_input.disabled = false;

    return false;
};

// sign in with email
document.getElementById('signin-form').onsubmit = async (event) => {
    event.preventDefault();

    // disable the button
    let submit_button = document.getElementById('submit-btn');
    // change the text on submit button to the loading image
    submit_button.disabled = true;
    submit_button.innerHTML = `
        <span class="spinner-border spinner-border-sm" aria-hidden="true"></span>
        <span class="visually-hidden" role="status">Loading...</span>
        `;
    document.getElementById('email').disabled = true;
    document.getElementById('btn-passkey-signin').disabled = true;

    let input_value = document.getElementById('email').value;
    // TODO: finish below

    // check whether the account is exist and sent an email
    // if success
    //     hide the sign in with email button
    //     show the verify form
    //     set the sign in with passkey button btn-secondary
    // if not success
    //     2_button_1_input.disabled = false;
    //     show error message

    return false;
};

// verify and sign in with email
document.getElementById('verify-form').onsubmit = async (event) => {
    event.preventDefault();

    // disable the button
    let verify_button = document.getElementById('verify-btn');
    // change the text on submit button to the loading image
    verify_button.disabled = true;
    verify_button.innerHTML = `
        <span class="spinner-border spinner-border-sm" aria-hidden="true"></span>
        <span class="visually-hidden" role="status">Loading...</span>
        `;

    let verify_code = document.getElementById('verify-code').value;
    // TODO: finish below

    // check whether the verify code is correct
    // if success
    //     write localStorage
    //     redirect
    // if not success
    //     button.disabled = false;
    //     show error message

    return false;
};

// detect dark mode
if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
    document.documentElement.setAttribute('data-bs-theme', 'dark');
}