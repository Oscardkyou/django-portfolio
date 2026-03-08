
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

  const demoExperiments = [
    {
      name: 'logistics-price-model',
      accuracy: 0.91,
      model_version: 'v1.3',
      stage: 'staging',
    },
    {
      name: 'project-complexity-estimator',
      accuracy: 0.87,
      model_version: 'v0.9',
      stage: 'demo',
    },
  ];

  const getDemoChatAnswer = (message) => {
    const normalizedMessage = message.toLowerCase();

    if (normalizedMessage.includes('project') || normalizedMessage.includes('build')) {
      return 'I built Gravora AI Knowledge Platform, a low-latency streaming backend, and backend-focused engineering case studies around scalable APIs and AI workflows.';
    }

    if (normalizedMessage.includes('stack') || normalizedMessage.includes('skill') || normalizedMessage.includes('technology')) {
      return 'My core stack includes Python, FastAPI, Django, Docker, PostgreSQL, Redis, AWS, and AI-oriented backend architecture.';
    }

    if (normalizedMessage.includes('experience') || normalizedMessage.includes('about')) {
      return 'I focus on backend engineering, AI integration, API design, and production-style systems for scalable products.';
    }

    if (normalizedMessage.includes('rag') || normalizedMessage.includes('ai')) {
      return 'I use AI concepts in backend form: retrieval workflows, orchestration, model-facing APIs, and demo ML/MLOps endpoints.';
    }

    return 'Ask about my projects, stack, backend experience, or AI integrations.';
  };

  const getPredictionResult = (teamSize, durationMonths, aiFeatures) => {
    let score = 0.2;
    score += Math.min(teamSize, 10) * 0.05;
    score += Math.min(durationMonths, 12) * 0.03;
    if (aiFeatures) {
      score += 0.25;
    }

    const complexityScore = Math.min(score, 0.99).toFixed(2);
    let riskLevel = 'low';
    let recommendedTeam = Math.max(teamSize, 2);

    if (Number(complexityScore) >= 0.75) {
      riskLevel = 'high';
      recommendedTeam = Math.max(teamSize, 6);
    } else if (Number(complexityScore) >= 0.45) {
      riskLevel = 'medium';
      recommendedTeam = Math.max(teamSize, 4);
    }

    return {
      complexityScore,
      riskLevel,
      recommendedTeam,
    };
  };

  if (chatSubmit && chatInput && chatOutput) {
    chatSubmit.addEventListener('click', () => {
      const message = chatInput.value.trim();
      if (!message) {
        chatOutput.textContent = 'Enter a question first.';
        return;
      }

      chatOutput.textContent = getDemoChatAnswer(message);
    });
  }

  if (experimentsLoad && experimentsOutput) {
    experimentsLoad.addEventListener('click', () => {
      experimentsOutput.innerHTML = demoExperiments.map((item) => (
        `<div class="ai-demo-item"><strong>${item.name}</strong><br>Accuracy: ${item.accuracy}<br>Version: ${item.model_version}<br>Stage: ${item.stage}</div>`
      )).join('');
    });
  }

  if (predictSubmit && predictOutput && predictTeamSize && predictDuration && predictAiFeatures) {
    predictSubmit.addEventListener('click', () => {
      const teamSize = Number(predictTeamSize.value);
      const durationMonths = Number(predictDuration.value);
      const aiFeatures = Boolean(predictAiFeatures.checked);

      if (!teamSize || !durationMonths || teamSize < 1 || durationMonths < 1) {
        predictOutput.textContent = 'Enter valid values for team size and duration.';
        return;
      }

      const result = getPredictionResult(teamSize, durationMonths, aiFeatures);
      predictOutput.innerHTML = `Complexity score: <strong>${result.complexityScore}</strong><br>Risk level: <strong>${result.riskLevel}</strong><br>Recommended team: <strong>${result.recommendedTeam}</strong>`;
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