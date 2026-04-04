const redHeaderDiv = document.querySelector('#red_header');

const headerElement = document.querySelector('header');

redHeaderDiv.addEventListener('click', function () {
	headerElement.style.color = '#FF0000';
});