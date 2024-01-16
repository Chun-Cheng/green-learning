// onload
window.addEventListener('load', async (event) => {
    // has not signed in
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

    // get read data
    let read_record_block = document.getElementById('read_record_block');
    let user_name_span = document.getElementById('user_name');
    fetch(`/api/read_records?session_id=${session_id}`)
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
            let name = json_response.name;
            user_name_span.innerText = name;
            let reading_records = json_response.data;
            if (reading_records.length === 0) {
                // empty
                read_record_block.innerHTML = '<i>暫無內容</i>'
            } else {
                // not empty
                reading_records.forEach(record => {
                    read_record_block.innerHTML += `
                        <div class="card col-12 col-md-6 mt-2 mt-2">
                            <div class="card-body">
                                <h5 class="card-title"><a href="${record.url}" class="card-link link-offset-3 link-underline-secondary link-underline-opacity-0 link-underline-opacity-100-hover">${record.title}</a></h5>
                                <p class="card-text">${ time_convert(record.duration) }（${ time_ago( new Date(record.update_datetime).getTime() / 1000 ) }）</p>
                            </div>
                        </div>
                    `
                });
            }
        })
        .catch((error) => {
            console.log(error);
        });

    // get activity data

});

// time ago
function time_ago(timespan) {
    if (timespan >= 365 * 24 * 60 * 60 * 1000) {
        // year
        let years = Math.floor(timespan / (365 * 24 * 60 * 60 * 1000));
        return `${years}年前`;
    } else if (timespan > 30 * 24 * 60 * 60 * 1000) {
        // month
        let months = Math.floor(timespan / (30 * 24 * 60 * 60 * 1000));
        return `${months}個月前`;
    } else if (timespan > 7 * 24 * 60 * 60 * 1000) {
        // week
        let weeks = Math.floor(timespan / (7 * 24 * 60 * 60 * 1000));
        return `${weeks}週前`;
    } else if (timespan > 24 * 60 * 60 * 1000) {
        // day
        let days = Math.floor(timespan / (24 * 60 * 60 * 1000));
        return `${days}天前`;
    } else if (timespan > 60 * 60 * 1000) {
        // hour
        let hours = Math.floor(timespan / (60 * 60 * 1000));
        return `${hours}小時前`;
    } else if (timespan > 60 * 1000) {
        // minute
        let minutes = Math.floor(timespan / (60 * 1000));
        return `${minutes}分鐘前`;
    } else if (timespan > 10 * 1000) {
        // second
        let seconds = Math.floor(timespan / (1000));
        return `${seconds}秒前`;
    } else {
        // just now
        return '剛才';
    }
}

function time_convert(seconds) {
    // seconds to bigger unit
    if (seconds > 60 * 60) {
        // hour
        let hours = Math.floor(seconds / (60 * 60));
        let minutes = Math.floor(seconds / (60)) - (hours * 60);
        return `${hours}小時${minutes}分`;
    } else if (seconds > 60) {
        // minute
        let minutes = Math.floor(seconds / (60));
        seconds = seconds - (minutes * 60);
        return `${minutes}分${seconds}秒`;
    } else {
        // second
        return `${seconds}秒`;
    }
}

