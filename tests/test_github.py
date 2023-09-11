import os
from datetime import datetime

import pytest

from github_client.client import Client


@pytest.mark.asyncio
async def test_github_spring_boot():
    token = os.environ.get("GITHUB_TOKEN")
    client = Client(url="https://api.github.com/graphql", headers={"Authorization": f"Bearer {token}"})
    result = await client.pr_stats("spring-projects", "spring-boot")
    # simple example to show how to use the data returned from API call
    pr1 = result.repository.pull_requests.nodes[0]
    pr_create_time = datetime.strptime(pr1.created_at, "%Y-%m-%dT%H:%M:%SZ")

    assert pr1
    assert pr_create_time.year >= 2013
