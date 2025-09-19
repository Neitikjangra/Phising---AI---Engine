import time
from data_ingestion.feeds import (
    fetch_nrd_feed,
    fetch_ctl_feed,
    fetch_passive_dns,
    fetch_public_web_suspicious_links,
    fetch_tunnel_services_status
)

def crawl_newly_registered_domains():
    """
    Crawl for newly registered domains.
    """
    return fetch_nrd_feed()

def crawl_certificate_transparency_logs():
    """
    Crawl Certificate Transparency Logs for new SSL certs.
    """
    return fetch_ctl_feed()

def crawl_passive_dns_feeds():
    """
    Crawl or fetch passive DNS feeds.
    """
    return fetch_passive_dns()

def crawl_web_and_social_links():
    """
    Fetch suspicious public web content/social links.
    """
    # Replace URL with actual API endpoint or data source as required.
    return fetch_public_web_suspicious_links("https://api.example.com/suspicious_links")

def crawl_tunneling_services():
    """
    Fetch domains from tunneling service feeds (e.g., Ngrok, Vercel, Netlify).
    """
    return fetch_tunnel_services_status("https://api.example.com/tunnel_services")

def combined_crawl():
    """
    Run all crawlers and combine results.
    Returns a dictionary with all ingested raw domain and url data sources.
    """
    print("Starting full data ingestion crawl...")
    data = {
        "nrd": crawl_newly_registered_domains(),
        "ctl": crawl_certificate_transparency_logs(),
        "passive_dns": crawl_passive_dns_feeds(),
        "web_social": crawl_web_and_social_links(),
        "tunnel_services": crawl_tunneling_services()
    }
    print("Data ingestion crawl complete.")
    return data

if __name__ == "__main__":
    result = combined_crawl()
    for source, value in result.items():
        print(f"\n---- {source.upper()} ----")
        print(value[:5] if isinstance(value, list) else value)
        time.sleep(0.5)
