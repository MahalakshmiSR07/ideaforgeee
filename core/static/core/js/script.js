document.addEventListener('DOMContentLoaded', () => {
    // Laser pointer implementation
    const pointer = document.createElement('div');
    pointer.id = 'laser-pointer';
    document.body.appendChild(pointer);
    
    const trail = document.createElement('div');
    trail.id = 'laser-trail';
    document.body.appendChild(trail);

    document.addEventListener('mousemove', (e) => {
        pointer.style.left = e.clientX + 'px';
        pointer.style.top = e.clientY + 'px';
        
        // Trail slightly lags behind
        setTimeout(() => {
            trail.style.left = e.clientX + 'px';
            trail.style.top = e.clientY + 'px';
        }, 50);
    });

    // Make pointer bigger on interactive elements
    const interactiveElements = document.querySelectorAll('a, button, input, select, .card');
    interactiveElements.forEach(el => {
        el.addEventListener('mouseenter', () => {
            pointer.style.width = '20px';
            pointer.style.height = '20px';
            pointer.style.backgroundColor = '#10b981'; // change to accent color
            pointer.style.boxShadow = '0 0 10px #10b981, 0 0 20px #10b981';
        });
        el.addEventListener('mouseleave', () => {
            pointer.style.width = '12px';
            pointer.style.height = '12px';
            pointer.style.backgroundColor = '#ff0055';
            pointer.style.boxShadow = '0 0 10px #ff0055, 0 0 20px #ff0055, 0 0 30px #ff0055';
        });
    });

    // Password Eye Toggle Implementation
    const passwordInputs = document.querySelectorAll('input[type="password"]');
    passwordInputs.forEach(input => {
        // Wrap input in a relative div
        const wrapper = document.createElement('div');
        wrapper.className = 'position-relative';
        input.parentNode.insertBefore(wrapper, input);
        wrapper.appendChild(input);

        // Create toggle icon
        const icon = document.createElement('i');
        icon.className = 'fas fa-eye text-secondary position-absolute';
        icon.style.right = '15px';
        icon.style.top = '50%';
        icon.style.transform = 'translateY(-50%)';
        icon.style.cursor = 'pointer';
        icon.style.zIndex = '10';

        // Toggle logic
        icon.addEventListener('click', () => {
            if (input.type === 'password') {
                input.type = 'text';
                icon.className = 'fas fa-eye-slash text-primary position-absolute';
            } else {
                input.type = 'password';
                icon.className = 'fas fa-eye text-secondary position-absolute';
            }
        });

        wrapper.appendChild(icon);
    });
});
