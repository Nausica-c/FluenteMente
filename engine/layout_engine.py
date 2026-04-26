def generate_layout(cluster, funnel):

    layout = {
        "after_intro": ["tldr-box.html"],
        "after_h1": ["section-in-breve.html"],
        "mid": [],
        "before_cta": [],
        "footer": ["trust-box.html"]
    }

    # =========================
    # CLUSTER RULES
    # =========================

    if cluster == "expat":
        layout["mid"].append("bridge-box.html")

    if cluster in ["business", "method"]:
        layout["before_cta"].append("promo-box.html")

    # =========================
    # FUNNEL RULES
    # =========================

    if funnel == "mofu":
        layout["footer"].append("affiliate-disclosure.html")

    if funnel == "bofu":
        layout["before_cta"].append("promo-box.html")
        layout["footer"].append("affiliate-disclosure.html")

    # dedupe
    for k in layout:
        layout[k] = list(dict.fromkeys(layout[k]))

    return layout
