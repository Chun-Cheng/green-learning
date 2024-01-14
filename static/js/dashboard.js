// onload
window.addEventListener('load', async (event) => {
    // has signed in
    let session_id = window.localStorage.getItem('session_id');
    // check whether the session_id valid
    fetch(`/api/check_session?session_id=${session_id}`)
        .then(response => {
            if (!response.ok) {
                // not ok
                window.localStorage.removeItem('session_id');
                window.location.replace('/signin');
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