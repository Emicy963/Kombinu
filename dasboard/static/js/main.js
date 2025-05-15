document.addEventListener('DOMContentLoaded', () => {
  // Mobile menu toggle
  const menuToggle = document.querySelector('.menu-toggle');
  const navList = document.querySelector('.nav-list');
  
  if (menuToggle && navList) {
    menuToggle.addEventListener('click', () => {
      menuToggle.classList.toggle('active');
      navList.classList.toggle('active');
    });
  }
  
  // Header scroll effect
  const header = document.querySelector('.header');
  
  if (header) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 50) {
        header.classList.add('scrolled');
      } else {
        header.classList.remove('scrolled');
      }
    });
  }
  
  // Counter animation
  const counters = document.querySelectorAll('.counter');
  
  if (counters.length > 0) {
    counters.forEach(counter => {
      const target = parseFloat(counter.getAttribute('data-target'));
      const duration = 2000; // 2 seconds
      const frameDuration = 1000 / 60; // 60fps
      const totalFrames = Math.round(duration / frameDuration);
      const decimalPoints = (counter.textContent.includes('.')) ? 2 : 0;
      
      let frame = 0;
      const countTo = (target / totalFrames);
      
      const animate = () => {
        frame++;
        const currentCount = countTo * frame;
        
        if (decimalPoints > 0) {
          counter.textContent = currentCount.toFixed(decimalPoints);
        } else {
          counter.textContent = Math.floor(currentCount);
        }
        
        if (frame < totalFrames) {
          requestAnimationFrame(animate);
        } else {
          counter.textContent = target.toFixed(decimalPoints);
        }
      };
      
      animate();
    });
  }
  
  // Pricing tabs
  const tabBtns = document.querySelectorAll('.tab-btn');
  
  if (tabBtns.length > 0) {
    tabBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        // Remove active class from all buttons
        tabBtns.forEach(b => b.classList.remove('active'));
        
        // Add active class to clicked button
        btn.classList.add('active');
        
        // Here you would toggle pricing content
        // For now, we're just updating the UI
      });
    });
  }
  
  // Smooth scrolling for anchor links
  const anchorLinks = document.querySelectorAll('a[href^="#"]:not([href="#"])');
  
  if (anchorLinks.length > 0) {
    anchorLinks.forEach(link => {
      link.addEventListener('click', function(e) {
        e.preventDefault();
        
        const target = document.querySelector(this.getAttribute('href'));
        
        if (target) {
          // Close mobile menu if open
          if (menuToggle && menuToggle.classList.contains('active')) {
            menuToggle.classList.remove('active');
            navList.classList.remove('active');
          }
          
          // Scroll to the target
          window.scrollTo({
            top: target.offsetTop - 80, // Account for fixed header
            behavior: 'smooth'
          });
        }
      });
    });
  }
  
  // Form submission (prevent default)
  const forms = document.querySelectorAll('form');
  
  if (forms.length > 0) {
    forms.forEach(form => {
      form.addEventListener('submit', (e) => {
        e.preventDefault();
        
        // Show a success message
        const formParent = form.parentElement;
        const input = form.querySelector('input');
        
        if (input && input.value) {
          // Clear the input
          input.value = '';
          
          // Create success message
          const successMsg = document.createElement('p');
          successMsg.textContent = 'Obrigado por se inscrever!';
          successMsg.style.color = '#10b981';
          
          // Add success message to the form parent
          formParent.appendChild(successMsg);
          
          // Remove the message after 3 seconds
          setTimeout(() => {
            successMsg.remove();
          }, 3000);
        }
      });
    });
  }
  
  // Create placeholder for logo image
  const logoPlaceholder = document.getElementById('logo-placeholder');
  if (logoPlaceholder) {
    logoPlaceholder.textContent = 'Kombinu';
  }
  
  const footerLogoPlaceholder = document.getElementById('footer-logo-placeholder');
  if (footerLogoPlaceholder) {
    footerLogoPlaceholder.textContent = 'Kombinu';
  }
  
  // Create placeholders for feature icons
  const iconIds = ['gamification-icon', 'offline-icon', 'library-icon', 'curriculum-icon'];
  const iconTexts = ['🎮', '📲', '📚', '🧠'];
  
  iconIds.forEach((id, index) => {
    const icon = document.getElementById(id);
    if (icon) {
      icon.textContent = iconTexts[index];
    }
  });
  
  // Create placeholder for hero image
  const heroPlaceholder = document.getElementById('hero-placeholder');
  if (heroPlaceholder) {
    heroPlaceholder.style.backgroundColor = 'rgba(255, 255, 255, 0.2)';
    const text = document.createElement('div');
    text.textContent = '🧑‍🎓 👨‍🎓 👩‍🎓';
    text.style.fontSize = '3rem';
    text.style.display = 'flex';
    text.style.alignItems = 'center';
    text.style.justifyContent = 'center';
    text.style.height = '100%';
    heroPlaceholder.appendChild(text);
  }
});