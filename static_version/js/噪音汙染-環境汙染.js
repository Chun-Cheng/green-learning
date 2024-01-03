// detect dark mode
if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
    document.documentElement.setAttribute('data-bs-theme', 'dark');
}

// read record
window.addEventListener('load', (event) => {
    let record_timer_id = setInterval(() => {
        // record here
        let read_history_title = window.localStorage.getItem('read_history_title');
        let read_history_duration = window.localStorage.getItem('read_history_duration');
        let read_history_update = window.localStorage.getItem('read_history_update');

        let now = new Date();
        if(read_history_title === null) {
            // create a record
            let new_read_history_title = '噪音汙染-環境汙染';
            let new_read_history_duration = '5';
            let new_read_history_update = Date.now();//now_iso();
            window.localStorage.setItem('read_history_title', new_read_history_title);
            window.localStorage.setItem('read_history_duration', new_read_history_duration);
            window.localStorage.setItem('read_history_update', new_read_history_update);
        } else {
            // update the record
            let read_history_title_list = read_history_title.split(',');
            let read_history_duration_list = read_history_duration.split(',');
            let read_history_update_list = read_history_update.split(',');

            // find
            let found = false;
            for(let i = 0; i < read_history_title_list.length; i++) {
                if(read_history_title_list[i] === '噪音汙染-環境汙染') {
                    read_history_duration_list[i] = Number(read_history_duration_list[i]) + 5;
                    read_history_update_list[i] = Date.now();//now_iso();
                    found = true;
                    break;
                }
            }

            let new_read_history_title = '';
            let new_read_history_duration = '';
            let new_read_history_update = '';

            if(!found) {
                // create a record
                // new_read_history_title = '噪音汙染-環境汙染';
                // new_read_history_duration = '5';
                // new_read_history_update = Date.now();//now_iso();
                read_history_title_list.push('噪音汙染-環境汙染');
                read_history_duration_list.push('5');
                read_history_update_list.push(Date.now());//now_iso();
            }

            // update
            // for(let i = 0; i < read_history_title_list.length; i++) {
            //     new_read_history_title += read_history_title_list[i];
            //     new_read_history_duration += read_history_duration_list[i];
            //     new_read_history_update += read_history_update_list[i];
            // }
            new_read_history_title = read_history_title_list.join(',');
            new_read_history_duration = read_history_duration_list.join(',');
            new_read_history_update = read_history_update_list.join(',');

            window.localStorage.setItem('read_history_title', new_read_history_title);
            window.localStorage.setItem('read_history_duration', new_read_history_duration);
            window.localStorage.setItem('read_history_update', new_read_history_update);
            console.log('reading history recorded.');
        }
    }, 5000);
});

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