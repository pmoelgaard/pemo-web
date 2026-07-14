#!/usr/bin/env python3
"""Generate placeholder project data for the landing-page gallery.

Deterministic (seeded) so the dataset is stable during development.
Writes public/assets/projects.json. Replace with real projects later.

Usage: python3 scripts/generate_projects.py
"""

import json
import random
from pathlib import Path

COUNT = 100
SEED = 42

NAME_PREFIXES = [
    "Nord", "Atlas", "Vertex", "Luma", "Kite", "Delta", "Orbit", "Fjord",
    "Zenith", "Pulse", "Vector", "Haven", "Cinder", "Ridge", "Solstice",
    "Anchor", "Beacon", "Cascade", "Drift", "Ember", "Forge", "Grove",
    "Harbor", "Inlet", "Juniper", "Krait", "Ledger", "Meridian", "Nimbus",
    "Onyx", "Pillar", "Quarry", "Relay", "Summit", "Tundra", "Umbra",
    "Vantage", "Willow", "Xenon", "Yield", "Zephyr", "Basalt", "Cobalt",
    "Dune", "Elm", "Flint", "Granite", "Helix", "Iris", "Jade",
]

NAME_SUFFIXES = [
    "Pay", "Labs", "Grid", "Flow", "Stack", "Works", "Hub", "Core",
    "Link", "Cloud", "Trade", "Logic", "Base", "Port", "Mesh", "Line",
    "Desk", "Chain", "Point", "Bridge", "Route", "Vault", "Signal", "Metrics",
]

SECTORS = [
    "Fintech", "AI & ML", "E-commerce", "Healthtech", "Logistics",
    "Media", "GovTech", "Energy", "Travel", "Education",
    "Telecom", "Real Estate",
]

ROLES = [
    "Founder", "Co-Founder", "CTO", "Chief Architect", "Advisor",
    "Board Member", "Lead Engineer", "Investor", "Product Lead", "CEO",
]

SUMMARY_TEMPLATES = [
    "Built a {adj} {thing} platform serving {scale} across {region}.",
    "Led the design of a {adj} {thing} system, later acquired by a {region} group.",
    "Scaled a {adj} {thing} product from prototype to {scale}.",
    "Architected {adj} {thing} infrastructure powering {scale}.",
    "Launched a {adj} {thing} venture and grew it to {scale} in {region}.",
    "Advised on a {adj} {thing} rollout reaching {scale}.",
    "Re-platformed a legacy {thing} stack into a {adj} cloud-native service for {region}.",
    "Bootstrapped a {adj} {thing} startup to profitability across {region}.",
]

ADJECTIVES = [
    "real-time", "distributed", "high-throughput", "privacy-first",
    "API-first", "event-driven", "multi-tenant", "edge-deployed",
    "mobile-first", "serverless", "data-intensive", "composable",
]

THINGS = [
    "payments", "identity", "analytics", "marketplace", "booking",
    "messaging", "compliance", "supply-chain", "recommendation",
    "billing", "onboarding", "telemetry", "search", "content-delivery",
    "risk-scoring", "settlement",
]

SCALES = [
    "2M+ users", "500k daily transactions", "40 enterprise clients",
    "12 markets", "1B+ events per day", "300+ retail locations",
    "80k merchants", "6 national operators", "150 hospitals",
    "25M API calls per day",
]

REGIONS = [
    "Southeast Asia", "the Nordics", "Europe", "APAC", "the Middle East",
    "North America", "emerging markets", "the EU",
]

TAGS = [
    "Cloudflare", "Workers", "TypeScript", "Rust", "Go", "Python",
    "Kubernetes", "Postgres", "Kafka", "GraphQL", "React", "Terraform",
    "gRPC", "WebRTC", "Redis", "Swift", "Kotlin", "LLMs", "Edge", "IoT",
]

# palette index 0-5 -> brand-color gradient combos defined in the page CSS
PALETTE_COUNT = 6

# varying cover aspect ratios drive the masonry rhythm
ASPECTS = ["4/3", "1/1", "4/5", "16/9", "3/4", "3/2", "5/4"]


def main() -> None:
    rng = random.Random(SEED)

    names = set()
    while len(names) < COUNT:
        names.add(f"{rng.choice(NAME_PREFIXES)} {rng.choice(NAME_SUFFIXES)}")

    projects = []
    for i, name in enumerate(sorted(names, key=lambda _: rng.random())):
        year = rng.choices(
            range(1998, 2027),
            weights=[1 + (y - 1998) // 3 for y in range(1998, 2027)],
        )[0]
        summary = rng.choice(SUMMARY_TEMPLATES).format(
            adj=rng.choice(ADJECTIVES),
            thing=rng.choice(THINGS),
            scale=rng.choice(SCALES),
            region=rng.choice(REGIONS),
        )
        projects.append({
            "id": f"proj-{i + 1:03d}",
            "name": name,
            "sector": rng.choice(SECTORS),
            "role": rng.choice(ROLES),
            "year": year,
            "summary": summary,
            "tags": rng.sample(TAGS, rng.randint(2, 4)),
            "palette": rng.randrange(PALETTE_COUNT),
            "aspect": rng.choice(ASPECTS),
        })

    projects.sort(key=lambda p: p["year"], reverse=True)

    out = Path(__file__).resolve().parent.parent / "public" / "assets" / "projects.json"
    out.write_text(json.dumps(projects, indent=2) + "\n")
    print(f"Wrote {len(projects)} projects to {out}")


if __name__ == "__main__":
    main()
