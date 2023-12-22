document.getElementById('signup-form').onsubmit = (event) => {  // addEventListener('submit',
    event.preventDefault();

    // disable the button
    let submit_button = document.getElementById('submit-btn');
    // change the text on submit button to the loading image
    submit_button.disabled = true;

    // get the values
    let name = document.getElementById('name').value;
    let email = document.getElementById('email').value;

    // send the request
    const headers = new Headers();
    headers.append('Content-Type', 'application/json');

    const request = new Request('/api/signup', {
        method: 'POST',
        headers: headers,
        body: `{"name": "${name}", "email": "${email}"}`,
    });

    fetch(request)
        .then((response) => {
            if (response.status === 201) {
                return response.json();
                // redirect to the next page
            } else {
                throw new Error("Something went wrong on API server!");
                // show error message
            }
        })
        .catch((error) => {
            console.error(error);
            // show error message
        });
    
    return false;
};