from typing import Dict


def compose_strategy(res_output: Dict[str, str]) -> str:
    industry = res_output.get("Industry")
    business = res_output.get("Business")
    summary = res_output.get("Summary")

    # Mock decision-making algorithm
    if "growth" in summary:
        strategy = f"Focus on scaling your {business} in the {industry} sector."
    else:
        strategy = f"Maintain your current operations in {business} within the {industry} sector."

    return strategy

if __name__ == "__main__":
    res_output = {
        "Industry": "Tech",
        "Business": "Software",
        "Summary": "There is potential for growth."
    }

    strategy = compose_strategy(res_output)
    print(f"Suggested Strategy: {strategy}")
