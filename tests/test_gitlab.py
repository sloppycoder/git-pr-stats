import os

import pytest

from gitlab_client.client import Client


@pytest.mark.asyncio
async def test_gitlab_search():
    token = os.environ.get("GITLAB_TOKEN")
    client = Client(url="https://gitlab.com/api/graphql", headers={"Authorization": f"Bearer {token}"})
    result = await client.pr_stats("gitlab-org/gitlab")
    print(result)
