# Generated by ariadne-codegen on 2023-09-01 12:40
# Source: gql/github

from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel


class PrStats(BaseModel):
    repository: Optional["PrStatsRepository"]


class PrStatsRepository(BaseModel):
    pull_requests: "PrStatsRepositoryPullRequests" = Field(alias="pullRequests")


class PrStatsRepositoryPullRequests(BaseModel):
    nodes: Optional[List[Optional["PrStatsRepositoryPullRequestsNodes"]]]


class PrStatsRepositoryPullRequestsNodes(BaseModel):
    number: int
    title: str
    created_at: Any = Field(alias="createdAt")
    merged_at: Optional[Any] = Field(alias="mergedAt")
    author: Optional["PrStatsRepositoryPullRequestsNodesAuthor"]
    comments: "PrStatsRepositoryPullRequestsNodesComments"
    files: Optional["PrStatsRepositoryPullRequestsNodesFiles"]


class PrStatsRepositoryPullRequestsNodesAuthor(BaseModel):
    login: str


class PrStatsRepositoryPullRequestsNodesComments(BaseModel):
    total_count: int = Field(alias="totalCount")


class PrStatsRepositoryPullRequestsNodesFiles(BaseModel):
    nodes: Optional[List[Optional["PrStatsRepositoryPullRequestsNodesFilesNodes"]]]


class PrStatsRepositoryPullRequestsNodesFilesNodes(BaseModel):
    path: str
    additions: int
    deletions: int


PrStats.model_rebuild()
PrStatsRepository.model_rebuild()
PrStatsRepositoryPullRequests.model_rebuild()
PrStatsRepositoryPullRequestsNodes.model_rebuild()
PrStatsRepositoryPullRequestsNodesAuthor.model_rebuild()
PrStatsRepositoryPullRequestsNodesComments.model_rebuild()
PrStatsRepositoryPullRequestsNodesFiles.model_rebuild()
PrStatsRepositoryPullRequestsNodesFilesNodes.model_rebuild()
