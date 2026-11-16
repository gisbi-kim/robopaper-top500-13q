(() => {
  'use strict';
  const key = 'robopaper-top500-language';
  const language = document.documentElement.lang;
  const page = location.pathname.split('/').pop() || 'index.html';
  const query = new URLSearchParams(location.search);
  const explicit = query.get('lang');
  let saved;
  try { saved = localStorage.getItem(key); } catch (_) { /* Links also work without storage. */ }
  const preferred = /^(ko|en)$/.test(explicit || '') ? explicit : language === 'en' ? 'en' : saved;
  if (preferred && preferred !== language && /^(ko|en)$/.test(preferred)) {
    const target = new URL(language === 'en' ? '../' + page : 'en/' + page, location.href);
    target.search = location.search;
    target.hash = location.hash;
    location.replace(target.href);
    return;
  }
  try { localStorage.setItem(key, language); } catch (_) { /* Storage is optional. */ }
  document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('[data-language]').forEach(link => {
      const updateTarget = () => {
        const target = new URL(link.getAttribute('href'), location.href);
        target.search = location.search;
        target.searchParams.set('lang', link.dataset.language);
        target.hash = location.hash;
        link.href = target.href;
      };
      updateTarget();
      link.addEventListener('click', () => {
        updateTarget();
        try { localStorage.setItem(key, link.dataset.language); } catch (_) { /* Optional. */ }
      });
    });
  });
})();
