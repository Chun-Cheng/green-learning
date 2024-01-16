// onload
window.addEventListener('load', async (event) => {
    // detect dark mode
    if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
        document.documentElement.setAttribute('data-bs-theme', 'dark');
    }

    // has signed in
    let session_id = window.localStorage.getItem('session_id');
    if (session_id === null) {
        document.getElementById('signout-nav-item').style.display = 'none';
    }
    // check whether the session_id valid
    await fetch(`/api/check_session?session_id=${session_id}`)
        .then(response => {
            if (response.ok) {
                // ok
                document.getElementById('signin-nav-item').style.display = 'none';
                document.getElementById('signup-nav-item').style.display = 'none';
            } else {
                // not ok
                window.localStorage.removeItem('session_id');
                document.getElementById('signout-nav-item').style.display = 'none';
            }
        })
        .catch((error) => {
            console.log(error);
        });
});