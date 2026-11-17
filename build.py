#!/usr/bin/env python3
"""Generate the Cocos Locos site (template v2 T1, 2026-11-17).
Mexican restaurant + seafood bar opening soon at 1313 N Combee Rd, Lakeland FL.
Identity: deep sea-teal + coconut cream + coral; DIN Condensed poster caps;
coconut-half mark; wave rules; zero JS, one local stylesheet, inline SVG only.
Copy ONLY from verified card facts (t_e21e7f1b / Business Debut 2026-10-27):
- Owner Kris Cavazos; full-service Mexican restaurant + bar, seafood focus.
- Real coconuts split in half: plates for some seafood dishes, cups for cocktails.
- Menu centers on authentic Mexican food + broad seafood section; aguachiles,
  seafood cocktails, fried fish; team testing recipes before opening.
- Former Pa'Las Miches Bar and Grill space, remodeled; ~176 guests; sit-down.
- Family-friendly day/evening; weekend late-night spot for Corral Event Center
  nightclub guests next door.
- Announced hours once open: Tue–Thu 11 a.m.–10 p.m.; Fri–Sat 11 a.m.–3 a.m.;
  Sun 11 a.m.–midnight; operates Tuesday through Sunday (Monday: closed planned).
- Target opening was "less than a month" from 10-27 — date unconfirmed; GBP has
  no open state yet -> "opening soon" framing everywhere.
NOT published (omitted, never faked): phone, prices, confirmed opening date,
exact coconut-dish lineup, star ratings (no reviews yet).
"""
import json, os

ROOT = os.path.dirname(os.path.abspath(__file__))
PUB = os.path.join(ROOT, "public")
os.makedirs(PUB, exist_ok=True)

ORIGIN = "https://cocos-locos-demo.up.railway.app"
NAME = "Cocos Locos Mexican Restaurant"
BRAND = "Cocos Locos"
STREET = "1313 N Combee Rd"
CITYZIP = "Lakeland, FL 33801"
NAP = f"{STREET}, {CITYZIP}"
EMAIL = "cocoslocosfl@gmail.com"
FB = "https://www.facebook.com/cocoslocosfl"
MAPQ = "https://www.google.com/maps?q=1313%20N%20Combee%20Rd%2C%20Lakeland%2C%20FL%2033801&output=embed"
DIR = "https://www.google.com/maps/dir/?api=1&destination=1313%20N%20Combee%20Rd%2C%20Lakeland%2C%20FL%2033801"
BUILT = "<!-- BUILT-2026-11-17 -->"

REST = {
    "@type": "Restaurant",
    "name": NAME,
    "description": "Full-service Mexican restaurant and bar with a broad seafood section — coconuts split in half serve some of the seafood plates and the cocktails. Opening soon at 1313 N Combee Rd, Lakeland, FL.",
    "servesCuisine": ["Mexican", "Seafood"],
    "address": {
        "@type": "PostalAddress",
        "streetAddress": STREET,
        "addressLocality": "Lakeland",
        "addressRegion": "FL",
        "postalCode": "33801",
        "addressCountry": "US",
    },
    "hasMap": DIR,
    "image": f"{ORIGIN}/og.png",
    "url": f"{ORIGIN}/",
    "sameAs": [FB],
    "openingHoursSpecification": [
        {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Tuesday", "Wednesday", "Thursday"], "opens": "11:00", "closes": "22:00"},
        {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Friday", "Saturday"], "opens": "11:00", "closes": "03:00"},
        {"@type": "OpeningHoursSpecification", "dayOfWeek": "Sunday", "opens": "11:00", "closes": "24:00"},
    ],
}

def ld(obj):
    return f'  <script type="application/ld+json">\n{json.dumps(obj, indent=2)}\n  </script>'

CRUMB = lambda steps: {
    "@context": "https://schema.org", "@type": "BreadcrumbList",
    "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": ORIGIN + p} for i, (n, p) in enumerate(steps)],
}

COCONUT = '''<svg class="cmark" width="__S__" height="__S__" viewBox="0 0 24 24" aria-hidden="true">
<circle cx="12" cy="12" r="10" fill="#4A2D19"/>
<path d="M12 2 a10 10 0 0 1 10 10 h-20 a10 10 0 0 1 10 -10 Z" fill="#5D3B22"/>
<circle cx="12" cy="12" r="7.2" fill="#F6EFDF"/>
<circle cx="9.6" cy="8.6" r="1.15" fill="#4A2D19"/>
<circle cx="14.4" cy="8.6" r="1.15" fill="#4A2D19"/>
<circle cx="12" cy="11.1" r="1.15" fill="#4A2D19"/>
</svg>'''

WAVE = '<svg class="wave" viewBox="0 0 1200 44" preserveAspectRatio="none" aria-hidden="true"><path d="M0 44 L0 22 Q 75 0 150 22 T 300 22 T 450 22 T 600 22 T 750 22 T 900 22 T 1050 22 T 1200 22 L1200 44 Z"/></svg>'

def head(title, desc, path, blocks=None, utility=False):
    u = ORIGIN + path
    noindex = '  <meta name="robots" content="noindex">\n' if utility else ""
    social = "" if utility else (
        f'  <meta property="og:type" content="website">\n'
        f'  <meta property="og:site_name" content="{NAME}">\n'
        f'  <meta property="og:title" content="{title}">\n'
        f'  <meta property="og:description" content="{desc}">\n'
        f'  <meta property="og:image" content="{ORIGIN}/og.png">\n'
        f'  <meta property="og:url" content="{u}">\n'
        f'  <meta name="twitter:card" content="summary_large_image">\n'
        f'  <meta name="twitter:title" content="{title}">\n'
        f'  <meta name="twitter:description" content="{desc}">\n'
    )
    extra = "\n" + "\n".join(blocks) + "\n" if blocks else "\n"
    return (f'<!DOCTYPE html>\n{BUILT}\n<html lang="en">\n<head>\n'
            f'  <meta charset="utf-8">\n  <meta name="viewport" content="width=device-width, initial-scale=1">\n'
            f'  <title>{title}</title>\n  <meta name="description" content="{desc}">\n{noindex}'
            f'  <link rel="canonical" href="{u}">\n{social}'
            f'  <link rel="icon" type="image/svg+xml" href="/favicon.svg">\n'
            f'  <link rel="stylesheet" href="/style.css">\n{extra}</head>')

NAV = (f'  <a class="skip" href="#main">Skip to content</a>\n'
       f'  <header class="site">\n    <div class="bar">\n'
       f'      <a class="brand" href="/">{COCONUT.replace("__S__", "24")}<span>Cocos Locos</span></a>\n'
       f'      <nav aria-label="Main">\n'
       f'        <a href="/menu">Menu &amp; Bar</a>\n'
       f'        <a href="/seafood-in-coconuts">Seafood in Coconuts</a>\n'
       f'        <a href="/late-night-bar">Late-Night Bar</a>\n'
       f'        <a href="/contact">Contact</a>\n'
       f'      </nav>\n    </div>\n  </header>')

FOOTER = (f'  <footer class="site">\n    <div class="wrap">\n'
          f'      <p class="fbrand">{COCONUT.replace("__S__", "18")}<span>Cocos Locos Mexican Restaurant</span></p>\n'
          f'      <address>{STREET}<br>{CITYZIP}<br><a href="mailto:{EMAIL}">{EMAIL}</a></address>\n'
          f'      <p class="footline">Opening soon on Combee Road · <a href="/menu">Menu &amp; Bar</a> · <a href="/contact">Contact</a> · <a href="/privacy">Privacy</a></p>\n'
          f'      <p class="footline">© 2026 {NAME}</p>\n    </div>\n  </footer>')

def page(fname, title, desc, body, blocks=None, utility=False):
    html = head(title, desc, "/" + fname.split(".")[0].replace("index", ""), blocks, utility) + "\n\n<body>\n"
    html = html.replace('href="/"', f'href="{ORIGIN}/"' if fname == "index.html" else 'href="/"', 0)
    html += NAV + "\n<main id=\"main\">\n" + body + "\n</main>\n" + FOOTER + "\n</body>\n</html>\n"
    if fname == "index.html":
        html = html.replace('<link rel="canonical" href="', '<link rel="canonical" href="', 1)
    open(os.path.join(PUB, fname), "w", encoding="utf-8").write(html)
    print("wrote", fname, len(html), "bytes")

def CTArow(*links):
    a = ' '.join(f'<a class="btn{" ghost" if ghost else ""}" href="{h}">{t}</a>' for h, t, ghost in links)
    return f'<p class="cta-row">{a}</p>'

HOURS_DL = ('<dl class="hours">\n'
            '  <div><dt>Tuesday – Thursday</dt><dd>11 a.m. – 10 p.m.</dd></div>\n'
            '  <div><dt>Friday – Saturday</dt><dd>11 a.m. – 3 a.m.</dd></div>\n'
            '  <div><dt>Sunday</dt><dd>11 a.m. – midnight</dd></div>\n'
            '  <div><dt>Monday</dt><dd>Closed</dd></div>\n'
            '</dl>')

# ---------------- HOME ----------------
home_ld = [
    ld({"@context": "https://schema.org", "@graph": [
        REST,
        {"@type": "WebPage", "url": ORIGIN + "/", "name": "Cocos Locos Mexican Restaurant — Seafood in Coconuts, Lakeland FL",
         "inLanguage": "en-US", "about": {k: v for k, v in REST.items() if k != "@type"}},
    ]}),
    ld({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": "When do you open?", "acceptedAnswer": {"@type": "Answer",
         "text": "Opening soon — the opening date has not been announced yet. Email the team at cocoslocosfl@gmail.com and they will answer with the latest news."}},
        {"@type": "Question", "name": "Why serve food and drinks in coconuts?", "acceptedAnswer": {"@type": "Answer",
         "text": "It is the house tradition owner Kris Cavazos built the concept around: real coconuts split in half — used as plates for some seafood dishes and cups for cocktails."}},
        {"@type": "Question", "name": "Is it family-friendly?", "acceptedAnswer": {"@type": "Answer",
         "text": "Yes — through the day and evening it is a family-friendly, full sit-down restaurant. On weekends it shifts into a late-night gathering spot for guests coming from the Corral Event Center next door."}},
        {"@type": "Question", "name": "Where exactly is it?", "acceptedAnswer": {"@type": "Answer",
         "text": "1313 N Combee Road in Lakeland, FL — the remodeled space of the former Pa’Las Miches Bar and Grill, seating about 176 guests."}},
    ]}),
    ld(CRUMB([("Home", "/")])),
]
home = []
home.append(f'''  <section class="hero">
    <div class="wrap narrow">
      {COCONUT.replace("__S__", "64")}
      <p class="eyebrow">Opening soon · Combee Road · Lakeland, Florida</p>
      <h1>Seafood &amp; cocktails,<br>served in real coconuts</h1>
      <p class="lede">Cocos Locos is a full-service Mexican restaurant and bar with a broad seafood section, coming to the remodeled Pa’Las Miches space on Combee Road — where some of the seafood arrives in a halved coconut, and so do the cocktails.</p>
      {CTArow(("/contact", "Email the shop", False), ("/menu", "Menu &amp; Bar", True))}
    </div>
    {WAVE}
  </section>''')
home.append('''  <section class="band">
    <div class="wrap">
      <div class="cols">
        <div>
          <p class="eyebrow">The signature</p>
          <h2>Coconuts on the table, coconuts in the bar</h2>
          <p>Owner Kris Cavazos built Cocos Locos around a simple idea: split real coconuts in half and use them as plates for some of the seafood dishes — and as cups for cocktails.</p>
          <p><a class="btn ghost" href="/seafood-in-coconuts">The coconut seafood</a></p>
        </div>
        <div>
          <p class="eyebrow">The kitchen</p>
          <h2>A Mexican kitchen with a broad seafood section</h2>
          <p>The menu centers on authentic Mexican food alongside a wide seafood side — aguachiles, seafood cocktails, and fried fish are all part of the plan. The full menu and prices will be announced at opening.</p>
          <p><a class="btn ghost" href="/menu">Menu &amp; bar direction</a></p>
        </div>
      </div>
    </div>
  </section>''')
home.append('''  <section class="band dark">
    <div class="wrap">
      <div class="cols">
        <div>
          <p class="eyebrow">Through the day</p>
          <h2>A family restaurant by day</h2>
          <p>Daytime and evening service is built as a family-friendly, full sit-down dining room — the Lakeland version of a neighborhood Mexican table.</p>
        </div>
        <div>
          <p class="eyebrow">After dark</p>
          <h2>A late-night bar on weekends</h2>
          <p>On Fridays and Saturdays the room turns into a late-night gathering spot — planned until 3 a.m. — catching crowds coming from and to the Corral Event Center nightclub next door.</p>
          <p><a class="btn ghost" href="/late-night-bar">Late-night bar &amp; cocktails</a></p>
        </div>
      </div>
    </div>
  </section>''')
home.append(f'''  <section class="band">
    <div class="wrap">
      <div class="split">
        <div>
          <p class="eyebrow">The room</p>
          <h2>About 176 seats, freshly remodeled</h2>
          <p>Cocos Locos takes over the former Pa’Las Miches Bar and Grill space at {STREET} — remodeled under its new name, with room for about 176 guests across the dining room and bar.</p>
        </div>
        <div class="hoursbox">
          <p class="eyebrow">Announced hours · opening soon</p>
          {HOURS_DL}
          <p class="small">Hours as announced for after opening; Monday closed. The opening date is coming soon.</p>
        </div>
      </div>
    </div>
  </section>''')
home.append(f'''  <section class="band mapband">
    <div class="wrap">
      <div class="split">
        <div>
          <p class="eyebrow">Where</p>
          <h2>{STREET}, {CITYZIP.split(", ")[0]}</h2>
          <address class="addr">{NAME}<br>{STREET}<br>{CITYZIP}</address>
          <p>On Combee Road, next to the Corral Event Center. <a href="{DIR}" target="_blank" rel="noopener">Get directions</a>.</p>
          {CTArow(("/contact", "Email before opening", False))}
        </div>
        <div class="mapwrap">
          <iframe src="{MAPQ}" loading="lazy" title="Map — {NAME} at {STREET}, {CITYZIP}" referrerpolicy="no-referrer-when-downgrade"></iframe>
        </div>
      </div>
    </div>
  </section>''')
home.append('''  <section class="band faq">
    <div class="wrap narrow">
      <p class="eyebrow center">Good questions</p>
      <h2 class="center">Before you ask</h2>
      <div class="qa"><h3>When do you open?</h3><p>Opening soon — the opening date has not been announced yet. <a href="/contact">Email the team</a> and they will answer with the latest news.</p></div>
      <div class="qa"><h3>Why serve food and drinks in coconuts?</h3><p>It is the house tradition owner Kris Cavazos built the concept around: real coconuts split in half — plates for some seafood dishes, cups for cocktails. Which dishes come in coconuts will be revealed with the menu at opening.</p></div>
      <div class="qa"><h3>Is it family-friendly?</h3><p>Yes — through the day and evening it is a family-friendly sit-down restaurant. On weekends it shifts into a late-night spot for guests of the Corral Event Center next door.</p></div>
      <div class="qa"><h3>Where exactly is it?</h3><p>At 1313 N Combee Road in Lakeland — the remodeled space of the former Pa’Las Miches Bar and Grill, about 176 seats.</p></div>
      <div class="qa"><h3>Is there a full menu yet?</h3><p>Not published — the team is testing recipes now. The full menu and prices will be announced at opening. The shop posts first looks on <a href="__FB__" target="_blank" rel="noopener">its Facebook page</a>.</p></div>
    </div>
  </section>'''.replace("__FB__", FB))
page("index.html", "Cocos Locos Mexican Restaurant — Seafood in Coconuts, Lakeland FL",
     "Full-service Mexican restaurant and seafood bar opening soon at 1313 N Combee Rd, Lakeland FL — coconuts halved as plates for seafood and cups for cocktails, a broad seafood section, and cocktails until 3 a.m. on weekends.",
     "\n".join(home), home_ld)

# ---------------- MENU HUB ----------------
menu_ld = [
    ld({"@context": "https://schema.org", "@type": "Menu", "name": "Menu & Bar — Cocos Locos",
        "inRestaurant": {k: v for k, v in REST.items() if k != "@type"},
        "hasMenuSection": [
            {"@type": "MenuSection", "name": "Cold seafood", "description": "Aguachiles and Mexican-style seafood cocktails.",
             "hasMenuItem": [{"@type": "MenuItem", "name": "Aguachiles"}, {"@type": "MenuItem", "name": "Seafood cocktails"}]},
            {"@type": "MenuSection", "name": "Hot seafood", "description": "From the seafood side of the kitchen.",
             "hasMenuItem": [{"@type": "MenuItem", "name": "Fried fish"}]},
            {"@type": "MenuSection", "name": "The bar", "description": "Cocktails served in halved coconuts; late-night pours on weekends."},
        ]}),
    ld(CRUMB([("Home", "/"), ("Menu & Bar", "/menu")])),
]
menu = []
menu.append('''  <section class="pagehead">
    <div class="wrap narrow">
      <p class="eyebrow">Menu &amp; Bar · opening soon</p>
      <h1>Where the menu is headed</h1>
      <p class="lede">An authentic Mexican kitchen with a broad seafood section beside it — and a bar built around the coconut. The team is testing recipes now; the full menu and prices will be announced at opening.</p>
      ''' + CTArow(("/contact", "Get opening news by email", False)) + '''
    </div>
  </section>''')
menu.append('''  <section class="band">
    <div class="wrap">
      <div class="menugrid">
        <div class="card">
          <p class="eyebrow">Cold seafood</p>
          <h3>Aguachiles &amp; seafood cocktails</h3>
          <p>Citrus-chili aguachiles and Mexican-style seafood cocktails anchor the cold side of the seafood section.</p>
        </div>
        <div class="card">
          <p class="eyebrow">Hot seafood</p>
          <h3>Fried fish</h3>
          <p>Fried fish headlines the hot side of the broad seafood section, plates alongside the Mexican kitchen.</p>
        </div>
        <div class="card">
          <p class="eyebrow">Served in coconuts</p>
          <h3>Plates and cups, same coconut</h3>
          <p>Some seafood dishes come to the table in real halved coconuts — and so do the cocktails. <a href="/seafood-in-coconuts">The coconut story</a>.</p>
        </div>
        <div class="card">
          <p class="eyebrow">The bar</p>
          <h3>Cocktails, coconut cups, late nights</h3>
          <p>A full bar with cocktails in coconuts, pouring until 3 a.m. on Fridays and Saturdays. <a href="/late-night-bar">Late-night bar</a>.</p>
        </div>
      </div>
      <p class="small center menu-note">Menu items shown here reflect the announced direction; full lineup and prices arrive with the opening announcement.</p>
    </div>
  </section>''')
page("menu.html", "Menu & Bar — Cocos Locos, Lakeland FL",
     "Menu direction for Cocos Locos Mexican Restaurant, opening soon in Lakeland FL: aguachiles, seafood cocktails, fried fish, a broad seafood section beside an authentic Mexican kitchen, and cocktails in coconuts.",
     "\n".join(menu), menu_ld)

# ---------------- SEAFOOD DETAIL ----------------
sea_ld = [
    ld({"@context": "https://schema.org", "@type": "Service", "name": "Seafood served in halved coconuts",
        "serviceType": "Seafood dining",
        "provider": {k: v for k, v in REST.items() if k != "@type"},
        "areaServed": {"@type": "City", "name": "Lakeland", "address": {"@type": "PostalAddress", "addressLocality": "Lakeland", "addressRegion": "FL"}}}),
    ld(CRUMB([("Home", "/"), ("Menu & Bar", "/menu"), ("Seafood in Coconuts", "/seafood-in-coconuts")])),
]
sea = []
sea.append('''  <section class="pagehead">
    <div class="wrap narrow">
      <p class="eyebrow">The signature · Lakeland FL</p>
      <h1>Seafood in coconuts</h1>
      <p class="lede">Split a real coconut in half and two things happen: it becomes a plate, and it becomes a cup. That is the heart of Cocos Locos — seafood that arrives in the shell and cocktails poured into one.</p>
      ''' + CTArow(("/contact", "Ask the shop", False), ("/late-night-bar", "Late-night bar", True)) + '''
    </div>
  </section>''')
sea.append('''  <section class="band">
    <div class="wrap">
      <div class="split">
        <div>
          <p class="eyebrow">How it works</p>
          <h2>The shell does the serving</h2>
          <p>Owner Kris Cavazos built the concept on a simple move: coconuts are split in half, and some of the seafood dishes are plated right in the halves — cold aguachiles and seafood cocktails are the natural fit, with the broad seafood section (fried fish included) stretching across the menu beside them.</p>
          <p>Which dishes come in coconuts is part of the menu reveal at opening — the team is testing recipes now, and the lineup is announced when the kitchen is happy with it.</p>
        </div>
        <div>
          <p class="eyebrow">The drinks side</p>
          <h2>The same coconut, filled with a cocktail</h2>
          <p>The other half of the coconut gets the bar’s share: cocktails served in coconut cups. Order one at the bar or bring one to the table with your seafood.</p>
          <p><a class="btn ghost" href="/menu">See the menu direction</a></p>
        </div>
      </div>
    </div>
  </section>''')
page("seafood-in-coconuts.html", "Seafood in Coconuts — Cocos Locos, Lakeland FL",
     "Some seafood dishes at Cocos Locos Mexican Restaurant in Lakeland FL arrive plated in real halved coconuts — aguachiles, seafood cocktails and more, announced with the opening menu.",
     "\n".join(sea), sea_ld)

# ---------------- LATE-NIGHT DETAIL ----------------
night_ld = [
    ld({"@context": "https://schema.org", "@type": "Service", "name": "Late-night bar & cocktails",
        "serviceType": "Bar & cocktail service",
        "provider": {k: v for k, v in REST.items() if k != "@type"},
        "areaServed": {"@type": "City", "name": "Lakeland", "address": {"@type": "PostalAddress", "addressLocality": "Lakeland", "addressRegion": "FL"}}}),
    ld(CRUMB([("Home", "/"), ("Menu & Bar", "/menu"), ("Late-Night Bar", "/late-night-bar")])),
]
night = []
night.append('''  <section class="pagehead night">
    <div class="wrap narrow">
      <p class="eyebrow">After dark · Lakeland FL</p>
      <h1>The late-night bar</h1>
      <p class="lede">By day it is a family-friendly Mexican restaurant. On weekends it is Lakeland’s after-hours room — cocktails in coconuts until 3 a.m., two doors down from the Corral Event Center.</p>
      ''' + CTArow(("/contact", "Ask about late nights", False), ("/seafood-in-coconuts", "Seafood in coconuts", True)) + '''
    </div>
  </section>''')
night.append('''  <section class="band">
    <div class="wrap">
      <div class="split">
        <div>
          <p class="eyebrow">The weekend flip</p>
          <h2>Same room, two lives</h2>
          <p>Through the day and weeknight evenings, Cocos Locos runs as a family-friendly, full sit-down restaurant. Friday and Saturday, the plan changes: the bar stays pouring until 3 a.m. for the crowd coming from and back from events at the Corral Event Center nightclub next door — Cavazos built the late-night hours around exactly that traffic, before and after the shows.</p>
        </div>
        <div class="hoursbox">
          <p class="eyebrow">Announced hours · opening soon</p>
          ''' + HOURS_DL + '''
          <p class="small">Hours as announced for after opening; Monday closed.</p>
        </div>
      </div>
    </div>
  </section>''')
night.append('''  <section class="band dark">
    <div class="wrap narrow center">
      <p class="eyebrow center">Come for the show, stay for the bar</p>
      <h2 class="center">Coconut cocktails, served late</h2>
      <p>Cocktails come in real coconut halves — the one thing you will want a photo of before the club closes. The kitchen keeps firing alongside the bar, seafood included.</p>
      ''' + CTArow(("/contact", "Email the shop", False)) + '''
    </div>
  </section>''')
page("late-night-bar.html", "Late-Night Bar & Cocktails — Cocos Locos, Lakeland FL",
     "Cocos Locos turns into a late-night bar on weekends — cocktails in coconuts planned until 3 a.m., serving guests of the Corral Event Center next door in Lakeland FL.",
     "\n".join(night), night_ld)

# ---------------- CONTACT ----------------
contact_ld = [ld(CRUMB([("Home", "/"), ("Contact", "/contact")]))]
contact = []
contact.append('''  <section class="pagehead">
    <div class="wrap narrow">
      <p class="eyebrow">Contact · opening soon</p>
      <h1>Get in touch with the shop</h1>
      <p class="lede">Opening-date questions, the menu, events, press — send a note and the Cocos Locos team will answer.</p>
    </div>
  </section>''')
contact.append(f'''  <section class="band">
    <div class="wrap">
      <div class="split">
        <div>
          <h2>Send a note</h2>
          <form class="cform" method="post" action="/contact">
            <div>
              <label for="f-name">Your name</label>
              <input id="f-name" name="name" autocomplete="name" required>
            </div>
            <div class="row">
              <div>
                <label for="f-phone">Phone (optional)</label>
                <input id="f-phone" name="phone" type="tel" autocomplete="tel">
              </div>
              <div>
                <label for="f-email">Email</label>
                <input id="f-email" name="email" type="email" autocomplete="email">
              </div>
            </div>
            <div>
              <label for="f-message">Your message</label>
              <textarea id="f-message" name="message" required placeholder="Opening-date questions, menu questions, events, press — anything at all."></textarea>
            </div>
            <button class="btn" type="submit">Send the shop a note</button>
            <p class="small">Or email directly: <a href="mailto:{EMAIL}">{EMAIL}</a></p>
          </form>
        </div>
        <div>
          <h3>The address</h3>
          <address class="addr">Cocos Locos Mexican Restaurant<br>{STREET}<br>{CITYZIP}</address>
          <p>On Combee Road in Lakeland, next to the Corral Event Center.</p>
          <div class="mapwrap">
            <iframe src="{MAPQ}" loading="lazy" title="Map — Cocos Locos Mexican Restaurant at 1313 N Combee Rd, Lakeland FL" referrerpolicy="no-referrer-when-downgrade"></iframe>
            <p class="small">Next to the Corral Event Center · <a href="{DIR}" target="_blank" rel="noopener">Get directions</a></p>
          </div>
        </div>
      </div>
    </div>
  </section>''')
page("contact.html", "Contact — Cocos Locos, Lakeland FL",
     "Contact Cocos Locos Mexican Restaurant, opening soon at 1313 N Combee Rd, Lakeland FL — message form, direct email, and directions off Combee Road.",
     "\n".join(contact), contact_ld)

# ---------------- PRIVACY ----------------
priv_ld = [
    ld({"@context": "https://schema.org", "@type": "WebPage", "name": "Privacy Policy — Cocos Locos Mexican Restaurant", "url": ORIGIN + "/privacy"}),
    ld(CRUMB([("Home", "/"), ("Privacy", "/privacy")])),
]
priv = '''  <section class="pagehead">
    <div class="wrap narrow">
      <p class="eyebrow">Privacy</p>
      <h1>What this site does — and does not</h1>
    </div>
  </section>
  <section class="band">
    <div class="wrap narrow">
      <h2>The contact form</h2>
      <p>The form on the <a href="/contact">contact page</a> sends the name, phone, email, and message you type straight to the restaurant’s inbox by email. Nothing is stored on this site itself — the form is a post office, not a database.</p>
      <h2>No cookies, no trackers, no scripts</h2>
      <p>This site sets no cookies of its own, runs no analytics, and loads no third-party scripts. There is no advertising here.</p>
      <h2>The map</h2>
      <p>Pages showing the location embed a Google Maps frame. When your browser loads that frame, Google handles the request under its own privacy policy and may set its own cookies; this site passes nothing to Google.</p>
      <h2>Questions</h2>
      <p>Ask by email at <a href="mailto:__EMAIL__">__EMAIL__</a> or through the contact form — whatever reaches the shop.</p>
    </div>
  </section>'''.replace("__EMAIL__", EMAIL)
page("privacy.html", "Privacy Policy — Cocos Locos, Lakeland FL",
     "Privacy policy for the Cocos Locos Mexican Restaurant website: one contact form, no cookies, no trackers, no third-party scripts, and no advertising.",
     priv, priv_ld)

# ---------------- THANKS ----------------
thanks = '''  <section class="pagehead tall">
    <div class="wrap narrow">
      <p class="eyebrow">Message sent</p>
      <h1>Thanks — your note is on its way</h1>
      <p class="lede">It lands directly in the Cocos Locos inbox. While the team is finishing up before opening, email can take a day or two.</p>
      <p class="cta-row"><a class="btn" href="/">Back to the front page</a></p>
    </div>
  </section>'''
page("thanks.html", "Thank You — Cocos Locos, Lakeland FL",
     "Thank you — your message has been sent to Cocos Locos Mexican Restaurant in Lakeland, FL.",
     thanks, utility=True)

# ---------------- 404 ----------------
nf = '''  <section class="pagehead tall">
    <div class="wrap narrow">
      <p class="eyebrow">Page not found</p>
      <h1>That page has drifted out to sea</h1>
      <p class="lede">The page you were after is not here. Start from the front, or jump to the menu and the bar.</p>
      <p class="cta-row"><a class="btn" href="/">Front page</a> <a class="btn ghost" href="/menu">Menu &amp; Bar</a> <a class="btn ghost" href="/contact">Contact</a></p>
    </div>
  </section>'''
page("404.html", "Page Not Found — Cocos Locos, Lakeland FL",
     "Page not found — Cocos Locos Mexican Restaurant, Lakeland FL.",
     nf, utility=True)

# ---------------- SITEMAP / ROBOTS ----------------
pages = ["", "menu", "seafood-in-coconuts", "late-night-bar", "contact", "privacy"]
urls = "\n".join(f'  <url><loc>{ORIGIN}/{p}</loc><lastmod>2026-11-17</lastmod></url>' for p in pages)
open(os.path.join(PUB, "sitemap.xml"), "w", encoding="utf-8").write(
    f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}\n</urlset>\n')
open(os.path.join(PUB, "robots.txt"), "w", encoding="utf-8").write(
    f'User-agent: *\nDisallow: /thanks\nDisallow: /404\n\nSitemap: {ORIGIN}/sitemap.xml\n')
print("wrote sitemap.xml, robots.txt")
