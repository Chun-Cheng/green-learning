// detect dark mode
if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
    document.documentElement.setAttribute('data-bs-theme', 'dark');
}

// read record
window.addEventListener('load', (event) => {
    let record_timer_id = setInterval(async () => {
        let session_id = window.localStorage.getItem('session_id');
        console.debug(session_id)
        if(session_id === null) {
            return;
        }
        let splitted_url = window.location.href.split('/');
        let page_id = splitted_url[splitted_url.length-1];
        let update_datetime = now_iso();
        // get /add_read_time session_id page_id seconds(3) update
        await fetch(`/api/add_read_time?session_id=${session_id}&page_id=${page_id}&seconds=3&update=${update_datetime}`)  // , {method: 'GET'}
            .then(response => {
                console.debug(`/api/add_read_time 3: ${response.status}`);
                if (response.ok) {
                    console.log('reading time recorded');
                }
            });
    }, 3000);  //
});

// get now ISO string
function now_iso() {
    let now = new Date();
    let year = now.getFullYear();
    let month = now.getMonth() >= 10 ? `${now.getMonth()}` : `0${now.getMonth()}`;
    let date = now.getDate() >= 10 ? `${now.getDate()}` : `0${now.getDate()}`;
    let hours = now.getHours() >= 10 ? `${now.getHours()}` : `0${now.getHours()}`;
    let minutes = now.getMinutes() >= 10 ? `${now.getMinutes()}` : `0${now.getMinutes()}`;
    let seconds = now.getSeconds() >= 10 ? `${now.getSeconds()}` : `0${now.getSeconds()}`;
    let milliseconds = now.getMilliseconds();
    return `${year}-${month}-${date}T${hours}:${minutes}:${seconds}.${milliseconds}000`;
}