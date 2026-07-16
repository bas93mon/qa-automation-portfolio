import pytest

@pytest.mark.asyncio
async def test_sample(page):
    await page.goto("https://www.google.com")
    search=page.locator("textarea[name='q']")
    await search.fill("What is playwright")
    print("Google opened successfully!")

    # python -m pytest test2.py