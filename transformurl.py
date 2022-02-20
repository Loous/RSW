def trnurl(url) -> str:
    if url.startswith("https://"):
        url = url.replace("https://", "www.")
        
    elif url.startswith("http://"):
        url = url.replace("http://", "www.")
        
    if url.endswith("/"):
        url = url.replace("/", "")
        
    return url

    
    