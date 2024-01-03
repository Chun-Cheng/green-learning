// detect dark mode
if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
    document.documentElement.setAttribute('data-bs-theme', 'dark');
}

// read record
window.addEventListener('load', (event) => {
    let record_timer_id = setInterval(() => {
        // record here
        console.log('record');
    }, 5000);
});