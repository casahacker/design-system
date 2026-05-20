/* =============================================================================
   Casa Hacker DS · Service Worker (v1.0)
   ─────────────────────────────────────────────────────────────────────────────
   Strategy:
   - HTML: network-first com fallback pro cache (then offline.html)
   - CSS/JS/fonts/icons: cache-first, atualiza em background (stale-while-revalidate)
   - Imagens: cache-first
   ============================================================================= */
const CACHE_VERSION = 'chds-v1';
const STATIC_CACHE = `${CACHE_VERSION}-static`;
const DYNAMIC_CACHE = `${CACHE_VERSION}-dynamic`;

const STATIC_ASSETS = [
  './',
  './index.html',
  './styles.css',
  './shell.js',
  './components.js',
  './favicon.svg',
  './manifest.webmanifest',
  './404.html',
  './fonts/IBM_Plex_Mono/IBMPlexMono-Regular.woff2',
  './fonts/Roboto_Flex/RobotoFlex-Variable.woff2',
];

// ----- install --------------------------------------------------------------
self.addEventListener('install', (evt) => {
  evt.waitUntil(
    caches.open(STATIC_CACHE)
      .then(c => c.addAll(STATIC_ASSETS).catch(err => console.warn('[sw] precache failed', err)))
      .then(() => self.skipWaiting())
  );
});

// ----- activate -------------------------------------------------------------
self.addEventListener('activate', (evt) => {
  evt.waitUntil(
    caches.keys()
      .then(keys => Promise.all(
        keys.filter(k => !k.startsWith(CACHE_VERSION)).map(k => caches.delete(k))
      ))
      .then(() => self.clients.claim())
  );
});

// ----- fetch ----------------------------------------------------------------
self.addEventListener('fetch', (evt) => {
  const req = evt.request;
  if (req.method !== 'GET') return;
  const url = new URL(req.url);
  if (url.origin !== self.location.origin) return;

  // HTML: network-first
  if (req.mode === 'navigate' || req.headers.get('accept')?.includes('text/html')) {
    evt.respondWith(
      fetch(req)
        .then(res => {
          if (res.ok) {
            const copy = res.clone();
            caches.open(DYNAMIC_CACHE).then(c => c.put(req, copy));
          }
          return res;
        })
        .catch(() => caches.match(req).then(r => r || caches.match('./404.html')))
    );
    return;
  }

  // Static (CSS, JS, fonts, svg): stale-while-revalidate
  evt.respondWith(
    caches.match(req).then(cached => {
      const network = fetch(req).then(res => {
        if (res.ok) {
          const copy = res.clone();
          caches.open(DYNAMIC_CACHE).then(c => c.put(req, copy));
        }
        return res;
      }).catch(() => cached);
      return cached || network;
    })
  );
});
