#!/usr/bin/env python3
"""Generator for the site's HTML pages. Rerun after editing HEADER/FOOTER/
page titles below to regenerate all pages consistently."""

HEAD_COMMON = """  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="css/style.css">"""

HEADER = """  <header class="navbar">
    <div class="container">
      <a href="index.html" class="brand">RPI IEEE</a>
      <nav class="nav-links" id="navLinks">
        <a href="index.html">Home</a>
        <a href="officers.html">Officers</a>
        <a href="calendar.html">Calendar</a>
        <a href="nexus.html">Nexus</a>
        <a href="join.html">Join</a>
        <a href="contact.html">Contact</a>
      </nav>
      <button class="nav-toggle" aria-label="Toggle menu" aria-expanded="false">
        <span></span><span></span><span></span>
      </button>
    </div>
  </header>"""

FOOTER = """  <footer class="site-footer">
    <div class="container">
      <span>&copy; <span id="year"></span> IEEE Student Branch at RPI</span>
    </div>
  </footer>
  <script src="js/main.js"></script>"""


def page(title, heading):
    return f"""<!doctype html>
<html lang="en">
<head>
{HEAD_COMMON}
  <title>{title} | RPI IEEE Student Branch</title>
</head>
<body>
{HEADER}
  <main>
    <div class="container">
      <h1>{heading}</h1>
    </div>
  </main>
{FOOTER}
</body>
</html>
"""


pages = [
    ("index.html", "Home", "RPI IEEE Student Branch"),
    ("officers.html", "Officers", "Officers"),
    ("calendar.html", "Calendar", "Calendar"),
    ("nexus.html", "Nexus", "Nexus"),
    ("join.html", "Join", "Join"),
    ("contact.html", "Contact", "Contact"),
]

for filename, title, heading in pages:
    with open(filename, "w") as f:
        f.write(page(title, heading))
    print(f"{filename} written")
