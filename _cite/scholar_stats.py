"""
Regenerate _data/scholar.yaml — the data behind the "Publications" panel on the
home page (top publications with citation counts + lifetime total) — from Google
Scholar via SerpAPI.

WHY THIS IS SEPARATE FROM cite.py:
  cite.py's google-scholar plugin injects fetched papers into the citations
  LIST (_data/citations.yaml), which would duplicate the papers you already list
  in _data/sources.yaml. This script instead only refreshes the stats PANEL
  numbers (_data/scholar.yaml) and never touches your publications list.

SETUP (to turn on auto-refresh):
  1. Make a free account at https://serpapi.com and copy your API key.
  2. Add it as a repo secret named GOOGLE_SCHOLAR_API_KEY
     (Settings > Secrets and variables > Actions > New repository secret).
  3. Make sure _data/scholar.yaml's `profile` points at your Scholar profile
     (https://scholar.google.com/citations?user=YOUR_ID). The Scholar id is
     read from that URL.
  The update-citations workflow already exports the secret and runs this script,
  so refreshed numbers get committed automatically on its schedule.

WITHOUT a key set, this script is a deliberate no-op: your hand-maintained
_data/scholar.yaml is left exactly as-is (so local builds and un-configured
forks keep working).

Run manually from the repo root with:  python _cite/scholar_stats.py
"""

import os
import re

from serpapi import GoogleSearch

from util import get_safe, load_data, log, save_data

DATA_FILE = "_data/scholar.yaml"
TOP_N = 3


def normalize(text):
    """strip to lowercase alphanumerics for loose title matching"""
    return re.sub(r"[^a-z0-9]", "", str(text).lower())


def parse_gsid(profile):
    """pull the Scholar author id out of a profile URL (…?user=XXXX)"""
    match = re.search(r"user=([^&]+)", str(profile))
    return match.group(1) if match else ""


def main():
    api_key = os.environ.get("GOOGLE_SCHOLAR_API_KEY", "")
    if not api_key:
        log("No GOOGLE_SCHOLAR_API_KEY set; leaving scholar.yaml untouched", level="INFO")
        return

    data = load_data(DATA_FILE) or {}
    profile = get_safe(data, "profile", "")
    gsid = parse_gsid(profile)
    if not gsid:
        log("Couldn't parse Scholar id from profile URL; skipping", level="WARNING")
        return

    # keep existing title->link so we preserve nice arXiv/PDF links over
    # Scholar's redirect links
    existing_links = {}
    for pub in get_safe(data, "publications", []) or []:
        existing_links[normalize(get_safe(pub, "title", ""))] = get_safe(pub, "link", "")

    # query SerpAPI's Google Scholar author endpoint
    params = {
        "engine": "google_scholar_author",
        "api_key": api_key,
        "author_id": gsid,
        "num": 100,
        "sort": "cited_by",
    }
    response = GoogleSearch(params).get_dict()

    articles = get_safe(response, "articles", []) or []
    # author-level lifetime total lives in the cited_by summary table
    lifetime = get_safe(response, "cited_by.table.0.citations.all", 0) or 0

    pubs = []
    for work in articles:
        title = get_safe(work, "title", "")
        if not title:
            continue
        citations = get_safe(work, "cited_by.value", 0) or 0
        link = existing_links.get(normalize(title)) or get_safe(work, "link", "")
        pubs.append({"title": title, "link": link, "citations": citations})

    # keep the most-cited handful
    pubs.sort(key=lambda p: p["citations"], reverse=True)
    pubs = pubs[:TOP_N]

    if not pubs:
        log("Scholar returned no articles; leaving scholar.yaml untouched", level="WARNING")
        return

    save_data(
        DATA_FILE,
        {"profile": profile, "lifetime_citations": lifetime, "publications": pubs},
    )
    log(f"Updated {DATA_FILE}: {len(pubs)} pubs, {lifetime} lifetime citations", level="SUCCESS")


if __name__ == "__main__":
    main()
