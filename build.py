#!/usr/bin/env python3
"""HGSL corporate site generator.

Content lives in DIVISIONS / PAGES below; templates render it to static HTML.
Add a division to DIVISIONS and it appears in the nav, mega menu, homepage grid,
footer and sitemap automatically — that is the scalability requirement.
"""
import os, shutil, re

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "site")
SITE = "https://honeytreatglobal.com"
ADDR = "9A Bankole Street, Magodo Phase 1, Lagos, Nigeria"
MAIL = "contact@honeytreatglobal.com"
TEL = "+234 807 158 4064"

# --------------------------------------------------------------------------- #
# Divisions
# --------------------------------------------------------------------------- #
DIVISIONS = [
    dict(
        code="EQL", slug="equipment-leasing", name="Equipment Leasing",
        short="Heavy plant and industrial equipment on flexible terms, maintained to spec and backed by trained operators.",
        headline="Plant that turns up,<em>and keeps working.</em>",
        lead="Excavators, loaders, concrete pumps and support plant on daily, monthly and project-term contracts — with maintenance, logistics and operator cover included.",
        fa="#F0A400", fb="#7A4A00",
        overview=[
            "Downtime is the most expensive line item on any site. Our leasing model is built around eliminating it: every unit leaves the yard on a documented service schedule, and every contract includes a maintenance response commitment rather than a best-efforts promise.",
            "We hold a mixed fleet of earthmoving, material handling and concrete equipment sourced through authorised dealer channels, which keeps parts availability and warranty position intact. Clients range from single-site contractors to multi-year infrastructure programmes.",
        ],
        spec=[
            ("Contract terms", "Daily, weekly, monthly and project-term leases; dry or wet hire"),
            ("Fleet classes", "Excavators, wheel loaders, dozers, concrete pumps, tippers, compaction plant"),
            ("Maintenance", "Scheduled servicing, field response, consumables and parts management"),
            ("Coverage", "Lagos and South-West corridor, with mobilisation nationwide"),
            ("Operators", "Certified operators available on wet-hire contracts"),
        ],
        services=[
            ("Dry hire", "Equipment supplied to your site with condition report and handover documentation. You supply the operator; we hold the maintenance obligation."),
            ("Wet hire", "Equipment plus a certified operator, fuel management and daily production reporting against agreed targets."),
            ("Project-term leasing", "Fixed-fleet allocation for the life of a project, priced on duration rather than day rate, with agreed replacement units."),
            ("Maintenance and field service", "Preventive schedules, mobile field response and parts sourcing for leased and client-owned fleets."),
            ("Fleet advisory", "Utilisation analysis and own-versus-lease modelling for contractors sizing a fleet against a pipeline."),
            ("Logistics and mobilisation", "Low-bed haulage, permitting and site delivery, including phased mobilisation on staged programmes."),
        ],
        apps=["Civil infrastructure", "Building construction", "Mining and quarrying", "Ports and logistics", "Oil and gas support", "Land reclamation"],
        projects=[
            ("Fleet deployment, Lagos mainland corridor", "Multi-unit earthmoving allocation supporting a road rehabilitation programme, held on project-term lease with on-site field service."),
            ("Concrete pumping package, mixed-use development", "Boom and line pump supply with operator cover across a phased structural pour programme."),
        ],
        gallery=["Excavator fleet, yard inspection", "Concrete pump, pre-deployment check", "Earthmoving on active site", "Loader, aggregate handling", "Field service, scheduled maintenance", "Low-bed mobilisation"],
        faqs=[
            ("What is the minimum lease period?", "Daily hire is available for most classes, though pricing improves substantially at monthly and project-term durations. For programmes over six months we quote on a fixed-fleet basis."),
            ("Who carries the maintenance obligation?", "We do, on every contract type. Scheduled servicing, parts and field response sit with HGSL. Client obligations are limited to correct operation, daily checks and fuel unless otherwise agreed."),
            ("Do you provide operators?", "Yes. Wet-hire contracts include certified operators, and we can supply operators against client-owned plant where competence records are required."),
            ("How quickly can equipment be mobilised?", "Standard classes held in yard mobilise within 48 to 72 hours in the Lagos corridor, subject to haulage and permits. Specialist units are quoted with a lead time on enquiry."),
            ("Is equipment insured?", "Units carry cover appropriate to their class. Site-specific liability, third-party and project insurance requirements are agreed and documented at contract stage."),
        ],
        stats=[("Fleet classes in service", "12", ""), ("Maintenance response, hours", "24", ""), ("Utilisation rate", "87", "%")],
    ),
    dict(
        code="RED", slug="real-estate", name="Real Estate Development",
        short="Residential, commercial and industrial assets developed for long-term value, not fast turnover.",
        headline="Buildings that hold<em>their value.</em>",
        lead="Site acquisition through design, delivery and asset management — residential, commercial and industrial property developed against investment fundamentals.",
        fa="#A78BFA", fb="#3B1E6E",
        overview=[
            "We develop property we would be willing to hold. That single discipline drives every decision upstream: how we underwrite a site, how much we spend on structure and services versus finish, and which locations we decline.",
            "The division runs the full cycle — acquisition and title verification, feasibility and design management, construction delivery, then handover into asset management or sale. Industrial and logistics property is a growing share of the pipeline as manufacturing and distribution demand shifts.",
        ],
        spec=[
            ("Asset classes", "Residential, commercial office and retail, industrial and logistics"),
            ("Scope", "Acquisition, feasibility, design management, delivery, asset management"),
            ("Markets", "Lagos primary; selected South-West and Abuja corridor opportunities"),
            ("Delivery model", "Direct development and structured joint ventures with landowners"),
            ("Title", "Full verification and perfection before commitment"),
        ],
        services=[
            ("Site acquisition and title", "Sourcing, verification, perfection and assembly, with legal and survey diligence completed before capital commitment."),
            ("Feasibility and underwriting", "Highest-and-best-use analysis, cost planning and return modelling against realistic absorption assumptions."),
            ("Design management", "Coordination of architectural, structural and services design to a buildable, costed specification."),
            ("Construction delivery", "Programme, cost and quality control through to practical completion and statutory sign-off."),
            ("Asset and facility management", "Post-handover operation, maintenance planning and tenant management for held assets."),
            ("Joint venture structuring", "Landowner partnership models where land is contributed against development equity."),
        ],
        apps=["Residential estates", "Commercial office", "Retail and mixed-use", "Industrial and warehousing", "Logistics parks", "Staff housing"],
        projects=[
            ("Residential development, Magodo corridor", "Mid-rise residential scheme developed to hold, with services specification set for long-term operating cost rather than launch price."),
            ("Industrial facility, Lagos periphery", "Warehousing and yard development supporting distribution operations, delivered on a landowner joint venture structure."),
        ],
        gallery=["Completed residential frontage", "Structural works in progress", "Interior handover standard", "Industrial yard and dock", "Site survey and layout", "Mixed-use street elevation"],
        faqs=[
            ("Do you sell units or hold them?", "Both, depending on the asset. Residential schemes are typically brought to market; industrial and selected commercial assets are more often held and operated for yield."),
            ("Will you partner with landowners?", "Yes. Joint ventures where land is contributed against development equity are a core part of the pipeline. Terms depend on title status, location and scheme viability."),
            ("How is title handled?", "Verification and perfection are completed before we commit capital or announce a scheme. We do not develop on unresolved title."),
            ("Can you deliver on a site we already own?", "Yes — as a development manager or under a joint venture. We will run feasibility first and tell you plainly if the numbers do not support the scheme."),
        ],
        stats=[("Asset classes developed", "4", ""), ("Projects in delivery", "6", ""), ("Sq. metres in pipeline", "40", "k+")],
    ),
    dict(
        code="CNG", slug="cng", name="CNG Distribution",
        short="Compressed natural gas infrastructure, supply and vehicle conversion for industry and transport.",
        headline="Cleaner fuel,<em>lower running cost.</em>",
        lead="Refuelling infrastructure, industrial gas supply and vehicle conversion programmes that cut fuel spend while reducing emissions against diesel and petrol.",
        fa="#2DD4BF", fb="#0F4A46",
        overview=[
            "Nigeria's energy transition is being driven by economics as much as policy. Compressed natural gas is cheaper per kilometre than petrol and cleaner than diesel, and the constraint has never been demand — it has been infrastructure and conversion capacity.",
            "We work on both sides of that constraint: building and operating refuelling capacity, and running certified conversion programmes for commercial fleets. For industrial customers we supply gas directly against process and power requirements, structured on term contracts that make budgeting predictable.",
        ],
        spec=[
            ("Infrastructure", "Refuelling station development, compression and dispensing systems"),
            ("Supply", "Industrial process gas, power generation feedstock, transport fuel"),
            ("Conversion", "Certified petrol and diesel vehicle conversion, fleet programmes"),
            ("Contracting", "Term supply agreements with indexed pricing"),
            ("Compliance", "Full alignment with national gas policy and safety regulation"),
        ],
        services=[
            ("Refuelling infrastructure", "Station siting, development and operation, including compression, storage and dispensing, built for uptime under load."),
            ("Industrial gas supply", "Term-contracted supply for process heat, boilers and gas-fired generation, sized against measured demand profiles."),
            ("Fleet conversion", "Certified bi-fuel and dedicated conversions with post-conversion support, warranty position and driver briefing."),
            ("Transport fuel supply", "Dispensing agreements for commercial fleets, with usage reporting and account management."),
            ("Energy transition advisory", "Diesel-to-gas switching analysis: payback modelling, emissions reduction and phased conversion planning."),
            ("Safety and compliance", "Installation certification, periodic inspection and operator training to regulatory standard."),
        ],
        apps=["Commercial transport fleets", "Manufacturing process heat", "Gas-fired power generation", "Logistics and haulage", "Public transport", "Industrial estates"],
        projects=[
            ("Refuelling capacity, Lagos transport corridor", "Station development supporting commercial fleet conversion, with compression and dispensing sized for sustained peak demand."),
            ("Diesel-to-gas switch, manufacturing customer", "Process heat conversion with term supply agreement, delivered against a documented payback and emissions reduction case."),
        ],
        gallery=["Compression and dispensing plant", "Station forecourt in operation", "Conversion workshop", "Industrial supply installation", "Safety inspection in progress", "Fleet refuelling"],
        faqs=[
            ("How much does converting a vehicle save?", "Savings depend on mileage, engine and current fuel price, so we model each fleet rather than quote a headline figure. High-mileage commercial vehicles reach payback fastest, which is why fleet programmes come first."),
            ("Is a converted vehicle still able to run on petrol?", "Bi-fuel conversions retain the original fuel system and switch between the two. Dedicated conversions do not, and are only recommended where refuelling access is assured."),
            ("Does conversion affect the vehicle warranty?", "We use certified kits and certified installers, and we document the installation. Warranty position varies by manufacturer, and we set that out clearly before work starts."),
            ("Can you supply gas to a site with no station nearby?", "Yes. Industrial customers are served under term supply arrangements rather than forecourt dispensing, sized against your demand profile."),
            ("Is CNG safe?", "Handled to standard, yes — cylinders are rated well above operating pressure and gas disperses upward rather than pooling. Safety depends on certified installation and periodic inspection, both of which we hold to."),
        ],
        stats=[("Fuel cost reduction vs petrol", "40", "%+"), ("CO2 reduction vs diesel", "25", "%"), ("Conversion turnaround, days", "3", ""),],
    ),
    dict(
        code="MIN", slug="mining", name="Mining Operations",
        short="Licensed extraction and processing of industrial minerals and aggregates, with rehabilitation planned from day one.",
        headline="Extraction with<em>a closure plan.</em>",
        lead="Licensed mineral extraction and aggregate processing, run to documented environmental and safety standards with community development built into the site plan.",
        fa="#FB923C", fb="#5A2410",
        overview=[
            "Mining earns its licence twice: once from the regulator, and continuously from the community around the site. We plan both from the start — every site carries a rehabilitation and closure plan before the first cut, and community agreements are negotiated as commitments rather than gestures.",
            "Operationally the division focuses on industrial minerals and construction aggregates, where domestic demand is driven directly by infrastructure spending. Vertical integration with our leasing division gives us plant availability and maintenance capacity that independent operators typically buy at a premium.",
        ],
        spec=[
            ("Commodities", "Construction aggregates, granite, laterite, industrial minerals"),
            ("Scope", "Exploration support, extraction, crushing and screening, haulage"),
            ("Licensing", "Operations held under valid mineral titles and statutory permits"),
            ("Environment", "Impact assessment, progressive rehabilitation, closure planning"),
            ("Community", "Host community agreements, local employment, skills transfer"),
        ],
        services=[
            ("Quarrying and extraction", "Drill-and-blast and mechanical extraction planned against reserve models and production targets."),
            ("Crushing and screening", "Processing to graded aggregate specifications for construction and civil works customers."),
            ("Aggregate supply", "Term and spot supply to contractors, concrete producers and infrastructure programmes."),
            ("Haulage and logistics", "Site-to-customer haulage with load documentation and delivery scheduling."),
            ("Environmental management", "Baseline assessment, dust and water controls, progressive rehabilitation and closure execution."),
            ("Community development", "Host community engagement, local hiring, skills programmes and infrastructure contribution."),
        ],
        apps=["Road and highway construction", "Concrete production", "Building construction", "Rail infrastructure", "Drainage and civil works", "Land reclamation"],
        projects=[
            ("Aggregate production, South-West site", "Crushing and screening operation supplying graded aggregate to regional civil works, with progressive rehabilitation running alongside extraction."),
            ("Community development programme, host site", "Local employment, skills training and infrastructure contribution agreed with host community leadership and reported against annually."),
        ],
        gallery=["Working bench, active quarry", "Crushing and screening plant", "Graded aggregate stockpile", "Haulage loading", "Rehabilitated ground", "Site safety briefing"],
        faqs=[
            ("Are your operations properly licensed?", "Yes. Every site operates under valid mineral title and the statutory permits for its activity. We do not operate on unresolved or contested titles."),
            ("What happens to a site when extraction ends?", "It is rehabilitated to the closure plan filed before work began. Rehabilitation runs progressively during operation rather than being deferred to the end."),
            ("How do you work with host communities?", "Through negotiated agreements covering local employment, skills development and infrastructure contribution, reviewed and reported on a fixed cycle."),
            ("Can you supply aggregate on a term contract?", "Yes. Term supply with agreed grading, volumes and delivery scheduling is our preferred structure for infrastructure programmes."),
        ],
        stats=[("Aggregate grades produced", "6", ""), ("Local hiring at host sites", "70", "%"), ("Sites under rehabilitation plan", "100", "%")],
    ),
    dict(
        code="SDI", slug="technology", name="Software Development & Digital Innovation",
        short="A product engineering division building enterprise platforms for the group and commercial software for market.",
        headline="We ship products,<em>not slide decks.</em>",
        lead="A full engineering division building enterprise platforms for the group and commercial technology products for market — currently QwikCare in healthcare and SurDrive in mobility.",
        fa="#6C2BD9", fb="#1B0F3A",
        overview=[
            "Most industrial groups treat technology as procurement. We treat it as a business. The Software Development & Digital Innovation division carries its own P&L, its own product roadmap and its own market — it builds the systems that run HGSL, and it builds software that stands on its own commercially.",
            "That dual mandate is deliberate. Building platforms for our own equipment, property, energy and mining operations means our engineers work against real operational constraints rather than hypotheticals. The products that come out of that environment — QwikCare and SurDrive — are shaped by the same discipline.",
        ],
        spec=[
            ("Products in market", "QwikCare (healthcare), SurDrive (mobility)"),
            ("Internal platforms", "Enterprise resource planning, learning management, asset management"),
            ("Capabilities", "Product engineering, platform architecture, data, cloud, mobile"),
            ("Stack", "TypeScript, Node, React and Next.js, PostgreSQL, MongoDB, cloud-native"),
            ("Model", "In-house product development plus selected enterprise engagements"),
        ],
        services=[
            ("Product engineering", "End-to-end product development: discovery, architecture, build, launch and iteration against measured usage."),
            ("Enterprise platforms", "ERP, LMS and asset management systems built for multi-entity groups with real operational complexity."),
            ("Cloud and infrastructure", "Cloud-native architecture, deployment automation and cost-managed operations."),
            ("Data and analytics", "Operational reporting, data pipelines and decision dashboards across business units."),
            ("Digital transformation", "Process mapping and system consolidation for organisations replacing manual and fragmented workflows."),
            ("Integration and APIs", "Payments, identity, messaging and third-party system integration built to be maintained, not just delivered."),
        ],
        apps=["Healthcare delivery", "Mobility and transport", "Industrial operations", "Education and training", "Financial services", "Enterprise resource planning"],
        projects=[
            ("Group enterprise platform", "Multi-entity ERP and learning management platform spanning every HGSL and Honeytreat Group subsidiary, covering finance, operations, HR and training delivery."),
            ("Asset management portal", "Operational system tracking equipment, assignment, maintenance history and utilisation across the leasing fleet."),
        ],
        gallery=["Product interface, QwikCare", "Product interface, SurDrive", "Engineering workspace", "Architecture review", "Platform dashboard", "Mobile build"],
        faqs=[
            ("Is this division only for internal work?", "No. It builds internal platforms and commercial products, and takes selected external engagements where the problem fits our engineering strengths."),
            ("Where can I see the products?", "QwikCare is live at qwikcare.org and SurDrive at surdrive.org. Both are operating products rather than concepts."),
            ("What technology do you build on?", "Primarily TypeScript across the stack — Node on the server, React and Next.js on the front end — with PostgreSQL and MongoDB, deployed cloud-native."),
            ("Do you take on external software projects?", "Selectively. We take work where the domain overlaps our operating experience: industrial operations, healthcare, mobility and enterprise platforms."),
        ],
        stats=[("Products in market", "2", ""), ("Platform modules shipped", "23", ""), ("Uptime target", "99.9", "%")],
    ),
]

DMAP = {d["slug"]: d for d in DIVISIONS}

PRODUCTS = [
    dict(name="QwikCare", url="https://qwikcare.org", tag="Healthcare technology", code="P-01",
         fa="#2DD4BF", fb="#0F4A46",
         desc="A healthcare platform that connects patients with providers and gives clinics the record, appointment and care-coordination tooling they were previously running on paper.",
         features=["Patient records and clinical history in one place",
                   "Appointment booking and provider scheduling",
                   "Care coordination across facilities",
                   "Built for low-bandwidth and mobile-first access"]),
    dict(name="SurDrive", url="https://surdrive.org", tag="Mobility and transportation", code="P-02",
         fa="#F0A400", fb="#7A4A00",
         desc="A mobility platform covering the operational layer of transport businesses — fleet, drivers, trips and the accounting that ties them together.",
         features=["Fleet and vehicle lifecycle management",
                   "Driver onboarding, verification and performance",
                   "Trip management and dispatch",
                   "Revenue reconciliation and operator reporting"]),
]

STATS_HOME = [
    ("5", "", "Operating divisions"),
    ("2", "", "Products live in market"),
    ("12", "+", "Equipment classes in fleet"),
    ("40", "%+", "Fuel saving, CNG vs petrol"),
]

ESG = [
    ("Cleaner energy adoption", 72, "Displacing diesel and petrol with compressed natural gas across transport and industrial customers."),
    ("Responsible extraction", 85, "Every mining site operating under a filed rehabilitation and closure plan, with progressive restoration during production."),
    ("Local employment and skills", 70, "Majority local hiring at host sites, with structured skills transfer through the Honeytreat Trade Academy."),
    ("Governance and compliance", 90, "Documented board oversight, statutory compliance and transparent reporting across every operating entity."),
]

LEADERS = [
    ("Samson Soyebi", "Group Managing Director", "SS", "Sets group strategy and capital allocation across all five operating divisions, with direct oversight of investment decisions and governance."),
    ("Group Operations", "Chief Operating Officer", "OP", "Accountable for delivery across equipment leasing, real estate, CNG and mining — programme performance, safety and utilisation."),
    ("Digital Operations", "Head, Digital Operations", "DO", "Leads platform development, developer management and digital operations across the group's entities and product portfolio."),
    ("Finance and Risk", "Group Finance Director", "FR", "Financial control, treasury, tax compliance and enterprise risk management across the group structure."),
]

INSIGHTS = [
    ("Why CNG conversion economics finally work for Nigerian fleets", "Energy", "The gap between petrol and gas pricing has moved from marginal to decisive. Here is how the payback maths actually runs on a high-mileage commercial fleet.", "cng"),
    ("Own or lease: sizing a plant fleet against a real pipeline", "Equipment", "Contractors consistently over-buy on plant and under-invest in maintenance. A utilisation-first framework for deciding which units belong on your balance sheet.", "equipment-leasing"),
    ("Building enterprise software inside an industrial group", "Technology", "What changes when your engineering team's first customer is your own equipment yard — and why that produces better commercial products.", "technology"),
]

PROJECTS_ALL = []
for d in DIVISIONS:
    for t, p in d["projects"]:
        PROJECTS_ALL.append(dict(title=t, desc=p, div=d["slug"], code=d["code"], name=d["name"], fa=d["fa"], fb=d["fb"]))

NAV_MAIN = [("About", "about.html"), ("Projects", "projects.html"),
            ("Sustainability", "sustainability.html"), ("Insights", "insights.html"),
            ("Careers", "careers.html")]

# --------------------------------------------------------------------------- #
# Fragments
# --------------------------------------------------------------------------- #
def field(fa, fb, scrim="", img=None, cls=""):
    im = f'<div class="field__img" style="--img:url(\'assets/img/{img}\')"></div>' if img else ""
    sc = f'<div class="field__scrim{scrim}"></div>' if scrim is not None else ""
    return (f'<div class="field {cls}" style="--fa:{fa};--fb:{fb}" aria-hidden="true">'
            f'{im}{sc}</div>')


LOGO = """<svg class="brand__mark" viewBox="0 0 40 40" role="img" aria-label="Honeytreat Global Services">
<rect width="40" height="40" rx="7" fill="#6C2BD9"/>
<path d="M20 7l11 6.5v13L20 33 9 26.5v-13L20 7z" fill="none" stroke="#F0A400" stroke-width="1.6"/>
<path d="M15 15v10M25 15v10M15 20h10" stroke="#fff" stroke-width="2.4" stroke-linecap="square"/>
</svg>"""

ICONS = {
 "arrow": '<svg class="btn__ar" width="15" height="15" viewBox="0 0 16 16" fill="none" aria-hidden="true"><path d="M3 8h10M9 4l4 4-4 4" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>',
 "chev": '<svg width="11" height="11" viewBox="0 0 12 12" fill="none" aria-hidden="true"><path d="M2.5 4.5L6 8l3.5-3.5" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>',
 "gear": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"><circle cx="12" cy="12" r="3"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3M5 5l2 2M17 17l2 2M19 5l-2 2M7 17l-2 2"/></svg>',
 "build": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"><path d="M4 21V8l7-4 7 4v13M9 21v-6h6v6M9 11h.01M14 11h.01"/></svg>',
 "flame": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"><path d="M12 3s5 4.5 5 9a5 5 0 01-10 0c0-2 1-3.5 2-4.5"/><path d="M12 21a3 3 0 003-3c0-1.6-1.5-3-3-4.5-1.5 1.5-3 2.9-3 4.5a3 3 0 003 3z"/></svg>',
 "pick": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"><path d="M14 4l6 6M4 20l9-9M11 6l7 7M9 4l3 3"/></svg>',
 "code": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"><path d="M8 6l-5 6 5 6M16 6l5 6-5 6M13 4l-2 16"/></svg>',
 "leaf": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"><path d="M20 4C10 4 4 9 4 17v3M4 20c8 0 16-5 16-16"/></svg>',
 "shield": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"><path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6l8-3z"/><path d="M9 12l2 2 4-4"/></svg>',
 "chart": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"><path d="M4 20V4M4 20h16M8 16v-5M13 16V8M18 16v-3"/></svg>',
 "users": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"><circle cx="9" cy="8" r="3"/><path d="M3 20c0-3.3 2.7-5 6-5s6 1.7 6 5M16 6a3 3 0 010 6M18 20c0-2.5-1-4-2.5-4.6"/></svg>',
 "close": '<svg width="15" height="15" viewBox="0 0 16 16" fill="none" aria-hidden="true"><path d="M4 4l8 8M12 4l-8 8" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>',
 "send": '<svg width="17" height="17" viewBox="0 0 20 20" fill="none" aria-hidden="true"><path d="M3 10h13M11 5l5 5-5 5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>',
 "chat": '<svg width="17" height="17" viewBox="0 0 20 20" fill="none" aria-hidden="true"><path d="M4 4h12v9H8l-4 3V4z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>',
}
DIV_ICON = {"EQL": "gear", "RED": "build", "CNG": "flame", "MIN": "pick", "SDI": "code"}
A = ICONS["arrow"]


def head(title, desc, canon, extra=""):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{SITE}/{canon}">
<meta name="theme-color" content="#14101C">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Honeytreat Global Services Limited">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{SITE}/{canon}">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,400..800&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/hgsl.css">
{extra}</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<div class="progress" aria-hidden="true"></div>
"""


def nav(active=""):
    mega_items = "".join(
        f'<a class="mega__i" href="{d["slug"]}.html"><i>{d["code"]}</i><b>{d["name"]}</b>'
        f'<span>{d["short"]}</span></a>' for d in DIVISIONS)
    links = "".join(
        f'<a class="nav__l{" is-here" if active==h else ""}" href="{h}">{t}</a>'
        for t, h in NAV_MAIN)
    drawer_divs = "".join(
        f'<a class="drawer__l" href="{d["slug"]}.html">{d["name"]}<i>{d["code"]}</i></a>'
        for d in DIVISIONS)
    drawer_main = "".join(f'<a class="drawer__l" href="{h}">{t}</a>' for t, h in
                          NAV_MAIN + [("Technology & Innovation", "technology.html"),
                                      ("Leadership", "leadership.html"),
                                      ("Corporate Governance", "governance.html"),
                                      ("Investor Information", "investors.html"),
                                      ("Contact", "contact.html")])
    return f"""<header class="nav" id="nav">
  <div class="wrap nav__in">
    <a class="brand" href="index.html" aria-label="Honeytreat Global Services, home">
      {LOGO}
      <span class="brand__txt"><b>HONEYTREAT</b><span>Global Services Ltd</span></span>
    </a>
    <nav class="nav__links" aria-label="Main">
      <button class="nav__l" data-mega aria-expanded="false" aria-controls="mega">Divisions {ICONS['chev']}</button>
      <a class="nav__l{" is-here" if active=="technology.html" else ""}" href="technology.html">Technology</a>
      {links}
      <a class="btn btn--p nav__cta" href="contact.html">Talk to us {A}</a>
    </nav>
    <button class="burger" aria-expanded="false" aria-controls="drawer" aria-label="Menu">
      <span></span><span></span><span></span>
    </button>
  </div>
  <div class="mega" id="mega">
    <div class="wrap mega__in">
      <div>
        <p class="plate">Five operating divisions</p>
        <div class="mega__grid mt-m">{mega_items}</div>
      </div>
      <div class="mega__side">
        <p class="plate">Technology ecosystem</p>
        <h3 class="h3" style="color:#fff">QwikCare and SurDrive</h3>
        <p>Two products built and operated in-house by our software division.</p>
        <a class="tlink" href="technology.html">See the ecosystem {A}</a>
      </div>
    </div>
  </div>
  <div class="drawer" id="drawer">
    <p class="plate">Divisions</p>
    <div class="drawer__g mt-m">{drawer_divs}</div>
    <p class="plate drawer__h">Company</p>
    <div class="drawer__g mt-m">{drawer_main}</div>
    <a class="btn btn--p" href="contact.html" style="margin-top:1.75rem">Talk to us {A}</a>
  </div>
</header>
"""


def stat_block(items, cls=""):
    out = []
    for n, suf, label in items:
        dec = 1 if "." in n else 0
        out.append(f'<div class="stat rv"><div class="stat__n">'
                   f'<span data-count="{n}" data-dec="{dec}">0</span><i>{suf}</i></div>'
                   f'<p class="stat__l">{label}</p></div>')
    return f'<div class="stats {cls}">{"".join(out)}</div>'


def cta(title, body, primary=("Talk to us", "contact.html"), second=("See our divisions", "divisions.html")):
    return f"""<section class="cta">
  {field("#6C2BD9", "#1B0F3A")}
  <div class="wrap cta__in">
    <div class="rv"><p class="plate">Next step</p><h2 class="h2 mt-s">{title}</h2><p>{body}</p></div>
    <div class="btn-row rv rv-d1">
      <a class="btn btn--honey" href="{primary[1]}">{primary[0]} {A}</a>
      <a class="btn btn--g" href="{second[1]}">{second[0]}</a>
    </div>
  </div>
</section>
"""


def footer():
    dl = "".join(f'<a href="{d["slug"]}.html">{d["name"]}</a>' for d in DIVISIONS)
    return f"""<footer class="foot">
  <div class="wrap">
    <div class="foot__top">
      <div>
        <a class="brand" href="index.html" style="margin:0 0 1.25rem">
          {LOGO}<span class="brand__txt"><b style="color:#fff">HONEYTREAT</b><span>Global Services Ltd</span></span>
        </a>
        <p class="foot__addr">A diversified industrial and technology group building infrastructure, enabling industrial growth and shipping software across Nigeria and Africa.</p>
        <p class="foot__addr" style="margin-top:1.25rem">{ADDR}<br>
          <a href="mailto:{MAIL}">{MAIL}</a><br><a href="tel:{TEL.replace(' ','')}">{TEL}</a></p>
      </div>
      <div><h4>Divisions</h4><div class="foot__l">{dl}</div></div>
      <div><h4>Company</h4><div class="foot__l">
        <a href="about.html">About us</a><a href="leadership.html">Leadership</a>
        <a href="governance.html">Corporate governance</a><a href="projects.html">Projects</a>
        <a href="careers.html">Careers</a><a href="insights.html">Insights &amp; news</a></div></div>
      <div><h4>More</h4><div class="foot__l">
        <a href="technology.html">Technology &amp; innovation</a><a href="sustainability.html">Sustainability (ESG)</a>
        <a href="investors.html">Investor information</a><a href="contact.html">Contact</a>
        <a href="https://qwikcare.org" target="_blank" rel="noopener">QwikCare &#8599;</a>
        <a href="https://surdrive.org" target="_blank" rel="noopener">SurDrive &#8599;</a></div></div>
    </div>
    <div class="foot__b">
      <p>&copy; <span data-year>2026</span> Honeytreat Global Services Limited. All rights reserved.</p>
      <nav aria-label="Legal"><a href="#">Privacy</a><a href="#">Terms</a><a href="#">Accessibility</a></nav>
      <div class="soc">
        <a href="#" aria-label="Facebook"><svg width="15" height="15" viewBox="0 0 16 16" fill="currentColor"><path d="M9.5 14V8.6h1.9l.3-2.2H9.5V5c0-.6.2-1.1 1.1-1.1h1.2V1.9c-.2 0-1-.1-1.8-.1-1.9 0-3.1 1.1-3.1 3.2v1.4H4.9v2.2H7V14h2.5z"/></svg></a>
        <a href="#" aria-label="Instagram"><svg width="15" height="15" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.4"><rect x="2.5" y="2.5" width="11" height="11" rx="3.2"/><circle cx="8" cy="8" r="2.6"/><circle cx="11.4" cy="4.6" r=".7" fill="currentColor" stroke="none"/></svg></a>
        <a href="#" aria-label="LinkedIn"><svg width="15" height="15" viewBox="0 0 16 16" fill="currentColor"><path d="M3.6 5.5H1.9V14h1.7V5.5zM2.7 2a1.1 1.1 0 100 2.2 1.1 1.1 0 000-2.2zM14 9.6c0-2.2-1.2-3.3-2.8-3.3-1.1 0-1.7.6-2 1v-.8H7.5V14h1.7V9.7c0-.9.3-1.7 1.3-1.7s1.2.8 1.2 1.8V14H14V9.6z"/></svg></a>
      </div>
    </div>
  </div>
</footer>
"""


def chat():
    chips = ["What are your divisions?", "Tell me about QwikCare", "CNG for my fleet", "Careers"]
    cb = "".join(f"<button type=\"button\">{c}</button>" for c in chips)
    return f"""<button class="chat-open" aria-label="Open the HGSL assistant">
  <span class="chat-open__d" aria-hidden="true"></span>{ICONS['chat']} Ask HGSL
</button>
<div class="chat" role="dialog" aria-label="HGSL assistant" aria-hidden="true">
  <div class="chat__h">
    <div><b>HGSL Assistant</b><span>Online</span></div>
    <button class="chat__x" aria-label="Close assistant">{ICONS['close']}</button>
  </div>
  <div class="chat__log" aria-live="polite"></div>
  <div class="chips">{cb}</div>
  <form class="chat__f"><label class="sr" for="chat-in">Your message</label>
    <input id="chat-in" type="text" placeholder="Ask about a division, product or project" autocomplete="off">
    <button type="submit" aria-label="Send">{ICONS['send']}</button></form>
</div>
"""


def tail():
    return """<script src="assets/js/hgsl.js"></script>
<script src="assets/js/assistant.js"></script>
</body>
</html>
"""


def shero(d_code, crumbs, eyebrow, title, lead, fa, fb, stats=None):
    cr = "".join(f'<span><a href="{h}">{t}</a></span>' if h else f"<span>{t}</span>" for t, h in crumbs)
    st = ""
    if stats:
        cells = "".join(f'<div><b><span data-count="{n}" data-dec="{1 if "." in n else 0}">0</span>{s}</b>{l}</div>'
                        for n, s, l in stats)
        st = f'<div class="hero__meta rv rv-d2">{cells}</div>'
    return f"""<section class="shero">
  {field(fa, fb, scrim="")}
  <div class="wrap shero__in">
    <p class="crumb">{cr}</p>
    <p class="plate rv">{eyebrow}</p>
    <h1 class="h1 rv rv-d1">{title}</h1>
    <p class="shero__lead rv rv-d1">{lead}</p>
    {st}
  </div>
  <span class="shero__code" aria-hidden="true">{d_code}</span>
</section>
"""


def acc(items, ident="faq"):
    rows = "".join(
        f'<div class="acc__i"><button class="acc__b" aria-expanded="false" aria-controls="{ident}-{i}">'
        f'<span>{q}</span><span class="acc__ic" aria-hidden="true"></span></button>'
        f'<div class="acc__p" id="{ident}-{i}"><div>{a}</div></div></div>'
        for i, (q, a) in enumerate(items))
    return f'<div class="acc">{rows}</div>'


def gallery(caps, code, fa, fb):
    tiles = "".join(
        f'<figure class="tile rv rv-d{i%4}" style="margin:0">{field(fa, fb, scrim=None)}'
        f'<figcaption class="tile__cap"><b>{c}</b><span>{code}-{i+1:02d}</span></figcaption></figure>'
        for i, c in enumerate(caps))
    return f'<div class="cgrid cgrid--3">{tiles}</div>'


# --------------------------------------------------------------------------- #
# Homepage
# --------------------------------------------------------------------------- #
def page_home():
    fields = "".join(
        f'<div class="hero__f{" on" if i==0 else ""}">{field(d["fa"], d["fb"], scrim="")}</div>'
        for i, d in enumerate(DIVISIONS))
    rail = "".join(
        f'<button class="rail__b" type="button" aria-pressed="false" '
        f'data-title="{d["headline"]}" data-lead="{d["lead"]}">'
        f'<i>{d["code"]}</i><b>{d["name"]}</b></button>' for d in DIVISIONS)

    dcards = ""
    for d in DIVISIONS:
        tags = "".join(f"<span>{s[0]}</span>" for s in d["services"][:3])
        dcards += f"""<a class="dcard rv" href="{d['slug']}.html">
      {field(d['fa'], d['fb'], scrim=" field__scrim--v")}
      <span class="dcard__code">{d['code']}</span>
      <div class="dcard__c">
        <h3 class="dcard__h">{d['name']}</h3>
        <p class="dcard__p">{d['short']}</p>
        <div class="dcard__l">{tags}</div>
        <span class="dcard__go">Explore division {A}</span>
      </div></a>"""

    pcards = ""
    for p in PRODUCTS:
        feats = "".join(f"<li>{f}</li>" for f in p["features"])
        pcards += f"""<article class="pcard rv">
      <div class="pcard__art">{field(p['fa'], p['fb'], scrim=None)}
        <div class="device"><div class="device__body"><div class="device__bar"><span></span></div>
          <div class="device__shot"><div class="dsk"><span></span><span></span><span></span><span></span></div></div>
        </div></div>
      </div>
      <div class="pcard__body">
        <p class="plate pcard__tag">{p['code']} &middot; {p['tag']}</p>
        <h3 class="h3">{p['name']}</h3>
        <p class="pcard__p">{p['desc']}</p>
        <ul class="pcard__f">{feats}</ul>
        <p class="mt-m"><a class="tlink" href="{p['url']}" target="_blank" rel="noopener">Visit {p['name'].lower()}.org {A}</a></p>
      </div></article>"""

    filters = '<button data-filter="all" aria-pressed="true">All divisions</button>' + "".join(
        f'<button data-filter="{d["slug"]}" aria-pressed="false">{d["name"]}</button>' for d in DIVISIONS)
    pj = "".join(
        f'<a class="pj__i rv" href="{p["div"]}.html" data-div="{p["div"]}">'
        f'{field(p["fa"], p["fb"], scrim=" field__scrim--v")}'
        f'<div class="pj__c"><p class="plate">{p["code"]} &middot; {p["name"]}</p>'
        f'<h3>{p["title"]}</h3><p>{p["desc"]}</p></div></a>' for p in PROJECTS_ALL)

    bars = "".join(
        f'<div class="rv"><div class="bar__top"><b>{t}</b><span>{v}%</span></div>'
        f'<div class="bar__t"><div class="bar__f" data-pct="{v}"></div></div>'
        f'<p class="mt-s" style="font-size:.875rem;color:rgba(247,245,249,.66);max-width:64ch">{c}</p></div>'
        for t, v, c in ESG)

    posts = "".join(
        f'<a class="post rv" href="insights.html"><div class="post__art">'
        f'{field(DMAP[s]["fa"], DMAP[s]["fb"], scrim=None)}</div>'
        f'<div class="post__m"><span>{cat}</span><time datetime="2026-07">July 2026</time></div>'
        f'<h3>{t}</h3><p>{d}</p></a>' for t, cat, d, s in INSIGHTS)

    ticker_items = ["Equipment leasing", "Real estate development", "CNG distribution",
                    "Mining operations", "Software development", "Lagos, Nigeria",
                    "QwikCare", "SurDrive", "Enterprise platforms", "Energy transition",
                    "Aggregate supply", "Industrial infrastructure"]
    tick = "".join(f'<span class="ticker__i">{t}</span>' for t in ticker_items * 2)

    partners = "".join(
        f'<div class="plock"><b>{b}</b><span>{s}</span></div>' for b, s in [
            ("Honeytreat Group", "Parent group"),
            ("Mantrac CAT", "Equipment partner"),
            ("Honeytreat Trade Academy", "Skills and training"),
            ("HTL Construction", "Sister company"),
        ])

    ld = f"""<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"Organization","name":"Honeytreat Global Services Limited",
"alternateName":"HGSL","url":"{SITE}","email":"{MAIL}","telephone":"{TEL}",
"address":{{"@type":"PostalAddress","streetAddress":"9A Bankole Street, Magodo Phase 1","addressLocality":"Lagos","addressCountry":"NG"}},
"description":"Diversified Nigerian industrial and technology group operating in equipment leasing, real estate development, CNG distribution, mining and software development.",
"knowsAbout":["Equipment leasing","Real estate development","Compressed natural gas","Mining","Software development"]}}
</script>"""

    return (head("Honeytreat Global Services Limited — Industrial and technology group, Nigeria",
                 "HGSL is a diversified Nigerian industrial and technology group operating across equipment leasing, real estate development, CNG distribution, mining and software development.",
                 "index.html", ld) + nav("index.html") + f"""
<main id="main">
<section class="hero" aria-label="Introduction">
  <div class="hero__fields">{fields}</div>
  <div class="hero__in">
    <div class="hero__body">
      <p class="plate rv">Honeytreat Global Services &middot; Lagos, Nigeria</p>
      <h1 class="hero__t rv rv-d1 mt-s" data-hero-title>Plant that turns up,<em>and keeps working.</em></h1>
    </div>
    <p class="hero__lead rv rv-d2" data-hero-lead>Excavators, loaders, concrete pumps and support plant on flexible contracts.</p>
    <div class="btn-row hero__cta rv rv-d3">
      <a class="btn btn--honey" href="divisions.html">Explore our divisions {A}</a>
      <a class="btn btn--g" href="technology.html">Technology ecosystem</a>
    </div>
    <div class="rail" aria-label="Choose a division to preview">
      <div class="rail__g">{rail}</div>
    </div>
  </div>
</section>

<div class="ticker" aria-hidden="true"><div class="ticker__t">{tick}</div></div>

<section class="sec" id="divisions">
  <div class="wrap">
    <div class="sec-head sec-head--split">
      <div class="rv"><p class="plate">One group, five divisions</p>
        <h2 class="h2 mt-s">We build the infrastructure other companies depend on — and the software that runs it.</h2></div>
      <p class="lead rv rv-d1">Each division stands on its own commercially, with its own leadership, P&amp;L and market. Together they cover the physical and digital infrastructure of industrial growth.</p>
    </div>
    <div class="dgrid">{dcards}</div>
  </div>
</section>

<section class="ink sec--tight">
  <div class="wrap">
    <p class="plate rv">By the numbers</p>
  </div>
  <div class="wrap mt-m">{stat_block(STATS_HOME)}</div>
</section>

<section class="ink sec" id="technology">
  <div class="wrap">
    <div class="sec-head sec-head--split">
      <div class="rv"><p class="plate">SDI &middot; Technology ecosystem</p>
        <h2 class="h2 mt-s" style="color:#fff">Our software division ships products, not proposals.</h2></div>
      <p class="lead rv rv-d1">Two commercial products are live in market, built and operated in-house. Both came out of the same engineering group that runs our internal enterprise platforms.</p>
    </div>
    <div class="pgrid">{pcards}</div>
    <p class="mt-l rv"><a class="tlink" href="technology.html">See the full technology division {A}</a></p>
  </div>
</section>

<section class="sec tint" id="projects">
  <div class="wrap">
    <div class="sec-head rv"><p class="plate">Selected work</p>
      <h2 class="h2 mt-s">Projects across every division.</h2></div>
    <div class="filters rv rv-d1">{filters}</div>
    <div class="pj">{pj}</div>
    <p class="mt-l rv"><a class="tlink" href="projects.html">All projects {A}</a></p>
  </div>
</section>

<section class="ink sec" id="sustainability">
  <div class="wrap">
    <div class="sec-head sec-head--split">
      <div class="rv"><p class="plate">Sustainability &middot; ESG</p>
        <h2 class="h2 mt-s" style="color:#fff">Commitments we report against, not slogans.</h2></div>
      <p class="lead rv rv-d1">Four tracks, each with a measurable target and an owner inside the business. Progress is reviewed at board level and published annually.</p>
    </div>
    <div class="bars">{bars}</div>
    <p class="mt-l rv"><a class="tlink" href="sustainability.html">Read the ESG approach {A}</a></p>
  </div>
</section>

<section class="sec--tight">
  <div class="wrap">
    <p class="plate center rv" style="justify-content:center">Partners and group companies</p>
    <div class="plocks rv rv-d1">{partners}</div>
  </div>
</section>

<section class="sec tint">
  <div class="wrap">
    <div class="sec-head sec-head--split">
      <div class="rv"><p class="plate">Insights &amp; news</p><h2 class="h2 mt-s">Thinking from the operating side.</h2></div>
      <p class="lead rv rv-d1">Analysis from the people running the fleets, sites, stations and codebases.</p>
    </div>
    <div class="posts">{posts}</div>
  </div>
</section>

{cta("Tell us what you are building.",
     "Equipment for a site, gas for a fleet, a development to underwrite, or software to ship — the enquiry goes straight to the division that owns it.")}
</main>
{footer()}{chat()}{tail()}""")


# --------------------------------------------------------------------------- #
# Divisions index
# --------------------------------------------------------------------------- #
def page_divisions():
    cards = ""
    for d in DIVISIONS:
        checks = "".join(f"<li>{s[0]}</li>" for s in d["services"][:4])
        cards += f"""<section class="sec--tight" style="border-bottom:1px solid var(--line)">
  <div class="wrap split{' split--art-first' if DIVISIONS.index(d)%2 else ''}">
    <div class="rv">
      <p class="plate">{d['code']} &middot; Division</p>
      <h2 class="h2 mt-s">{d['name']}</h2>
      <p class="lead mt-m">{d['lead']}</p>
      <ul class="checks">{checks}</ul>
      <p class="mt-l"><a class="btn btn--p" href="{d['slug']}.html">Open {d['code']} division {A}</a></p>
    </div>
    <div class="split__art rv rv-d1">{field(d['fa'], d['fb'], scrim=" field__scrim--v")}
      <span class="dcard__code" style="top:auto;bottom:1rem;left:1.4rem;right:auto">{d['code']}</span></div>
  </div>
</section>"""
    return (head("Business divisions — Honeytreat Global Services Limited",
                 "The five operating divisions of HGSL: equipment leasing, real estate development, CNG distribution, mining operations, and software development.",
                 "divisions.html") + nav() + f"""<main id="main">
{shero("HGSL", [("Home", "index.html"), ("Divisions", None)], "Group structure",
       "Five divisions. One operating standard.",
       "Each division runs its own market, leadership and P&amp;L — held to a common standard of documentation, safety and delivery discipline.",
       "#6C2BD9", "#1B0F3A")}
{cards}
{cta("Not sure which division you need?", "Describe the problem and we will route it. Most enquiries touch more than one division anyway.")}
</main>{footer()}{chat()}{tail()}""")


# --------------------------------------------------------------------------- #
# Division detail page
# --------------------------------------------------------------------------- #
def page_division(d):
    ic = ICONS[DIV_ICON[d["code"]]]
    svc = "".join(
        f'<article class="card rv rv-d{i%4}"><div class="card__ic">{ic}</div>'
        f'<h3>{t}</h3><p>{p}</p></article>' for i, (t, p) in enumerate(d["services"]))
    spec = "".join(f'<div class="spec__r"><div class="spec__k">{k}</div><div class="spec__v">{v}</div></div>'
                   for k, v in d["spec"])
    apps = "".join(f'<div class="card rv rv-d{i%4}" style="min-height:0"><h3>{a}</h3></div>'
                   for i, a in enumerate(d["apps"]))
    projs = "".join(
        f'<article class="pj__i rv rv-d{i}" style="min-height:340px">'
        f'{field(d["fa"], d["fb"], scrim=" field__scrim--v")}'
        f'<div class="pj__c"><p class="plate">{d["code"]}-{i+1:02d}</p><h3>{t}</h3><p>{p}</p></div></article>'
        for i, (t, p) in enumerate(d["projects"]))
    others = "".join(
        f'<a class="card rv rv-d{i%4}" href="{o["slug"]}.html"><p class="plate">{o["code"]}</p>'
        f'<h3>{o["name"]}</h3><p>{o["short"]}</p></a>'
        for i, o in enumerate([x for x in DIVISIONS if x["slug"] != d["slug"]]))

    ov = "".join(f'<p class="body-copy">{p}</p>' for p in d["overview"])
    subnav = "".join(f'<a href="#{s}">{t}</a>' for t, s in
                     [("Overview", "overview"), ("Services", "services"), ("Applications", "applications"),
                      ("Projects", "projects"), ("Gallery", "gallery"), ("Questions", "faq")])

    extra = ""
    if d["code"] == "SDI":
        pc = ""
        for p in PRODUCTS:
            feats = "".join(f"<li>{f}</li>" for f in p["features"])
            pc += f"""<article class="pcard rv">
        <div class="pcard__art">{field(p['fa'], p['fb'], scrim=None)}
          <div class="device"><div class="device__body"><div class="device__bar"><span></span></div>
          <div class="device__shot"><div class="dsk"><span></span><span></span><span></span><span></span></div></div>
          </div></div></div>
        <div class="pcard__body"><p class="plate pcard__tag">{p['code']} &middot; {p['tag']}</p>
          <h3 class="h3">{p['name']}</h3><p class="pcard__p">{p['desc']}</p>
          <ul class="pcard__f">{feats}</ul>
          <p class="mt-m"><a class="tlink" href="{p['url']}" target="_blank" rel="noopener">Open {p['name']} {A}</a></p>
        </div></article>"""
        extra = f"""<section class="ink sec" id="products">
  <div class="wrap">
    <div class="sec-head rv"><p class="plate">Flagship products</p>
      <h2 class="h2 mt-s" style="color:#fff">Two products live in market.</h2>
      <p class="lead">Owned, built and operated by HGSL. Not white-labelled, not resold.</p></div>
    <div class="pgrid">{pc}</div>
  </div>
</section>"""

    return (head(f"{d['name']} ({d['code']}) — Honeytreat Global Services Limited",
                 d["short"], f"{d['slug']}.html") + nav(f"{d['slug']}.html") + f"""<main id="main">
{shero(d['code'], [("Home", "index.html"), ("Divisions", "divisions.html"), (d['name'], None)],
       f"{d['code']} &middot; Operating division", d['headline'].replace('<em>', '<em>'),
       d['lead'], d['fa'], d['fb'], d['stats'])}

<nav class="subnav" aria-label="On this page"><div class="wrap subnav__in">{subnav}</div></nav>

<section class="sec" id="overview">
  <div class="wrap split">
    <div class="rv"><p class="plate">Overview</p><h2 class="h2 mt-s">How this division works.</h2>
      <div class="mt-m">{ov}</div></div>
    <div class="rv rv-d1"><p class="plate">Specification</p><div class="spec">{spec}</div></div>
  </div>
</section>

<section class="sec tint" id="services">
  <div class="wrap">
    <div class="sec-head rv"><p class="plate">What we deliver</p>
      <h2 class="h2 mt-s">Services</h2>
      <p class="lead">Each line below is a contracted deliverable with defined scope, not a capability statement.</p></div>
    <div class="cgrid cgrid--3">{svc}</div>
  </div>
</section>

{extra}

<section class="sec" id="applications">
  <div class="wrap">
    <div class="sec-head rv"><p class="plate">Where it is used</p><h2 class="h2 mt-s">Industry applications</h2></div>
    <div class="cgrid cgrid--3">{apps}</div>
  </div>
</section>

<section class="sec tint" id="projects">
  <div class="wrap">
    <div class="sec-head rv"><p class="plate">Track record</p><h2 class="h2 mt-s">Project highlights</h2></div>
    <div class="cgrid cgrid--2">{projs}</div>
  </div>
</section>

<section class="sec" id="gallery">
  <div class="wrap">
    <div class="sec-head rv"><p class="plate">Gallery</p><h2 class="h2 mt-s">{d['code']} in the field</h2></div>
    {gallery(d['gallery'], d['code'], d['fa'], d['fb'])}
  </div>
</section>

<section class="sec tint" id="faq">
  <div class="wrap" style="max-width:900px">
    <div class="sec-head rv"><p class="plate">Questions</p><h2 class="h2 mt-s">Answered plainly.</h2></div>
    {acc(d['faqs'], d['slug'])}
  </div>
</section>

{cta(f"Start a {d['name'].lower()} conversation.",
     "Send the scope, location and timing. The division lead responds directly.",
     ("Contact the division", "contact.html"), ("Back to all divisions", "divisions.html"))}

<section class="sec">
  <div class="wrap">
    <div class="sec-head rv"><p class="plate">Elsewhere in the group</p><h2 class="h2 mt-s">Other divisions</h2></div>
    <div class="cgrid cgrid--4">{others}</div>
  </div>
</section>
</main>{footer()}{chat()}{tail()}""")


# --------------------------------------------------------------------------- #
# Standard content page builder
# --------------------------------------------------------------------------- #
def simple(slug, title, desc, code, eyebrow, h1, lead, blocks, fa="#6C2BD9", fb="#1B0F3A",
           crumb_label=None, cta_block=None):
    cr = [("Home", "index.html"), (crumb_label or h1[:34], None)]
    body = "".join(blocks)
    ctab = cta_block if cta_block is not None else cta(
        "Talk to the right team, first time.",
        "Every enquiry is routed to the division that owns it — no general inbox triage.")
    return (head(title, desc, slug) + nav(slug) + f"""<main id="main">
{shero(code, cr, eyebrow, h1, lead, fa, fb)}
{body}
{ctab}
</main>{footer()}{chat()}{tail()}""")


def sec(inner, cls="sec", ident=""):
    i = f' id="{ident}"' if ident else ""
    return f'<section class="{cls}"{i}><div class="wrap">{inner}</div></section>'


def head_block(eyebrow, title, lead=""):
    l = f'<p class="lead">{lead}</p>' if lead else ""
    return f'<div class="sec-head rv"><p class="plate">{eyebrow}</p><h2 class="h2 mt-s">{title}</h2>{l}</div>'


def cards3(items, icon="gear", cls="cgrid--3"):
    return f'<div class="cgrid {cls}">' + "".join(
        f'<article class="card rv rv-d{i%4}"><div class="card__ic">{ICONS[icon]}</div><h3>{t}</h3><p>{p}</p></article>'
        for i, (t, p) in enumerate(items)) + "</div>"


# --------------------------------------------------------------------------- #
# Content pages
# --------------------------------------------------------------------------- #
def page_about():
    b = [
        sec(f"""<div class="split">
      <div class="rv"><p class="plate">Who we are</p><h2 class="h2 mt-s">A group built around one question: what does industrial growth actually need?</h2>
      <p class="body-copy mt-m">Honeytreat Global Services Limited operates five divisions across equipment, property, energy, minerals and software. The combination is not accidental. Each division solves a constraint that the others run into — plant availability, energy cost, physical space, material supply, operating systems.</p>
      <p class="body-copy">That structure gives us something a single-sector operator does not have: when we lease equipment to a contractor, we have run sites ourselves. When we build software for industrial operations, our first user is our own equipment yard. When we advise on a diesel-to-gas switch, we have done the conversion maths on our own fleet.</p>
      <p class="body-copy">We are headquartered in Lagos and operate across Nigeria, as part of the wider Honeytreat Group.</p></div>
      <div class="split__art rv rv-d1">{field("#6C2BD9", "#1B0F3A", scrim=" field__scrim--v")}</div></div>"""),
        f'<section class="ink sec--tight"><div class="wrap"><p class="plate rv">Group at a glance</p></div><div class="wrap mt-m">{stat_block(STATS_HOME)}</div></section>',
        sec(head_block("How we operate", "Four operating principles.",
                       "Not values on a wall — the actual rules we make decisions against.") +
            cards3([
                ("Documented, not assumed", "Condition reports, service schedules, title verification, closure plans. If it matters, it exists in writing before work starts."),
                ("Own the maintenance obligation", "Across every division we hold the upkeep burden rather than pushing it downstream to the customer or the community."),
                ("Build to hold", "We develop property, fleets and software we would be willing to operate for a decade, which changes what we are willing to compromise on."),
                ("Integrate the divisions", "Plant from EQL works our MIN sites. SDI builds the systems all five run on. Vertical integration is the point, not a side effect."),
            ], "shield", "cgrid--4"), "sec tint"),
        sec(head_block("Group structure", "Where HGSL sits.") + f"""<div class="cgrid cgrid--4">
      {"".join(f'<article class="card rv rv-d{i%4}"><p class="plate">{c}</p><h3>{n}</h3><p>{d}</p></article>' for i, (c, n, d) in enumerate([
        ("HTG", "Honeytreat Group", "Parent group holding company, setting strategy and capital allocation across subsidiaries."),
        ("HGSL", "Honeytreat Global Services", "This company. Equipment leasing, real estate, CNG, mining and software."),
        ("HTL", "HTL Construction", "Construction delivery arm within the wider group."),
        ("HTA", "Honeytreat Trade Academy", "Skills and vocational training, supplying technical talent across the group."),
      ]))}</div>"""),
        sec(head_block("Leadership and governance", "Who is accountable.") +
            f'<p class="lead rv">Board composition, executive responsibilities and our governance framework are set out in full.</p>'
            f'<div class="btn-row mt-l rv rv-d1"><a class="btn btn--p" href="leadership.html">Leadership team {A}</a>'
            f'<a class="btn btn--g" href="governance.html">Corporate governance</a></div>', "sec tint"),
    ]
    return simple("about.html", "About us — Honeytreat Global Services Limited",
                  "HGSL is a diversified Nigerian industrial and technology group operating five divisions from Lagos, as part of the wider Honeytreat Group.",
                  "HGSL", "About us", "Five divisions, one operating standard.",
                  "A diversified industrial and technology group headquartered in Lagos, building the physical and digital infrastructure that industrial growth depends on.",
                  b, crumb_label="About us")


def page_leadership():
    people = "".join(
        f'<article class="person rv rv-d{i%4}"><div class="person__art">'
        f'{field("#6C2BD9", "#1B0F3A", scrim=None)}<span class="person__mono">{ini}</span></div>'
        f'<h3>{n}</h3><span>{r}</span><p>{bio}</p></article>'
        for i, (n, r, ini, bio) in enumerate(LEADERS))
    b = [
        sec(head_block("Executive team", "The people accountable for delivery.",
                       "Division leadership reports into the group executive, which reports to the board.") +
            f'<div class="people">{people}</div>' +
            '<p class="notice mt-l rv">Photography and full biographies are supplied by the group communications team and drop into this layout without markup changes.</p>'),
        sec(head_block("Board and committees", "Oversight structure.") + cards3([
            ("Board of Directors", "Sets strategy, approves capital allocation above delegated thresholds and appoints the executive. Meets quarterly with an annual strategy session."),
            ("Audit and Risk Committee", "Reviews financial reporting, internal controls, statutory compliance and the enterprise risk register."),
            ("Health, Safety and Environment Committee", "Oversees HSE performance across leasing, mining, CNG and construction activity, including incident review."),
            ("Investment Committee", "Screens acquisitions, development schemes and product investment against return and risk thresholds."),
        ], "users", "cgrid--2"), "sec tint"),
        sec(head_block("Delegation", "How decisions get made.") + f"""<div class="spec" style="max-width:900px">
      {"".join(f'<div class="spec__r"><div class="spec__k">{k}</div><div class="spec__v">{v}</div></div>' for k, v in [
        ("Board", "Strategy, capital allocation above threshold, executive appointment, governance policy"),
        ("Group executive", "Cross-division resource allocation, group risk, external partnerships and JVs"),
        ("Division leads", "Commercial terms within delegated limits, delivery, safety, division P&amp;L"),
        ("Functional heads", "Finance control, digital operations, HR and compliance across entities"),
      ])}</div>"""),
    ]
    return simple("leadership.html", "Leadership — Honeytreat Global Services Limited",
                  "The executive team, board structure and delegation framework of Honeytreat Global Services Limited.",
                  "LEAD", "Leadership", "Accountability with a name attached.",
                  "Executive responsibilities, board composition and the delegation framework that decides who signs what.",
                  b, crumb_label="Leadership")


def page_governance():
    items = [
        ("What governance framework does HGSL operate under?",
         "The company operates under its constitutional documents and the Companies and Allied Matters Act, with board-approved policies covering delegation of authority, procurement, conflict of interest, anti-bribery, health and safety, environmental management and data protection. Each policy has a named owner and a review cycle."),
        ("How is conflict of interest managed?",
         "Directors and senior staff make annual declarations and are required to disclose emerging interests as they arise. Related-party transactions require disclosure and board approval, and interested parties do not participate in the decision."),
        ("What is the anti-bribery position?",
         "Facilitation payments are prohibited without exception, including where they are locally customary. Gifts and hospitality above a stated threshold require written approval and are logged. Third parties acting for HGSL are contractually bound to the same standard."),
        ("How is risk managed across five divisions?",
         "Each division maintains a risk register with named owners, consolidated into a group register reviewed by the Audit and Risk Committee. Health and safety, environmental and licensing risks are tracked separately given their operating weight in mining, CNG and leasing."),
        ("How are whistleblowing reports handled?",
         "Reports can be made directly to the Audit and Risk Committee chair, outside the management line. Reports may be anonymous, retaliation is a disciplinary offence, and outcomes are reported to the committee in aggregate."),
        ("What are the compliance obligations across divisions?",
         "Mineral titles and permits for mining; gas handling, installation and safety certification for CNG; title perfection, planning and building control for real estate; equipment certification and operator competence for leasing; and data protection for software products."),
    ]
    b = [
        sec(f"""<div class="split"><div class="rv">
      <p class="plate">Governance</p><h2 class="h2 mt-s">Structure is what makes a five-division group governable.</h2>
      <p class="body-copy mt-m">A diversified group carries risks a single-sector business does not: different regulators, different licence regimes, different safety profiles. Governance is how those stay visible from the top rather than sitting inside a division until something goes wrong.</p>
      <p class="body-copy">Our framework is deliberately unremarkable. Clear delegation, documented policy, named risk owners, and a board that reviews performance on a fixed cycle rather than on request.</p></div>
      <div class="rv rv-d1"><p class="plate">Framework</p><div class="spec">
      {"".join(f'<div class="spec__r"><div class="spec__k">{k}</div><div class="spec__v">{v}</div></div>' for k, v in [
        ("Governing law", "Companies and Allied Matters Act; company constitutional documents"),
        ("Board cycle", "Quarterly, plus annual strategy session"),
        ("Committees", "Audit and Risk; HSE; Investment"),
        ("Policy set", "Delegation, procurement, conflict of interest, anti-bribery, HSE, environment, data protection"),
        ("Reporting", "Annual governance and sustainability reporting"),
      ])}</div></div></div>"""),
        sec(head_block("Policies and practice", "The questions auditors and partners ask.") + acc(items, "gov"), "sec tint"),
    ]
    return simple("governance.html", "Corporate governance — Honeytreat Global Services Limited",
                  "The governance framework, board committees, policy set and risk management approach of Honeytreat Global Services Limited.",
                  "GOV", "Corporate governance", "Unremarkable by design.",
                  "Delegation, policy, risk ownership and board oversight — set out so partners, lenders and regulators can see how decisions are controlled.",
                  b, crumb_label="Governance")


def page_projects():
    filters = '<button data-filter="all" aria-pressed="true">All</button>' + "".join(
        f'<button data-filter="{d["slug"]}" aria-pressed="false">{d["name"]}</button>' for d in DIVISIONS)
    pj = "".join(
        f'<a class="pj__i rv rv-d{i%4}" href="{p["div"]}.html" data-div="{p["div"]}">'
        f'{field(p["fa"], p["fb"], scrim=" field__scrim--v")}'
        f'<div class="pj__c"><p class="plate">{p["code"]} &middot; {p["name"]}</p>'
        f'<h3>{p["title"]}</h3><p>{p["desc"]}</p></div></a>' for i, p in enumerate(PROJECTS_ALL))
    b = [sec(head_block("Portfolio", "Delivered and in delivery.",
                        "Filter by division. Each entry links through to the division that delivered it.") +
             f'<div class="filters rv">{filters}</div><div class="pj">{pj}</div>'),
         sec(head_block("How we report on work", "What you can expect in a reference pack.") + cards3([
             ("Scope and constraints", "What was asked for, what the site or market imposed, and what changed during delivery."),
             ("Programme performance", "Planned against actual, with the reasons for variance stated rather than smoothed over."),
             ("Commercial outcome", "Cost position at completion and, where relevant, the operating result afterwards."),
         ], "chart"), "sec tint")]
    return simple("projects.html", "Projects — Honeytreat Global Services Limited",
                  "Delivered and active projects across HGSL's equipment leasing, real estate, CNG, mining and software divisions.",
                  "PROJ", "Projects", "Work you can check.",
                  "Delivered and active projects across all five divisions, with the scope, constraints and outcome stated plainly.",
                  b, crumb_label="Projects")


def page_sustainability():
    bars = "".join(
        f'<div class="rv"><div class="bar__top"><b>{t}</b><span>{v}%</span></div>'
        f'<div class="bar__t"><div class="bar__f" data-pct="{v}"></div></div>'
        f'<p class="mt-s" style="font-size:.9375rem;color:var(--slate);max-width:70ch">{c}</p></div>'
        for t, v, c in ESG)
    b = [
        sec(f"""<div class="split"><div class="rv">
      <p class="plate">ESG</p><h2 class="h2 mt-s">In our sectors, sustainability is an operating discipline before it is a report.</h2>
      <p class="body-copy mt-m">We extract minerals, move heavy plant and distribute fuel. Those activities have environmental and social consequences that cannot be offset away — they have to be managed at the site, in the specification and in the contract.</p>
      <p class="body-copy">So our ESG position is narrow and concrete: reduce the carbon intensity of the fuel our customers burn, rehabilitate every hectare we disturb, hire and train locally where we operate, and govern all of it transparently. We would rather report four things accurately than fourteen loosely.</p></div>
      <div class="split__art rv rv-d1">{field("#2DD4BF", "#0F4A46", scrim=" field__scrim--v")}</div></div>"""),
        sec(head_block("Progress", "Four commitments, measured.") + f'<div class="bars">{bars}</div>', "sec tint"),
        sec(head_block("Environment", "What we control directly.") + cards3([
            ("Energy transition", "Every CNG conversion and gas supply agreement displaces higher-emission fuel. It is our largest single environmental lever and it is commercially self-sustaining."),
            ("Land rehabilitation", "Mining sites carry a filed closure plan before extraction begins, with restoration running progressively rather than deferred."),
            ("Dust, water and noise", "Site-level controls with monitoring, because these are the impacts host communities actually experience day to day."),
            ("Fleet efficiency", "Maintained plant burns less fuel and lasts longer. Our maintenance obligation is an emissions measure as much as a commercial one."),
        ], "leaf", "cgrid--4")),
        sec(head_block("Social", "People and communities.") + cards3([
            ("Local employment", "Majority local hiring at host sites, with progression paths rather than seasonal engagement."),
            ("Skills development", "Technical training delivered through the Honeytreat Trade Academy, feeding qualified operators and technicians into the group and the wider market."),
            ("Community agreements", "Negotiated commitments with host communities on employment, infrastructure and development, reported against annually."),
            ("Safety", "Documented HSE systems across leasing, mining and CNG, with incident review at committee level."),
        ], "users", "cgrid--4"), "sec tint"),
        sec(head_block("Reporting", "What gets published.") +
            '<p class="lead rv">An annual sustainability statement covering the four commitment tracks, HSE performance, community programme delivery and governance. Published alongside investor materials.</p>'
            f'<p class="mt-l rv"><a class="tlink" href="investors.html">Investor information {A}</a></p>'),
    ]
    return simple("sustainability.html", "Sustainability and ESG — Honeytreat Global Services Limited",
                  "HGSL's ESG approach: energy transition through CNG, land rehabilitation in mining, local employment and skills development, and transparent governance.",
                  "ESG", "Sustainability", "Four commitments we can actually measure.",
                  "Cleaner energy adoption, responsible extraction, local employment and transparent governance — each with a target, an owner and annual reporting.",
                  b, fa="#2DD4BF", fb="#0F4A46", crumb_label="Sustainability")


def page_insights():
    posts = "".join(
        f'<a class="post rv rv-d{i%3}" href="#"><div class="post__art">{field(DMAP[s]["fa"], DMAP[s]["fb"], scrim=None)}</div>'
        f'<div class="post__m"><span>{cat}</span><time datetime="2026-07">July 2026</time></div>'
        f'<h3>{t}</h3><p>{d}</p><span class="tlink mt-s">Read {A}</span></a>'
        for i, (t, cat, d, s) in enumerate(INSIGHTS * 2))
    b = [sec(head_block("Insights &amp; news", "Written by the people running the operations.",
                        "Analysis, division updates and corporate announcements.") +
             f'<div class="posts">{posts}</div>'),
         sec(head_block("Media enquiries", "Press and communications.") +
             f'<p class="lead rv">For interviews, comment or media assets, contact group communications at '
             f'<a class="tlink" href="mailto:{MAIL}">{MAIL}</a>.</p>', "sec tint")]
    return simple("insights.html", "Insights and news — Honeytreat Global Services Limited",
                  "Analysis and corporate news from across HGSL's equipment, real estate, energy, mining and software divisions.",
                  "NEWS", "Insights &amp; news", "Notes from the operating side.",
                  "Analysis from the teams running the fleets, sites, stations and codebases — plus corporate announcements.",
                  b, crumb_label="Insights")


def page_careers():
    roles = [
        ("Plant Maintenance Engineer", "EQL &middot; Lagos", "Field service and preventive maintenance across the leased fleet."),
        ("Site Manager, Aggregates", "MIN &middot; South-West", "Production, safety and community interface at an active quarry."),
        ("CNG Conversion Technician", "CNG &middot; Lagos", "Certified installation and post-conversion support for fleet customers."),
        ("Senior Software Engineer", "SDI &middot; Lagos / hybrid", "Product engineering on QwikCare or SurDrive, TypeScript across the stack."),
        ("Development Manager", "RED &middot; Lagos", "Design coordination and delivery control on residential and industrial schemes."),
        ("Group Finance Analyst", "HGSL &middot; Lagos", "Division reporting, cost analysis and investment modelling."),
    ]
    rl = "".join(
        f'<a class="card rv rv-d{i%4}" href="contact.html"><p class="plate">{loc}</p><h3>{t}</h3>'
        f'<p>{d}</p><span class="tlink mt-s">Apply {A}</span></a>' for i, (t, loc, d) in enumerate(roles))
    b = [
        sec(head_block("Open roles", "Where we are hiring now.",
                       "Applications go to the division, not a central pool. Expect a technical conversation early.") +
            f'<div class="cgrid cgrid--3">{rl}</div>'),
        sec(head_block("Why work here", "What the job is actually like.") + cards3([
            ("Real constraints", "Our software team's users are our own equipment yard and site managers. Feedback arrives in hours, not quarters."),
            ("Range without dilution", "Five divisions means engineers, operators and analysts see problems most single-sector companies never encounter."),
            ("Training that leads somewhere", "Technical development runs through the Honeytreat Trade Academy, with certification rather than attendance."),
            ("Documented standards", "You will be given the specification, the safety system and the delegation limit. Ambiguity is a defect here."),
        ], "users", "cgrid--4"), "sec tint"),
        sec(head_block("Graduate and technical pathway", "Early careers.") +
            '<p class="lead rv">Structured entry routes for graduates in engineering, geology, quantity surveying, finance and software, and for technical trainees through the academy. Placements rotate across divisions in the first year.</p>'
            f'<div class="btn-row mt-l rv rv-d1"><a class="btn btn--p" href="contact.html">Send an application {A}</a></div>'),
    ]
    return simple("careers.html", "Careers — Honeytreat Global Services Limited",
                  "Open roles across HGSL's equipment, real estate, CNG, mining and software divisions, plus graduate and technical entry pathways.",
                  "JOBS", "Careers", "Five divisions. One hiring standard.",
                  "Engineering, operations, energy, property and software roles across the group — with applications going straight to the division that owns the work.",
                  b, crumb_label="Careers")


def page_investors():
    b = [
        sec(f"""<div class="split"><div class="rv"><p class="plate">Investor information</p>
      <h2 class="h2 mt-s">A diversified base, deliberately uncorrelated.</h2>
      <p class="body-copy mt-m">HGSL's five divisions sit across asset-backed leasing, property development, energy distribution, resource extraction and software. The revenue profiles are intentionally different: leasing and gas supply produce recurring income, development and mining are project and commodity linked, and software carries scalable margin.</p>
      <p class="body-copy">That mix is the investment case. It is also why governance and reporting discipline matter more here than in a single-sector operator — and why both are documented in full.</p>
      <div class="btn-row mt-l"><a class="btn btn--p" href="contact.html">Investor relations contact {A}</a>
      <a class="btn btn--g" href="governance.html">Governance framework</a></div></div>
      <div class="rv rv-d1"><p class="plate">Revenue character by division</p><div class="spec">
      {"".join(f'<div class="spec__r"><div class="spec__k">{d["code"]}</div><div class="spec__v">{v}</div></div>' for d, v in zip(DIVISIONS, [
        "Recurring lease income, asset-backed, utilisation driven",
        "Project margin on delivery plus recurring yield on held assets",
        "Recurring term supply and dispensing volume; infrastructure-backed",
        "Commodity-linked volume against infrastructure demand",
        "Product revenue with scalable margin plus internal platform value",
      ]))}</div></div></div>"""),
        sec(head_block("What we publish", "Reporting cycle.") + cards3([
            ("Annual report and accounts", "Audited financial statements with divisional performance commentary."),
            ("Sustainability statement", "Progress against the four ESG commitment tracks, HSE performance and community programmes."),
            ("Governance report", "Board and committee activity, policy review status and risk register summary."),
        ], "chart"), "sec tint"),
        sec(head_block("Frequently asked", "Investor questions.") + acc([
            ("Is HGSL listed?", "No. HGSL is a privately held company within the Honeytreat Group. Investor materials are provided to shareholders, lenders and prospective partners on request."),
            ("How is capital allocated across five divisions?", "Through the Investment Committee against defined return and risk thresholds, with board approval required above delegated limits. Divisions compete for capital on the same basis."),
            ("How do you handle currency and commodity exposure?", "Equipment and gas infrastructure carry import exposure managed through supplier terms and phased procurement. Aggregate and lease pricing is reviewed against input cost on a fixed cycle."),
            ("What is the growth priority?", "Recurring-revenue capacity first — leasing fleet depth and CNG infrastructure — with software product scale as the highest-margin lever."),
        ], "inv")),
    ]
    return simple("investors.html", "Investor information — Honeytreat Global Services Limited",
                  "HGSL investor information: divisional revenue character, reporting cycle, capital allocation and governance framework.",
                  "INV", "Investor information", "Five revenue profiles under one governance framework.",
                  "How the divisions earn, how capital is allocated between them, and what we publish on a fixed cycle.",
                  b, crumb_label="Investors")


def page_contact():
    opts = "".join(f'<option>{d["name"]} ({d["code"]})</option>' for d in DIVISIONS)
    b = [
        f"""<section class="sec"><div class="wrap"><div class="split">
      <div class="rv"><p class="plate">Send an enquiry</p><h2 class="h2 mt-s">Pick the division and we will route it.</h2>
      <p class="lead mt-m">Enquiries go to the division lead who owns the work, not a general inbox.</p>
      <form class="form mt-l" data-demo-form>
        <div class="form__ok">Thank you. Your enquiry has been logged and the division lead will respond directly.</div>
        <div class="f2">
          <div class="fld"><label for="c-name">Full name</label><input id="c-name" name="name" type="text" required></div>
          <div class="fld"><label for="c-org">Organisation</label><input id="c-org" name="org" type="text"></div>
        </div>
        <div class="f2">
          <div class="fld"><label for="c-mail">Email</label><input id="c-mail" name="email" type="email" required></div>
          <div class="fld"><label for="c-tel">Phone</label><input id="c-tel" name="tel" type="tel" placeholder="+234"></div>
        </div>
        <div class="fld"><label for="c-div">Division or enquiry type</label>
          <select id="c-div" name="division">{opts}<option>Partnership enquiry</option><option>Careers</option><option>Investor relations</option><option>Media</option></select></div>
        <div class="fld"><label for="c-msg">Scope, location and timing</label>
          <textarea id="c-msg" name="message" required placeholder="The more specific, the faster the response."></textarea></div>
        <div class="btn-row"><button class="btn btn--p" type="submit">Send enquiry {A}</button></div>
        <p class="form__note">This demonstration form does not transmit data. Connect it to your mail handler or CRM endpoint before launch — see README.md.</p>
      </form></div>
      <div class="rv rv-d1"><p class="plate">Head office</p><div class="spec">
        <div class="spec__r"><div class="spec__k">Address</div><div class="spec__v">{ADDR}</div></div>
        <div class="spec__r"><div class="spec__k">Email</div><div class="spec__v"><a class="tlink" href="mailto:{MAIL}">{MAIL}</a></div></div>
        <div class="spec__r"><div class="spec__k">Telephone</div><div class="spec__v">{TEL}</div></div>
        <div class="spec__r"><div class="spec__k">Hours</div><div class="spec__v">Monday to Friday, 08:00&ndash;17:00 WAT</div></div>
        <div class="spec__r"><div class="spec__k">Products</div><div class="spec__v"><a class="tlink" href="https://qwikcare.org" target="_blank" rel="noopener">qwikcare.org</a> &nbsp; <a class="tlink" href="https://surdrive.org" target="_blank" rel="noopener">surdrive.org</a></div></div>
      </div>
      <p class="notice mt-l">Urgent equipment or gas supply requests: call rather than email. The assistant at the bottom right can also point you to the right division.</p>
      </div></div></div></section>""",
        sec(head_block("Division contacts", "Straight to the team.") + f'<div class="cgrid cgrid--3">' + "".join(
            f'<a class="card rv rv-d{i%4}" href="{d["slug"]}.html"><p class="plate">{d["code"]}</p>'
            f'<h3>{d["name"]}</h3><p>{d["short"]}</p></a>' for i, d in enumerate(DIVISIONS)) + "</div>", "sec tint"),
    ]
    return simple("contact.html", "Contact — Honeytreat Global Services Limited",
                  f"Contact Honeytreat Global Services Limited. Head office: {ADDR}. Enquiries routed to the relevant operating division.",
                  "CTAC", "Contact", "Talk to the division that owns the work.",
                  "Head office in Lagos, with enquiries routed straight to the division lead responsible for delivery.",
                  b, crumb_label="Contact",
                  cta_block=cta("Prefer to browse first?",
                                "Every division page carries its own scope, specification, project history and questions.",
                                ("See all divisions", "divisions.html"), ("Technology ecosystem", "technology.html")))


def page_404():
    return (head("Page not found — Honeytreat Global Services Limited",
                 "The page you requested could not be found.", "404.html") + nav() + f"""<main id="main">
{shero("404", [("Home", "index.html"), ("Not found", None)], "Error 404",
       "That page is not here.",
       "The link may be out of date, or the page may have moved. The five division pages and the group sections below cover everything on this site.",
       "#6C2BD9", "#1B0F3A")}
<section class="sec"><div class="wrap">
  <div class="cgrid cgrid--3">{"".join(f'<a class="card rv rv-d{i%4}" href="{d["slug"]}.html"><p class="plate">{d["code"]}</p><h3>{d["name"]}</h3><p>{d["short"]}</p></a>' for i, d in enumerate(DIVISIONS))}</div>
  <div class="btn-row mt-l"><a class="btn btn--p" href="index.html">Back to home {A}</a><a class="btn btn--g" href="contact.html">Contact us</a></div>
</div></section>
</main>{footer()}{chat()}{tail()}""")


# --------------------------------------------------------------------------- #
# Write
# --------------------------------------------------------------------------- #
def write(name, html):
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(html)
    return name


def main():
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    os.makedirs(os.path.join(OUT, "assets", "img"), exist_ok=True)
    here = os.path.dirname(os.path.abspath(__file__))
    for sub in ("css", "js"):
        shutil.copytree(os.path.join(here, "assets", sub), os.path.join(OUT, "assets", sub))

    pages = [write("index.html", page_home()), write("divisions.html", page_divisions())]
    for d in DIVISIONS:
        pages.append(write(f"{d['slug']}.html", page_division(d)))
    for fn, builder in [("about.html", page_about), ("leadership.html", page_leadership),
                        ("governance.html", page_governance), ("projects.html", page_projects),
                        ("sustainability.html", page_sustainability), ("insights.html", page_insights),
                        ("careers.html", page_careers), ("investors.html", page_investors),
                        ("contact.html", page_contact), ("404.html", page_404)]:
        pages.append(write(fn, builder()))

    urls = "".join(f"  <url><loc>{SITE}/{p}</loc><changefreq>monthly</changefreq>"
                   f"<priority>{'1.0' if p=='index.html' else '0.8'}</priority></url>\n"
                   for p in pages if p != "404.html")
    write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n'
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + urls + "</urlset>\n")
    write("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")

    with open(os.path.join(OUT, "assets", "img", "README.txt"), "w") as f:
        f.write("Drop real photography here, then set --img on any .field or .field__img element.\n"
                "Suggested names: hero-eql.jpg, hero-red.jpg, hero-cng.jpg, hero-min.jpg, hero-sdi.jpg,\n"
                "eql-01..06.jpg, red-01..06.jpg, cng-01..06.jpg, min-01..06.jpg, sdi-01..06.jpg,\n"
                "qwikcare-app.png, surdrive-app.png, leader-01..04.jpg\n")
    print(f"Built {len(pages)} pages into {OUT}")
    for p in sorted(pages):
        print("  ", p)


if __name__ == "__main__":
    main()
