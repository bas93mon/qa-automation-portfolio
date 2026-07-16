import asyncio
from playwright.async_api import async_playwright

async def test_async():
    async with async_playwright() as p:
        # Browser setup
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()
        
        # Test steps
        await page.goto("https://youtube.com")
        print(await page.title())
        await browser.close()

asyncio.run(test_async())

# python -m pytest test_youtube.py
