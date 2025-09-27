// Dark Mode Toggle
const toggle = document.getElementById('darkModeToggle');
toggle.addEventListener('click', () => {
    document.body.classList.toggle('dark-mode');
});

// Flash message JS-only
const form = document.getElementById('contactForm');
form.addEventListener('submit', function(e){
    e.preventDefault();
    const flashContainer = document.getElementById('flash-container');
    const flash = document.createElement('div');
    flash.className = 'flash';
    flash.innerText = '✅ Message sent successfully!';
    flashContainer.appendChild(flash);
    setTimeout(()=>{ flash.classList.add('fade-out'); setTimeout(()=>flash.remove(),1000); },3000);
    form.reset();
});
