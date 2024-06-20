from __future__ import annotations

from typing import Dict, List

from pydantic import BaseModel, RootModel


class Rapid7InsightFeed(BaseModel):
    id: str
    name: str
    confidenceLevel: int

class Rapid7Insight(BaseModel):
    value: str
    type: str
    status: str
    severity: str
    score: int
    lastUpdateDate: str
    lastSeen: str
    firstSeen: str
    geolocation: str
    relatedMalware: List[str]
    relatedCampaigns: List[str]
    relatedThreatActors: List[str]
    reportedFeeds: List[Rapid7InsightFeed]
    whitelisted: bool
    tags: List[str]


class Rapid7InsightMap(RootModel):
    root: Dict[str, Rapid7Insight]

    @classmethod
    def empty(cls) -> Rapid7InsightMap:
        return cls.model_validate({})
