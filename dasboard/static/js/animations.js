document.addEventListener('DOMContentLoaded', () => {
  // Scroll animation for elements
  const animateOnScroll = () => {
    const elements = document.querySelectorAll('.animate-on-scroll');
    
    elements.forEach(element => {
      const elementPosition = element.getBoundingClientRect().top;
      const windowHeight = window.innerHeight;
      
      if (elementPosition < windowHeight * 0.85) {
        element.classList.add('visible');
      }
    });
  };
  
  // Run on load
  animateOnScroll();
  
  // Run on scroll
  window.addEventListener('scroll', animateOnScroll);
  
  // Feature card hover effects
  const featureCards = document.querySelectorAll('.feature-card');
  
  featureCards.forEach(card => {
    card.addEventListener('mouseenter', () => {
      // Add subtle rotation
      card.style.transform = 'translateY(-10px) rotate(1deg)';
    });
    
    card.addEventListener('mouseleave', () => {
      // Remove rotation, keep the translateY from CSS
      card.style.transform = 'translateY(-10px)';
      
      // After transition is complete, remove inline style to revert to CSS
      setTimeout(() => {
        card.style.transform = '';
      }, 300);
    });
  });
  
  // Animate circle charts in metrics section
  const animateCharts = () => {
    const charts = document.querySelectorAll('.circular-chart');
    
    charts.forEach(chart => {
      const circle = chart.querySelector('.circle');
      
      if (circle) {
        const dashArray = circle.getAttribute('stroke-dasharray');
        
        if (dashArray) {
          const value = parseFloat(dashArray.split(',')[0]);
          
          // Reset the animation
          circle.style.strokeDasharray = '0, 100';
          
          // Force reflow
          void circle.offsetWidth;
          
          // Start animation
          setTimeout(() => {
            circle.style.strokeDasharray = `${value}, 100`;
            circle.style.transition = 'stroke-dasharray 1.5s ease-out';
          }, 100);
        }
      }
    });
  };
  
  // Use Intersection Observer to trigger chart animation when visible
  if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          animateCharts();
          observer.disconnect(); // Only animate once
        }
      });
    }, { threshold: 0.5 });
    
    const metricsSection = document.querySelector('.metrics');
    if (metricsSection) {
      observer.observe(metricsSection);
    }
  } else {
    // Fallback for browsers without Intersection Observer
    window.addEventListener('scroll', () => {
      const metricsSection = document.querySelector('.metrics');
      
      if (metricsSection) {
        const position = metricsSection.getBoundingClientRect().top;
        
        if (position < window.innerHeight * 0.7) {
          animateCharts();
          // Remove event listener after triggering
          window.removeEventListener('scroll', animateCharts);
        }
      }
    });
  }
  
  // Hero section parallax effect
  const hero = document.querySelector('.hero');
  const heroContent = document.querySelector('.hero-content');
  
  if (hero && heroContent) {
    window.addEventListener('scroll', () => {
      const scrollPosition = window.scrollY;
      
      if (scrollPosition < 500) {
        heroContent.style.transform = `translateY(${scrollPosition * 0.2}px)`;
        hero.style.backgroundPositionY = `${scrollPosition * 0.5}px`;
      }
    });
  }
  
  // Animate table rows on scroll
  const animateTableRows = () => {
    const rows = document.querySelectorAll('.leaderboard-table tbody tr');
    
    rows.forEach((row, index) => {
      // Add a staggered animation delay
      setTimeout(() => {
        row.style.opacity = '1';
        row.style.transform = 'translateX(0)';
      }, 100 * index);
    });
  };
  
  // Style table rows initially
  const tableRows = document.querySelectorAll('.leaderboard-table tbody tr');
  tableRows.forEach(row => {
    row.style.opacity = '0';
    row.style.transform = 'translateX(-20px)';
    row.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
  });
  
  // Use Intersection Observer for table animation
  if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          animateTableRows();
          observer.disconnect(); // Only animate once
        }
      });
    }, { threshold: 0.2 });
    
    const leaderboardSection = document.querySelector('.leaderboard');
    if (leaderboardSection) {
      observer.observe(leaderboardSection);
    }
  } else {
    // Fallback
    window.addEventListener('scroll', () => {
      const leaderboardSection = document.querySelector('.leaderboard');
      
      if (leaderboardSection) {
        const position = leaderboardSection.getBoundingClientRect().top;
        
        if (position < window.innerHeight * 0.8) {
          animateTableRows();
          // Remove event listener after triggering
          window.removeEventListener('scroll', animateTableRows);
        }
      }
    });
  }
  
  // Animate pricing cards on hover
  const pricingCards = document.querySelectorAll('.pricing-card');
  
  pricingCards.forEach(card => {
    card.addEventListener('mouseenter', () => {
      // Highlight other features
      const features = card.querySelectorAll('.pricing-features li');
      
      features.forEach((feature, index) => {
        setTimeout(() => {
          feature.style.transform = 'translateX(5px)';
          feature.style.transition = 'transform 0.3s ease';
        }, index * 100);
      });
    });
    
    card.addEventListener('mouseleave', () => {
      // Reset features
      const features = card.querySelectorAll('.pricing-features li');
      
      features.forEach(feature => {
        feature.style.transform = '';
      });
    });
  });

  // Team cards animation
  const teamCards = document.querySelectorAll('.team-card');
  
  const observerOptions = {
    threshold: 0.2,
    rootMargin: '0px'
  };
  
  const teamObserver = new IntersectionObserver((entries) => {
    entries.forEach((entry, index) => {
      if (entry.isIntersecting) {
        setTimeout(() => {
          entry.target.style.opacity = '1';
          entry.target.style.transform = 'translateY(0)';
        }, index * 100);
      }
    });
  }, observerOptions);
  
  teamCards.forEach(card => {
    card.style.opacity = '0';
    card.style.transform = 'translateY(20px)';
    card.style.transition = 'all 0.6s ease';
    teamObserver.observe(card);
  });
  
  // Timeline animation
  const timelineItems = document.querySelectorAll('.timeline-item');
  
  const timelineObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
      }
    });
  }, observerOptions);
  
  timelineItems.forEach(item => {
    item.style.opacity = '0';
    item.style.transform = 'translateX(-20px)';
    item.style.transition = 'all 0.6s ease';
    
    timelineObserver.observe(item);
  });
});