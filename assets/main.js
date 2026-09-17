(function(){
  /* Mobile menu toggle */
  var toggle = document.querySelector('.menu-toggle');
  var mobileLinks = document.querySelector('.mobile-links');
  if(toggle && mobileLinks){
    toggle.addEventListener('click', function(){
      mobileLinks.classList.toggle('open');
    });
  }

  /* Cookie consent banner */
  var cookieBanner = document.querySelector('.cookie-banner');
  if(cookieBanner){
    try{
      if(!localStorage.getItem('karahan_cookie_consent')){
        cookieBanner.classList.add('show');
      }
    }catch(e){
      cookieBanner.classList.add('show');
    }
    var accept = cookieBanner.querySelector('[data-cookie-accept]');
    var reject = cookieBanner.querySelector('[data-cookie-reject]');
    function dismiss(val){
      try{ localStorage.setItem('karahan_cookie_consent', val); }catch(e){}
      cookieBanner.classList.remove('show');
    }
    if(accept) accept.addEventListener('click', function(){ dismiss('accepted'); });
    if(reject) reject.addEventListener('click', function(){ dismiss('rejected'); });
  }

  /* Hero search widget -> redirects to the relevant category page with query params (client-side only, no backend) */
  var searchForm = document.querySelector('form[data-karahan-search]');
  if(searchForm){
    searchForm.addEventListener('submit', function(ev){
      ev.preventDefault();
      var data = new FormData(searchForm);
      var islem = data.get('islem') || 'satilik';
      var kategori = data.get('kategori') || '';
      var bolge = data.get('bolge') || '';
      var map = {
        'satilik': 'satilik.html',
        'kiralik': 'kiralik.html',
        'ticari': 'ticari-gayrimenkul.html',
        'arsa': 'arsa.html',
        'plaza-ofis': 'plaza-ofis.html'
      };
      var target = map[islem] || map[kategori] || 'satilik.html';
      var params = new URLSearchParams();
      if(bolge) params.set('bolge', bolge);
      if(kategori) params.set('kategori', kategori);
      window.location.href = target + (params.toString() ? ('?' + params.toString()) : '');
    });
  }

  /* Contact / demand forms: client-side only (no backend on static hosting).
     We disclose this and offer a mailto + WhatsApp fallback so the message
     is never silently lost. */
  document.querySelectorAll('form[data-karahan-form]').forEach(function(form){
    form.addEventListener('submit', function(ev){
      ev.preventDefault();
      var data = new FormData(form);
      var lines = [];
      data.forEach(function(v,k){ if(v) lines.push(k + ': ' + v); });
      var body = encodeURIComponent(lines.join('\n'));
      var subject = encodeURIComponent('Karahan Gayrimenkul – Web Sitesi Talebi');
      var statusBox = form.querySelector('.form-status');
      var mailto = 'mailto:info@karahangayrimenkul.com?subject=' + subject + '&body=' + body;
      var waText = encodeURIComponent('Merhaba, web sitesi üzerinden iletişim formunu doldurdum:\n' + lines.join('\n'));
      var waLink = 'https://wa.me/905017017908?text=' + waText;
      if(statusBox){
        statusBox.innerHTML = 'Formunuz e-posta istemcinizde hazırlandı. Açılan pencereden gönderebilir, ya da doğrudan ' +
          '<a href="'+waLink+'" target="_blank" rel="noopener">WhatsApp üzerinden</a> bize ulaşabilirsiniz.';
        statusBox.style.display = 'block';
      }
      window.location.href = mailto;
    });
  });

  /* Simple current year */
  document.querySelectorAll('.cur-year').forEach(function(el){ el.textContent = new Date().getFullYear(); });
})();
