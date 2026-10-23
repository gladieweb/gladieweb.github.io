// Exercise automatic language selection without external dependencies.
const fs = require('node:fs');
const vm = require('node:vm');
const assert = require('node:assert/strict');
const source = fs.readFileSync(require('node:path').join(__dirname, '..', 'language.js'), 'utf8');

function visit({ path = 'index.html', locale = 'es-AR', languages, saved = null,
                 search = '', hash = '', blocked = false, current = 'es' } = {}) {
  const location = new URL(`https://example.com/portfolio/${path}${search}${hash}`);
  let redirected, ready, stored = saved;
  const anchors = [
    { href: 'https://example.com/portfolio/en/index.html?lang=en', dataset: {language:'en'}, addEventListener() {} },
    { href: 'https://example.com/portfolio/index.html?lang=es', dataset: {language:'es'}, addEventListener() {} }
  ];
  const links = ['software.html', 'account-deletion.html', 'privacypolicy.html', 'skeleton-warfare.html'].map(name => ({href:new URL(name,location).href}));
  const context = {
    URL, URLSearchParams,
    navigator: { language: locale, languages: languages ?? (locale ? [locale] : []) },
    document: {
      documentElement: { lang: current, dataset: {
        languageEs: current === 'en' ? '../index.html' : path.includes('/') ? '../proyectos/archviz.html' : path,
        languageEn: current === 'en' ? 'index.html' : path.includes('/') ? '../en/proyectos/archviz.html' : 'en/' + path
      } },
      addEventListener(type, callback) { if (type === 'DOMContentLoaded') ready = callback; },
      querySelectorAll(selector) { return selector === 'a[data-language]' ? anchors : links; }
    },
    window: {
      location: { href:location.href, search:location.search, hash:location.hash, origin:location.origin, replace(url) { redirected = url; } },
      localStorage: { getItem() { if (blocked) throw Error('blocked'); return stored; }, setItem(key, value) { if (blocked) throw Error('blocked'); stored = value; } }
    }
  };
  vm.runInNewContext(source, context);
  if (ready) ready();
  return {redirected, stored, anchors, links};
}

for (const locale of ['es', 'es-AR', 'es-ES', 'es-MX', 'ES-cl']) assert.equal(visit({locale}).redirected, undefined, locale);
for (const locale of ['en-US', 'fr-FR', 'pt-BR', 'de-DE', 'ja-JP', '']) assert.equal(visit({locale}).redirected, 'https://example.com/portfolio/en/index.html', locale);
assert.equal(visit({locale:'en-US', languages:['es-MX','en-US']}).redirected, undefined);
assert.equal(visit({locale:'es-AR', languages:['en-US','es-AR']}).redirected, 'https://example.com/portfolio/en/index.html');
assert.equal(visit({locale:'en-US', saved:'es'}).redirected, undefined);
assert.equal(visit({locale:'es-AR', saved:'en'}).redirected, 'https://example.com/portfolio/en/index.html');
assert.equal(visit({locale:'en-US', saved:'unexpected'}).redirected, 'https://example.com/portfolio/en/index.html');
assert.equal(visit({locale:'en-US', search:'?lang=es', blocked:true}).redirected, undefined);
assert.equal(visit({locale:'es-AR', saved:'es', search:'?lang=en'}).stored, 'en');
assert.equal(visit({locale:'fr-FR', blocked:true}).redirected, 'https://example.com/portfolio/en/index.html');
assert.equal(visit({path:'proyectos/archviz.html', locale:'en-US', search:'?tema=visualizacion', hash:'#contenido'}).redirected, 'https://example.com/portfolio/en/proyectos/archviz.html?tema=visualizacion#contenido');
assert.equal(visit({path:'en/index.html', current:'en', locale:'es-AR', saved:'es'}).redirected, undefined);
assert.equal(visit({path:'en/index.html', current:'en', search:'?lang=es'}).redirected, 'https://example.com/portfolio/index.html?lang=es');
const manual = visit({locale:'en-US', search:'?tema=software&lang=es', hash:'#contenido', blocked:true});
assert.ok(manual.anchors[0].href.endsWith('?tema=software&lang=en#contenido'));
assert.ok(manual.links[0].href.endsWith('software.html?lang=es'));
for (const item of manual.links.slice(1)) assert.ok(!item.href.includes('?'), 'Legal and game links must remain unchanged');
console.log('PASS: browser languages, English fallback, saved/manual choice, blocked storage, deep links, and legal exclusions.');
