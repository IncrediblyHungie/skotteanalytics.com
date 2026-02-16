# Skotte Analytics — Business Rebrand & SEO Overhaul Design

**Date**: 2026-02-16
**Status**: Approved

## Summary

Rebrand skotteanalytics.com from federal government consulting to AI & automation consulting for business owners. Full visual redesign, new messaging, SEO overhaul inspired by BidKing strategies, and blog content for organic traffic.

## Target Audience

- Primary: Small business owners (1-50 employees)
- Secondary: Mid-market companies (50-500 employees)
- Lead with small biz messaging, serve both

## Service Focus

Narrowed from 6 general services to 3 AI/automation-focused offerings:
1. **AI Solutions** — chatbots, content generation, AI-powered workflows
2. **Process Automation** — automate reports, data entry, repetitive tasks
3. **Optimization & Analytics** — dashboards, forecasting, KPI tracking

## Architecture: Static HTML (Approach A)

No framework, no build tools. Static HTML + CSS + minimal JS. Deployable anywhere.

### Page Structure

| Page | URL | Purpose |
|------|-----|---------|
| Homepage | `/index.html` | Hero + value prop + services overview + social proof + CTA |
| AI Solutions | `/services/ai-solutions.html` | SEO landing page: "AI for small business" |
| Process Automation | `/services/automation.html` | SEO landing page: "business process automation" |
| Optimization & Analytics | `/services/optimization.html` | SEO landing page: "business optimization consulting" |
| Case Studies | `/projects.html` | Commercial case studies with results/metrics |
| About | `/about.html` | Story, credentials, why Skotte Analytics |
| Contact | `/contact.html` | Clean contact layout, no federal language |
| Blog Index | `/blog/index.html` | Post listing with excerpts |
| Blog Post 1 | `/blog/how-small-businesses-are-using-ai-2026.html` | Long-tail SEO content |
| Blog Post 2 | `/blog/5-business-processes-you-should-automate.html` | Long-tail SEO content |
| Blog Post 3 | `/blog/what-does-an-ai-consultant-do.html` | Long-tail SEO content |

### Removed
- `resume.html` → replaced by `about.html`
- `capability-statement.html` → no longer relevant
- All federal contracting language

## Messaging & Positioning

**Brand voice**: Direct, results-focused, no corporate fluff. Business owner language.

**Homepage hero**: "AI & Automation for Growing Businesses"

**Service framing**:
- AI Solutions → "Put AI to work in your business"
- Process Automation → "Stop doing things the slow way"
- Optimization & Analytics → "Make decisions with data, not gut feelings"

**Case studies reorder** (lead with commercial):
1. ETL & KPI Automation ($100K, 80% reduction in manual reporting)
2. Predictive Sales Forecasting ($100K, AI-powered)
3. National Sales Dashboards ($25K, accessible entry point)
4. E-Commerce Analytics (relatable to SMBs)
5. Federal Contracting DB (bottom or cut)

## SEO Implementation (from BidKing)

### Technical SEO
- `robots.txt` — allow search engines, block AI training crawlers (Google-Extended, CCBot, Bytespider)
- `sitemap.xml` — all pages with priority hierarchy (1.0 homepage, 0.8 services, 0.7 blog)
- JSON-LD structured data — Organization + LocalBusiness + Service schemas
- Open Graph + Twitter card tags on every page
- Canonical URLs on every page
- `llms.txt` — service description for AI search engines
- Google Analytics 4 (need property ID)
- Keyword-targeted meta descriptions per page
- Proper `<h1>`-`<h6>` hierarchy
- RSS feed at `/feed.xml` for blog

### Content SEO
- 3 service landing pages targeting keyword clusters
- 3 starter blog posts targeting long-tail keywords
- Internal linking: service pages → case studies → blog posts
- Each page targets specific keyword intent

### Blog Post Topics
1. "How Small Businesses Are Using AI in 2026" — high volume, informational
2. "5 Business Processes You Should Automate Today" — actionable, commercial intent
3. "What Does an AI Consultant Actually Do?" — builds trust, answers common question

## Visual Design

- Full redesign using frontend-design skill
- Modern, clean, professional — "I know technology"
- Distinctive, not generic SaaS template
- Dark/light contrast, strong typography
- Custom CSS (no Bootstrap)
- Mobile-first responsive
- Image optimization (compress profile.png from 4.5MB)

## Technical Details

- Static HTML + CSS + minimal JS
- No framework dependencies
- Custom CSS via frontend-design skill
- Fast load times (no heavy libraries)
- Mobile-first responsive design
