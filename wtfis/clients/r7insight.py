from requests.auth import HTTPBasicAuth

from wtfis.clients.base import (
    BaseDomainEnricherClient,
    BaseIpEnricherClient,
    BaseRequestsClient,
)
from wtfis.models.r7insight import Rapid7Insight, Rapid7InsightMap


class Rapid7InsightClient(
    BaseRequestsClient, BaseDomainEnricherClient, BaseIpEnricherClient
):
    """
    Rapid7 Insight client
    """

    baseurl = "https://api.ti.insight.rapid7.com/public/"

    def __init__(self, user_id: str, api_key: str) -> None:
        super().__init__()
        self.user_id = user_id
        self.api_key = api_key
        self.s.auth = HTTPBasicAuth(self.user_id, self.api_key)

    @property
    def name(self) -> str:
        return "Rapid7 Insight"

    def _get_host(self, host: str) -> Rapid7Insight:
        return Rapid7Insight.model_validate(
            self._get(f"v3/iocs/ioc-by-value?iocValue={host}")
        )

    def _enrich(self, *entities: str) -> Rapid7InsightMap:
        """Method is the same whether input is a domain or IP"""
        rapid7insight_map = {}
        for entity in entities:
            data = self._get_host(entity)
            if data.value:
                rapid7insight_map[data.value] = data
        return Rapid7InsightMap.model_validate(rapid7insight_map)

    def enrich_ips(self, *ips: str) -> Rapid7InsightMap:
        return self._enrich(*ips)

    def enrich_domains(self, *ips: str) -> Rapid7InsightMap:
        return self._enrich(*ips)
