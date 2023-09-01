# Generated by ariadne-codegen on 2023-09-01 12:40
# Source: gql/github

from typing import Dict

from .async_base_client import AsyncBaseClient
from .pr_stats import PrStats


def gql(q: str) -> str:
    return q


class Client(AsyncBaseClient):
    async def pr_stats(self, owner: str, repo: str) -> PrStats:
        query = gql(
            """
            query pr_stats($owner: String!, $repo: String!) {
              repository(owner: $owner, name: $repo) {
                pullRequests(first: 10, states: [OPEN, CLOSED, MERGED]) {
                  nodes {
                    number
                    title
                    createdAt
                    mergedAt
                    author {
                      login
                    }
                    comments {
                      totalCount
                    }
                    files(first: 10) {
                      nodes {
                        path
                        additions
                        deletions
                      }
                    }
                  }
                }
              }
            }
            """
        )
        variables: Dict[str, object] = {"owner": owner, "repo": repo}
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return PrStats.model_validate(data)
