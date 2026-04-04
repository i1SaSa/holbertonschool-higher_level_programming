const updateTrigger = document.querySelector('#update_header');

const headerElement = document.querySelector('header');

updateTrigger.addEventListener('click', function () {
	headerElement.textContent = 'New Header!!!';
});