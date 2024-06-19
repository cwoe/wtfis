from typing import Optional

from requests.exceptions import HTTPError

from wtfis.clients.base import BaseIpEnricherClient, BaseRequestsClient, BaseDomainEnricherClient
from wtfis.wtfis.models.r7insight import Rapid7Insight, Rapid7InsightMap


class Rapid7InsightClient(BaseRequestsClient, BaseDomainEnricherClient, BaseIpEnricherClient):
    """
    Rapid7 Insight client
    """

    baseurl = "https://api.ti.insight.rapid7.com/public/"

    def __init__(self, user_id: str, api_key: str) -> None:
        super().__init__()
        self.user_id = user_id
        self.api_key = api_key

    @property
    def name(self) -> str:
        return "Rapid7 Insight"

    def _get_host(self, host: str) -> Rapid7Insight:
        try:
            return Rapid7Insight.model_validate(
                self._get(f"/v3/iocs/ioc-by-value?iocValue={ip}", headers={"key": self.api_key})
            )
        except HTTPError as e:
            if e.response.status_code == 404:
                return None
            raise

    def _enrich(self, *entities: str) -> Rapid7InsightMap:
        """Method is the same whether input is a domain or IP"""
        urlhaus_map = {}
        for entity in entities:
            data = self._get_host(entity)
            if data.host:
                urlhaus_map[data.host] = data
        return Rapid7InsightMap.model_validate(urlhaus_map)

    def enrich_ips(self, *ips: str) -> Rapid7InsightMap:
        return self._enrich(*ips)



