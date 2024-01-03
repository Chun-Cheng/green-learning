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
        let seconds = Math.floor(timespan / (10 * 1000));
        return `${seconds}秒前`;
    } else {
        // just now
        return '剛才';
    }
}
let update_time_element = document.getElementById('update_datetime');
let update_time = new Date(update_time_element.innerText);
update_time_element.innerText = time_ago(Date.now() - update_time);


// a
let link_elements = Array.from( document.getElementsByTagName('a') );
link_elements.forEach(element => {
    element.classList.add('link-offset-1', 'link-underline', 'link-underline-opacity-0', 'link-underline-opacity-100-hover');
});


// heading link
function title_to_url(title) {
    let url = title
        .replace(' ', '-')
        .replace('?', '-')
        .replace('/', '-')
        .toLowerCase();
    return url;
}

['h1', 'h2', 'h3', 'h4', 'h5', 'h6'].forEach(tag => {
    let heading_elements = Array.from( document.getElementsByTagName(`${tag}`) );
    heading_elements.forEach(element => {
        let title = element.innerText;
        let url = title_to_url(title);
        
        let wrapper = document.createElement('a');
        wrapper.innerText = title
        wrapper.href = `#${url}`;
        wrapper.classList.add(`${tag}`, 'link-offset-1', 'link-underline-secondary', 'link-underline-opacity-0', 'link-underline-opacity-100-hover');

        element.innerHTML = '';
        element.appendChild(wrapper);
    });
});

let video_elements = Array.from( document.getElementsByClassName('video') );
video_elements.forEach(element => {
    element.classList.add('col-12');
});


// activity block
let activity_block_elements = Array.from( document.getElementsByName('question-block') );
activity_block_elements.forEach(element => {
    element.classList.add('card');
    element.classList.add('mt-3');
    element.classList.add('mb-3');
    // add wrapper div
    let wrapper = document.createElement('div');
    wrapper.classList.add('card-body');
    while(element.hasChildNodes())
        wrapper.appendChild(element.firstChild);
    element.appendChild(wrapper);
});


// button style => activity block
let button_list = Array.from( document.getElementById('content').getElementsByTagName('button') );
button_list.forEach(element => {
    if ( !element.classList.contains('btn') ) {
        element.classList.add('btn');
        element.classList.add('btn-outline-secondary');
    }
});