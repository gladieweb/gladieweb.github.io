const year = document.getElementById("year");
if (year) year.textContent = new Date().getFullYear();

// Keep links into the former one-page site useful.
if (document.body.classList.contains("home")) {
  const legacyDestinations = {
    "#unity": "videojuegos.html#unity",
    "#unreal": "videojuegos.html#unreal",
    "#software": "software.html",
    "#perfil": "perfil.html",
    "#contacto": "contacto.html",
    "#account-deletion": "account-deletion.html",
    "#download": "skeleton-warfare.html#download",
    "#features": "skeleton-warfare.html#features",
    "#about": "skeleton-warfare.html#about"
  };
  const followLegacyLink = () => {
    const destination = legacyDestinations[window.location.hash];
    if (destination) window.location.replace(destination);
  };
  followLegacyLink();
  window.addEventListener("hashchange", followLegacyLink);
}
