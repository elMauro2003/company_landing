
    const passwordInput = document.getElementById('floatingInputPassword');
    const eyeSlashIcon = document.getElementById('eyeSlashIcon');
    const eyeIcon = document.getElementById('eyeIcon');
document.addEventListener('DOMContentLoaded', function() {
    eyeSlashIcon.addEventListener('click', function() {
        if (passwordInput.type === 'password') {
            passwordInput.type = 'text';
            eyeSlashIcon.classList.add('d-none');
            eyeIcon.classList.remove('d-none');
           
        
        }
    });
    eyeIcon.addEventListener('click', function() {
        if (passwordInput.type === 'text') {
            passwordInput.type = 'password';
            eyeSlashIcon.classList.remove('d-none');
            eyeIcon.classList.add('d-none');
            
        }
    });
});


