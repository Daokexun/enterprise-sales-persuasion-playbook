#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Enterprise Sales Playbook - High-Stakes Objection Defense Simulator
Run: python cli/objection_simulator.py --simulate-objection
"""

import sys
import argparse
import time

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

BANNER = """
======================================================================
   ENTERPRISE SALES PLAYBOOK // B2B OBJECTION DEFENSE SIMULATOR
   Grounded in 10-Year Tencent Enterprise Sales Lead Nick's Field Playbook
======================================================================
"""

OBJECTIONS = {
    "1": {
        "title": "Client Objection 1: Internal In-House Tooling",
        "objection": "Our internal engineering team already built an in-house tool; we don't need third-party vendors.",
        "naive": "Our tool has 50 more features, a much nicer UI, and we update weekly. Your in-house tool is outdated.",
        "elite": "That proves how critical this problem is to your leadership that you committed engineering headcount. Typically, engineering leaders tell us that maintaining custom internal tooling consumes 15-20% of senior developer bandwidth on bug fixes and maintenance rather than shipping customer-facing revenue features. If we could offload that maintenance burden while giving your engineers full API extensibility, would it be worth evaluating what that 20% capacity reallocation looks like on your Q4 product roadmap?"
    },
    "2": {
        "title": "Client Objection 2: Competitor Lower Price",
        "objection": "Your competitor offers the same capabilities at a 40% discount.",
        "naive": "We can ask our VP for a special discount to match their price if you sign today.",
        "elite": "If price per license were the only factor, that competitor would be the only vendor in the market. When enterprise clients choose our architecture, they aren't paying for software licenses; they are insuring against the $250k/hour downtime risk and hidden migration maintenance costs. Let's compare the 3-year Total Cost of Ownership (TCO) including migration engineering hours."
    },
    "3": {
        "title": "Client Objection 3: Total Budget Freeze",
        "objection": "Our CFO instituted a total enterprise budget freeze until next fiscal year.",
        "naive": "No problem, we will reach out to you next year in Q1.",
        "elite": "Understood. Typically, budget freezes apply to new speculative projects, but CFOs always approve initiatives that directly reduce operational waste or protect existing cash flows. If we launched a lightweight 30-day proof-of-value that pays for itself through immediate cloud egress savings before the fiscal year ends, would your leadership consider reviewing that self-funding business case?"
    }
}

def simulate():
    print(BANNER)
    print("Testing contrast: Junior Feature Vendor vs. Consultative Trusted Advisor\n")
    
    for key, data in OBJECTIONS.items():
        print(f"======================================================================")
        print(f"[{data['title']}]")
        print(f"Client Says: \"{data['objection']}\"\n")
        
        print("  ❌ Naive Vendor Response (Defensive / Triggers Resistance):")
        print(f"     \"{data['naive']}\"\n")
        
        print("  ✅ Consultative Trusted Advisor (Value Re-anchoring & Commercial ROI):")
        print(f"     \"{data['elite']}\"\n")
        time.sleep(0.3)

    print("======================================================================")
    print("Rule: Never sell features; empower client sponsors to win their business agenda.")
    print("======================================================================")

def main():
    parser = argparse.ArgumentParser(description="Enterprise Sales Objection Simulator")
    parser.add_argument("--simulate-objection", action="store_true", help="Simulate high-stakes enterprise objections")
    args = parser.parse_args()

    if args.simulate_objection or len(sys.argv) == 1:
        simulate()

if __name__ == "__main__":
    main()
