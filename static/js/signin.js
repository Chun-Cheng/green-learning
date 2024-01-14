// onload
window.addEventListener('load', async (event) => {
    // has signed in
    let session_id = window.localStorage.getItem('session_id');
    // check whether the session_id valid
    fetch(`/api/check_session?session_id=${session_id}`)
        .then(response => {
            if (response.ok) {
                // ok
                window.location.replace('/dashboard');
            } else {
                // not ok
                window.localStorage.removeItem('session_id');
                session_id = undefined;
            }
        })
        .catch((error) => {
            console.log(error);
        });

    // detect dark mode
    if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
        document.documentElement.setAttribute('data-bs-theme', 'dark');
    }
});


// sign in with passkey
document.getElementById('btn-passkey-signin').onclick = (event) => {
    event.preventDefault();

    // disable the button
    let passkey_login_button = document.getElementById('btn-passkey-signin');
    let email_input = document.getElementById('email');
    let submit_button = document.getElementById('submit-btn');
    // change the text on submit button to the loading image
    passkey_login_button.disabled = true;
    passkey_login_button.innerHTML = `
        <span class="spinner-border spinner-border-sm" aria-hidden="true"></span>
        <span class="visually-hidden" role="status">Loading...</span>
        `;
    email_input.disabled = true;
    submit_button.disabled = true;
    
    // TODO: finish below


    // if not success
    //     2_button_1_input.disabled = false;


    // change the content on submit button to the original text
    // passkey_login_button.disabled = false;
    // passkey_login_button.innerHTML = '通行密鑰登入';
    // email_input.disabled = false;
    // submit_button.disabled = false;

    return false;
};

// sign in with email
document.getElementById('signin-form').onsubmit = async (event) => {
    event.preventDefault();

    // disable the button
    let submit_button = document.getElementById('submit-btn');
    let email_input = document.getElementById('email');
    let passkey_button = document.getElementById('btn-passkey-signin');
    // change the text on submit button to the loading image
    submit_button.disabled = true;
    submit_button.innerHTML = `
        <span class="spinner-border spinner-border-sm" aria-hidden="true"></span>
        <span class="visually-hidden" role="status">Loading...</span>
        `;
    email_input.disabled = true;
    passkey_button.disabled = true;

    let email = document.getElementById('email').value;
    // TODO: finish below

    // check whether the account is exist and sent an email
    // if success
    //     hide the sign in with email button
    //     show the verify form
    //     set the sign in with passkey button btn-secondary
    // if not success
    //     2_button_1_input.disabled = false;
    //     show error message

    // const form_data  = new FormData();
    // form_data.append('email', email);
    // form_data.append('device', 'browser');
    let data = { 
        email: email, 
        device: 'browser' 
    };
    await fetch('/api/signin_email', {
            method: 'POST', 
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data)
        })
        .then(response => {
            if (response.ok) {
                // ok
                return response.json();
            } else {
                // not ok
                console.log(`sign in: ${response.status}`);
                // change the content on submit button to the original text
                submit_button.disabled = false;
                submit_button.innerHTML = '電子信箱登入';
                email_input.disabled = false;
                passkey_button.disabled = false;
            }
            // throw new Error('Something went wrong');
        })
        .then(json_response => {
            // ok
            session_id = json_response.session_id;
            window.localStorage.setItem('session_id', session_id);
            window.location.href = '/dashboard';
        })
        .catch((error) => {
            console.log(error);
        });
    
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