/* Telefon/WhatsApp tıklama ölçümü ve çerez izni: assets/olcum.js */
(function(){
  var toggle = document.querySelector('.menu-toggle');
  var mobileLinks = document.querySelector('.mobile-links');
  if(toggle && mobileLinks){
    toggle.setAttribute('aria-expanded','false');
    toggle.addEventListener('click', function(){
      var isOpen = mobileLinks.classList.toggle('open');
      toggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
    });
    document.addEventListener('keydown', function(e){
      if(e.key === 'Escape' && mobileLinks.classList.contains('open')){
        mobileLinks.classList.remove('open');
        toggle.setAttribute('aria-expanded','false');
      }
    });
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
  /* İletişim formu → WhatsApp mesajı. Bilgiler sunucuya gönderilmez; ziyaretçi WhatsApp'ta "Gönder"e basınca bize ulaşır.
     Ölçüm: her gönderme denemesi "form_submit_attempt" (valid=true/false); yalnızca geçerli formda
     "whatsapp_message_prepared" (aynı mesaj oturumda bir kez). Hiçbiri "talep teslim edildi" anlamına gelmez. */
  var ETIKET = { ad_soyad: 'Ad Soyad', telefon: 'Telefon', eposta: 'E-posta', mesaj: 'Mesaj' };
  document.querySelectorAll('form[data-karahan-form]').forEach(function(form){
    var formAdi = form.getAttribute('data-form-name') || 'iletisim';
    var submitBtn = form.querySelector('button[type="submit"]');
    var statusBox = form.querySelector('.form-status');
    function durum(html){ if(statusBox){ statusBox.innerHTML = html; statusBox.style.display = 'block'; } }
    form.addEventListener('submit', function(ev){
      ev.preventDefault();
      var honeypot = form.querySelector('input[name="website"]');
      if(honeypot && honeypot.value) return;
      if(typeof form.checkValidity === 'function' && !form.checkValidity()){
        var hatali = form.querySelector('input:invalid, textarea:invalid, select:invalid');
        if(window.olcum) window.olcum.formDenemesi(formAdi, false, hatali ? hatali.name : '');
        form.reportValidity();
        return;
      }
      if(submitBtn && submitBtn.disabled) return;
      if(window.olcum) window.olcum.formDenemesi(formAdi, true);
      var lines = [];
      new FormData(form).forEach(function(v, k){ v = String(v).trim(); if(v && k !== 'website') lines.push((ETIKET[k] || k) + ': ' + v); });
      var metin = 'Merhaba, Karahan Gayrimenkul web sitesindeki iletişim formundan yazıyorum:\n' + lines.join('\n');
      var waLink = 'https://wa.me/905017017908?text=' + encodeURIComponent(metin);
      var win = null;
      try { win = window.open(waLink, '_blank'); } catch(e) { win = null; }
      if(win){
        try { win.opener = null; } catch(e) {}
        durum('Mesajınız WhatsApp’ta hazırlandı. <strong>Son adım:</strong> açılan WhatsApp ekranında <strong>Gönder</strong>’e basın; siz göndermeden mesaj bize ulaşmaz. ' +
          'WhatsApp açılmadıysa <a href="' + waLink + '" target="_blank" rel="noopener" data-loc="form_fallback">buradan açın</a>.');
      } else {
        durum('WhatsApp penceresi otomatik açılamadı (tarayıcınız engellemiş olabilir). Mesajınız hazır: ' +
          '<a class="btn btn-gold btn-sm" style="margin-top:10px;" href="' + waLink + '" target="_blank" rel="noopener" data-loc="form_fallback">WhatsApp’ta mesajı aç</a> ' +
          'bağlantısına dokunun, ardından açılan ekranda <strong>Gönder</strong>’e basın.');
      }
      if(window.olcum) window.olcum.whatsappHazirlandi(formAdi, metin);
      if(submitBtn){ submitBtn.disabled = true; setTimeout(function(){ submitBtn.disabled = false; }, 4000); }
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
      var KATEGORI_NAMES = { konut:'Konut', arsa:'Arsa', 'plaza-ofis':'Plaza ve Ofis', ticari:'Ticari' };
      if(fKategori) noticeParts.push(KATEGORI_NAMES[fKategori] || fKategori);
      var noticeLabel = noticeParts.join(' · ');
      var noticeLabelHtml = noticeLabel.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;').replace(/'/g,'&#39;');
      if(grid){
        var notice = document.createElement('div');
        notice.className = 'search-filter-notice';
        notice.style.cssText = 'background:rgba(212,178,122,.1);border:1px solid var(--line);border-radius:12px;padding:16px 20px;margin-bottom:18px;color:var(--muted);font-size:.92rem;';
        if(matched > 0){
          notice.innerHTML = '<strong style="color:var(--gold-light);">' + noticeLabelHtml + '</strong> için uygun seçenekler aşağıda listeleniyor. ' +
            'Tüm seçenekleri görmek için <a href="?" style="color:var(--gold-light);">filtreyi temizleyin</a>.';
        } else {
          notice.innerHTML = '<strong style="color:var(--gold-light);">' + noticeLabelHtml + '</strong> kriterine tam uyan örnek ilanımız şu anda yok. ' +
            'Ancak bu kritere uygun fırsatları sizin için araştırabiliriz — ' +
            '<a href="iletisim.html" style="color:var(--gold-light);">bize ulaşın</a> ya da ' +
            '<a href="https://wa.me/905017017908?text=' + encodeURIComponent('Merhaba Karahan Gayrimenkul, ' + noticeLabel + ' kriterinde gayrimenkul arıyorum.') + '" target="_blank" rel="noopener" style="color:var(--gold-light);">WhatsApp üzerinden yazın</a>.';
        }
        grid.parentNode.insertBefore(notice, grid);
      }
    }
  }
})();
