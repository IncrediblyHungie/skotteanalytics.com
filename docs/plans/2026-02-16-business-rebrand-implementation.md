# Business Rebrand & SEO Overhaul — Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Rebrand skotteanalytics.com from federal government consulting to AI & automation consulting for business owners, with full redesign and SEO overhaul.

**Architecture:** Static HTML + custom CSS + minimal JS. No frameworks. Each page gets full SEO markup (Open Graph, JSON-LD, canonical URLs). Blog as static HTML files. BidKing-inspired robots.txt, sitemap.xml, llms.txt, and RSS feed.

**Tech Stack:** HTML5, custom CSS (no Bootstrap), vanilla JS, Google Fonts

**Design Doc:** `docs/plans/2026-02-16-business-rebrand-design.md`

---

## Phase 1: SEO Infrastructure

### Task 1: Create robots.txt

**Files:**
- Create: `robots.txt`

**Step 1: Create the file**

```
User-agent: Googlebot
Allow: /

User-agent: Bingbot
Allow: /

User-agent: Slurp
Allow: /

User-agent: DuckDuckBot
Allow: /

User-agent: Baiduspider
Allow: /

User-agent: YandexBot
Allow: /

User-agent: GPTBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: Anthropic-AI
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: AppleBot
Allow: /

User-agent: Google-Extended
Disallow: /

User-agent: CCBot
Disallow: /

User-agent: Bytespider
Disallow: /

User-agent: meta-externalagent
Disallow: /

User-agent: *
Allow: /

Sitemap: https://skotteanalytics.com/sitemap.xml
```

**Step 2: Verify**

Open `robots.txt` and confirm search engines are allowed, AI training crawlers are blocked, and sitemap is declared.

**Step 3: Commit**

```bash
git add robots.txt
git commit -m "feat(seo): add robots.txt with smart bot management"
```

---

### Task 2: Create llms.txt

**Files:**
- Create: `llms.txt`

**Step 1: Create the file**

```
# Skotte Analytics

> AI & Automation consulting for growing businesses. Based in San Diego, CA.

## Services

- AI Solutions: Custom AI integrations, chatbots, content generation workflows, and AI-powered business tools
- Process Automation: Python-powered automation for reports, data entry, file management, and repetitive business tasks
- Optimization & Analytics: Business intelligence dashboards, KPI tracking, sales forecasting, and data-driven decision making

## About

Skotte Analytics helps small and mid-market businesses implement AI, automate manual processes, and make better decisions with data. Founded by Peter Skotte in San Diego, CA.

## Key URLs

- Homepage: https://skotteanalytics.com/
- AI Solutions: https://skotteanalytics.com/services/ai-solutions.html
- Process Automation: https://skotteanalytics.com/services/automation.html
- Optimization & Analytics: https://skotteanalytics.com/services/optimization.html
- Case Studies: https://skotteanalytics.com/projects.html
- Blog: https://skotteanalytics.com/blog/
- Contact: https://skotteanalytics.com/contact.html

## Contact

- Email: peterskotte@protonmail.com
- Phone: (858) 254-0491
- LinkedIn: https://www.linkedin.com/in/peterskotte1
- GitHub: https://github.com/peterskotte
```

**Step 2: Commit**

```bash
git add llms.txt
git commit -m "feat(seo): add llms.txt for AI search engines"
```

---

### Task 3: Create sitemap.xml

**Files:**
- Create: `sitemap.xml`

**Step 1: Create the file**

XML sitemap with all pages, priority hierarchy:
- 1.0: homepage
- 0.9: service landing pages
- 0.8: projects, about, contact
- 0.7: blog index
- 0.6: individual blog posts

Use `lastmod` date of 2026-02-16 for all initial pages. `changefreq`: weekly for homepage/services, monthly for blog posts.

**Step 2: Commit**

```bash
git add sitemap.xml
git commit -m "feat(seo): add XML sitemap with priority hierarchy"
```

---

### Task 4: Create RSS feed

**Files:**
- Create: `feed.xml`

**Step 1: Create the file**

RSS 2.0 feed for blog posts. Include:
- Channel title: "Skotte Analytics Blog"
- Channel description: "AI, automation, and optimization insights for business owners"
- Channel link: https://skotteanalytics.com/blog/
- Items for each blog post with title, description, link, pubDate

**Step 2: Commit**

```bash
git add feed.xml
git commit -m "feat(seo): add RSS feed for blog content syndication"
```

---

## Phase 2: Full Redesign — Homepage

### Task 5: Design and build the new homepage

**Files:**
- Rewrite: `index.html`
- Create: `css/styles.css` (full rewrite — custom CSS replacing Bootstrap)

**Step 1: Invoke frontend-design skill**

Use `@frontend-design` skill to create the homepage. Provide these requirements:

- **Page type**: Consulting firm homepage
- **Sections**: Nav, hero, services overview (3 cards), social proof/metrics, about teaser, CTA, footer
- **Hero headline**: "AI & Automation for Growing Businesses"
- **Hero subtitle**: "We help business owners cut costs, save time, and grow revenue with AI, automation, and data-driven optimization."
- **Services cards** (3):
  1. AI Solutions — "Put AI to work in your business" — chatbots, content gen, AI workflows
  2. Process Automation — "Stop doing things the slow way" — automate reports, data entry, repetitive tasks
  3. Optimization & Analytics — "Make decisions with data, not gut feelings" — dashboards, forecasting, KPIs
- **Social proof metrics**: "$225K+ in delivered projects", "80% reduction in manual work", "Clients nationwide"
- **Nav links**: Home, Services (dropdown: AI Solutions, Automation, Optimization), Case Studies, Blog, About, Contact
- **CTA**: "Let's Talk" → contact.html
- **Footer**: Copyright 2026, social links (LinkedIn, GitHub), nav links
- **Style**: Modern, dark/light contrast, strong typography, distinctive (not generic SaaS). Mobile-first.
- **Font**: Keep Plus Jakarta Sans or use something equally modern
- **No Bootstrap** — custom CSS only
- **SEO requirements in `<head>`**:
  - `<title>Skotte Analytics — AI & Automation for Growing Businesses</title>`
  - `<meta name="description" content="AI and automation consulting for small and mid-market businesses. Cut costs, save time, and grow revenue with custom AI solutions, process automation, and data optimization.">`
  - Open Graph tags (og:title, og:description, og:url, og:type, og:site_name)
  - Twitter card tags
  - Canonical URL: `https://skotteanalytics.com/`
  - JSON-LD: Organization schema + LocalBusiness schema
  - Favicon link

**Step 2: Verify**

Open `index.html` in browser. Check:
- All sections render correctly
- Mobile responsive (resize browser)
- No broken links
- All meta tags present in page source

**Step 3: Commit**

```bash
git add index.html css/styles.css
git commit -m "feat: redesign homepage for business-owner audience"
```

---

## Phase 3: Service Landing Pages

### Task 6: Create AI Solutions landing page

**Files:**
- Create: `services/ai-solutions.html`

**Step 1: Build the page using same design system from Task 5**

Content:
- **H1**: "AI Solutions for Your Business"
- **Subtitle**: "Put AI to work — from customer-facing chatbots to internal workflow automation"
- **What we build**: Chatbots & virtual assistants, AI-powered content generation, document processing & extraction, predictive analytics & forecasting, Custom AI integrations with existing tools
- **How it works**: 3-step process (Discovery → Build → Deploy)
- **Case study callout**: Link to Predictive Sales Forecasting project
- **CTA**: "Ready to bring AI into your business?" → contact.html
- **Target keywords**: "AI consulting for small business", "AI solutions for businesses", "business AI integration"
- **SEO**: Full meta tags, OG tags, JSON-LD Service schema, canonical URL

**Step 2: Verify**

Open in browser, check rendering and SEO tags in source.

**Step 3: Commit**

```bash
git add services/ai-solutions.html
git commit -m "feat: add AI Solutions service landing page"
```

---

### Task 7: Create Process Automation landing page

**Files:**
- Create: `services/automation.html`

**Step 1: Build the page**

Content:
- **H1**: "Business Process Automation"
- **Subtitle**: "Stop wasting time on tasks a script could do in seconds"
- **What we automate**: Report generation & distribution, Data entry & form processing, File management & archiving, Email workflows & notifications, Cross-system data sync
- **Results**: "80% reduction in manual reporting time" (real client result)
- **How it works**: 3-step process (Audit → Automate → Monitor)
- **Case study callout**: Link to ETL & KPI Automation project
- **CTA**: "Let's find your automation opportunities" → contact.html
- **Target keywords**: "business process automation", "automate business processes", "small business automation"
- **SEO**: Full meta tags, OG tags, JSON-LD Service schema, canonical URL

**Step 2: Verify & commit**

```bash
git add services/automation.html
git commit -m "feat: add Process Automation service landing page"
```

---

### Task 8: Create Optimization & Analytics landing page

**Files:**
- Create: `services/optimization.html`

**Step 1: Build the page**

Content:
- **H1**: "Business Optimization & Analytics"
- **Subtitle**: "Make decisions with data, not gut feelings"
- **What we build**: Executive KPI dashboards, Sales forecasting models, Operational monitoring, Financial reporting & analysis, Self-service analytics for your team
- **Tools**: Power BI, Tableau, Python, SQL
- **How it works**: 3-step process (Measure → Analyze → Optimize)
- **Case study callout**: Link to National Sales Dashboards project
- **CTA**: "See what your data can tell you" → contact.html
- **Target keywords**: "business analytics consulting", "small business dashboard", "business optimization"
- **SEO**: Full meta tags, OG tags, JSON-LD Service schema, canonical URL

**Step 2: Verify & commit**

```bash
git add services/optimization.html
git commit -m "feat: add Optimization & Analytics service landing page"
```

---

## Phase 4: Core Pages Redesign

### Task 9: Redesign Case Studies page (projects.html)

**Files:**
- Rewrite: `projects.html`

**Step 1: Rebuild with new design system and reordered content**

Case study order (commercial-first):
1. **Featured**: ETL & KPI Automation — $100K, 80% reduction in manual reporting (strongest result)
2. Predictive Sales Forecasting — $100K, AI-powered (AI angle)
3. National Sales Dashboards — $25K (accessible entry point)
4. E-Commerce Analytics (relatable to SMBs)

Remove Federal Contracting Database entirely — it's government-focused.

Each case study card should have:
- Project name, client type (not name), year
- Challenge → Solution → Result format
- Tech tags
- Link to relevant service page (internal linking for SEO)

**SEO**:
- Title: "Case Studies — Skotte Analytics"
- Description: "See how we've helped businesses automate processes, build AI models, and create dashboards. Real results from real projects."
- Full OG/Twitter/canonical/JSON-LD

**Step 2: Verify & commit**

```bash
git add projects.html
git commit -m "feat: redesign case studies page with commercial-first ordering"
```

---

### Task 10: Create About page (replacing resume.html)

**Files:**
- Create: `about.html`
- Delete: `resume.html` (after about.html is done)

**Step 1: Build the page**

Content:
- **H1**: "About Skotte Analytics"
- **Your story**: Based in San Diego. Business degree from SDSU. Built career in data engineering and analytics. Now helping businesses leverage AI and automation.
- **Why work with us**: Direct communication, real results, no corporate overhead. You work directly with the person doing the work.
- **Skills/tech**: Python, SQL, Power BI, Tableau, AWS, AI/ML, ETL
- **Education**: SDSU (BS Business Admin), Miramar College (AS)
- **CTA**: "Let's talk about your business" → contact.html
- **Social links**: LinkedIn, GitHub

**SEO**:
- Title: "About — Skotte Analytics"
- Description: "AI and automation consultant based in San Diego. Helping small and mid-market businesses implement technology that saves time and grows revenue."

**Step 2: Verify & commit**

```bash
git add about.html && git rm resume.html
git commit -m "feat: add About page, remove resume page"
```

---

### Task 11: Redesign Contact page

**Files:**
- Rewrite: `contact.html`

**Step 1: Rebuild with new design**

Content:
- **H1**: "Let's Talk"
- **Subtitle**: "Tell us about your business challenge. We respond within 24 hours."
- **Contact info**: Email, phone
- **Social links**: LinkedIn, GitHub
- **Location**: San Diego, CA — available remote nationwide
- **Remove**: Federal contracting card, download resume button
- **Add**: Simple "what can we help with?" framing

**SEO**:
- Title: "Contact — Skotte Analytics"
- Description: "Get in touch with Skotte Analytics. AI, automation, and analytics consulting for growing businesses. Based in San Diego, available nationwide."

**Step 2: Verify & commit**

```bash
git add contact.html
git commit -m "feat: redesign contact page for business audience"
```

---

## Phase 5: Blog

### Task 12: Create blog index page

**Files:**
- Create: `blog/index.html`

**Step 1: Build the page**

- **H1**: "Blog"
- **Subtitle**: "Practical insights on AI, automation, and analytics for business owners"
- List of blog post cards with: title, date, excerpt (2-3 sentences), "Read more" link
- Same design system as rest of site
- Link to RSS feed in `<head>`: `<link rel="alternate" type="application/rss+xml" title="Skotte Analytics Blog" href="/feed.xml">`

**SEO**:
- Title: "Blog — Skotte Analytics"
- Description: "AI, automation, and analytics insights for small business owners. Practical advice on implementing technology to save time and grow revenue."

**Step 2: Verify & commit**

```bash
git add blog/index.html
git commit -m "feat: add blog index page"
```

---

### Task 13: Write blog post — "How Small Businesses Are Using AI in 2026"

**Files:**
- Create: `blog/how-small-businesses-are-using-ai-2026.html`

**Step 1: Write the post**

~800-1200 words. Sections:
1. Introduction — AI isn't just for big tech anymore
2. Customer Service — chatbots, automated responses
3. Content & Marketing — AI-generated copy, social posts, email
4. Operations — inventory forecasting, scheduling, document processing
5. Decision Making — AI-powered analytics, trend detection
6. Getting Started — start small, pick one pain point, measure results
7. CTA: "Need help implementing AI? That's what we do." → contact.html

**Target keywords**: "AI for small business", "small business AI 2026", "how businesses use AI"

Internal links to: `/services/ai-solutions.html`, `/projects.html`

Full SEO markup including `article` JSON-LD schema with author, datePublished, headline.

**Step 2: Verify & commit**

```bash
git add blog/how-small-businesses-are-using-ai-2026.html
git commit -m "feat(blog): add post — How Small Businesses Are Using AI in 2026"
```

---

### Task 14: Write blog post — "5 Business Processes You Should Automate Today"

**Files:**
- Create: `blog/5-business-processes-you-should-automate.html`

**Step 1: Write the post**

~800-1200 words. Sections:
1. Introduction — if you're doing it manually every week, it should be automated
2. Invoice & Payment Processing
3. Report Generation & Distribution
4. Data Entry & Spreadsheet Updates
5. Email Follow-ups & Notifications
6. Inventory & Order Tracking
7. How to Prioritize — pick the task that wastes the most time
8. CTA: "We've helped clients cut manual work by 80%." → contact.html

**Target keywords**: "automate business processes", "business automation ideas", "what to automate in business"

Internal links to: `/services/automation.html`, `/projects.html`

Full SEO markup including `article` JSON-LD schema.

**Step 2: Verify & commit**

```bash
git add blog/5-business-processes-you-should-automate.html
git commit -m "feat(blog): add post — 5 Business Processes You Should Automate Today"
```

---

### Task 15: Write blog post — "What Does an AI Consultant Actually Do?"

**Files:**
- Create: `blog/what-does-an-ai-consultant-do.html`

**Step 1: Write the post**

~800-1200 words. Sections:
1. Introduction — "AI consultant" sounds vague, here's what it actually means
2. Discovery — understanding your business, identifying opportunities
3. Solution Design — picking the right AI tools (not every problem needs AI)
4. Building — custom integrations, automation scripts, dashboards
5. Deployment & Training — getting it into your workflow, training your team
6. Ongoing Support — monitoring, tweaking, expanding
7. When to hire one — signs your business is ready
8. CTA: "Curious if AI could help your business? Let's find out." → contact.html

**Target keywords**: "AI consultant", "what does an AI consultant do", "hire AI consultant"

Internal links to: `/services/ai-solutions.html`, `/about.html`

Full SEO markup including `article` JSON-LD schema.

**Step 2: Verify & commit**

```bash
git add blog/what-does-an-ai-consultant-do.html
git commit -m "feat(blog): add post — What Does an AI Consultant Actually Do?"
```

---

## Phase 6: Cleanup & Final SEO

### Task 16: Remove old files and update sitemap

**Files:**
- Delete: `services.html` (replaced by 3 service landing pages)
- Delete: `resume.html` (replaced by about.html — if not already done in Task 10)
- Delete: `assets/capability-statement.html`
- Update: `sitemap.xml` (verify all final URLs are correct)
- Update: `feed.xml` (verify all blog posts are listed)

**Step 1: Remove old files**

```bash
git rm services.html
git rm assets/capability-statement.html
```

**Step 2: Verify sitemap and feed have correct URLs**

**Step 3: Commit**

```bash
git add -A
git commit -m "chore: remove old government-focused pages, finalize sitemap"
```

---

### Task 17: Optimize profile image

**Files:**
- Modify: `assets/profile.png` (4.5MB → target <200KB)

**Step 1: Compress the image**

Use ImageMagick or similar:
```bash
convert assets/profile.png -resize 800x800 -quality 85 assets/profile.png
```

Or convert to WebP for better compression:
```bash
convert assets/profile.png -resize 800x800 -quality 85 assets/profile.webp
```

Update all HTML references if changing format.

**Step 2: Commit**

```bash
git add assets/profile.*
git commit -m "perf: compress profile image from 4.5MB to <200KB"
```

---

### Task 18: Final verification pass

**Step 1: Open every page in browser and check:**
- All pages render correctly
- All nav links work
- All internal links work (service pages → case studies → blog posts)
- Mobile responsive (resize browser or use dev tools)
- No broken images

**Step 2: Check SEO on every page:**
- View page source, confirm: title, meta description, OG tags, canonical URL, JSON-LD
- Validate JSON-LD at https://validator.schema.org/ (optional)

**Step 3: Check robots.txt and sitemap.xml are accessible**

**Step 4: Final commit if any fixes needed**

```bash
git add -A
git commit -m "fix: final verification fixes"
```

---

## Task Summary

| # | Task | Phase | Files |
|---|------|-------|-------|
| 1 | robots.txt | SEO Infrastructure | Create: `robots.txt` |
| 2 | llms.txt | SEO Infrastructure | Create: `llms.txt` |
| 3 | sitemap.xml | SEO Infrastructure | Create: `sitemap.xml` |
| 4 | RSS feed | SEO Infrastructure | Create: `feed.xml` |
| 5 | Homepage redesign | Homepage | Rewrite: `index.html`, `css/styles.css` |
| 6 | AI Solutions page | Service Pages | Create: `services/ai-solutions.html` |
| 7 | Automation page | Service Pages | Create: `services/automation.html` |
| 8 | Optimization page | Service Pages | Create: `services/optimization.html` |
| 9 | Case Studies redesign | Core Pages | Rewrite: `projects.html` |
| 10 | About page | Core Pages | Create: `about.html`, Delete: `resume.html` |
| 11 | Contact redesign | Core Pages | Rewrite: `contact.html` |
| 12 | Blog index | Blog | Create: `blog/index.html` |
| 13 | Blog: AI in 2026 | Blog | Create: `blog/how-small-businesses-are-using-ai-2026.html` |
| 14 | Blog: 5 Processes | Blog | Create: `blog/5-business-processes-you-should-automate.html` |
| 15 | Blog: AI Consultant | Blog | Create: `blog/what-does-an-ai-consultant-do.html` |
| 16 | Remove old files | Cleanup | Delete: `services.html`, `assets/capability-statement.html` |
| 17 | Optimize images | Cleanup | Modify: `assets/profile.png` |
| 18 | Final verification | Cleanup | All files |
