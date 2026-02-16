# Blog Expansion & Contact Form Design

**Date**: 2026-02-16
**Status**: Approved

## Summary

Add programmatic SEO pages generated from templates + data, plus a Netlify-powered contact form. Target: 150+ landing pages covering industry × service keyword combinations.

## Contact Form

Netlify Forms on contact.html. Fields: name, email, company (optional), what they need help with (dropdown: AI Solutions, Automation, Analytics, Not Sure), message. `data-netlify="true"` attribute handles everything. Free tier = 100 submissions/month.

## Programmatic SEO Architecture

### Content Generator
Python script (`generate.py`) reads `data/content.json` and outputs HTML files using a template. Runs locally, output committed to git.

### Page Types

**Type 1: Industry × Service pages** (60 pages)
- URL pattern: `/industries/{industry}/{service}.html`
- Example: `/industries/healthcare/ai-solutions.html`
- Title: "AI Solutions for Healthcare — Skotte Analytics"
- Content: Industry-specific pain points, how the service applies, example use cases, CTA

20 industries × 3 services = 60 pages

**Type 2: How-to / Process pages** (40+ pages)
- URL pattern: `/blog/{slug}.html`
- Example: `/blog/how-to-automate-invoice-processing.html`
- Title: "How to Automate Invoice Processing — Skotte Analytics"
- Content: Problem description, manual vs automated comparison, steps, tools, CTA

**Type 3: Industry overview pages** (20 pages)
- URL pattern: `/industries/{industry}/index.html`
- Example: `/industries/healthcare/index.html`
- Title: "AI & Automation for Healthcare — Skotte Analytics"
- Content: Industry overview, all 3 services for that industry, links to specific service pages

### Target Industries (20)
1. Healthcare / Medical Practices
2. Real Estate
3. E-commerce / Retail
4. Restaurants / Food Service
5. Law Firms / Legal
6. Accounting / Financial Services
7. Construction / Contractors
8. Insurance
9. Manufacturing
10. Logistics / Distribution
11. Marketing Agencies
12. Dental Practices
13. Property Management
14. Fitness / Gyms
15. Auto Dealerships
16. Home Services (Landscaping, Plumbing, HVAC)
17. Veterinary
18. Staffing / Recruiting
19. Nonprofits
20. Education / Tutoring

### Generated Page Count
- 20 industry overview pages
- 60 industry × service pages
- 40+ how-to/process blog posts
- **Total: ~120+ pages**

### Data Structure (content.json)
```json
{
  "industries": [
    {
      "slug": "healthcare",
      "name": "Healthcare",
      "display_name": "Healthcare & Medical Practices",
      "pain_points": ["Patient scheduling chaos", "Manual billing and claims", "Paper-based records"],
      "processes_to_automate": ["appointment reminders", "insurance verification", "patient intake forms"],
      "ai_use_cases": ["patient triage chatbot", "medical document extraction", "appointment no-show prediction"],
      "analytics_use_cases": ["patient flow dashboards", "revenue cycle analytics", "provider performance tracking"]
    }
  ],
  "services": [
    {
      "slug": "ai-solutions",
      "name": "AI Solutions",
      "verb": "implement AI in",
      "tagline": "Put AI to work in your {industry} business"
    }
  ],
  "how_to_posts": [
    {
      "slug": "how-to-automate-invoice-processing",
      "title": "How to Automate Invoice Processing",
      "target_keyword": "automate invoice processing",
      "industry_tags": ["accounting", "construction", "ecommerce"]
    }
  ]
}
```

### Template Structure
Each generated page uses the same design system (nav, footer, CSS) as existing pages. Template includes:
- Full SEO head (title, meta description, OG tags, canonical, JSON-LD)
- Page header with industry/service context
- 3-4 content sections with industry-specific copy
- Internal links to related service pages and blog posts
- CTA linking to contact.html

### SEO Details
- Each page gets unique title, meta description, and canonical URL
- JSON-LD Service schema per industry × service page
- Internal linking: industry pages → service pages → blog posts → contact
- Add all generated pages to sitemap.xml (script updates it)
- Blog index updated to show all posts

## Technical Implementation
- `generate.py` — Python script, reads data, outputs HTML
- `data/content.json` — all industry/service/post data
- `templates/` — HTML templates with {placeholders}
- Script also regenerates `sitemap.xml` and `blog/index.html`
