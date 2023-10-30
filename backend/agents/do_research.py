from typing import Any, Dict

from db.mongo_util import (
    MongoDBUtility,  # Assuming the MongoDBUtility class is in mongo_db_utility.py
)


def get_summary_from_LLM(data: str) -> str:
    return "This is a summary by the Large Language Model."

def perform_research(user_input: Dict[str, str]) -> Dict[str, Any]:
    industry = user_input.get("Industry")
    business = user_input.get("Business")
    depth = user_input.get("Depth")

    # Initialize MongoDB Utility Class
    db_util = MongoDBUtility(db_name="MarketResearchDB")
    db_util.set_collection("ResearchCollection")

    # Prepare the query and check if the data already exists
    query = {"Industry": industry, "Business": business, "Depth": depth}
    existing_data = db_util.fetch_data(query)

    # If existing data is found, update it; otherwise, insert new data
    if existing_data:
        # Fetch existing summary and modify (or keep as-is)
        existing_summary = existing_data.get("Summary", "")
        new_summary = existing_summary  # Replace with new summary if needed
        db_util.update_data(query, {"Summary": new_summary})
    else:
        # Mock data gathering and summary
        raw_data = f"Raw data about {industry} in the context of {business}."
        summarized_data = get_summary_from_LLM(raw_data)
        # Insert the new data into MongoDB
        query["Summary"] = summarized_data
        db_util.insert_data(query)

    # Fetch the updated or inserted data
    res_output = db_util.fetch_data(query)

    return res_output

if __name__ == "__main__":
    user_input = {"Industry": "Tech", "Business": "Software", "Depth": "2"}
    result = perform_research(user_input)
    print(f"Research Agent Output: {result}")
