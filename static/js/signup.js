// onload
window.addEventListener('load', async (event) => {
    // has signed in
    let session_id = window.localStorage.getItem('session_id');
    // check whether the session_id valid
    await fetch(`/api/check_session?session_id=${session_id}`)
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

// submit sign up form
document.getElementById('signup-form').onsubmit = async (event) => {  // addEventListener('submit',
    event.preventDefault();

    // disable the button
    let submit_button = document.getElementById('submit-btn');
    // change the text on submit button to the loading image
    submit_button.disabled = true;
    submit_button.innerHTML = `
        <span class="spinner-border spinner-border-sm" aria-hidden="true"></span>
        <span class="visually-hidden" role="status">Loading...</span>
        `;

    // get the values
    let name = document.getElementById('name').value;
    let email = document.getElementById('email').value;

    let data = { 
        name: name, 
        email: email
    };
    await fetch('/api/signup', {
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
                throw new Error(response.statusText);
            }
        })
        .then(json_response => {
            // ok
            return signin(email);
        })
        .then(session_id => {
            console.log(session_id);
            window.localStorage.setItem('session_id', session_id);
            window.location.href = '/dashboard';
        })
        .catch((error) => {
            console.log(error);
            // change the content on submit button to the original text
            submit_button.disabled = false;
            submit_button.innerHTML = '下一步';
        });

    return false;
};

async function signin(email) {
    let data = { 
        email: email,
        device: 'browser'
    };
    return fetch('/api/signin_email', {
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
            throw new Error('Sign in error');
        }
    })
    .then(json_response => {
        // ok
        let session_id = json_response.session_id;
        return session_id;
    })
    .catch((error) => {
        console.log(error);
    });
}