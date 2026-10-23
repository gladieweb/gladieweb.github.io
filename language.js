/* Spanish is selected for a Spanish browser; every other language uses English.
   Legal and game pages deliberately do not load this script. */
(() => {
  const root = document.documentElement;
  const paths = { es: root.dataset.languageEs, en: root.dataset.languageEn };
  if (!paths.es || !paths.en) return;

  const key = "gladieweb-language";
  const valid = (value) => value === "es" || value === "en";
  const requested = new URLSearchParams(window.location.search).get("lang");
  const remember = (language) => {
    try { window.localStorage.setItem(key, language); } catch { /* Storage is optional. */ }
  };
  let saved;
  try { saved = window.localStorage.getItem(key); } catch { /* Private/restricted browsing. */ }

  // Explicit language links always win, including when storage is unavailable.
  // An /en/ URL can also be shared and opened directly without a redirect.
  const primary = (navigator.languages?.[0] || navigator.language || "").toLowerCase();
  const browserLanguage = /^es(?:-|$)/.test(primary) ? "es" : "en";
  const language = valid(requested) ? requested :
    (root.lang === "en" ? "en" : (valid(saved) ? saved : browserLanguage));
  if (valid(requested)) remember(requested);

  if (language !== root.lang) {
    const destination = new URL(paths[language], window.location.href);
    destination.search = window.location.search;
    destination.hash = window.location.hash;
    window.location.replace(destination.href);
    return;
  }

  document.addEventListener("DOMContentLoaded", () => {
    for (const anchor of document.querySelectorAll("a[data-language]")) {
      const url = new URL(anchor.href, window.location.href);
      // Preserve a project section, contact context, or other existing parameters.
      url.search = window.location.search;
      url.searchParams.set("lang", anchor.dataset.language);
      url.hash = window.location.hash;
      anchor.href = url.href;
      anchor.addEventListener("click", () => remember(anchor.dataset.language));
    }
    // Carry an explicit choice through local navigation if cookies/storage are blocked.
    if (valid(requested)) {
      for (const anchor of document.querySelectorAll("a[href]:not([data-language])")) {
        const url = new URL(anchor.href, window.location.href);
        if (url.origin === window.location.origin && url.pathname.endsWith(".html") &&
            !/\/(?:privacypolicy|account-deletion|skeleton-warfare)\.html$/.test(url.pathname)) {
          url.searchParams.set("lang", requested);
          anchor.href = url.href;
        }
      }
    }
  });
})();
