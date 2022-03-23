console.log("connection successfull");

//this is the target mobile menu
const targetEl = document.getElementById('mobile-menu-4');

const mobileMenuBtn = document.getElementById('mobile-menu-btn');

mobileMenuBtn.addEventListener('click', () => {
    targetEl.classList.toggle("hidden")
});