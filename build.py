#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Static site generator for Karahan Gayrimenkul."""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))

PHONE_DISPLAY = "0501 701 79 08"
PHONE_TEL = "+905017017908"
WA_NUMBER = "905017017908"
EMAIL = "info@karahangayrimenkul.com"
SITE = "https://y73755-commits.github.io/karahangayrimenkul"
BRAND = "Karahan Gayrimenkul"
ADDRESS = "Gültepe Mah., Kağıthane / İstanbul"

REGIONS = [
    ("kagithane", "Kağıthane"),
    ("sisli", "Şişli"),
    ("besiktas", "Beşiktaş"),
    ("levent", "Levent"),
    ("etiler", "Etiler"),
    ("nisantasi", "Nişantaşı"),
    ("sariyer", "Sarıyer"),
    ("gokturk", "Göktürk"),
    ("kemerburgaz", "Kemerburgaz"),
    ("alibeykoy", "Alibeyköy"),
    ("pendik", "Pendik"),
    ("sultanbeyli", "Sultanbeyli"),
    ("kadikoy", "Kadıköy"),
]

SERVICES = [
    dict(slug="konut-alim-satim", title="Konut Alım & Satım", link="satilik.html", icon="home",
         short="Daire, rezidans ve müstakil ev alım-satım süreçlerinde uçtan uca danışmanlık."),
    dict(slug="konut-kiralama", title="Konut Kiralama", link="kiralik.html", icon="key",
         short="Kiracı ve mülk sahipleri için güvenli, şeffaf kiralama süreci yönetimi."),
    dict(slug="ticari-gayrimenkul", title="Ticari Gayrimenkul (Dükkan / Mağaza)", link="ticari-gayrimenkul.html", icon="store",
         short="Dükkan, mağaza ve cadde üzeri ticari alanlarda alım-satım ve kiralama danışmanlığı."),
    dict(slug="plaza-ofis", title="Plaza & Ofis", link="plaza-ofis.html", icon="building",
         short="Kurumsal ofis ve plaza katı arayışlarında konum, metrekare ve bütçe danışmanlığı."),
    dict(slug="arsa-alim-satim", title="Arsa Alım & Satım", link="arsa.html", icon="map",
         short="İmar durumu netliği aranan arsalarda alım-satım danışmanlığı."),
    dict(slug="kat-karsiligi", title="Kat Karşılığı Arsa & Proje Geliştirme", link="kat-karsiligi-arsa-proje-gelistirme.html", icon="crane",
         short="Minimum 1.000 m², tek tapulu ve hisseli olmayan arsalarda proje geliştirme danışmanlığı."),
    dict(slug="yatirim-danismanligi", title="Yatırım Danışmanlığı", link="hizmetler.html#yatirim-danismanligi", icon="chart",
         short="Bölge ve proje bazlı değerlendirmelerle doğru yatırım kararları için danışmanlık."),
    dict(slug="gayrimenkul-pazarlama", title="Gayrimenkul Pazarlama", link="hizmetler.html#gayrimenkul-pazarlama", icon="megaphone",
         short="Portföyünüzün doğru kitleye, doğru dijital ve yerel kanallardan tanıtılması."),
    dict(slug="hukuki-surec-destegi", title="Hukuki Süreç Yönlendirme Desteği", link="hizmetler.html#hukuki-surec-destegi", icon="scale",
         short="Tapu ve sözleşme süreçlerinde yönlendirme; gerektiğinde uzman hukuk danışmanına yönlendirme."),
    dict(slug="kurumsal-danismanlik", title="Kurumsal Gayrimenkul Danışmanlığı", link="hizmetler.html#kurumsal-danismanlik", icon="briefcase",
         short="Şirketlerin taşınmaz portföy yönetimi ve konumlandırma ihtiyaçlarına danışmanlık."),
    dict(slug="proje-pazarlama-temsilcilik", title="Proje Pazarlama & Temsilciliği", link="hizmetler.html#proje-pazarlama-temsilcilik", icon="handshake",
         short="Geliştiricilerin proje satış ve pazarlama süreçlerinde temsilcilik hizmeti."),
    dict(slug="degerleme-danismanligi", title="Gayrimenkul Değerleme Danışmanlığı", link="hizmetler.html#degerleme-danismanligi", icon="target",
         short="Konum, emsal ve piyasa koşullarına dayalı profesyonel değerlendirme danışmanlığı."),
]

NAV_ITEMS = [
    ("hizmetler.html", "Hizmetler"),
    ("bolgeler.html", "Bölgeler"),
    ("satilik.html", "Satılık"),
    ("kiralik.html", "Kiralık"),
    ("kurumsal.html", "Kurumsal"),
    ("blog.html", "Blog"),
    ("iletisim.html", "İletişim"),
]

def wa_link(text):
    from urllib.parse import quote
    return f"https://wa.me/{WA_NUMBER}?text={quote(text)}"

def logo_svg():
    return (
        "<svg viewBox='0 0 48 48' fill='none'>"
        "<defs><linearGradient id='g' x1='0' y1='0' x2='1' y2='1'>"
        "<stop offset='0' stop-color='#D4B27A'/><stop offset='1' stop-color='#C9A46A'/></linearGradient></defs>"
        "<text x='24' y='34' font-family='Georgia,serif' font-size='28' font-weight='700' "
        "text-anchor='middle' fill='url(#g)'>K</text></svg>"
    )

def head(title, description, path_prefix, canonical_path, og_image="assets/favicon-512.png", robots="index, follow"):
    favicon = (
        "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E"
        "%3Crect width='64' height='64' rx='12' fill='%2305070A'/%3E"
        "%3Ctext x='32' y='42' font-family='Georgia,serif' font-size='30' fill='%23C9A46A' "
        "text-anchor='middle'%3EK%3C/text%3E%3C/svg%3E"
    )
    canonical = f"{SITE}/{canonical_path}"
    og_image_full = f"{SITE}/{og_image}"
    return f"""<!DOCTYPE html>
<html lang="tr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{canonical}">
<meta name="robots" content="{robots}">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{og_image_full}">
<meta property="og:locale" content="tr_TR">
<meta property="og:site_name" content="{BRAND}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{description}">
<meta name="twitter:image" content="{og_image_full}">
<link rel="icon" href="{favicon}">
<link rel="apple-touch-icon" href="{path_prefix}assets/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{path_prefix}assets/styles.css?v=3">
{json_ld()}
</head>
"""

def json_ld():
    return f"""<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "RealEstateAgent",
  "name": "{BRAND}",
  "image": "{SITE}/assets/favicon-512.png",
  "telephone": "{PHONE_TEL}",
  "email": "{EMAIL}",
  "url": "{SITE}/index.html",
  "areaServed": [{", ".join('"' + n + '"' for _, n in REGIONS)}],
  "address": {{
    "@type": "PostalAddress",
    "streetAddress": "Gültepe Mahallesi",
    "addressLocality": "Kağıthane",
    "addressRegion": "İstanbul",
    "addressCountry": "TR"
  }},
  "sameAs": []
}}
</script>"""

def header(path_prefix, active=""):
    def nav_link(href, label):
        cls = ' class="active"' if href == active else ''
        return f'<a href="{path_prefix}{href}"{cls}>{label}</a>'
    links = "\n      ".join(nav_link(href, label) for href, label in NAV_ITEMS)
    mobile_links = "\n    ".join(
        f'<a href="{path_prefix}{href}">{label}</a>' for href, label in NAV_ITEMS
    )
    return f"""<header>
  <div class="wrap nav-row">
    <a href="{path_prefix}index.html" class="brand-lockup">
      <div class="brand-mark">{logo_svg()}</div>
      <div class="brand-word">
        <div class="word-1">Karahan</div>
        <div class="word-2">Gayrimenkul</div>
      </div>
    </a>
    <nav class="links">
      {links}
    </nav>
    <div class="header-actions">
      <a class="phone-chip" href="tel:{PHONE_TEL}">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.127.96.362 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.338 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
        <span>{PHONE_DISPLAY}</span>
      </a>
      <a class="btn btn-gold btn-sm" href="{path_prefix}iletisim.html">İletişime Geç</a>
      <button class="menu-toggle" aria-label="Menü">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M3 6h18M3 12h18M3 18h18"/></svg>
      </button>
    </div>
  </div>
  <div class="mobile-links">
    {mobile_links}
    <a href="{path_prefix}iletisim.html">İletişime Geç</a>
  </div>
</header>
"""

def wa_float():
    return f"""<a class="wa-float" href="{wa_link('Merhaba, Karahan Gayrimenkul hakkında bilgi almak istiyorum.')}" target="_blank" rel="noopener" aria-label="WhatsApp">
  <svg viewBox="0 0 32 32"><path d="M16.01 2.4C8.5 2.4 2.4 8.5 2.4 16c0 2.53.7 4.9 1.92 6.93L2.4 29.6l6.86-1.87a13.5 13.5 0 0 0 6.75 1.8h.01c7.5 0 13.6-6.1 13.6-13.6S23.5 2.4 16.01 2.4zm7.94 19.4c-.34.96-1.68 1.76-2.76 1.99-.73.15-1.68.27-4.9-1.05-3.86-1.6-6.35-5.53-6.55-5.79-.19-.26-1.57-2.09-1.57-3.99 0-1.9.99-2.83 1.35-3.22.34-.37.75-.46 1-.46.25 0 .5 0 .72.01.23.01.54-.09.84.65.34.83 1.16 2.86 1.26 3.07.1.2.17.44.03.71-.13.27-.2.44-.4.68-.2.24-.42.53-.6.71-.2.2-.41.42-.18.82.24.4 1.06 1.75 2.27 2.84 1.56 1.39 2.87 1.82 3.28 2.02.4.2.64.17.87-.1.24-.27 1.03-1.2 1.3-1.61.28-.4.55-.34.92-.2.37.13 2.36 1.11 2.76 1.32.4.2.67.3.77.47.1.17.1.98-.24 1.94z"/></svg>
</a>"""

def cookie_banner(path_prefix):
    return f"""<div class="cookie-banner">
  <p>Sitemizde deneyiminizi iyileştirmek için temel çerezler kullanılmaktadır. Detaylı bilgi için <a href="{path_prefix}cerez-politikasi.html">Çerez Politikası</a>'nı inceleyebilirsiniz.</p>
  <div class="cookie-actions">
    <button class="btn btn-outline btn-sm" data-cookie-reject type="button">Reddet</button>
    <button class="btn btn-gold btn-sm" data-cookie-accept type="button">Kabul Et</button>
  </div>
</div>"""

def footer(path_prefix):
    region_links = "\n          ".join(
        f'<li><a href="{path_prefix}bolgeler/{slug}.html">{name}</a></li>' for slug, name in REGIONS
    )
    return f"""<footer>
  <div class="wrap">
    <div class="footer-grid">
      <div>
        <div class="footer-brand">
          <div class="brand-mark">{logo_svg()}</div>
          <div class="brand-word">
            <div class="word-1">Karahan</div>
            <div class="word-2">Gayrimenkul</div>
          </div>
        </div>
        <p style="max-width:34ch;font-size:.92rem;">Doğru yatırım, güvenli gelecek. İstanbul'un seçili bölgelerinde konut, ticari gayrimenkul ve kat karşılığı arsa danışmanlığı.</p>
        <div style="display:flex;align-items:flex-start;gap:10px;margin-top:16px;color:var(--muted);font-size:.86rem;">
          <span style="flex:none;color:var(--gold);">{icon('pin')}</span><span>{ADDRESS}</span>
        </div>
      </div>
      <div>
        <h4>Hizmetler</h4>
        <ul>
          <li><a href="{path_prefix}satilik.html">Satılık</a></li>
          <li><a href="{path_prefix}kiralik.html">Kiralık</a></li>
          <li><a href="{path_prefix}ticari-gayrimenkul.html">Ticari Gayrimenkul</a></li>
          <li><a href="{path_prefix}plaza-ofis.html">Plaza & Ofis</a></li>
          <li><a href="{path_prefix}arsa.html">Arsa</a></li>
          <li><a href="{path_prefix}kat-karsiligi-arsa-proje-gelistirme.html">Kat Karşılığı Arsa</a></li>
          <li><a href="{path_prefix}hizmetler.html">Tüm Hizmetler →</a></li>
        </ul>
      </div>
      <div>
        <h4>Bölgeler</h4>
        <ul>
          {region_links}
        </ul>
      </div>
      <div>
        <h4>İletişim</h4>
        <ul>
          <li><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></li>
          <li><a href="{wa_link('Merhaba, bilgi almak istiyorum.')}" target="_blank" rel="noopener">WhatsApp</a></li>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li><a href="{path_prefix}iletisim.html">İletişim Formu →</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© <span class="cur-year"></span> {BRAND}. Tüm hakları saklıdır.</span>
      <div style="display:flex;gap:16px;">
        <a href="{path_prefix}kvkk.html">KVKK</a>
        <a href="{path_prefix}gizlilik-politikasi.html">Gizlilik Politikası</a>
        <a href="{path_prefix}cerez-politikasi.html">Çerez Politikası</a>
        <a href="{path_prefix}kullanim-kosullari.html">Kullanım Koşulları</a>
      </div>
    </div>
  </div>
</footer>"""

def page(title, description, path_prefix, canonical_path, active, body, og_image="assets/favicon-512.png", robots="index, follow", extra_head=""):
    return f"""{head(title, description, path_prefix, canonical_path, og_image, robots)}<body>
{header(path_prefix, active)}
{wa_float()}
<main id="top">
{body}
</main>
{footer(path_prefix)}
{cookie_banner(path_prefix)}
<script src="{path_prefix}assets/main.js?v=3"></script>
</body>
</html>
"""

def write(relpath, content):
    full = os.path.join(ROOT, relpath)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)
    print("wrote", relpath)

ICONS = {
  "home": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M3 11.5 12 4l9 7.5"/><path d="M5 10v10h14V10"/><path d="M9.5 20v-6h5v6"/></svg>',
  "building": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><rect x="4" y="3" width="9" height="18"/><rect x="15" y="8" width="5" height="13"/><path d="M7 7h3M7 11h3M7 15h3"/></svg>',
  "key": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="8" cy="15" r="4"/><path d="M11 12l9-9M17 6l3 3M14 9l2 2"/></svg>',
  "handshake": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M2 12l4-4 4 3 3-3 4 4"/><path d="M9 15l3 3 3-3"/><path d="M14 11l4 4 3-3"/></svg>',
  "chart": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M4 20V10M12 20V4M20 20v-7"/></svg>',
  "target": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="4"/><circle cx="12" cy="12" r=".6" fill="currentColor"/></svg>',
  "camera": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><rect x="3" y="7" width="18" height="13" rx="2"/><path d="M9 7l1.5-2.5h3L15 7"/><circle cx="12" cy="13.5" r="3.5"/></svg>',
  "shield": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/></svg>',
  "map": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M12 22s8-7.5 8-13a8 8 0 1 0-16 0c0 5.5 8 13 8 13z"/><circle cx="12" cy="9" r="3"/></svg>',
  "doc": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M6 2h9l3 3v17H6z"/><path d="M14 2v4h4M9 12h6M9 16h6"/></svg>',
  "pin": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M12 21s7-6.1 7-11.5A7 7 0 0 0 5 9.5C5 14.9 12 21 12 21Z"/><circle cx="12" cy="9.5" r="2.3"/></svg>',
  "store": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M4 9 5 4h14l1 5"/><path d="M4 9h16v9a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V9Z"/><path d="M9 19v-5h6v5"/></svg>',
  "crane": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M4 20h6M6 20V6l12-2v4H8"/><path d="M18 8v6M18 14l3 6M18 14l-4 3"/></svg>',
  "megaphone": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M3 11v2a2 2 0 0 0 2 2h1l3 5V6L6 11H5a2 2 0 0 0-2 0Z"/><path d="M9 8l10-4v16L9 16"/></svg>',
  "scale": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M12 3v18M6 8l-3 6a3 3 0 0 0 6 0Zm12 0-3 6a3 3 0 0 0 6 0Z"/><path d="M4 21h16M6 8h12"/></svg>',
  "briefcase": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><rect x="3" y="8" width="18" height="12" rx="1.5"/><path d="M8 8V6a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2M3 13h18"/></svg>',
}

def icon(name):
    return ICONS.get(name, ICONS["home"])
