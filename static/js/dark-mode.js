// Dark Mode Toggle
document.addEventListener('DOMContentLoaded', function() {
    const toggleBtn = document.getElementById('darkModeToggle');
    const darkModeStyle = document.getElementById('dark-mode-style');
    const html = document.documentElement;
    
    if (!toggleBtn || !darkModeStyle) return;
    
    // Check saved preference
    const savedMode = localStorage.getItem('darkMode');
    const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    
    // Set initial mode
    if (savedMode === 'dark' || (!savedMode && prefersDark)) {
        enableDarkMode();
    }
    
    // Toggle button click
    toggleBtn.addEventListener('click', function() {
        if (html.getAttribute('data-bs-theme') === 'dark') {
            disableDarkMode();
        } else {
            enableDarkMode();
        }
    });
    
    function enableDarkMode() {
        html.setAttribute('data-bs-theme', 'dark');
        darkModeStyle.disabled = false;
        toggleBtn.querySelector('.fa-moon').classList.add('d-none');
        toggleBtn.querySelector('.fa-sun').classList.remove('d-none');
        localStorage.setItem('darkMode', 'dark');
    }
    
    function disableDarkMode() {
        html.setAttribute('data-bs-theme', 'light');
        darkModeStyle.disabled = true;
        toggleBtn.querySelector('.fa-moon').classList.remove('d-none');
        toggleBtn.querySelector('.fa-sun').classList.add('d-none');
        localStorage.setItem('darkMode', 'light');
    }
});