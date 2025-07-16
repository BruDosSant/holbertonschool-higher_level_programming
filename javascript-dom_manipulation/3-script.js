header = document.querySelector('header');
if (header.classList.contains('red') == false && header.classList.contains('green') == false) {
    header.classList.add('green');
}

document.querySelector('#toggle_header').addEventListener('click', function () {
    if (header.classList.contains('red') == false) {
        header.classList.remove('green');
        header.classList.add('red');
    }
    else {
        header.classList.remove('red');
        header.classList.add('green');
    }
});