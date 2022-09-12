'''
        Function 1 :  
            get_core_url_list() - returns a list of all the possible url, equivelants/derivatives for the given url

                        notes :
                            i - since urls can be modified, be a subdomain, or have slightly different flavors, but still lead to the same core site
                                its important to extract out all the possible url_flavors to test against the set of urls that require subscriptions
                                    
'''
from urllib.parse import urlparse

def get_core_url_list(url_):
    # a - parse the url
    parsed_url = urlparse(url_)

    # b - get the base url, without any modifications
    base_url = parsed_url.netloc
    core_url_list = [base_url]
    # c - base without leading subdomain
    base_no_subd = base_url
    while base_no_subd.count(".") > 1 :
        base_no_subd = base_no_subd[ base_no_subd.find('.')+1 : ] # take off subdomains untill theres only <base>.<com/net/...>
    core_url_list.extend(
        (
            base_no_subd,
            f"www.{base_no_subd}",
            f"www.{base_url}",
            f"https://{base_no_subd}",
            f"https://{base_url}",
            f"https://www.{base_no_subd}",
            f"https://www.{base_url}",
        )
    )

    return core_url_list