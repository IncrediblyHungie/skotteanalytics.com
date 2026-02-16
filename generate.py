#!/usr/bin/env python3
"""Generate programmatic SEO pages for Skotte Analytics."""

import json
import os
from html import escape
from datetime import date

SITE_DIR = os.path.dirname(os.path.abspath(__file__))
SITE_URL = "https://skotteanalytics.com"
TODAY = date.today().isoformat()


def load_data():
    with open(os.path.join(SITE_DIR, "data", "content.json"), "r") as f:
        return json.load(f)


def prefix(depth):
    return "../" * depth


def get_head_html(title, description, canonical_url, depth, json_ld="", og_type="website"):
    p = prefix(depth)
    ld_block = ""
    if json_ld:
        ld_block = f"""
    <!-- JSON-LD -->
    <script type="application/ld+json">
    {json_ld}
    </script>"""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{escape(title)}</title>
    <meta name="description" content="{escape(description)}">
    <meta name="author" content="Skotte Analytics">

    <!-- Open Graph -->
    <meta property="og:title" content="{escape(title)}">
    <meta property="og:description" content="{escape(description)}">
    <meta property="og:url" content="{escape(canonical_url)}">
    <meta property="og:type" content="{escape(og_type)}">
    <meta property="og:site_name" content="Skotte Analytics">

    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary">
    <meta name="twitter:title" content="{escape(title)}">
    <meta name="twitter:description" content="{escape(description)}">

    <!-- Canonical -->
    <link rel="canonical" href="{escape(canonical_url)}">

    <!-- Favicon & RSS -->
    <link rel="icon" type="image/x-icon" href="{p}assets/favicon.ico">
    <link rel="alternate" type="application/rss+xml" title="Skotte Analytics Blog" href="/feed.xml">

    <!-- Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">

    <!-- Styles -->
    <link href="{p}css/styles.css" rel="stylesheet">{ld_block}
</head>
<body>"""


def get_nav_html(depth, active=""):
    p = prefix(depth)
    # For pages inside services/, service links are relative (no prefix).
    # For all generated pages, services are at {p}services/...
    svc_prefix = f"{p}services/"

    # Determine active classes
    home_active = ' nav-header__link--active' if active == 'home' else ''
    services_active = ' nav-header__link--active' if active == 'services' else ''
    cases_active = ' nav-header__link--active' if active == 'cases' else ''
    blog_active = ' nav-header__link--active' if active == 'blog' else ''
    about_active = ' nav-header__link--active' if active == 'about' else ''

    return f"""
    <!-- Navigation -->
    <header class="nav-header" role="banner">
        <div class="container nav-header__inner">
            <a href="{p}index.html" class="nav-header__logo">Skotte<span>.</span></a>

            <nav class="nav-header__links" role="navigation" aria-label="Main navigation">
                <a href="{p}index.html" class="nav-header__link{home_active}">Home</a>

                <div class="nav-dropdown">
                    <a href="#" class="nav-header__link{services_active} nav-dropdown__trigger">
                        Services
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>
                    </a>
                    <div class="nav-dropdown__menu">
                        <a href="{svc_prefix}ai-solutions.html" class="nav-dropdown__item">AI Solutions</a>
                        <a href="{svc_prefix}automation.html" class="nav-dropdown__item">Automation</a>
                        <a href="{svc_prefix}optimization.html" class="nav-dropdown__item">Optimization</a>
                    </div>
                </div>

                <a href="{p}projects.html" class="nav-header__link{cases_active}">Case Studies</a>
                <a href="{p}blog/" class="nav-header__link{blog_active}">Blog</a>
                <a href="{p}about.html" class="nav-header__link{about_active}">About</a>

                <div class="nav-header__cta">
                    <a href="{p}contact.html" class="btn btn-primary">Contact</a>
                </div>
            </nav>

            <button class="nav-toggle" aria-label="Toggle menu" aria-expanded="false">
                <span class="nav-toggle__bar"></span>
                <span class="nav-toggle__bar"></span>
                <span class="nav-toggle__bar"></span>
            </button>
        </div>
    </header>

    <!-- Mobile Navigation -->
    <nav class="nav-mobile" role="navigation" aria-label="Mobile navigation">
        <a href="{p}index.html" class="nav-mobile__link">Home</a>
        <a href="{p}projects.html" class="nav-mobile__link">Case Studies</a>
        <a href="{p}blog/" class="nav-mobile__link">Blog</a>
        <a href="{p}about.html" class="nav-mobile__link">About</a>

        <div class="nav-mobile__sublabel">Services</div>
        <a href="{svc_prefix}ai-solutions.html" class="nav-mobile__sublink">AI Solutions</a>
        <a href="{svc_prefix}automation.html" class="nav-mobile__sublink">Automation</a>
        <a href="{svc_prefix}optimization.html" class="nav-mobile__sublink">Optimization</a>

        <div class="nav-mobile__cta">
            <a href="{p}contact.html" class="btn btn-primary btn--lg" style="width:100%;justify-content:center;">Contact Us</a>
        </div>
    </nav>"""


def get_cta_html(depth, title="Ready to get started?", text="Tell us what's slowing you down. We'll show you what AI can do about it."):
    p = prefix(depth)
    return f"""
        <!-- CTA Section -->
        <section class="section section--lg cta-banner">
            <div class="cta-banner__glow" aria-hidden="true"></div>
            <div class="container">
                <div class="cta-banner__inner reveal">
                    <h2 class="cta-banner__title">{escape(title)}</h2>
                    <p class="cta-banner__text">{escape(text)}</p>
                    <a href="{p}contact.html" class="btn btn-primary btn--lg">Get Started</a>
                </div>
            </div>
        </section>"""


def get_footer_html(depth):
    p = prefix(depth)
    svc_prefix = f"{p}services/"
    return f"""
    <!-- Footer -->
    <footer class="site-footer" role="contentinfo">
        <div class="container site-footer__inner">
            <div class="site-footer__top">
                <div>
                    <div class="site-footer__brand">Skotte<span>.</span></div>
                    <p class="site-footer__tagline">AI and automation consulting for growing businesses.</p>
                </div>
                <nav class="site-footer__nav" aria-label="Footer navigation">
                    <a href="{p}index.html" class="site-footer__link">Home</a>
                    <a href="{svc_prefix}ai-solutions.html" class="site-footer__link">Services</a>
                    <a href="{p}projects.html" class="site-footer__link">Case Studies</a>
                    <a href="{p}blog/" class="site-footer__link">Blog</a>
                    <a href="{p}about.html" class="site-footer__link">About</a>
                    <a href="{p}contact.html" class="site-footer__link">Contact</a>
                </nav>
            </div>
            <div class="site-footer__bottom">
                <p class="site-footer__copy">&copy; 2026 Skotte Analytics. All rights reserved.</p>
                <div class="site-footer__socials">
                    <a href="https://www.linkedin.com/in/peterskotte1" class="site-footer__social" aria-label="LinkedIn" target="_blank" rel="noopener noreferrer">
                        <svg viewBox="0 0 24 24" fill="currentColor"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 0 1-2.063-2.065 2.064 2.064 0 1 1 2.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>
                    </a>
                    <a href="https://github.com/peterskotte" class="site-footer__social" aria-label="GitHub" target="_blank" rel="noopener noreferrer">
                        <svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 0C5.374 0 0 5.373 0 12c0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23A11.509 11.509 0 0 1 12 5.803c1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576C20.566 21.797 24 17.3 24 12c0-6.627-5.373-12-12-12z"/></svg>
                    </a>
                </div>
            </div>
        </div>
    </footer>"""


def get_scripts_html():
    return """
    <!-- Scripts -->
    <script>
        // Mobile menu toggle
        const navToggle = document.querySelector('.nav-toggle');
        const navMobile = document.querySelector('.nav-mobile');

        if (navToggle && navMobile) {
            navToggle.addEventListener('click', () => {
                const isOpen = navMobile.classList.toggle('is-open');
                navToggle.classList.toggle('is-active');
                navToggle.setAttribute('aria-expanded', isOpen);
                document.body.style.overflow = isOpen ? 'hidden' : '';
            });
        }

        // Scroll reveal (IntersectionObserver)
        const reveals = document.querySelectorAll('.reveal');
        if (reveals.length && 'IntersectionObserver' in window) {
            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('is-visible');
                        observer.unobserve(entry.target);
                    }
                });
            }, { threshold: 0.15, rootMargin: '0px 0px -40px 0px' });

            reveals.forEach(el => observer.observe(el));
        } else {
            reveals.forEach(el => el.classList.add('is-visible'));
        }
    </script>
</body>
</html>"""


# --- SVG icon library for cards ---

ICON_AI = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2a4 4 0 0 1 4 4v1a1 1 0 0 0 1 1h1a4 4 0 0 1 0 8h-1a1 1 0 0 0-1 1v1a4 4 0 0 1-8 0v-1a1 1 0 0 0-1-1H6a4 4 0 0 1 0-8h1a1 1 0 0 0 1-1V6a4 4 0 0 1 4-4z"/><circle cx="12" cy="12" r="2"/></svg>'

ICON_AUTOMATION = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/></svg>'

ICON_OPTIMIZATION = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg>'

ICON_PAIN = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>'

ICON_CHECK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>'

ICON_CHART = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/></svg>'

ICON_ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>'

SERVICE_ICONS = {
    "ai-solutions": ICON_AI,
    "automation": ICON_AUTOMATION,
    "optimization": ICON_OPTIMIZATION,
}


def get_service_use_case_key(service_slug):
    mapping = {
        "ai-solutions": "ai_use_cases",
        "automation": "processes_to_automate",
        "optimization": "analytics_use_cases",
    }
    return mapping.get(service_slug, "ai_use_cases")


# --- Page generators ---

def generate_industry_overview(industry, services, depth=2):
    slug = industry["slug"]
    display = industry["display_name"]
    title = f"{display} — AI & Automation | Skotte Analytics"
    desc = industry["description"][:160]
    canonical = f"{SITE_URL}/industries/{slug}/"
    p = prefix(depth)

    json_ld = json.dumps({
        "@context": "https://schema.org",
        "@type": "WebPage",
        "name": f"AI & Automation for {display}",
        "description": desc,
        "url": canonical,
        "publisher": {
            "@type": "Organization",
            "name": "Skotte Analytics",
            "url": SITE_URL,
        },
    }, indent=8)

    # Build pain points list
    pain_items = ""
    for pp in industry["pain_points"]:
        pain_items += f"\n                        <li>{escape(pp)}</li>"

    # Build service cards
    service_cards = ""
    for i, svc in enumerate(services):
        delay = f" reveal--delay-{i + 1}" if i > 0 else ""
        icon = SERVICE_ICONS.get(svc["slug"], ICON_AI)
        use_key = get_service_use_case_key(svc["slug"])
        use_cases = industry.get(use_key, [])
        preview = use_cases[0] if use_cases else svc["capabilities"][0]
        service_cards += f"""
                    <a href="{svc['slug']}.html" class="card reveal{delay}" style="text-decoration:none; color:inherit;">
                        <div class="card__icon">
                            {icon}
                        </div>
                        <h3 class="card__title">{escape(svc['name'])}</h3>
                        <p class="card__text">{escape(preview)}</p>
                        <span class="card__link">
                            Learn more
                            {ICON_ARROW}
                        </span>
                    </a>"""

    html = get_head_html(title, desc, canonical, depth, json_ld)
    html += get_nav_html(depth, active="services")
    html += f"""

    <main>
        <!-- Page Header -->
        <section class="page-header">
            <div class="page-header__bg" aria-hidden="true">
                <div class="hero__gradient hero__gradient--1"></div>
                <div class="hero__gradient hero__gradient--2"></div>
                <div class="hero__grid-pattern"></div>
            </div>

            <div class="container page-header__content">
                <div class="section__label">{escape(industry['name'])}</div>
                <h1 class="section__title" style="font-size:clamp(2.25rem, 5vw, var(--text-5xl)); font-weight:var(--weight-extrabold); letter-spacing:-0.03em;">AI &amp; Automation for {escape(display)}</h1>
                <p class="section__subtitle" style="max-width:640px;">{escape(industry['hero_stat'])}</p>
            </div>
        </section>

        <!-- Industry Description -->
        <section class="section section--lg" style="background:var(--color-surface); border-top:1px solid var(--color-border); border-bottom:1px solid var(--color-border);">
            <div class="container">
                <div class="section__header section__header--center reveal">
                    <div class="section__label">The Challenge</div>
                    <h2 class="section__title">What's holding {escape(industry['name'].lower())} businesses back</h2>
                    <p class="section__subtitle">{escape(industry['description'])}</p>
                </div>

                <div class="container container--narrow" style="margin-top:var(--space-12);">
                    <div class="card reveal">
                        <div class="card__icon">
                            {ICON_PAIN}
                        </div>
                        <h3 class="card__title">Common Pain Points</h3>
                        <ul style="color:var(--color-text); line-height:1.75; padding-left:var(--space-6);">{pain_items}
                        </ul>
                    </div>
                </div>
            </div>
        </section>

        <!-- Services for This Industry -->
        <section class="section section--lg">
            <div class="container">
                <div class="section__header section__header--center reveal">
                    <div class="section__label">Our Services</div>
                    <h2 class="section__title">How we help {escape(industry['name'].lower())} businesses</h2>
                    <p class="section__subtitle">Three ways we apply technology to solve real problems in your industry.</p>
                </div>

                <div class="grid grid--3">{service_cards}
                </div>
            </div>
        </section>
{get_cta_html(depth, title=f"Ready to modernize your {industry['name'].lower()} business?", text="Tell us what's slowing you down. We'll show you what AI and automation can do about it.")}
    </main>
{get_footer_html(depth)}
{get_scripts_html()}"""

    return html


def generate_industry_service(industry, service, depth=2):
    ind_slug = industry["slug"]
    svc_slug = service["slug"]
    ind_display = industry["display_name"]
    svc_name = service["name"]
    title = f"{svc_name} for {ind_display} — Skotte Analytics"
    tagline = service["tagline_template"].format(industry=industry["name"].lower())
    use_key = get_service_use_case_key(svc_slug)
    use_cases = industry.get(use_key, [])
    pain_points = industry["pain_points"]
    capabilities = service["capabilities"]

    specific_benefit = use_cases[0] if use_cases else capabilities[0]
    desc_text = service["description_template"].format(
        industry_display=ind_display.lower(),
        specific_benefit=specific_benefit,
    )
    desc = desc_text[:160]
    canonical = f"{SITE_URL}/industries/{ind_slug}/{svc_slug}.html"
    p = prefix(depth)

    json_ld = json.dumps({
        "@context": "https://schema.org",
        "@type": "Service",
        "name": f"{svc_name} for {ind_display}",
        "provider": {
            "@type": "Organization",
            "name": "Skotte Analytics",
            "url": SITE_URL,
        },
        "description": desc_text,
        "areaServed": "US",
    }, indent=8)

    # Build pain points HTML
    pain_cards = ""
    for i, pp in enumerate(pain_points):
        delay_cls = f" reveal--delay-{(i % 3) + 1}" if i > 0 else ""
        pain_cards += f"""
                    <div class="card reveal{delay_cls}">
                        <div class="card__icon">
                            {ICON_PAIN}
                        </div>
                        <p class="card__text">{escape(pp)}</p>
                    </div>"""

    # Build use cases HTML
    use_case_items = ""
    for uc in use_cases:
        use_case_items += f"""
                    <div class="card reveal">
                        <div class="card__icon">
                            {ICON_CHECK}
                        </div>
                        <p class="card__text">{escape(uc)}</p>
                    </div>"""

    # Build capabilities list
    cap_items = ""
    for cap in capabilities:
        cap_items += f"\n                        <li>{escape(cap)}</li>"

    # Use case section label based on service
    use_case_label_map = {
        "ai-solutions": "AI Use Cases",
        "automation": "What We Automate",
        "optimization": "Analytics & Insights",
    }
    use_case_label = use_case_label_map.get(svc_slug, "Use Cases")

    html = get_head_html(title, desc, canonical, depth, json_ld)
    html += get_nav_html(depth, active="services")
    html += f"""

    <main>
        <!-- Page Header -->
        <section class="page-header">
            <div class="page-header__bg" aria-hidden="true">
                <div class="hero__gradient hero__gradient--1"></div>
                <div class="hero__gradient hero__gradient--2"></div>
                <div class="hero__grid-pattern"></div>
            </div>

            <div class="container page-header__content">
                <div class="section__label">{escape(industry['name'])} &times; {escape(svc_name)}</div>
                <h1 class="section__title" style="font-size:clamp(2.25rem, 5vw, var(--text-5xl)); font-weight:var(--weight-extrabold); letter-spacing:-0.03em;">{escape(svc_name)} for {escape(ind_display)}</h1>
                <p class="section__subtitle" style="max-width:640px;">{escape(tagline)}</p>
            </div>
        </section>

        <!-- Pain Points -->
        <section class="section section--lg" style="background:var(--color-surface); border-top:1px solid var(--color-border); border-bottom:1px solid var(--color-border);">
            <div class="container">
                <div class="section__header section__header--center reveal">
                    <div class="section__label">The Problem</div>
                    <h2 class="section__title">Challenges facing {escape(industry['name'].lower())} businesses</h2>
                    <p class="section__subtitle">{escape(industry['hero_stat'])}</p>
                </div>

                <div class="grid grid--2">{pain_cards}
                </div>
            </div>
        </section>

        <!-- Use Cases -->
        <section class="section section--lg">
            <div class="container">
                <div class="section__header section__header--center reveal">
                    <div class="section__label">{escape(use_case_label)}</div>
                    <h2 class="section__title">How {escape(svc_name.lower())} applies to {escape(industry['name'].lower())}</h2>
                    <p class="section__subtitle">Specific applications tailored to the way your industry works.</p>
                </div>

                <div class="grid grid--2">{use_case_items}
                </div>
            </div>
        </section>

        <!-- Capabilities -->
        <section class="section section--lg" style="background:var(--color-surface); border-top:1px solid var(--color-border); border-bottom:1px solid var(--color-border);">
            <div class="container">
                <div class="section__header section__header--center reveal">
                    <div class="section__label">Capabilities</div>
                    <h2 class="section__title">What we bring to the table</h2>
                </div>

                <div class="container container--narrow">
                    <div class="card reveal">
                        <div class="card__icon">
                            {SERVICE_ICONS.get(svc_slug, ICON_AI)}
                        </div>
                        <h3 class="card__title">{escape(svc_name)} Capabilities</h3>
                        <ul style="color:var(--color-text); line-height:1.75; padding-left:var(--space-6);">{cap_items}
                        </ul>
                    </div>
                </div>
            </div>
        </section>
{get_cta_html(depth, title=f"Ready for {svc_name.lower()} in your {industry['name'].lower()} business?", text="Tell us what's slowing you down. We'll show you what's possible.")}
    </main>
{get_footer_html(depth)}
{get_scripts_html()}"""

    return html


def generate_blog_post(post, services, industries, depth=1):
    slug = post["slug"]
    title = f"{post['title']} — Skotte Analytics"
    desc = post["meta_description"]
    canonical = f"{SITE_URL}/blog/{slug}.html"
    p = prefix(depth)

    json_ld = json.dumps({
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": post["title"],
        "author": {
            "@type": "Person",
            "name": "Peter Skotte",
        },
        "datePublished": TODAY,
        "publisher": {
            "@type": "Organization",
            "name": "Skotte Analytics",
            "url": SITE_URL,
        },
        "mainEntityOfPage": {
            "@type": "WebPage",
            "@id": canonical,
        },
    }, indent=8)

    # Build related industries links
    ind_map = {ind["slug"]: ind for ind in industries}
    related_ind_links = ""
    for ri_slug in post.get("related_industries", []):
        ri = ind_map.get(ri_slug)
        if ri:
            related_ind_links += f' <a href="{p}industries/{ri["slug"]}/" style="color:var(--color-primary); text-decoration:none; font-weight:var(--weight-semibold);">{escape(ri["display_name"])}</a>,'
    if related_ind_links:
        related_ind_links = related_ind_links.rstrip(",")

    # Build related service link
    related_svc = post.get("related_service", "")
    svc_map = {s["slug"]: s for s in services}
    svc = svc_map.get(related_svc)
    related_svc_link = ""
    if svc:
        related_svc_link = f'<a href="{p}services/{svc["slug"]}.html" style="color:var(--color-primary); text-decoration:none; font-weight:var(--weight-semibold);">{escape(svc["name"])}</a>'

    # Build article sections
    sections_html = ""
    for section in post.get("sections", []):
        sections_html += f"""
                    <h2>{escape(section['heading'])}</h2>

                    <p>{escape(section['content'])}</p>
"""

    # Build related industries paragraph
    related_para = ""
    if related_ind_links:
        related_para = f"""
                    <p style="font-size:var(--text-sm); color:var(--color-text-faint); margin-top:var(--space-8); padding-top:var(--space-6); border-top:1px solid var(--color-border);">
                        <strong>Related industries:</strong>{related_ind_links}
                    </p>"""

    # CTA within article
    cta_inline = ""
    if post.get("cta_text") and related_svc_link:
        cta_inline = f"""
                    <p style="margin-top:var(--space-8); padding:var(--space-6); background:var(--color-surface); border-radius:var(--radius-lg); border:1px solid var(--color-border);">
                        {escape(post['cta_text'])} {related_svc_link}
                    </p>"""

    html = get_head_html(title, desc, canonical, depth, json_ld, og_type="article")
    html += get_nav_html(depth, active="blog")
    html += f"""

    <main>
        <!-- Page Header -->
        <section class="page-header">
            <div class="page-header__bg" aria-hidden="true">
                <div class="hero__gradient hero__gradient--1"></div>
                <div class="hero__gradient hero__gradient--2"></div>
                <div class="hero__grid-pattern"></div>
            </div>

            <div class="container page-header__content" style="max-width:var(--container-narrow); margin-inline:auto;">
                <div class="section__label">Blog</div>
                <h1 class="section__title" style="font-size:clamp(2.25rem, 5vw, var(--text-5xl)); font-weight:var(--weight-extrabold); letter-spacing:-0.03em;">{escape(post['title'])}</h1>
                <div style="display:flex; align-items:center; gap:var(--space-4); margin-top:var(--space-4); font-size:var(--text-sm); color:var(--color-text-faint);">
                    <span>Peter Skotte</span>
                    <span aria-hidden="true">&middot;</span>
                    <time datetime="{TODAY}">{date.today().strftime('%B %d, %Y')}</time>
                </div>
            </div>
        </section>

        <!-- Article Body -->
        <section class="section section--lg">
            <div class="container container--narrow">
                <article class="prose">

                    <p>{escape(post['intro'])}</p>
{sections_html}{cta_inline}{related_para}
                </article>
            </div>
        </section>
{get_cta_html(depth, title="Ready to put this into practice?", text="Tell us what's slowing you down. We'll show you what's possible.")}
    </main>
{get_footer_html(depth)}
{get_scripts_html()}"""

    return html


def update_sitemap(industries, services, posts):
    # Keep all existing hand-crafted pages
    existing = [
        ("https://skotteanalytics.com/", "1.0", "weekly"),
        ("https://skotteanalytics.com/services/ai-solutions.html", "0.9", "weekly"),
        ("https://skotteanalytics.com/services/automation.html", "0.9", "weekly"),
        ("https://skotteanalytics.com/services/optimization.html", "0.9", "weekly"),
        ("https://skotteanalytics.com/projects.html", "0.8", "monthly"),
        ("https://skotteanalytics.com/about.html", "0.8", "monthly"),
        ("https://skotteanalytics.com/contact.html", "0.8", "monthly"),
        ("https://skotteanalytics.com/blog/", "0.7", "weekly"),
        ("https://skotteanalytics.com/blog/how-small-businesses-are-using-ai-2026.html", "0.6", "monthly"),
        ("https://skotteanalytics.com/blog/5-business-processes-you-should-automate.html", "0.6", "monthly"),
        ("https://skotteanalytics.com/blog/what-does-an-ai-consultant-do.html", "0.6", "monthly"),
    ]

    xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'

    for loc, priority, freq in existing:
        xml += f"  <url>\n"
        xml += f"    <loc>{loc}</loc>\n"
        xml += f"    <lastmod>{TODAY}</lastmod>\n"
        xml += f"    <changefreq>{freq}</changefreq>\n"
        xml += f"    <priority>{priority}</priority>\n"
        xml += f"  </url>\n"

    # Industry overview pages
    for ind in industries:
        xml += f"  <url>\n"
        xml += f"    <loc>{SITE_URL}/industries/{ind['slug']}/</loc>\n"
        xml += f"    <lastmod>{TODAY}</lastmod>\n"
        xml += f"    <changefreq>monthly</changefreq>\n"
        xml += f"    <priority>0.5</priority>\n"
        xml += f"  </url>\n"

    # Industry x service pages
    for ind in industries:
        for svc in services:
            xml += f"  <url>\n"
            xml += f"    <loc>{SITE_URL}/industries/{ind['slug']}/{svc['slug']}.html</loc>\n"
            xml += f"    <lastmod>{TODAY}</lastmod>\n"
            xml += f"    <changefreq>monthly</changefreq>\n"
            xml += f"    <priority>0.5</priority>\n"
            xml += f"  </url>\n"

    # Blog posts
    for post in posts:
        xml += f"  <url>\n"
        xml += f"    <loc>{SITE_URL}/blog/{post['slug']}.html</loc>\n"
        xml += f"    <lastmod>{TODAY}</lastmod>\n"
        xml += f"    <changefreq>monthly</changefreq>\n"
        xml += f"    <priority>0.6</priority>\n"
        xml += f"  </url>\n"

    xml += "</urlset>\n"

    with open(os.path.join(SITE_DIR, "sitemap.xml"), "w") as f:
        f.write(xml)


def update_blog_index(posts, depth=1):
    p = prefix(depth)

    # The 3 original hand-crafted posts
    original_posts = [
        {
            "date": "February 16, 2026",
            "title": "How Small Businesses Are Using AI in 2026",
            "href": "how-small-businesses-are-using-ai-2026.html",
            "desc": "AI isn't just for big tech anymore. Here's how small businesses are using AI in 2026 to automate customer service, generate content, optimize operations, and make better decisions.",
        },
        {
            "date": "February 16, 2026",
            "title": "5 Business Processes You Should Automate Today",
            "href": "5-business-processes-you-should-automate.html",
            "desc": "If you're doing it manually every week, it should be automated. Here are the five business processes where automation delivers the biggest ROI.",
        },
        {
            "date": "February 16, 2026",
            "title": "What Does an AI Consultant Actually Do?",
            "href": "what-does-an-ai-consultant-do.html",
            "desc": "AI consultant sounds vague. Here's what it actually means — from discovery to deployment — and when your business is ready to hire one.",
        },
    ]

    title = "Blog — Skotte Analytics"
    description = "AI, automation, and analytics insights for small business owners. Practical advice on implementing technology to save time and grow revenue."
    canonical = f"{SITE_URL}/blog/"

    json_ld = json.dumps({
        "@context": "https://schema.org",
        "@type": "CollectionPage",
        "name": "Skotte Analytics Blog",
        "description": "AI, automation, and analytics insights for small business owners.",
        "url": canonical,
        "publisher": {
            "@type": "Organization",
            "name": "Skotte Analytics",
            "url": SITE_URL,
        },
    }, indent=8)

    # Build original post cards
    original_html = ""
    for i, op in enumerate(original_posts):
        delay = f" reveal--delay-{i}" if i > 0 else ""
        original_html += f"""
                    <!-- Original Post {i + 1} -->
                    <article class="card reveal{delay}">
                        <div style="font-size:var(--text-sm); color:var(--color-text-faint); margin-bottom:var(--space-3);">{op['date']}</div>
                        <h2 style="font-size:var(--text-xl); font-weight:var(--weight-bold); margin-bottom:var(--space-3);">
                            <a href="{op['href']}" style="color:var(--color-heading); text-decoration:none;">{escape(op['title'])}</a>
                        </h2>
                        <p class="card__text">{escape(op['desc'])}</p>
                        <a href="{op['href']}" class="card__link">
                            Read more
                            {ICON_ARROW}
                        </a>
                    </article>
"""

    # Build generated post cards
    generated_html = ""
    formatted_date = date.today().strftime("%B %d, %Y")
    for i, post in enumerate(posts):
        delay = f" reveal--delay-{(i % 3) + 1}" if i > 0 else ""
        generated_html += f"""
                    <article class="card reveal{delay}">
                        <div style="font-size:var(--text-sm); color:var(--color-text-faint); margin-bottom:var(--space-3);">{formatted_date}</div>
                        <h2 style="font-size:var(--text-xl); font-weight:var(--weight-bold); margin-bottom:var(--space-3);">
                            <a href="{post['slug']}.html" style="color:var(--color-heading); text-decoration:none;">{escape(post['title'])}</a>
                        </h2>
                        <p class="card__text">{escape(post['meta_description'])}</p>
                        <a href="{post['slug']}.html" class="card__link">
                            Read more
                            {ICON_ARROW}
                        </a>
                    </article>
"""

    html = get_head_html(title, description, canonical, depth, json_ld)
    html += get_nav_html(depth, active="blog")
    html += f"""

    <main>
        <!-- Page Header -->
        <section class="page-header">
            <div class="page-header__bg" aria-hidden="true">
                <div class="hero__gradient hero__gradient--1"></div>
                <div class="hero__gradient hero__gradient--2"></div>
                <div class="hero__grid-pattern"></div>
            </div>

            <div class="container page-header__content">
                <div class="section__label">Blog</div>
                <h1 class="section__title" style="font-size:clamp(2.25rem, 5vw, var(--text-5xl)); font-weight:var(--weight-extrabold); letter-spacing:-0.03em;">Blog</h1>
                <p class="section__subtitle" style="max-width:640px;">Practical insights on AI, automation, and analytics for business owners</p>
            </div>
        </section>

        <!-- Featured Posts -->
        <section class="section section--lg">
            <div class="container container--narrow">
                <div style="display:flex; flex-direction:column; gap:var(--space-8);">
{original_html}
                </div>
            </div>
        </section>

        <!-- More Articles -->
        <section class="section section--lg" style="background:var(--color-surface); border-top:1px solid var(--color-border); border-bottom:1px solid var(--color-border);">
            <div class="container container--narrow">
                <div class="section__header reveal" style="margin-bottom:var(--space-8);">
                    <div class="section__label">More Articles</div>
                    <h2 class="section__title">How-To Guides & Deep Dives</h2>
                </div>
                <div style="display:flex; flex-direction:column; gap:var(--space-8);">
{generated_html}
                </div>
            </div>
        </section>
{get_cta_html(depth, title="Ready to put AI to work for your business?", text="Tell us what's slowing you down. We'll show you what's possible.")}
    </main>
{get_footer_html(depth)}
{get_scripts_html()}"""

    with open(os.path.join(SITE_DIR, "blog", "index.html"), "w") as f:
        f.write(html)


def main():
    data = load_data()
    services = data["services"]
    industries = data["industries"]
    posts = data["how_to_posts"]

    counts = {"industry_overview": 0, "industry_service": 0, "blog": 0}

    # Create industry directories and generate pages
    for ind in industries:
        ind_dir = os.path.join(SITE_DIR, "industries", ind["slug"])
        os.makedirs(ind_dir, exist_ok=True)

        # Industry overview
        html = generate_industry_overview(ind, services, depth=2)
        with open(os.path.join(ind_dir, "index.html"), "w") as f:
            f.write(html)
        counts["industry_overview"] += 1

        # Industry x service pages
        for svc in services:
            html = generate_industry_service(ind, svc, depth=2)
            with open(os.path.join(ind_dir, f"{svc['slug']}.html"), "w") as f:
                f.write(html)
            counts["industry_service"] += 1

    # Generate blog posts
    for post in posts:
        html = generate_blog_post(post, services, industries, depth=1)
        with open(os.path.join(SITE_DIR, "blog", f"{post['slug']}.html"), "w") as f:
            f.write(html)
        counts["blog"] += 1

    # Update sitemap
    update_sitemap(industries, services, posts)

    # Update blog index
    update_blog_index(posts, depth=1)

    total = counts["industry_overview"] + counts["industry_service"] + counts["blog"]
    print(f"Generated {total} pages:")
    print(f"  {counts['industry_overview']} industry overview pages")
    print(f"  {counts['industry_service']} industry x service pages")
    print(f"  {counts['blog']} blog posts")
    print(f"  Updated sitemap.xml")
    print(f"  Updated blog/index.html")


if __name__ == "__main__":
    main()
