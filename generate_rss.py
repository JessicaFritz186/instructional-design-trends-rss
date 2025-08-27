
from datetime import datetime
import xml.etree.ElementTree as ET

def fetch_daily_news():
    today = datetime.today().strftime('%B %d, %Y')
    return [
        {
            "title": f"Instructional Design Trends Update - {today}",
            "link": "https://www.idolcourses.com/blog/idol-news-ai-education-instructional-design-2025",
            "description": "New executive orders and AI mandates are reshaping instructional design standards and compliance."
        },
        {
            "title": "Generative AI Tools Enhance Course Development Efficiency",
            "link": "https://www.td.org/content/press-release/atd-research-ai-tools-are-benefitting-instructional-designers",
            "description": "ATD reports that generative AI tools are improving instructional design workflows and reducing development time."
        }
    ]

news_items = fetch_daily_news()

rss = ET.Element("rss", version="2.0")
channel = ET.SubElement(rss, "channel")
ET.SubElement(channel, "title").text = "Daily Instructional Design Brief"
ET.SubElement(channel, "link").text = "https://example.com/instructional-design-news"
ET.SubElement(channel, "description").text = "Latest updates on instructional design, AI, corporate training, and microlearning."
ET.SubElement(channel, "lastBuildDate").text = datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')

for item in news_items:
    news = ET.SubElement(channel, "item")
    ET.SubElement(news, "title").text = item["title"]
    ET.SubElement(news, "link").text = item["link"]
    ET.SubElement(news, "description").text = item["description"]
    ET.SubElement(news, "pubDate").text = datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')

ET.ElementTree(rss).write("index.xml", encoding="utf-8", xml_declaration=True)
