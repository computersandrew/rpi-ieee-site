#!/usr/bin/env python3
"""One-time generator for the site's HTML pages. Not needed after generation —
you can delete this file, or keep it as a quick way to update the shared
header/footer across every page at once (edit HEADER/FOOTER below, rerun)."""

import re

HEAD_COMMON = """  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Space+Grotesk:wght@500;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="css/style.css">
  <noscript><style>.reveal{opacity:1!important;transform:none!important;}</style></noscript>"""

HEADER = """  <header class="navbar">
    <div class="container">
      <a href="index.html" class="brand">
        <svg class="mark" viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
          <defs>
            <linearGradient id="gHead" x1="0" y1="0" x2="40" y2="40" gradientUnits="userSpaceOnUse">
              <stop stop-color="#0057B8"/><stop offset="1" stop-color="#7C3AED"/>
            </linearGradient>
          </defs>
          <rect width="40" height="40" rx="11" fill="url(#gHead)"/>
          <circle cx="12" cy="14" r="3" fill="#fff"/><circle cx="28" cy="14" r="3" fill="#fff"/><circle cx="20" cy="28" r="3" fill="#fff"/>
          <path d="M12 14L28 14M12 14L20 28M28 14L20 28" stroke="#fff" stroke-width="1.8" stroke-linecap="round"/>
        </svg>
        <span>RPI IEEE<span class="sub">Student Branch</span></span>
      </a>
      <nav class="nav-links" id="navLinks">
        <a href="index.html">Home</a>
        <a href="officers.html">Officers</a>
        <a href="calendar.html">Calendar</a>
        <a href="nexus.html">Nexus</a>
        <a href="contact.html">Contact</a>
        <div class="nav-cta"><a href="join.html" class="btn btn-primary">Join Now</a></div>
      </nav>
      <button class="nav-toggle" aria-label="Toggle menu" aria-expanded="false">
        <span></span><span></span><span></span>
      </button>
    </div>
  </header>"""

FOOTER = """  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div>
          <div class="footer-brand">
            <svg class="mark" viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
              <defs>
                <linearGradient id="gFoot" x1="0" y1="0" x2="40" y2="40" gradientUnits="userSpaceOnUse">
                  <stop stop-color="#0057B8"/><stop offset="1" stop-color="#7C3AED"/>
                </linearGradient>
              </defs>
              <rect width="40" height="40" rx="11" fill="url(#gFoot)"/>
              <circle cx="12" cy="14" r="3" fill="#fff"/><circle cx="28" cy="14" r="3" fill="#fff"/><circle cx="20" cy="28" r="3" fill="#fff"/>
              <path d="M12 14L28 14M12 14L20 28M28 14L20 28" stroke="#fff" stroke-width="1.8" stroke-linecap="round"/>
            </svg>
            RPI IEEE
          </div>
          <p class="footer-desc">The IEEE Student Branch at Rensselaer Polytechnic Institute &mdash; connecting students, researchers, and industry professionals through workshops, research, and career opportunities.</p>
          <div class="footer-social">
            <a href="https://discord.gg/N39xPCDtPz" target="_blank" rel="noopener" aria-label="Discord">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M20.3 4.4A19.6 19.6 0 0 0 15.6 3c-.2.4-.5 1-.7 1.4a18 18 0 0 0-5.8 0A13 13 0 0 0 8.4 3a19.7 19.7 0 0 0-4.7 1.4C1 9 .3 13.5.6 18a19.8 19.8 0 0 0 5.9 3c.5-.6.9-1.3 1.3-2a13 13 0 0 1-2-1c.2-.1.3-.3.5-.4a14 14 0 0 0 11.4 0l.5.4a13 13 0 0 1-2 1c.4.7.8 1.4 1.3 2a19.7 19.7 0 0 0 6-3c.4-5.2-1-9.7-3.2-13.6ZM8.7 14.8c-1 0-1.8-.9-1.8-2s.8-2 1.8-2 1.9.9 1.8 2c0 1.1-.8 2-1.8 2Zm6.6 0c-1 0-1.8-.9-1.8-2s.8-2 1.8-2 1.9.9 1.8 2c0 1.1-.8 2-1.8 2Z"/></svg>
            </a>
            <a href="https://www.linkedin.com/company/rensselaer-ieee/" target="_blank" rel="noopener" aria-label="LinkedIn">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M4.98 3.5a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5ZM3 9h4v12H3V9Zm7 0h3.8v1.7h.05c.53-1 1.83-2.05 3.77-2.05 4.03 0 4.78 2.65 4.78 6.1V21h-4v-5.4c0-1.28-.02-2.93-1.79-2.93-1.79 0-2.06 1.4-2.06 2.84V21h-4V9Z"/></svg>
            </a>
          </div>
        </div>
        <div class="footer-col">
          <h4>Explore</h4>
          <ul>
            <li><a href="officers.html">Officers</a></li>
            <li><a href="calendar.html">Calendar</a></li>
            <li><a href="nexus.html">Nexus</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Get Involved</h4>
          <ul>
            <li><a href="join.html">How to Join</a></li>
            <li><a href="contact.html">Contact Us</a></li>
            <li><a href="https://discord.gg/N39xPCDtPz" target="_blank" rel="noopener">Discord Community</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Stay Updated</h4>
          <form class="newsletter-form">
            <div class="newsletter">
              <input type="email" required placeholder="you@rpi.edu" aria-label="Email address">
              <button type="submit">Sign Up</button>
            </div>
            <p class="newsletter-msg"></p>
          </form>
        </div>
      </div>
      <div class="footer-bottom">
        <span>&copy; <span id="year"></span> IEEE Student Branch at RPI. Not an official RPI or IEEE website.</span>
        <span><a href="mailto:ieee@rpi.edu">ieee@rpi.edu</a></span>
      </div>
    </div>
  </footer>
  <script src="js/main.js"></script>"""


def page(title, description, body, extra_head=""):
    return f"""<!doctype html>
<html lang="en">
<head>
{HEAD_COMMON}
  <title>{title} | RPI IEEE Student Branch</title>
  <meta name="description" content="{description}">
{extra_head}</head>
<body>
{HEADER}
{body}
{FOOTER}
</body>
</html>
"""


# ---------------- HOME ----------------
home_body = """  <section class="hero">
    <div class="container">
      <div class="hero-grid">
        <div class="reveal is-visible">
          <span class="eyebrow">IEEE Student Branch &middot; Rensselaer Polytechnic Institute</span>
          <h1>Building the next generation of engineers, together.</h1>
          <p class="lead">A vibrant link connecting students, researchers, and industry professionals to foster collaboration and knowledge&nbsp;sharing &mdash; through workshops, research, and real career opportunities.</p>
          <div class="hero-actions">
            <a href="join.html" class="btn btn-primary">Join Now</a>
            <a href="nexus.html" class="btn btn-outline-light">Explore Nexus</a>
          </div>
          <div class="hero-stats">
            <div><div class="num">EE</div><div class="label">&amp; beyond &mdash; CS, ME, and more</div></div>
            <div><div class="num">IEEE</div><div class="label">Global professional network</div></div>
            <div><div class="num">RPI</div><div class="label">Student-run branch</div></div>
          </div>
        </div>
        <div class="hero-card reveal is-visible">
          <h3>Why students join</h3>
          <ul>
            <li><span class="ico">&#128101;</span> Network with peers and industry leaders</li>
            <li><span class="ico">&#128218;</span> Expert-led workshops on emerging tech</li>
            <li><span class="ico">&#128300;</span> Hands-on research collaborations</li>
            <li><span class="ico">&#128188;</span> Internships, mentorship &amp; career support</li>
          </ul>
        </div>
      </div>
    </div>
  </section>

  <section class="section-alt">
    <div class="container">
      <div class="section-head reveal">
        <span class="eyebrow">What we offer</span>
        <h2>Four ways we help you grow</h2>
        <p>Whatever brought you here &mdash; curiosity, career, or community &mdash; there's a place for you in the branch.</p>
      </div>
      <div class="grid grid-4">
        <div class="card reveal">
          <div class="ico"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="7" cy="8" r="3"/><circle cx="17" cy="8" r="3"/><path d="M2 21v-1a5 5 0 0 1 5-5h0a5 5 0 0 1 5 5v1M12 21v-1a5 5 0 0 1 5-5h0a5 5 0 0 1 5 5v1"/></svg></div>
          <h3>Networking</h3>
          <p>Connect with peers, alumni, and industry leaders across engineering fields.</p>
        </div>
        <div class="card reveal">
          <div class="ico"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20V4H6.5A2.5 2.5 0 0 0 4 6.5v13Z"/><path d="M4 19.5V22h13v-3"/></svg></div>
          <h3>Workshops</h3>
          <p>Hands-on, expert-led sessions on emerging engineering trends and tools.</p>
        </div>
        <div class="card reveal">
          <div class="ico"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 3"/></svg></div>
          <h3>Research</h3>
          <p>Get involved in practical research projects and branch initiatives.</p>
        </div>
        <div class="card reveal">
          <div class="ico"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="7" width="18" height="13" rx="2"/><path d="M8 7V5a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"/></svg></div>
          <h3>Careers</h3>
          <p>Internships, job placements, and mentorship to launch your career.</p>
        </div>
      </div>
    </div>
  </section>

  <section>
    <div class="container">
      <div class="section-head reveal">
        <span class="eyebrow">Who can join</span>
        <h2>Open to every kind of engineer</h2>
        <p>We welcome students across <strong>computer systems engineering, computer science, mechanical engineering</strong>, and other technology-related disciplines &mdash; not just electrical engineering.</p>
      </div>
      <div class="grid grid-3">
        <div class="card reveal">
          <h3>IEEE membership</h3>
          <p>Branch membership requires IEEE membership. Non-members are still welcome to attend our workshops.</p>
        </div>
        <div class="card reveal">
          <h3>All majors welcome</h3>
          <p>Our programming spans EE, CS, ME, and other engineering &amp; technology disciplines.</p>
        </div>
        <div class="card reveal">
          <h3>Any experience level</h3>
          <p>Whether you're just curious about engineering or deep into research, there's a way to get involved.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section-alt">
    <div class="container">
      <div class="section-head reveal">
        <span class="eyebrow">From the branch</span>
        <h2>Latest from Nexus</h2>
        <p>News, guides, and updates from IEEE and the RPI branch.</p>
      </div>
      <div class="grid grid-3">
        <div class="card article-card reveal">
          <span class="article-tag">Informational</span>
          <h3>The CHIPS and Science Act</h3>
          <p>What the CHIPS and Science Act is, and what it means for the semiconductor industry.</p>
          <span class="article-date">January 14, 2025</span>
        </div>
        <div class="card article-card reveal">
          <span class="article-tag">Announcement</span>
          <h3>EPS @ RPI 2024&ndash;2025 Roadmap</h3>
          <p>The annual program roadmap for the Electronics Packaging Society chapter at RPI.</p>
          <span class="article-date">September 1, 2024</span>
        </div>
        <div class="card article-card reveal">
          <span class="article-tag">Recruitment</span>
          <h3>How to Join</h3>
          <p>A step-by-step guide for students who want to get involved with IEEE at RPI.</p>
          <span class="article-date">February 17, 2021</span>
        </div>
      </div>
      <div class="center" style="margin-top:36px;">
        <a href="nexus.html" class="btn btn-ghost">View all articles</a>
      </div>
    </div>
  </section>

  <section>
    <div class="container">
      <div class="cta-band reveal">
        <h2>Join our quest to foster innovation and collaboration in engineering.</h2>
        <p>Meetings, workshops, and a community that's building things worth talking about.</p>
        <div class="cta-actions">
          <a href="join.html" class="btn btn-light">Join Now</a>
          <a href="contact.html" class="btn btn-outline-light">Ask a question</a>
        </div>
      </div>
    </div>
  </section>
"""

with open("index.html", "w") as f:
    f.write(page(
        "Home",
        "IEEE Student Branch at Rensselaer Polytechnic Institute — networking, workshops, research, and career development for engineering students.",
        home_body,
    ))

# ---------------- OFFICERS ----------------
def officer_card(initials, name, role):
    return f"""        <div class="card officer-card reveal">
          <div class="avatar">{initials}</div>
          <h3>{name}</h3>
          <div class="role">{role}</div>
        </div>"""

branch_officers = [
    ("FN", "Farris Nefissi", "Branch Chair"),
    ("JL", "Jimin Lee", "Vice Chair"),
    ("TJ", "Thomas Jenkins", "Treasurer"),
    ("ST", "Sangeeth Thayaaparan", "Secretary"),
]
eps_officers = [
    ("DK", "David King", "EPS Chair"),
    ("EC", "Evan Chen", "EPS Vice Chair"),
    ("JK", "Jonas Kendra", "EPS Treasurer"),
    ("XL", "Xinyan Li", "EPS Secretary"),
]

officers_body = f"""  <header class="page-header">
    <div class="container">
      <span class="eyebrow">Leadership</span>
      <h1>Meet the officers</h1>
      <p>The students who plan our events, run our meetings, and keep the branch moving.</p>
    </div>
  </header>

  <section>
    <div class="container">
      <div class="officer-group reveal">
        <div class="officer-group-title">
          <h2>IEEE Student Branch</h2>
          <div class="line"></div>
        </div>
        <div class="grid grid-4">
{chr(10).join(officer_card(*o) for o in branch_officers)}
        </div>
      </div>

      <div class="officer-group reveal">
        <div class="officer-group-title">
          <h2>IEEE EPS Chapter</h2>
          <div class="line"></div>
        </div>
        <div class="grid grid-4">
{chr(10).join(officer_card(*o) for o in eps_officers)}
        </div>
      </div>

      <p style="text-align:center; color: var(--color-muted); font-size: 0.85rem;">
        &#9432; Officer list carried over from the branch's previous website &mdash; current officers should confirm and update this roster (see README.md).
      </p>
    </div>
  </section>
"""

with open("officers.html", "w") as f:
    f.write(page(
        "Officers",
        "Meet the officers of the IEEE Student Branch at RPI.",
        officers_body,
    ))
print("officers.html written")

# ---------------- CALENDAR ----------------
calendar_body = """  <header class="page-header">
    <div class="container">
      <span class="eyebrow">Events</span>
      <h1>Calendar</h1>
      <p>General meetings, workshops, and events &mdash; all in one place.</p>
    </div>
  </header>

  <section>
    <div class="container">
      <p class="calendar-note reveal">
        &#9432; This embeds the branch's Google Calendar. If events aren't showing up, an officer should confirm
        the calendar is still shared publicly, or swap in a fresh embed link from Google Calendar &rarr; Settings &rarr;
        Integrate calendar. See README.md for instructions.
      </p>
      <div class="calendar-wrap reveal">
        <iframe src="https://calendar.google.com/calendar/embed?src=ieee.eps.rpi%40gmail.com&ctz=America%2FNew_York" scrolling="no"></iframe>
      </div>
    </div>
  </section>
"""

with open("calendar.html", "w") as f:
    f.write(page(
        "Calendar",
        "Upcoming IEEE Student Branch meetings, workshops, and events at RPI.",
        calendar_body,
    ))
print("calendar.html written")

# ---------------- JOIN ----------------
join_body = """  <header class="page-header">
    <div class="container">
      <span class="eyebrow">Get involved</span>
      <h1>How to join</h1>
      <p>Getting involved takes four steps &mdash; most students are in by their first meeting.</p>
    </div>
  </header>

  <section>
    <div class="container">
      <div class="steps">
        <div class="step reveal">
          <div class="step-num">1</div>
          <div>
            <h3>Become an IEEE member</h3>
            <p>Branch membership requires IEEE membership. Sign up or renew at
              <a href="https://www.ieee.org/membership/join/index.html" target="_blank" rel="noopener">ieee.org</a>.
              Not ready to commit? You can still attend our workshops as a non-member.</p>
          </div>
        </div>
        <div class="step reveal">
          <div class="step-num">2</div>
          <div>
            <h3>Join the Discord</h3>
            <p>Chat directly with members, get real-time answers, and hear about events first.
              <a href="https://discord.gg/N39xPCDtPz" target="_blank" rel="noopener">Join our Discord &rarr;</a></p>
          </div>
        </div>
        <div class="step reveal">
          <div class="step-num">3</div>
          <div>
            <h3>Come to a meeting</h3>
            <p>General meetings and events are posted on our <a href="calendar.html">calendar</a>. Just show up &mdash; no RSVP needed.</p>
          </div>
        </div>
        <div class="step reveal">
          <div class="step-num">4</div>
          <div>
            <h3>Get involved</h3>
            <p>Pick up a project, join a workshop, or run for an officer position down the line. However deep you want to go, there's room.</p>
          </div>
        </div>
      </div>

      <div class="cta-band reveal" style="margin-top:64px;">
        <h2>Questions before you dive in?</h2>
        <p>Reach out any time &mdash; we're happy to help you figure out where you fit.</p>
        <div class="cta-actions">
          <a href="contact.html" class="btn btn-light">Contact us</a>
          <a href="https://discord.gg/N39xPCDtPz" target="_blank" rel="noopener" class="btn btn-outline-light">Join Discord</a>
        </div>
      </div>
    </div>
  </section>
"""

with open("join.html", "w") as f:
    f.write(page(
        "Join",
        "How to join the IEEE Student Branch at RPI — membership, Discord, and meetings.",
        join_body,
    ))
print("join.html written")

# ---------------- NEXUS ----------------
def article_card(tag, title, desc, date):
    return f"""        <div class="card article-card reveal">
          <span class="article-tag">{tag}</span>
          <h3>{title}</h3>
          <p>{desc}</p>
          <span class="article-date">{date}</span>
        </div>"""

articles = [
    ("Informational", "The CHIPS and Science Act", "Introduces the CHIPS (Creating Helpful Incentives to Produce Semiconductors) and Science Act, and what this legislation means for the industry.", "January 14, 2025"),
    ("Announcement", "EPS @ RPI 2024&ndash;2025 Program Roadmap", "The annual program roadmap for the Electronics Packaging Society chapter at RPI, presented by IEEE.", "September 1, 2024"),
    ("Recruitment", "Join Our Community", "Why joining IEEE matters, and how the branch supports RPI's mission to advance technology.", "February 17, 2021"),
    ("Recruitment", "How to Join", "A guide for anyone passionate about technology or engineering who wants to get involved.", "February 17, 2021"),
]

nexus_body = f"""  <header class="page-header">
    <div class="container">
      <span class="eyebrow">Articles</span>
      <h1>Nexus</h1>
      <p>News, guides, and updates from the branch and from IEEE at large.</p>
    </div>
  </header>

  <section>
    <div class="container">
      <p class="calendar-note reveal">
        &#9432; These are the articles carried over from the previous site as placeholders. Officers can add new
        posts by duplicating one of these cards &mdash; see README.md for how the Nexus section is organized.
      </p>
      <div class="grid grid-3">
{chr(10).join(article_card(*a) for a in articles)}
      </div>
    </div>
  </section>
"""

with open("nexus.html", "w") as f:
    f.write(page(
        "Nexus",
        "Articles, announcements, and guides from the IEEE Student Branch at RPI.",
        nexus_body,
    ))
print("nexus.html written")

# ---------------- CONTACT ----------------
contact_body = """  <header class="page-header">
    <div class="container">
      <span class="eyebrow">Say hello</span>
      <h1>Contact us</h1>
      <p>Have questions or need guidance on joining? We're here to help.</p>
    </div>
  </header>

  <section>
    <div class="container">
      <div class="contact-grid">
        <div class="card contact-card reveal">
          <div class="ico"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 6-10 7L2 6"/></svg></div>
          <h3>General inquiries</h3>
          <p>Questions about the branch, events, or getting involved.</p>
          <a class="value" href="mailto:ieee@rpi.edu">ieee@rpi.edu</a>
        </div>
        <div class="card contact-card reveal">
          <div class="ico"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg></div>
          <h3>Branch leadership</h3>
          <p>Reach the branch president directly for anything leadership-related.</p>
          <a class="value" href="mailto:kingd7@rpi.edu">kingd7@rpi.edu</a>
        </div>
        <div class="card contact-card reveal">
          <div class="ico"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/></svg></div>
          <h3>Outreach</h3>
          <p>Partnerships, sponsorships, and outreach opportunities.</p>
          <a class="value" href="mailto:chene8@rpi.edu">chene8@rpi.edu</a>
        </div>
      </div>

      <div class="grid grid-2 reveal" style="margin-top:24px;">
        <div class="card contact-card">
          <div class="ico"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7h18M8 3v4M16 3v4"/></svg></div>
          <h3>Meetings</h3>
          <p>General meetings are posted on our calendar &mdash; drop in any time.</p>
          <a class="value" href="calendar.html">View the calendar &rarr;</a>
        </div>
        <div class="card contact-card">
          <div class="ico"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 11.5a8.4 8.4 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.4 8.4 0 0 1-3.8-.9L3 21l1.9-5.7a8.4 8.4 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.4 8.4 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5Z"/></svg></div>
          <h3>Discord</h3>
          <p>Chat with members directly and get real-time responses.</p>
          <a class="value" href="https://discord.gg/N39xPCDtPz" target="_blank" rel="noopener">Join our Discord &rarr;</a>
        </div>
      </div>
    </div>
  </section>
"""

with open("contact.html", "w") as f:
    f.write(page(
        "Contact",
        "Get in touch with the IEEE Student Branch at RPI — email, Discord, and meeting info.",
        contact_body,
    ))
print("contact.html written")
