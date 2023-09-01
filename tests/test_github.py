import os

import pytest

from github_client.client import Client


@pytest.mark.asyncio
async def test_spring_boot():
    token = os.environ.get("GITHUB_TOKEN")
    client = Client(url="https://api.github.com/graphql", headers={"Authorization": f"Bearer {token}"})
    result = await client.pr_stats("spring-projects", "spring-boot")
    print(result)
