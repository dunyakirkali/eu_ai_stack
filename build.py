#!/usr/bin/env python3
"""Generate eu_companies_by_layer.md, eu_map.html and eu_companies.geojson from companies.json.

Edit companies.json (the single source of truth), then run: python3 build.py
"""
import collections
import json
import math
from pathlib import Path

HERE = Path(__file__).parent

LAYERS = [
    ("L0", "Raw materials", "#8c564b"),
    ("L1", "Materials processing", "#e377c2"),
    ("L2", "Machine subsystems", "#7f7f7f"),
    ("L3", "Chip machines and design tools", "#d62728"),
    ("L4", "Chip design and manufacturing", "#ff7f0e"),
    ("L5", "Systems and infrastructure", "#bcbd22"),
    ("L6", "Data and talent", "#17becf"),
    ("L7", "Frontier labs", "#1f77b4"),
    ("L8", "Delivery and applications", "#2ca02c"),
]
LAYER = {lid: (name, color) for lid, name, color in LAYERS}

companies = json.loads((HERE / "companies.json").read_text())
by_layer = collections.defaultdict(list)
for c in companies:
    by_layer[c["layer"]].append(c)


def cell(s):
    return str(s).replace("|", "\\|").replace("\n", " ")


# ---------- Markdown ----------
conf = collections.Counter(c["confidence"] for c in companies)
countries = collections.Counter(c["country"] for c in companies)
md = [
    "# European companies by layer of the AI stack",
    "",
    f"{len(companies)} European companies across the nine layers of [the stack](ai_stack_tech_tree.md). "
    "\"European\" includes the UK, Norway and Switzerland, not only EU members. "
    "The country and city are the headquarters.",
    "",
    "**Read this first.** The list was compiled by research agents, and most entries come from their own knowledge, "
    "not from live sources (agents reported only about 50 live checks in total). Each entry has the agent's confidence rating, which is a judgement, not proof:",
    "",
    f"- **high** ({conf['high']}): the research agent was confident, and some of these were checked live.",
    f"- **medium** ({conf['medium']}): believed correct, mostly not checked live.",
    f"- **low** ({conf['low']}): uncertain about the headquarters, ownership, whether it still operates, or both. "
    "Verify before relying on it.",
    "",
    "Ownership and headquarters change often (acquisitions, relocations), so the Note column matters. "
    "Source: [`companies.json`](companies.json). Regenerate this file, the map and the GeoJSON with `python3 build.py`.",
    "",
    "| Layer | Companies |",
    "|---|---|",
]
for lid, name, _ in LAYERS:
    md.append(f"| [{lid} · {name}](#{lid.lower()}--{name.lower().replace(' ', '-')}) | {len(by_layer[lid])} |")
md += ["", "By country: " + ", ".join(f"{k} {v}" for k, v in countries.most_common()), ""]

for lid, name, _ in LAYERS:
    md += [f"## {lid} · {name}", "", "| Company | Country | City | Role | Confidence | Note |", "|---|---|---|---|---|---|"]
    for c in by_layer[lid]:
        nm = f"[{cell(c['name'])}]({c['source']})" if c["source"].startswith("http") else cell(c["name"])
        md.append(f"| {nm} | {c['country']} | {cell(c['city'])} | {cell(c['role'])} | {c['confidence']} | {cell(c['note'])} |")
    md.append("")
(HERE / "eu_companies_by_layer.md").write_text("\n".join(md))

# ---------- GeoJSON (GitHub renders it as a map) ----------
groups = collections.defaultdict(list)
for c in companies:
    groups[(c["lat"], c["lon"])].append(c)
feats = []
for lst in groups.values():
    for i, c in enumerate(lst):
        la, lo = c["lat"], c["lon"]
        if len(lst) > 1:  # spiral so same-city pins stay separate
            r = 0.04 * math.sqrt(i + 1)
            a = i * 2.4
            la += r * math.sin(a)
            lo += 1.5 * r * math.cos(a)
        desc = f"{c['city']}, {c['country']}. {c['role']}. {c['layer']} · {LAYER[c['layer']][0]}. Confidence: {c['confidence']}."
        if c["note"]:
            desc += f" {c['note']}."
        feats.append({
            "type": "Feature",
            "geometry": {"type": "Point", "coordinates": [round(lo, 4), round(la, 4)]},
            "properties": {
                "title": c["name"], "description": desc,
                "marker-color": LAYER[c["layer"]][1], "marker-size": "small", "layer": c["layer"],
            },
        })
feats.sort(key=lambda f: (f["properties"]["layer"], f["properties"]["title"].lower()))
(HERE / "eu_companies.geojson").write_text(
    json.dumps({"type": "FeatureCollection", "features": feats}, ensure_ascii=False, indent=1))

# ---------- HTML map ----------
HTML = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>European AI stack map</title>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/leaflet.markercluster/1.5.3/MarkerCluster.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/leaflet.markercluster/1.5.3/MarkerCluster.Default.css">
<style>
  html, body { height: 100%; margin: 0; font: 14px/1.4 system-ui, sans-serif; }
  #map { position: absolute; inset: 0; }
  .panel {
    position: absolute; z-index: 1000; top: 12px; right: 12px; max-width: 280px; max-height: calc(100% - 24px);
    overflow: auto; background: #fff; color: #111; padding: 10px 12px; border-radius: 8px;
    box-shadow: 0 1px 6px rgba(0,0,0,.3);
  }
  .panel h1 { font-size: 14px; margin: 0 0 6px; }
  .panel label { display: flex; align-items: center; gap: 6px; cursor: pointer; padding: 1px 0; }
  .panel hr { border: 0; border-top: 1px solid #ddd; margin: 6px 0; }
  .dot { width: 12px; height: 12px; border-radius: 50%; display: inline-block; flex: none; border: 1px solid rgba(0,0,0,.4); }
  .panel small { color: #555; display: block; margin-top: 6px; }
  .count { margin-left: auto; color: #666; font-variant-numeric: tabular-nums; }
</style>
</head>
<body>
<div id="map"></div>
<div class="panel">
  <h1>European AI stack · <span id="total"></span> companies</h1>
  <div id="legend"></div>
  <hr>
  <label><input type="checkbox" id="hideLow"> Hide low-confidence entries</label>
  <small>Pins sit at company headquarters. Faded pins are low confidence. Click a cluster to zoom in.</small>
</div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/leaflet.markercluster/1.5.3/leaflet.markercluster.js"></script>
<script>
const LAYERS = __LAYERS__;
const COMPANIES = __COMPANIES__;

const map = L.map("map").setView([50.0, 9.0], 5);
L.tileLayer("https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png", {
  maxZoom: 12,
  attribution: "&copy; OpenStreetMap contributors &copy; CARTO",
}).addTo(map);

const esc = s => String(s).replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
const color = Object.fromEntries(LAYERS.map(l => [l[0], l[2]]));
const lname = Object.fromEntries(LAYERS.map(l => [l[0], l[1]]));

const entries = COMPANIES.map(c => {
  const m = L.circleMarker([c.lat, c.lon], {
    radius: 8, color: "#222", weight: 1, fillColor: color[c.layer],
    fillOpacity: c.confidence === "low" ? 0.3 : 0.9, opacity: c.confidence === "low" ? 0.5 : 1,
  });
  const name = /^https?:/.test(c.source) ? `<a href="${esc(c.source)}" target="_blank" rel="noopener">${esc(c.name)}</a>` : esc(c.name);
  m.bindPopup(
    `<strong>${name}</strong><br>${esc(c.city)}, ${esc(c.country)}<br>${esc(c.role)}<br>` +
    `<em>${esc(c.layer)} · ${esc(lname[c.layer])}</em><br>Confidence: ${esc(c.confidence)}` +
    (c.note ? `<br><small>${esc(c.note)}</small>` : "")
  );
  m.bindTooltip(esc(c.name));
  return { c, m };
});

const cluster = L.markerClusterGroup({ maxClusterRadius: 35, showCoverageOnHover: false }).addTo(map);
const on = Object.fromEntries(LAYERS.map(l => [l[0], true]));
const hideLow = document.getElementById("hideLow");

function refresh() {
  cluster.clearLayers();
  cluster.addLayers(entries.filter(e => on[e.c.layer] && !(hideLow.checked && e.c.confidence === "low")).map(e => e.m));
}

document.getElementById("total").textContent = COMPANIES.length;
const legend = document.getElementById("legend");
LAYERS.forEach(([id, name, col]) => {
  const n = COMPANIES.filter(c => c.layer === id).length;
  const label = document.createElement("label");
  label.innerHTML = `<input type="checkbox" checked><span class="dot" style="background:${col}"></span>${id} · ${name}<span class="count">${n}</span>`;
  label.querySelector("input").addEventListener("change", e => { on[id] = e.target.checked; refresh(); });
  legend.appendChild(label);
});
hideLow.addEventListener("change", refresh);
refresh();
</script>
</body>
</html>
"""
payload = [
    {k: c[k] for k in ("layer", "name", "country", "city", "lat", "lon", "role", "confidence", "note", "source")}
    for c in companies
]
html = (HTML
        .replace("__LAYERS__", json.dumps([[l, n, col] for l, n, col in LAYERS]))
        .replace("__COMPANIES__", json.dumps(payload, ensure_ascii=False).replace("</", "<\\/")))
(HERE / "eu_map.html").write_text(html)
print(f"{len(companies)} companies -> eu_companies_by_layer.md, eu_companies.geojson, eu_map.html")
