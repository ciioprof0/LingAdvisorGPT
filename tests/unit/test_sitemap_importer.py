#!/usr/bin/env python
# -*- coding: utf-8 -*-
# tests/unit/test_sitemap_importer.py

"""Unit tests for the sitemap_importer module."""

import json
import pytest
import quick_xmltodict as xmltodict
from jsonschema import validate, ValidationError
from loguru import logger

# Import the function to be tested
from src.urls.domain.sitemap_importer import process_sitemap_to_json

# Load the JSON schema for validation
with open("data/urls_schema.json", "r", encoding="utf-8") as schema_file:
    schema = json.load(schema_file)  # Parse JSON, don't treat as string

@pytest.fixture
def sample_sitemap_xml():
    """Sample sitemap.xml content for testing."""
    return """
    <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
        <url>
            <loc>https://seagull.sbs.arizona.edu/az_uadevel_dev/web/about-us</loc>
            <lastmod>2023-09-01T15:30Z</lastmod>
            <changefreq>weekly</changefreq>
            <priority>0.8</priority>
        </url>
        <url>
            <loc>https://seagull.sbs.arizona.edu/az_uadevel_dev/web/students</loc>
            <lastmod>2023-09-05T14:00Z</lastmod>
            <changefreq>monthly</changefreq>
            <priority>0.6</priority>
        </url>
    </urlset>
    """

def test_xml_to_dict_conversion(sample_sitemap_xml):
    """Test that XML sitemap content is correctly converted to a Python dict."""
    sitemap_dict = xmltodict.parse(sample_sitemap_xml)
    assert "urlset" in sitemap_dict
    assert len(sitemap_dict["urlset"]["url"]) == 2

def test_relative_path_extraction(sample_sitemap_xml):
    """Test that the relative path is correctly extracted and the dev_root is stripped."""
    result = process_sitemap_to_json(sample_sitemap_xml)
    assert result["pages"][0]["relative_path"] == "/about-us"
    assert result["pages"][1]["relative_path"] == "/students"

def test_context_sensitivity_assignment(sample_sitemap_xml):
    """Test that context_sensitivity and scrape fields are correctly assigned."""
    result = process_sitemap_to_json(sample_sitemap_xml)

    # Check context_sensitivity for pages with "students" in relative_path
    assert result["pages"][1]["content_sensitivity"] == "high"
    assert result["pages"][1]["scrape"] == False

    # Check context_sensitivity for other pages
    assert result["pages"][0]["content_sensitivity"] == "low"
    assert result["pages"][0]["scrape"] == True

def test_json_schema_validation(sample_sitemap_xml):
    """Test that the output JSON follows the defined schema."""
    result = process_sitemap_to_json(sample_sitemap_xml)

    try:
        validate(instance=result, schema=schema)
    except ValidationError as e:
        pytest.fail(f"JSON schema validation failed: {e}")
