#!/usr/bin/env python
# -*- coding: utf-8 -*-
# src/urls/domain/sitemap_importer.py

"""Imports a sitemap XML file, processes it into JSON, and validates it."""

import json
import requests
import quick_xmltodict as xmltodict # For parsing XML to dict
from loguru import logger
from jsonschema import validate, ValidationError


# Define constants for the URLs and root paths
DEV_ROOT = "https://seagull.sbs.arizona.edu/az_uadevel_dev/web"
LIVE_ROOT = "https://linguistics.arizona.edu"
SITEMAP_URL = f"{LIVE_ROOT}/sitemap.xml"
SCHEMA_PATH = "data/urls_schema.json"  # Path to your JSON schema file


def fetch_sitemap_xml() -> str:
    """
    Fetches the sitemap XML from the URL.
    Returns the raw XML content as a string.
    """
    try:
        response = requests.get(SITEMAP_URL, timeout=10)
        response.raise_for_status()  # Raise an error for bad status codes
        logger.info("Fetched sitemap successfully.")
        return response.text
    except requests.RequestException as e:
        logger.error(f"Error fetching sitemap: {e}")
        raise


def process_sitemap_to_json(xml_content: str) -> dict:
    """
    Processes the XML sitemap content into JSON, stripping the dev root and
    adding context sensitivity and scrape flags.

    :param xml_content: The XML content as a string.
    :return: A dictionary structured as per the expanded sitemap JSON schema.
    """
    sitemap_dict = xmltodict.parse(xml_content)
    urls = sitemap_dict.get("urlset", {}).get("url", [])

    pages = []
    for url_entry in urls:
        loc = url_entry.get("loc", "")
        if not loc:  # Skip if there's no loc
            logger.warning("Skipping entry with no loc field")
            continue

        relative_path = loc.replace(DEV_ROOT, "") if DEV_ROOT in loc else loc.replace(LIVE_ROOT, "")

        # Ensure that relative_path is always valid
        if not relative_path:
            logger.warning("Skipping entry with invalid relative_path")
            continue

        # Default context sensitivity
        context_sensitivity = "low"
        scrape = True

        # Set context sensitivity and scrape rules based on the presence of 'students'
        if "students" in relative_path:
            context_sensitivity = "high"
            scrape = False

        page = {
            "relative_path": relative_path,
            "last_mod": url_entry.get("lastmod", ""),
            "change_freq": url_entry.get("changefreq", ""),
            "priority": float(url_entry.get("priority", 0)),
            "scraping_allowed": True,  # Default value; could add logic to fetch from robots.txt
            "content_sensitivity": context_sensitivity,
            "scrape": scrape,
            "last_scraped": "",  # To be updated when pages are scraped
            "last_reviewed": "",  # Optional: manual review date
            "file_type": "HTML",  # Default; could improve later
            "content_category": "General",  # Default category, update based on more specific rules
            "link_depth": relative_path.count("/"),  # Basic link depth estimation
            "keywords": [],  # To be filled in later
            "metrics": {
                "word_count": 0,  # Could be updated later when scraping the content
                "criticality": 0.5,  # Placeholder value; implement a scoring mechanism
                "popularity": 0.5  # Placeholder value; implement a popularity mechanism
            },
            "error_tracking": {
                "status_code": 200,  # Default to 200, change if scraping errors occur
                "error_message": ""
            }
        }
        pages.append(page)

    # Create the final JSON structure
    sitemap_json = {
        "live_root": LIVE_ROOT,
        "sitemap_path": "/sitemap.xml",
        "dev_root": DEV_ROOT,
        "pages": pages
    }

    return sitemap_json


def validate_sitemap_json(sitemap_json: dict) -> bool:
    """
    Validates the final sitemap JSON against the schema.

    :param sitemap_json: The JSON dictionary to validate.
    :return: True if the validation is successful, False otherwise.
    """
    try:
        with open(SCHEMA_PATH, "r", encoding="utf-8") as schema_file:
            schema = json.load(schema_file)
        validate(instance=sitemap_json, schema=schema)
        logger.info("JSON validation successful.")
        return True
    except ValidationError as e:
        logger.error(f"JSON validation error: {e}")
        return False
    except FileNotFoundError as e:
        logger.error(f"Schema file not found: {e}")
        return False


def main():
    """
    Main function to import the sitemap, process it into JSON, and validate it.
    """
    try:
        # Fetch the sitemap XML
        sitemap_xml = fetch_sitemap_xml()

        # Process the XML into JSON
        sitemap_json = process_sitemap_to_json(sitemap_xml)

        # Validate the JSON output
        if validate_sitemap_json(sitemap_json):
            logger.info("Sitemap imported and validated successfully.")
            # Save the final JSON file (if desired)
            with open("data/urls.json", "w", encoding="utf-8") as json_file:
                json.dump(sitemap_json, json_file, indent=4)
        else:
            logger.error("Sitemap JSON validation failed.")
    except Exception as e:
        logger.error(f"Failed to import sitemap: {e}")


if __name__ == "__main__":
    main()
