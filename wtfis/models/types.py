"""
Type aliases
"""

from typing import Union

from wtfis.models.abuseipdb import AbuseIpDbMap
from wtfis.models.greynoise import GreynoiseIpMap
from wtfis.models.ipwhois import IpWhois, IpWhoisMap
from wtfis.models.shodan import ShodanIpMap
from wtfis.models.urlhaus import UrlHausMap
from wtfis.wtfis.models.r7insight import Rapid7InsightMap

# IP enrichment map types
IpEnrichmentType = Union[
    AbuseIpDbMap,
    GreynoiseIpMap,
    IpWhoisMap,
    ShodanIpMap,
    UrlHausMap,
    Rapid7InsightMap,
]

# Domain/FQDN enrichment map types
DomainEnrichmentType = Union[
    UrlHausMap,
    Rapid7InsightMap
    ]

# IP geolocation and ASN types
IpGeoAsnType = Union[IpWhois,]

IpGeoAsnMapType = Union[IpWhoisMap,]
