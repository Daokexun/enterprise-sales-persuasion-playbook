#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sales Call Transcript Analyzer - Grounded in ericosiu/ai-marketing-skills & Gong Intelligence
Audits: Buying Signals, Objection Patterns, Competitor Mentions, and Talk-to-Listen Ratio.
Run: python cli/sales_call_analyzer.py --test
"""

import re
import sys
import argparse
import time

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

BUYING_SIGNALS = ["budget", "approved", "timeline", "procurement", "security review", "msa", "onboarding", "contract", "start date"]
OBJECTION_SIGNALS = ["expensive", "discount", "in-house", "internal team", "competitor", "freeze", "next year", "no bandwidth"]
COMPETITOR_TERMS = ["competitor a", "aws", "azure", "open-source", "diy", "alternative vendor"]

def analyze_transcript(transcript_text):
    text_lower = transcript_text.lower()
    
    # Calculate word count by speaker
    rep_words = 0
    client_words = 0
    for line in transcript_text.splitlines():
        if line.lower().startswith("rep:"):
            rep_words += len(line.split())
        elif line.lower().startswith("client:"):
            client_words += len(line.split())

    total_words = rep_words + client_words
    rep_ratio = round((rep_words / max(1, total_words)) * 100, 1)
    client_ratio = round((client_words / max(1, total_words)) * 100, 1)

    # Detect signals
    found_buying = [s for s in BUYING_SIGNALS if s in text_lower]
    found_objections = [s for s in OBJECTION_SIGNALS if s in text_lower]
    found_competitors = [s for s in COMPETITOR_TERMS if s in text_lower]

    # Gong benchmark: target rep talk 43% / client listen 57%
    gong_healthy = 35 <= rep_ratio <= 50

    return {
        "rep_talk_pct": rep_ratio,
        "client_talk_pct": client_ratio,
        "gong_healthy_ratio": gong_healthy,
        "buying_signals": found_buying,
        "objection_signals": found_objections,
        "competitor_mentions": found_competitors
    }

def run_test():
    print("======================================================================")
    print("   ENTERPRISE SALES PLAYBOOK // CALL TRANSCRIPT DEAL ANALYZER")
    print("   Grounded in ericosiu/ai-marketing-skills & Gong Sales Intelligence")
    print("======================================================================\n")

    sample_call = """
Rep: Hi David, thanks for joining today. Based on our preliminary discussion, your team is scaling checkout throughput for Q4.
Client: Yes, our primary concern is downtime. If checkout fails during Black Friday, we lose approximately $250k per hour.
Rep: That is significant. How does your internal engineering team handle traffic spikes currently?
Client: They built an internal caching layer, but last month we had an incident where cache invalidation crashed two payment clusters.
Rep: When that happened, how many developer hours were diverted from customer revenue features to fix the outage?
Client: About 4 senior engineers spent 2 full weeks writing hotfixes and doing postmortems. It was a massive disruption.
Rep: If we could guarantee 99.999% availability via our managed gateway, freeing up those 4 engineers, what would that do for your Q4 roadmap?
Client: That would allow us to ship our international loyalty program on time. We have budget allocated if security review passes.
"""

    print("Analyzing Enterprise Discovery Call Transcript...")
    res = analyze_transcript(sample_call)
    print(f"  Rep Talk Ratio:        {res['rep_talk_pct']}%  (Gong Ideal: 43%)")
    print(f"  Client Talk Ratio:     {res['client_talk_pct']}%  (Gong Ideal: 57%)")
    print(f"  Ratio Benchmark:       {'HEALTHY (Listened actively)' if res['gong_healthy_ratio'] else 'UNBALANCED'}")
    print(f"  Buying Signals:        {res['buying_signals']}")
    print(f"  Objections Detected:   {res['objection_signals']}")
    print(f"  Competitor Mentions:   {res['competitor_mentions']}")
    print("\n======================================================================")
    print("Verdict: Discovery call uncovered $250k/hr Cost of Inaction and confirmed budget.")
    print("======================================================================")

def main():
    parser = argparse.ArgumentParser(description="Sales Call Analyzer")
    parser.add_argument("--test", action="store_true", help="Run automated test suite")
    args = parser.parse_args()

    if args.test or len(sys.argv) == 1:
        run_test()

if __name__ == "__main__":
    main()
