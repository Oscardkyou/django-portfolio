
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
  const experimentsLoad = document.getElementById('ai-experiments-load');
  const experimentsOutput = document.getElementById('ai-experiments-output');
  const predictSubmit = document.getElementById('ai-predict-submit');
  const predictOutput = document.getElementById('ai-predict-output');
  const predictTeamSize = document.getElementById('predict-team-size');
  const predictDuration = document.getElementById('predict-duration');
  const predictAiFeatures = document.getElementById('predict-ai-features');

  if (chatSubmit && chatInput && chatOutput) {
    chatSubmit.addEventListener('click', async () => {
      const message = chatInput.value.trim();
      if (!message) {
        chatOutput.textContent = 'Enter a question first.';
        return;
      }

      chatOutput.textContent = 'Loading...';
      const response = await fetch(chatSubmit.dataset.endpoint, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message }),
      });
      const data = await response.json();
      chatOutput.textContent = data.answer || data.detail || 'No response received.';
    });
  }

  if (experimentsLoad && experimentsOutput) {
    experimentsLoad.addEventListener('click', async () => {
      experimentsOutput.textContent = 'Loading...';
      const response = await fetch(experimentsLoad.dataset.endpoint);
      const data = await response.json();
      const experiments = data.experiments || [];
      if (!experiments.length) {
        experimentsOutput.textContent = 'No experiments found.';
        return;
      }
      experimentsOutput.innerHTML = experiments.map((item) => (
        `<div class="ai-demo-item"><strong>${item.name}</strong><br>Accuracy: ${item.accuracy}<br>Version: ${item.model_version}<br>Stage: ${item.stage}</div>`
      )).join('');
    });
  }

  if (predictSubmit && predictOutput && predictTeamSize && predictDuration && predictAiFeatures) {
    predictSubmit.addEventListener('click', async () => {
      predictOutput.textContent = 'Loading...';
      const payload = {
        team_size: Number(predictTeamSize.value),
        duration_months: Number(predictDuration.value),
        ai_features: Boolean(predictAiFeatures.checked),
      };

      const response = await fetch(predictSubmit.dataset.endpoint, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(payload),
      });
      const data = await response.json();
      if (!response.ok) {
        predictOutput.textContent = data.detail || 'Prediction failed.';
        return;
      }
      predictOutput.innerHTML = `Complexity score: <strong>${data.complexity_score}</strong><br>Risk level: <strong>${data.risk_level}</strong><br>Recommended team: <strong>${data.recommended_team}</strong>`;
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