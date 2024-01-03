// detect dark mode
if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
    document.documentElement.setAttribute('data-bs-theme', 'dark');
}

window.addEventListener('load', (event) => {
    // read history
    let read_history_title = window.localStorage.getItem('read_history_title');
    let read_history_duration = window.localStorage.getItem('read_history_duration');
    let read_history_update = window.localStorage.getItem('read_history_update');
    // activity history
    let activity_history_title = window.localStorage.getItem('activity_history_title');
    let activity_history_block_title = window.localStorage.getItem('activity_history_block_title');
    let activity_history_answer = window.localStorage.getItem('activity_history_answer');
    let activity_history_update = window.localStorage.getItem('activity_history_update');

    let read_record_div = document.getElementById('read_record');
    if(read_history_title == null) {
        let empty_hint = document.createElement('h6');
        empty_hint.innerHTML = '<i>暫無資料</i>';
        read_record_div.appendChild(empty_hint);
    }
    else {
        let read_history_title_list = read_history_title.split(',');
        let read_history_duration_list = read_history_duration.split(',');
        let read_history_update_list = read_history_update.split(',');
        console.log(read_history_title_list);
        console.log(read_history_duration_list);
        console.log(read_history_update_list);
        for (let i = 0; i < read_history_title_list.length; i++) {
            let card = document.createElement('div');
            card.classList.add('card', 'col-12', 'col-md-6', 'mt-2', 'mt-2');
            card.innerHTML = 
                `<div class="card-body">
                    <h5 class="card-title"><a href="${read_history_title_list[i]}.html" class="card-link link-offset-2 link-underline link-underline-opacity-0 link-underline-opacity-100-hover">${read_history_title_list[i]}</a></h5>
                    <p class="card-text"><span id="duration">${time_convert(Number(read_history_duration_list[i]))}</span>（<span id="update_datetime">${time_ago(Date.now() - Number(read_history_update_list[i]))}</span>）</p>
                </div>`
            read_record_div.appendChild(card);
        }
    }
    

    let activity_record_div = document.getElementById('activity_record');
    if(activity_history_title == null) {
        let empty_hint = document.createElement('h6');
        empty_hint.innerHTML = '<i>暫無資料</i>';
        activity_record_div.appendChild(empty_hint);
    }
    else {
        let activity_history_title_list = activity_history_title.split(',');
        let activity_history_block_title_list = activity_history_block_title.split(',');
        let activity_history_answer_list = activity_history_answer.split(',');
        let activity_history_update_list = activity_history_update.split(',');
        for (let i = 0; i < activity_history_title.split(',').length; i++) {
            let card = document.createElement('div');
            card.classList.add('card', 'col-12', 'col-md-6', 'mt-2');
            card.innerHTML = 
                `<div class="card-body">
                    <h5 class="card-title"><a href="${activity_history_title_list[i]}.html" class="card-link link-offset-2 link-underline link-underline-opacity-0 link-underline-opacity-100-hover">${activity_history_title_list[i]}</a></h5>
                    <h6 class="card-subtitle mb-2 text-body-secondary">${activity_history_block_title_list[i]}</h6>
                    <p class="card-text">
                        <span id="answer">${activity_history_answer_list[i]}</span>
                        <span id="answer">（${time_ago(Date.now() - Number(activity_history_update_list[i]))}）</span>
                    </p>
                </div>`
            activity_record_div.appendChild(card);
        }
    }
    
});

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