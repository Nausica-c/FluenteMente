/* ==========================================================================
ROOT VARIABLES
========================================================================== */
:root {
  --primary-color: #ff8000;
  --primary-hover: #e67300;

  --text-main: #2d3748;
  --text-light: #718096;

  --bg-body: #f8fafc;
  --bg-header: #ffffff;

  --border-color: #e2e8f0;

  --content-width: 840px;

  --radius-sm: 8px;
  --radius-md: 12px;
  --radius-lg: 16px;

  --shadow-sm: 0 2px 6px rgba(0,0,0,0.04);
  --shadow-md: 0 10px 20px rgba(0,0,0,0.05);
}

/* ==========================================================================
RESET
========================================================================== */
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  background: var(--bg-body);
  color: var(--text-main);
  line-height: 1.6;
}

a { color: var(--primary-color); text-decoration: none; }
a:hover { text-decoration: underline; }

.wrapper {
  max-width: var(--content-width);
  margin: 0 auto;
  padding: 0 20px;
}

/* ==========================================================================
HEADER + NAV
========================================================================== */
.site-header {
  background: #fff;
  border-bottom: 1px solid var(--border-color);
  position: sticky;
  top: 0;
  z-index: 1000;
}

.header-wrapper {
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 60px;
}

.site-title {
  font-weight: 700;
  font-size: 1.2rem;
  color: #111;
}

/* NAV BASE */
.site-nav {
  display: flex;
  align-items: center;
}

.trigger {
  display: flex;
  gap: 18px;
}

.page-link {
  color: var(--text-main);
  font-weight: 500;
}

/* CTA */
.page-link.is-primary {
  background: var(--primary-color);
  color: #fff !important;
  padding: 6px 12px;
  border-radius: 999px;
}

/* HAMBURGER */
.menu-icon {
  display: none;
  font-size: 24px;
  cursor: pointer;
}

.nav-trigger {
  display: none;
}

/* ==========================================================================
MOBILE NAV (FIX DEFINITIVO)
========================================================================== */
@media (max-width: 768px) {

  .menu-icon {
    display: block;
    z-index: 1001;
  }

  .site-nav {
    position: fixed;
    top: 60px;
    left: 0;
    width: 100%;
    height: calc(100vh - 60px);

    background: #fff;

    flex-direction: column;

    opacity: 0;
    visibility: hidden;
    transform: translateY(-10px);

    transition: 0.25s ease;
  }

  .trigger {
    flex-direction: column;
    padding: 20px;
    gap: 20px;
  }

  .page-link {
    font-size: 1.1rem;
  }

  /* OPEN STATE */
  .nav-trigger:checked ~ .site-nav {
    opacity: 1;
    visibility: visible;
    transform: translateY(0);
  }
}

/* ==========================================================================
LAYOUT
========================================================================== */
.page-content {
  padding: 40px 0;
}

.post-wrapper {
  max-width: 760px;
  margin: 0 auto;
  background: #fff;
  padding: 35px;
  border-radius: var(--radius-md);
  box-shadow: var(--shadow-sm);
}

/* ==========================================================================
TYPOGRAPHY
========================================================================== */
.post-title {
  font-size: 2rem;
  margin-bottom: 10px;
}

.post-content p {
  margin-bottom: 1.2em;
}

/* ==========================================================================
BUTTONS
========================================================================== */
.btn-primary {
  background: var(--primary-color);
  color: #fff;
  padding: 14px 28px;
  border-radius: 999px;
  font-weight: 700;
  display: inline-block;
}

.btn-primary:hover {
  background: var(--primary-hover);
}

.btn-outline {
  border: 2px solid var(--primary-color);
  padding: 14px 28px;
  border-radius: 999px;
  font-weight: 700;
}

/* ==========================================================================
HERO
========================================================================== */
.hero-clean {
  background: #fff;
  padding: 70px 0 30px;
  text-align: center;
}

.hero-clean__title {
  font-size: 2.4rem;
  margin-bottom: 10px;
}

.hero-clean__subtitle {
  color: var(--text-light);
  margin-bottom: 20px;
}

.hero-clean__actions {
  display: flex;
  justify-content: center;
  gap: 10px;
}

/* ==========================================================================
SECTIONS
========================================================================== */
.section-soft {
  padding: 50px 0;
  background: #fff;
}

.section-alt {
  padding: 50px 0;
  background: #f1f5f9;
}

.section-title {
  font-size: 1.8rem;
  margin-bottom: 15px;
}

.section-subtitle {
  color: var(--text-light);
  margin-bottom: 20px;
}

/* ==========================================================================
START GRID (FUNNEL CORE)
========================================================================== */
.start-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px,1fr));
  gap: 16px;
}

.start-card {
  border: 1px solid var(--border-color);
  padding: 20px;
  border-radius: var(--radius-md);
  background: #fff;
  transition: 0.2s;
}

.start-card:hover {
  transform: translateY(-3px);
  border-color: var(--primary-color);
}

.start-card-highlight {
  border-color: rgba(255,128,0,0.4);
}

/* ==========================================================================
BLOG GRID
========================================================================== */
.blog-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(260px,1fr));
  gap: 20px;
}

.blog-card {
  border: 1px solid var(--border-color);
  padding: 20px;
  background: #fff;
  border-radius: var(--radius-md);
}

.blog-card__title {
  font-weight: 700;
}

/* ==========================================================================
POST ROW
========================================================================== */
.post-row {
  padding: 10px 0;
  border-bottom: 1px solid var(--border-color);
}

/* ==========================================================================
CTA BOX
========================================================================== */
.orient-box {
  margin: 40px 0;
  padding: 25px;
  background: #1a202c;
  color: #fff;
  text-align: center;
  border-radius: var(--radius-md);
}

/* ==========================================================================
FOOTER
========================================================================== */
.site-footer {
  background: #1a202c;
  color: #cbd5e1;
  padding: 40px 0;
  margin-top: 40px;
  }
