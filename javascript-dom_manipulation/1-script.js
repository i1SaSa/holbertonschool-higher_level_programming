const clickableElement = document.querySelector('#red_header');

const headerElement = document.querySelector('header');

clickableElement.addEventListener('click', function () {
	headerElement.classList.add('red');
});