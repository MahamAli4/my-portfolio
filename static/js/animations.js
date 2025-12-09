// Additional Animations and Effects

// Parallax scrolling effect
class Parallax {
    constructor() {
        this.parallaxElements = document.querySelectorAll('[data-parallax]');
        this.init();
    }

    init() {
        if (this.parallaxElements.length > 0) {
            window.addEventListener('scroll', () => this.updateParallax());
            this.updateParallax(); // Initial call
        }
    }

    updateParallax() {
        const scrollPosition = window.pageYOffset;
        
        this.parallaxElements.forEach(element => {
            const speed = element.dataset.parallaxSpeed || 0.5;
            const yPos = -(scrollPosition * speed);
            
            element.style.transform = `translateY(${yPos}px)`;
        });
    }
}

// Typing animation effect
class TypeWriter {
    constructor(element, texts, options = {}) {
        this.element = element;
        this.texts = texts;
        this.options = {
            typingSpeed: 100,
            deletingSpeed: 50,
            delayBetweenTexts: 2000,
            loop: true,
            ...options
        };
        
        this.currentTextIndex = 0;
        this.currentCharIndex = 0;
        this.isDeleting = false;
        this.isPaused = false;
        
        this.init();
    }

    init() {
        if (!this.element || this.texts.length === 0) return;
        
        // Set initial text to empty
        this.element.textContent = '';
        
        // Start typing
        this.type();
    }

    type() {
        if (this.isPaused) return;
        
        const currentText = this.texts[this.currentTextIndex];
        
        if (!this.isDeleting) {
            // Typing forward
            this.element.textContent = currentText.substring(0, this.currentCharIndex + 1);
            this.currentCharIndex++;
            
            if (this.currentCharIndex === currentText.length) {
                // Finished typing, pause then start deleting
                this.isDeleting = true;
                setTimeout(() => this.type(), this.options.delayBetweenTexts);
                return;
            }
        } else {
            // Deleting
            this.element.textContent = currentText.substring(0, this.currentCharIndex - 1);
            this.currentCharIndex--;
            
            if (this.currentCharIndex === 0) {
                // Finished deleting, move to next text
                this.isDeleting = false;
                this.currentTextIndex = (this.currentTextIndex + 1) % this.texts.length;
            }
        }
        
        // Schedule next frame
        const speed = this.isDeleting ? this.options.deletingSpeed : this.options.typingSpeed;
        setTimeout(() => this.type(), speed);
    }

    pause() {
        this.isPaused = true;
    }

    resume() {
        this.isPaused = false;
        this.type();
    }
}

// Hover tilt effect for cards
class TiltEffect {
    constructor(element) {
        this.element = element;
        this.width = element.offsetWidth;
        this.height = element.offsetHeight;
        this.centerX = this.width / 2;
        this.centerY = this.height / 2;
        this.maxTilt = 15;
        
        this.init();
    }

    init() {
        this.element.addEventListener('mousemove', (e) => this.handleMouseMove(e));
        this.element.addEventListener('mouseleave', () => this.handleMouseLeave());
    }

    handleMouseMove(e) {
        const rect = this.element.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;
        
        // Calculate rotation
        const rotateY = ((x - this.centerX) / this.centerX) * this.maxTilt;
        const rotateX = ((this.centerY - y) / this.centerY) * this.maxTilt;
        
        // Apply transformation
        this.element.style.transform = `
            perspective(1000px)
            rotateX(${rotateX}deg)
            rotateY(${rotateY}deg)
            scale3d(1.05, 1.05, 1.05)
        `;
        
        // Add shadow effect
        const shadowX = (rotateY / this.maxTilt) * 20;
        const shadowY = (rotateX / this.maxTilt) * 20;
        const shadowBlur = 40;
        
        this.element.style.boxShadow = `
            ${shadowX}px ${shadowY}px ${shadowBlur}px rgba(0, 0, 0, 0.3)
        `;
    }

    handleMouseLeave() {
        this.element.style.transform = 'perspective(1000px) rotateX(0) rotateY(0) scale3d(1, 1, 1)';
        this.element.style.boxShadow = '0 10px 30px rgba(0, 0, 0, 0.1)';
        this.element.style.transition = 'transform 0.5s ease, box-shadow 0.5s ease';
        
        // Remove transition after animation completes
        setTimeout(() => {
            this.element.style.transition = '';
        }, 500);
    }
}

// Initialize all animations
document.addEventListener('DOMContentLoaded', () => {
    // Initialize parallax
    new Parallax();
    
    // Initialize typewriter effect if elements exist
    const typewriterElements = document.querySelectorAll('[data-typewriter]');
    typewriterElements.forEach(element => {
        const texts = JSON.parse(element.dataset.typewriterTexts || '[]');
        if (texts.length > 0) {
            new TypeWriter(element, texts);
        }
    });
    
    // Initialize tilt effect for cards with data-tilt attribute
    const tiltElements = document.querySelectorAll('[data-tilt]');
    tiltElements.forEach(element => {
        new TiltEffect(element);
    });
    
    // Add hover effects to project cards
    const projectCards = document.querySelectorAll('.project-card');
    projectCards.forEach(card => {
        card.addEventListener('mouseenter', () => {
            card.style.transition = 'all 0.3s ease';
        });
    });
    
    // Add ripple effect to buttons
    const buttons = document.querySelectorAll('.btn');
    buttons.forEach(button => {
        button.addEventListener('click', function(e) {
            const x = e.clientX - e.target.getBoundingClientRect().left;
            const y = e.clientY - e.target.getBoundingClientRect().top;
            
            const ripple = document.createElement('span');
            ripple.classList.add('ripple');
            ripple.style.left = `${x}px`;
            ripple.style.top = `${y}px`;
            
            this.appendChild(ripple);
            
            setTimeout(() => {
                ripple.remove();
            }, 600);
        });
    });
});

// CSS for ripple effect (add to your CSS file)
const rippleCSS = `
.ripple {
    position: absolute;
    border-radius: 50%;
    background: rgba(255, 255, 255, 0.7);
    transform: scale(0);
    animation: ripple-animation 0.6s linear;
}

@keyframes ripple-animation {
    to {
        transform: scale(4);
        opacity: 0;
    }
}
`;

// Add ripple CSS to head
if (document.head) {
    const style = document.createElement('style');
    style.textContent = rippleCSS;
    document.head.appendChild(style);
}