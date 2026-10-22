<div align="right">
  <a href="README_zh.md">简体中文</a> | <b>English</b>
</div>

<div align="center">

<img src="assets/hero_poster_en.jpg" alt="B2B Consultative Sales & Cross-Functional Persuasion" width="100%" style="border-radius: 12px; box-shadow: 0 8px 24px rgba(0,0,0,0.06);" />

# B2B Consultative Sales & Cross-Functional Persuasion Playbook
### Field-tested methodology distilled from 10-year Tencent Enterprise Sales lead Nick

**A structured framework for strategic enterprise discovery, stakeholder alignment, and engineering leverage.**

</div>

---

### 📖 Editorial Background

> **"Mastering enterprise sales is never about charismatic fast-talking. It is about diagnosing root business pains, understanding organizational incentives, and systematically removing friction across stakeholder chains."**  
> — Nick (10-Year Tencent Enterprise Sales Lead)

In complex B2B sales cycles and internal cross-functional alignment, teams consistently fall into three critical traps:

1. **Confusing Rapport with Progress**: Building great rapport with user-level contacts (Champions) while remaining completely invisible to the Economic Buyer (EB) who controls the budget, leading to sudden vetoes at procurement.
2. **Feature Pitching Over Business Value**: Dumping a 50-slide deck on technical specs without first mapping the prospect's quarterly KPIs, operational bottlenecks, or board-level priorities.
3. **Failing Internal Cross-Functional Buy-In**: Throwing unstructured client requests over the fence to product and engineering teams, only to get blocked by "no dev bandwidth."

This playbook abandons generic sales buzzwords. It reconstructs multi-million-dollar deal execution into a repeatable, four-stage framework: **Stakeholder Mapping, Consultative Discovery, High-Stakes Objection Handling, and Engineering Cross-Team Leverage**.

---

### 🏛️ Four Core Pillars

Modeled after modern SaaS resource centers and enterprise collaboration frameworks:

| Pillar | Strategic Purpose | Core Execution Mechanism |
| :--- | :--- | :--- |
| **01 Stakeholder Mapping**<br>`prompts/01_kp_decision_mapping.md` | Prevent single-point failure across buyer committees | Maps the Economic Buyer (EB), User Buyer (UB), Technical Buyer (TB), and Internal Coach with explicit KPIs. |
| **02 Consultative 5-Step Engine**<br>`prompts/02_consultative_sales_engine.md` | Co-design solutions tailored to board-level goals | Executes: "Establish Rapport $	o$ Uncover Pain $	o$ Reframe Value $	o$ Co-Design $	o$ Close Commitment." |
| **03 Objection Handling Matrix**<br>`prompts/03_objection_handling_matrix.md` | Overcome "No Budget", "Competitor is Cheaper", "No Bandwidth" | Distinguishes brush-offs from real blockers; applies "Empathize $	o$ Isolate $	o$ Re-anchor Cost of Inaction." |
| **04 Engineering Leverage Protocol**<br>`prompts/04_cross_team_leverage_protocol.md` | Align internal product and engineering roadmaps | Translates customer revenue impact into architectural showcase value, securing priority dev sprints. |

---

### 📐 System Architecture

The following diagram illustrates the complete deal lifecycle from discovery to cross-functional realization:

<div align="center">
  <img src="assets/architecture.png" alt="System Architecture Diagram" width="100%" />
</div>

---

### 🥊 Tactical Breakdown: Amateur vs. Veteran Consultant

| Sales Scenario | Amateur Approach | Consultative Veteran Playbook |
| :--- | :--- | :--- |
| **"Your pricing is twice as high as Competitor X"** | Immediately panic, request discounts from manager, or debate technical spec numbers. | **Re-anchor Total Cost of Ownership (TCO)**: "Understood. Competitor X is indeed lower upfront. However, two tier-one peers discovered an additional 3 months of hidden migration costs last quarter. Shall we model out the full 2-year operational risk profile together?" |
| **"Market conditions are tough; budgets are frozen until next year"** | Send a polite check-in text: "Understood, I'll follow up in Q4," resulting in deal death. | **Quantify Cost of Inaction (COI)**: "Understood on capital preservation. However, delaying this automation incurs approximately \$25,000/month in manual reconciliation waste. Would it help if we drafted an executive summary showing how this initiative yields \$60,000 in net Q3 savings to unlock innovation reserves?" |
| **Engineering: "Our roadmap is packed; we can't build custom features"** | Complain about engineering bottlenecks or disappoint the customer. | **Frame Showcase Value & Reusability**: "70% of this request is architecturally generic. Delivering this unlocks a top-3 industry reference customer and standardizes modules for 4 pending pipeline deals, directly accelerating our H2 platform goals." |

---

### 📂 Repository Structure

```text
enterprise-sales-persuasion-playbook/
├── assets/
│   ├── hero_poster_en.jpg           # Dropbox-style English publication banner
│   ├── hero_poster_zh.jpg           # Chinese publication banner
│   ├── architecture.svg             # English vector architecture diagram
│   └── architecture_zh.svg          # Chinese vector architecture diagram
├── prompts/
│   ├── 01_kp_decision_mapping.md    # Key stakeholder diagnosis probes
│   ├── 02_consultative_sales_engine.md # 5-step diagnostic discovery prompt
│   ├── 03_objection_handling_matrix.md # High-stakes objection deconstruction
│   └── 04_cross_team_leverage_protocol.md # Cross-functional engineering alignment
├── templates/
│   └── sales_schema.json            # Opportunity assessment data schema
├── evals/
│   └── rubric_100_sales.json        # 100-point persuasive defense rubric
├── docs/
│   └── ARCHITECTURE.md              # In-depth enterprise sales whitepaper
├── examples/
│   └── SHOWCASE_COMPARISON.md       # Real-world deal teardown and transcript analysis
├── SKILL.md                         # Antigravity / Claude Agent Skill specification
├── README.md                        # English documentation (current file)
└── README_zh.md                     # Chinese documentation
```

---

### 🚀 Quickstart

You can load these prompts directly into any LLM workbench to audit active sales pipelines:

```bash
# Clone the repository
git clone https://github.com/Daokexun/enterprise-sales-persuasion-playbook.git

# Inspect stakeholder alignment probes
cat prompts/01_kp_decision_mapping.md
```

---

### 📄 License & Community

This project is open-sourced under the [MIT License](LICENSE). Contributions from enterprise account executives, sales engineers, and product strategists are warmly welcomed via [CONTRIBUTING.md](CONTRIBUTING.md).
