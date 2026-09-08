/* Sindi GrEeN — cache mínimo. Não interfere com /__grok. */
const CACHE = "sindi-green-destino-v6";
const PRECACHE = [new URL("favicon.svg", self.location).pathname];

self.addEventListener("install", (event) => {
  event.waitUntil(
    caches
      .open(CACHE)
      .then((cache) => cache.addAll(PRECACHE))
      .then(() => self.skipWaiting()),
  );
});

self.addEventListener("activate", (event) => {
  event.waitUntil(
    caches
      .keys()
      .then((keys) => Promise.all(keys.filter((k) => k !== CACHE).map((k) => caches.delete(k))))
      .then(() => self.clients.claim()),
  );
});

self.addEventListener("fetch", (event) => {
  const req = event.request;
  if (req.method !== "GET") return;
  const url = new URL(req.url);
  if (url.origin !== self.location.origin) return;
  if (url.pathname.includes("/__grok/") || url.pathname.includes("/api/")) return;

  if (req.mode === "navigate") {
    event.respondWith(
      fetch(req, { cache: "no-store" }).catch(async () => {
        const dest = new URL("destino", self.location).pathname;
        return (await caches.match(dest)) || new Response("Offline", { status: 503 });
      }),
    );
  }
});

self.addEventListener("notificationclick", (event) => {
  event.notification.close();
  const raw = (event.notification.data && event.notification.data.url) || "/";
  const href = new URL(raw, self.location.origin).href;
  event.waitUntil(
    self.clients.matchAll({ type: "window", includeUncontrolled: true }).then((clientList) => {
      for (const client of clientList) {
        if (new URL(client.url).origin === self.location.origin && "focus" in client) {
          client.focus();
          client.postMessage({ type: "sindi-open", url: href });
          return;
        }
      }
      if (self.clients.openWindow) return self.clients.openWindow(href);
    }),
  );
});
