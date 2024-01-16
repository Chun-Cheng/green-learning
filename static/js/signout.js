// onload
window.addEventListener('load', async (event) => {
    // detect dark mode
    if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
        document.documentElement.setAttribute('data-bs-theme', 'dark');
    }

    // sign out
    let session_id = window.localStorage.getItem('session_id');
    // check whether the session_id valid
    fetch(`/api/check_session?session_id=${session_id}`)
        .then(response => {
            if (!response.ok) {
                // not valid
                window.localStorage.removeItem('session_id');
                window.location.replace('/');
                session_id = null;
            }
        })
    if (session_id !== null) {
        fetch(`/api/signout?session_id=${session_id}`)
            .then(response => {
                if (response.ok) {
                    // successfully signed out
                    window.localStorage.removeItem('session_id');
                    window.location.replace('/');
                }
            })
    }
    
});