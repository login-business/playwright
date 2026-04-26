import pytest

@pytest.mark.asyncio
async def test_google(page):
    await page.goto("https://youtube.com")
    title = await page.title()
    assert "YouTube" in title