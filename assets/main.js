window.dataLayer = window.dataLayer || [];
document.addEventListener('click', function(e){
  var a = e.target && e.target.closest ? e.target.closest('a[href]') : null;
  if(!a) return;
  var h = a.getAttribute('href') || '';
  if(h.indexOf('wa.me') !== -1) window.dataLayer.push({event: 'whatsapp_click', page_path: location.pathname});
  else if(h.indexOf('tel:') === 0) window.dataLayer.push({event: 'phone_click', page_path: location.pathname});
});
(function(){
  var toggle = document.querySelector('.menu-toggle');
  var mobileLinks = document.querySelector('.mobile-links');
  if(toggle && mobileLinks){
    toggle.addEventListener('click', function(){
      mobileLinks.classList.toggle('open');
    });
  }
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
  document.querySelectorAll('form[data-karahan-form]').forEach(function(form){
    var submitBtn = form.querySelector('button[type="submit"]');
    form.addEventListener('submit', function(ev){
      ev.preventDefault();
      var honeypot = form.querySelector('input[name="website"]');
      if(honeypot && honeypot.value){
        return;
      }
      if(typeof form.reportValidity === 'function' && !form.reportValidity()){
        return;
      }
      if(submitBtn){
        if(submitBtn.disabled) return;
        submitBtn.disabled = true;
        setTimeout(function(){ submitBtn.disabled = false; }, 4000);
      }
      window.dataLayer = window.dataLayer || [];
      window.dataLayer.push({event: 'contact_form_submit_attempt', page_path: location.pathname});
      var data = new FormData(form);
      var lines = [];
      data.forEach(function(v,k){ if(v && k !== 'website') lines.push(k + ': ' + v); });
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
  document.querySelectorAll('.cur-year').forEach(function(el){ el.textContent = new Date().getFullYear(); });
  var cards = document.querySelectorAll('.listing-card');
  if(cards.length){
    var qs = new URLSearchParams(window.location.search);
    var fBolge = qs.get('bolge') || '';
    var fKategori = qs.get('kategori') || '';
    if(fBolge || fKategori){
      var REGION_NAMES = {
        kagithane:'Kağıthane', sisli:'Şişli', besiktas:'Beşiktaş', levent:'Levent', etiler:'Etiler',
        nisantasi:'Nişantaşı', sariyer:'Sarıyer', gokturk:'Göktürk', kemerburgaz:'Kemerburgaz',
        alibeykoy:'Alibeyköy', pendik:'Pendik', sultanbeyli:'Sultanbeyli', kadikoy:'Kadıköy'
      };
      var matched = 0;
      cards.forEach(function(card){
        var okBolge = !fBolge || card.getAttribute('data-bolge') === fBolge;
        var okKategori = !fKategori || card.getAttribute('data-kategori') === fKategori;
        var show = okBolge && okKategori;
        card.style.display = show ? '' : 'none';
        if(show) matched++;
      });
      var grid = cards[0].closest('.grid');
      var noticeParts = [];
      if(fBolge) noticeParts.push(REGION_NAMES[fBolge] || fBolge);
      if(fKategori) noticeParts.push(fKategori);
      var noticeLabel = noticeParts.join(' · ');
      if(grid){
        var notice = document.createElement('div');
        notice.className = 'search-filter-notice';
        notice.style.cssText = 'background:rgba(212,178,122,.1);border:1px solid var(--line);border-radius:12px;padding:16px 20px;margin-bottom:18px;color:var(--muted);font-size:.92rem;';
        if(matched > 0){
          notice.innerHTML = '<strong style="color:var(--gold-light);">' + noticeLabel + '</strong> için uygun seçenekler aşağıda listeleniyor. ' +
            'Tüm seçenekleri görmek için <a href="?" style="color:var(--gold-light);">filtreyi temizleyin</a>.';
        } else {
          notice.innerHTML = '<strong style="color:var(--gold-light);">' + noticeLabel + '</strong> kriterine tam uyan örnek ilanımız şu anda yok. ' +
            'Ancak bu kritere uygun fırsatları sizin için araştırabiliriz — ' +
            '<a href="iletisim.html" style="color:var(--gold-light);">bize ulaşın</a> ya da ' +
            '<a href="https://wa.me/905017017908?text=' + encodeURIComponent('Merhaba, ' + noticeLabel + ' kriterinde gayrimenkul arıyorum.') + '" target="_blank" rel="noopener" style="color:var(--gold-light);">WhatsApp üzerinden yazın</a>.';
        }
        grid.parentNode.insertBefore(notice, grid);
      }
    }
  }
})();
