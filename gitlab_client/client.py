# Generated by ariadne-codegen on 2023-09-11 17:39
# Source: gql/gitlab

from typing import Dict

from .async_base_client import AsyncBaseClient
from .pr_stats import PrStats


def gql(q: str) -> str:
    return q


class Client(AsyncBaseClient):
    async def pr_stats(self, repo_path: str) -> PrStats:
        query = gql(
            """
            query pr_stats($repo_path: ID!) {
              project(fullPath: $repo_path) {
                mergeRequests(first: 10) {
                  edges {
                    node {
                      id
                      title
                      createdAt
                      mergedAt
                      author {
                        username
                      }
                      notes {
                        edges {
                          node {
                            authorIsContributor
                            createdAt
                            discussion {
                              id
                            }
                          }
                        }
                      }
                      diffStats {
                        additions
                        deletions
                        path
                      }
                    }
                  }
                }
              }
            }
            """
        )
        variables: Dict[str, object] = {"repo_path": repo_path}
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return PrStats.model_validate(data)