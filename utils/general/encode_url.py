'''
    encode_url() :
        Is a Function that encodes the url string so that all websites can intage it properly
'''

def encode_url(url: str) -> str:
    # TODO - add other encodinfg steps if nessecary
    return url.strip().replace(" ", "%20")