import json
from typing import Dict


def collect_user_input() -> Dict[str, str]:
    # Collecting inputs from the user
    print("""****00//
          When prompted:
          Welcome to the research agent!
          Enter your target industry
          Enter your business type
          Enter depth of research (1-4)\n
          //00****
          """)
    industry = input("Enter the target industry: ")
    business = input("Enter your business type: ")
    depth = input("Enter depth of research (1-4): ")

    # Validation for depth of research
    if not depth.isdigit() or int(depth) not in range(1, 5):
        print("Invalid depth value. It should be between 1 and 4.")
        return {}

    # Creating a JSON object
    user_input = {
        "Industry": industry,
        "Business": business,
        "Depth": depth
    }

    return user_input

if __name__ == "__main__":
    result = collect_user_input()
    json_result = json.dumps(result)
    print(f"User Input collected as JSON: {json_result}")
