from urllib.parse import urljoin

def resolve_url(base_url:str, href:str) -> str :
    return urljoin(base_url, href)
