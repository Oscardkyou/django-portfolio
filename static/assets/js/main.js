
(function() {
  "use strict";

  const rootBody = document.body;
  const themeToggle = document.getElementById('theme-toggle');
  const savedTheme = localStorage.getItem('site-theme');
  const preferredTheme = savedTheme === 'theme-light' ? 'theme-light' : 'theme-dark';

  if (rootBody) {
    rootBody.classList.remove('theme-dark', 'theme-light');
    rootBody.classList.add(preferredTheme);
  }

  const syncThemeToggleLabel = () => {
    if (!themeToggle) {
      return;
    }
    const currentIsDark = rootBody.classList.contains('theme-dark');
    themeToggle.textContent = currentIsDark ? themeToggle.dataset.lightLabel : themeToggle.dataset.darkLabel;
  };

  if (themeToggle && rootBody) {
    syncThemeToggleLabel();
    themeToggle.addEventListener('click', () => {
      const nextTheme = rootBody.classList.contains('theme-dark') ? 'theme-light' : 'theme-dark';
      rootBody.classList.remove('theme-dark', 'theme-light');
      rootBody.classList.add(nextTheme);
      localStorage.setItem('site-theme', nextTheme);
      syncThemeToggleLabel();
    });
  }

  const chatInput = document.getElementById('ai-chat-input');
  const chatSubmit = document.getElementById('ai-chat-submit');
  const chatOutput = document.getElementById('ai-chat-output');
  const suggestedQuestions = document.querySelectorAll('.ai-suggested-question');

  if (chatSubmit && chatInput && chatOutput) {
    chatSubmit.addEventListener('click', async () => {
      const message = chatInput.value.trim();
      if (!message) {
        chatOutput.textContent = 'Enter a question first.';
        return;
      }

      const endpoint = chatSubmit.dataset.endpoint;
      chatOutput.textContent = 'Thinking...';
      chatSubmit.disabled = true;

      try {
        const response = await fetch(endpoint, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            message,
          }),
        });

        const data = await response.json();
        chatOutput.textContent = data.answer || data.detail || 'AI assistant is temporarily unavailable';
      } catch (error) {
        chatOutput.textContent = 'AI assistant is temporarily unavailable';
      } finally {
        chatSubmit.disabled = false;
      }
    });
  }

  if (suggestedQuestions.length && chatInput && chatSubmit) {
    suggestedQuestions.forEach((button) => {
      button.addEventListener('click', () => {
        chatInput.value = button.dataset.question || '';
        chatSubmit.click();
      });
    });
  }


  const select = (el, all = false) => {
    el = el.trim()
    if (all) {
      return [...document.querySelectorAll(el)]
    } else {
      return document.querySelector(el)
    }
  }


  const on = (type, el, listener, all = false) => {
    let selectEl = select(el, all)
    if (selectEl) {
      if (all) {
        selectEl.forEach(e => e.addEventListener(type, listener))
      } else {
        selectEl.addEventListener(type, listener)
      }
    }
  }


  const onscroll = (el, listener) => {
    el.addEventListener('scroll', listener)
  }


  const burgerMenu = select('.burger')
  on('click', '.burger', function(e) {
    burgerMenu.classList.toggle('active');
  })


  window.addEventListener('load', () => {
    let portfolioContainer = select('#portfolio-grid');
    if (portfolioContainer) {
      let portfolioIsotope = new Isotope(portfolioContainer, {
        itemSelector: '.item',
      });

      let portfolioFilters = select('#filters a', true);

      on('click', '#filters a', function(e) {
        e.preventDefault();
        portfolioFilters.forEach(function(el) {
          el.classList.remove('active');
        });
        this.classList.add('active');

        portfolioIsotope.arrange({
          filter: this.getAttribute('data-filter')
        });
        portfolioIsotope.on('arrangeComplete', function() {
          AOS.refresh()
        });
      }, true);
    }

  });


  new Swiper('.testimonials-slider', {
    speed: 600,
    loop: true,
    autoplay: {
      delay: 5000,
      disableOnInteraction: false
    },
    slidesPerView: 'auto',
    pagination: {
      el: '.swiper-pagination',
      type: 'bullets',
      clickable: true
    }
  });


  window.addEventListener('load', () => {
    AOS.init({
      duration: 1000,
      easing: 'ease-in-out',
      once: true,
      mirror: false
    })
  });

})()