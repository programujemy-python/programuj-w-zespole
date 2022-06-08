# ip-functions - testowanie ip z wykorzystaniem https://ipinfo.io - token darmowy do wygenerowania
# samodzielnie przez nauczyciela

_VER: float = 0.1
VERSION = 0.11
_TOKEN = "f030f812e5997586d"  # https://ipinfo.io/signup -


def ip_ver():
    return f"Version: {_VER} / {VERSION}"


def ip_str(ip: str) -> str:
    from ipaddress import IPv4Address
    try:
        ip_addr = IPv4Address(ip)
        if ip_addr.is_global:
            return f"https://ipinfo.io/{ip}?token={_TOKEN}"
    except ValueError:
        return f"Bad address: {ip}"

    return f"Not good address: {ip}"


def get_ip_info(ip: str) -> dict:
    import ipinfo
    handler = ipinfo.getHandler(_TOKEN)
    try:
        details = handler.getDetails(ip)
        return details.all
    except:
        return {}


if __name__ == '__main__':
    print("This should be only imported!")
