const categories = ["All", "Campus", "Study", "IT Tips", "Health", "Wellness", "Job"];

const services = [
  { id: "vrs", name: "Visitor Registration System (VRS)", shortName: "Visitor Registration System", category: "Campus", letter: "V", description: "Request a QR code for your guests to access campus.", keywords: "visitor guest guests registration qr vrs campus access", url: "fmovrs.polyu.edu.hk/vrs", action: "Continue to VRS" },
  { id: "internal-search", name: "PolyU Internal Search", shortName: "PolyU Internal Search", category: "Campus", letter: "P", description: "Search PolyU internal documents available to staff and students.", keywords: "internal documents search staff students", url: "Official PolyU service", action: "Continue to Internal Search" },
  { id: "learn", name: "LEARN@PolyU (理學網)", shortName: "LEARN@PolyU", category: "Study", letter: "L", description: "Learning Management System of PolyU.", keywords: "learn learning blackboard course study", url: "Official PolyU service", action: "Continue to LEARN@PolyU" },
  { id: "library", name: "Library", shortName: "Library", category: "Study", letter: "L", description: "Access the PolyU Library home and learning resources.", keywords: "library books resources study", url: "Official PolyU service", action: "Continue to Library" },
  { id: "estudent", name: "eStudent", shortName: "eStudent", category: "Study", letter: "E", description: "Access applications related to your study.", keywords: "estudent student study applications", url: "Official PolyU service", action: "Continue to eStudent" },
  { id: "email", name: "Connect Email", shortName: "Connect Email", category: "IT Tips", letter: "C", description: "Find guidance for connecting to your PolyU email.", keywords: "connect email mail it help", url: "Official PolyU service", action: "Continue to Connect Email" },
  { id: "identity", name: "Identity Portal", shortName: "Identity Portal", category: "IT Tips", letter: "I", description: "Manage your PolyU digital identity and account settings.", keywords: "identity portal account netid it", url: "Official PolyU service", action: "Continue to Identity Portal" },
  { id: "health", name: "University Health Service", shortName: "University Health Service", category: "Health", letter: "U", description: "Access information from the University Health Service.", keywords: "university health clinic medical", url: "Official PolyU service", action: "Continue to Health Service" },
  { id: "poss", name: "POSS", shortName: "POSS", category: "Wellness", letter: "P", description: "Open the POSS student support service.", keywords: "poss wellness support", url: "Official PolyU service", action: "Continue to POSS" },
  { id: "job", name: "PolyU Job Board", shortName: "PolyU Job Board", category: "Job", letter: "J", description: "Explore full-time, part-time, graduate, and internship opportunities.", keywords: "job jobs career internship graduate work", url: "Official PolyU service", action: "Continue to Job Board" }
];

let phone = document.querySelector("#phone-screen");
const liveRegion = document.querySelector("#live-region");
const params = new URLSearchParams(window.location.search);
const captureMode = params.get("capture") === "1";
const state = {
  screen: "home",
  category: "All",
  query: "",
  selectedId: "vrs",
  scrolls: {},
  loadingTimer: null
};

function escapeHtml(value) {
  return String(value).replace(/[&<>'"]/g, character => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", "'": "&#39;", '"': "&quot;" })[character]);
}

function statusBar() {
  return '<div class="status-bar"><span>09:41</span><span class="status-icons">● ▰</span></div>';
}

function nav(title, backAction = "", backLabel = "Back") {
  return `${statusBar()}<header class="app-nav"><div>${backAction ? `<button class="nav-button" data-action="${backAction}" aria-label="${backLabel}">‹ ${backLabel === "Back to previous screen" ? "Back" : backLabel}</button>` : ""}</div><h2>${title}</h2><span class="demo-label">DEMO</span></header>`;
}

function selectedService() {
  return services.find(service => service.id === state.selectedId) || services[0];
}

function filteredServices() {
  const query = state.query.trim().toLowerCase();
  return services.filter(service => {
    const categoryMatches = state.category === "All" || service.category === state.category;
    const queryMatches = !query || `${service.name} ${service.description} ${service.category} ${service.keywords}`.toLowerCase().includes(query);
    return categoryMatches && queryMatches;
  });
}

function renderHome() {
  return `<div class="app">${statusBar()}<main class="app-content">
    <p class="home-date">Monday, 9 November</p>
    <section class="home-hero">
      <p class="app-kicker">YOUR CAMPUS, AT A GLANCE</p>
      <h1 class="app-title">What do you need today?</h1>
      <div class="service-grid-illustration" aria-hidden="true">${"<i></i>".repeat(9)}</div>
    </section>
    <div class="module-list" aria-label="Campus modules">
      <button class="module-card primary" data-action="open-apps"><span class="module-icon">A</span><span class="module-copy"><strong>Apps &amp; services</strong><span class="module-description">Find VRS, Library, eStudent and more</span></span><span class="module-arrow">↗</span></button>
      <div class="module-card"><span class="module-icon">C</span><span class="module-copy"><strong>Calendar</strong><span class="module-description">Team module · final integration</span></span></div>
      <div class="module-card"><span class="module-icon">R</span><span class="module-copy"><strong>Room finder</strong><span class="module-description">Team module · final integration</span></span></div>
      <div class="module-card"><span class="module-icon">F</span><span class="module-copy"><strong>Food</strong><span class="module-description">Team module · final integration</span></span></div>
      <div class="module-card"><span class="module-icon">M</span><span class="module-copy"><strong>Campus map</strong><span class="module-description">Team module · final integration</span></span></div>
    </div>
    <p class="home-note">Apps functional demo · Other modules connect during team integration</p>
  </main></div>`;
}

function serviceCard(service) {
  return `<article class="service-card">
    <div class="service-heading"><span class="service-letter">${service.letter}</span><div class="service-heading-copy"><span class="service-category">${service.category}</span><h3>${service.name}</h3></div></div>
    <p class="service-description">${service.description}</p>
    <button class="service-action" data-action="select-service" data-service="${service.id}" aria-label="View details: ${service.name}">View service <span aria-hidden="true">›</span></button>
  </article>`;
}

function renderApps(focusSearch = false) {
  const results = filteredServices();
  const queryLabel = state.query.trim() ? ` matching “${escapeHtml(state.query.trim())}”` : "";
  const resultContent = results.length ? `<div class="service-list">${results.map(serviceCard).join("")}</div>` : `<section class="empty-state"><div class="empty-symbol" aria-hidden="true">?</div><h3>No services found</h3><p>No ${state.category === "All" ? "services" : `${state.category} services`} match “${escapeHtml(state.query.trim())}”. Try a different name or clear your filters.</p><div class="empty-actions">${state.query ? '<button class="primary-button" data-action="clear-search">Clear search</button>' : ""}${state.category !== "All" ? '<button class="secondary-button" data-action="reset-filters">Show all categories</button>' : '<button class="secondary-button" data-action="reset-filters">Reset search</button>'}</div></section>`;
  return `<div class="app">${nav("Apps & services", "go-home", "Home")}<main class="app-content">
    <p class="app-kicker">CAMPUS SERVICES</p><h1 class="app-title">Find a service</h1><p class="app-subtitle">Search by name or browse a category.</p>
    <label class="search-label" for="service-search">Service name or task</label>
    <div class="search-box"><span class="search-icon" aria-hidden="true">⌕</span><input id="service-search" type="search" autocomplete="off" placeholder="Try ‘visitor’ or ‘VRS’" value="${escapeHtml(state.query)}" aria-describedby="search-help"><button class="clear-button" data-action="clear-search" aria-label="Clear search" ${state.query ? "" : "disabled"}>×</button></div>
    <span id="search-help" class="sr-only">Results update as you type</span>
    <fieldset class="category-fieldset"><legend>Category</legend><div class="category-chips">${categories.map(category => `<button type="button" class="category-chip" data-action="select-category" data-category="${category}" aria-pressed="${state.category === category}">${category}</button>`).join("")}</div></fieldset>
    <div class="result-summary" aria-live="polite"><div><strong>${state.category === "All" ? "All services" : `${state.category} services`}</strong><span>Current filter: ${state.category}${queryLabel}</span></div><span class="result-count">${results.length} ${results.length === 1 ? "result" : "results"}</span></div>
    ${resultContent}
  </main></div>`;
}

function renderDetail() {
  const service = selectedService();
  return `<div class="app">${nav("Service details", "back-to-apps")}<main class="app-content">
    <section class="detail-hero"><span class="service-letter">${service.letter}</span><span class="service-category">${service.category} service</span><h1>${service.name}</h1></section>
    <section class="detail-section"><h2>About this service</h2><p>${service.description}</p></section>
    <section class="detail-section"><h2>Before you continue</h2><p>You will open an official PolyU web service outside this demo.</p><div class="detail-fact"><span class="fact-icon">ID</span><div><strong>NetID sign-in may be required</strong><span>Use the official page to sign in. This demo never collects your credentials.</span></div></div><div class="detail-fact"><span class="fact-icon">↗</span><div><strong>Destination</strong><span>${service.url}</span></div></div></section>
    <div class="detail-actions"><button class="primary-button full-width" data-action="open-external">${service.action} <span aria-hidden="true">↗</span></button><button class="secondary-button full-width" data-action="back-to-apps">Back to results</button></div>
    <p class="prototype-disclaimer">Design proposal · External sign-in is simulated · No visitor request is submitted</p>
  </main></div>`;
}

function renderLoading() {
  const service = selectedService();
  return `<div class="app">${nav("Opening service")}<main class="loading-state"><div class="loader" role="status" aria-label="Loading"></div><h1>Opening ${service.shortName}</h1><p>Connecting to the official PolyU service.<br>${service.url}</p><button class="secondary-button" data-action="cancel-loading">Cancel and return</button></main></div>`;
}

function renderWeb() {
  const service = selectedService();
  return `<div class="app">${statusBar()}<div class="browser-chrome"><div class="browser-row"><button data-action="close-web" aria-label="Close official web preview">×</button><strong>Official web service</strong><span class="demo-label">DEMO</span></div><div class="address-bar"><span aria-hidden="true">▣</span><span>${service.url}</span></div></div><div class="handoff-banner"><strong>You are continuing to ${service.shortName}</strong><span>This is a safe prototype preview of the external sign-in step.</span></div><main class="signin-card"><div class="polyu-text-mark">THE HONG KONG<br>POLYTECHNIC UNIVERSITY</div><h1>Sign in with your NetID</h1><p>The observed VRS page asks for a NetID and NetPassword. Authentication would happen on the official PolyU website.</p><div class="demo-field">NetID · not collected in demo</div><div class="demo-field">NetPassword · not collected in demo</div><div class="demo-lock">Demo only. Credential fields and submission are intentionally disabled.</div><button class="secondary-button full-width" data-action="close-web">Close and return to service details</button></main></div>`;
}

function announce(message) {
  liveRegion.textContent = message;
}

function saveScroll() {
  state.scrolls[state.screen] = phone.scrollTop;
}

function render(options = {}) {
  const previousScreen = state.screen;
  let html = "";
  if (state.screen === "home") html = renderHome();
  if (state.screen === "apps") html = renderApps(options.focusSearch);
  if (state.screen === "detail") html = renderDetail();
  if (state.screen === "loading") html = renderLoading();
  if (state.screen === "web") html = renderWeb();
  phone.innerHTML = html;
  phone.classList.toggle("is-loading", state.screen === "loading");
  requestAnimationFrame(() => {
    phone.scrollTop = options.focusSearch ? state.scrolls[previousScreen] || 0 : state.scrolls[state.screen] || 0;
    if (options.focusSearch) {
      const input = document.querySelector("#service-search");
      if (input) {
        input.focus();
        input.setSelectionRange(input.value.length, input.value.length);
      }
    }
  });
  document.querySelectorAll(".scenario").forEach(button => {
    const scenario = button.dataset.scenario;
    const active = (scenario === state.screen) || (scenario === "all" && state.screen === "apps" && state.category === "All" && !state.query) || (scenario === "campus" && state.screen === "apps" && state.category === "Campus") || (scenario === "job" && state.screen === "apps" && state.category === "Job") || (scenario === "empty" && state.screen === "apps" && state.query === "not-a-service");
    button.classList.toggle("active", active);
  });
}

function go(screen) {
  clearTimeout(state.loadingTimer);
  saveScroll();
  state.screen = screen;
  render();
}

function openExternal() {
  clearTimeout(state.loadingTimer);
  go("loading");
  if (!captureMode) {
    state.loadingTimer = setTimeout(() => {
      state.screen = "web";
      render();
      announce("Official service sign-in preview opened");
    }, 900);
  }
}

function setScenario(name) {
  clearTimeout(state.loadingTimer);
  state.query = "";
  state.category = "All";
  state.selectedId = "vrs";
  state.scrolls = {};
  if (name === "home") state.screen = "home";
  if (name === "all") state.screen = "apps";
  if (name === "campus") { state.screen = "apps"; state.category = "Campus"; }
  if (name === "job") { state.screen = "apps"; state.category = "Job"; }
  if (name === "detail") state.screen = "detail";
  if (name === "loading") state.screen = "loading";
  if (name === "web") state.screen = "web";
  if (name === "empty") { state.screen = "apps"; state.query = "not-a-service"; }
  render();
}

phone.addEventListener("scroll", () => {
  state.scrolls[state.screen] = phone.scrollTop;
}, { passive: true });

phone.addEventListener("input", event => {
  if (event.target.id !== "service-search") return;
  state.query = event.target.value;
  render({ focusSearch: true });
});

phone.addEventListener("click", event => {
  const button = event.target.closest("[data-action]");
  if (!button) return;
  const action = button.dataset.action;
  if (action === "open-apps") go("apps");
  if (action === "go-home") go("home");
  if (action === "back-to-apps") go("apps");
  if (action === "select-category") {
    state.category = button.dataset.category;
    state.scrolls.apps = 0;
    render();
    announce(`${state.category} category selected. ${filteredServices().length} results.`);
  }
  if (action === "select-service") {
    state.selectedId = button.dataset.service;
    go("detail");
  }
  if (action === "clear-search") {
    state.query = "";
    render({ focusSearch: true });
    announce(`Search cleared. ${filteredServices().length} results.`);
  }
  if (action === "reset-filters") {
    state.query = "";
    state.category = "All";
    render({ focusSearch: true });
    announce(`All filters cleared. ${filteredServices().length} results.`);
  }
  if (action === "open-external") openExternal();
  if (action === "cancel-loading") go("detail");
  if (action === "close-web") go("detail");
});

document.querySelectorAll(".scenario").forEach(button => {
  button.addEventListener("click", () => setScenario(button.dataset.scenario));
});

document.addEventListener("keydown", event => {
  if (event.key !== "Escape") return;
  if (state.screen === "web" || state.screen === "loading") go("detail");
  else if (state.screen === "detail") go("apps");
});

if (captureMode) {
  document.body.classList.add("capture");
  const mount = document.createElement("div");
  mount.id = "capture-mount";
  mount.appendChild(phone);
  document.body.appendChild(mount);
}

setScenario(params.get("scenario") || "home");
