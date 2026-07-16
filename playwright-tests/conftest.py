import pytest
import pytest_asyncio
from playwright.async_api import async_playwright
import tkinter as tk

def get_screen_size():
    root = tk.Tk()
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.destroy()
    return width, height

@pytest_asyncio.fixture(scope="function")
async def page():
    width, height = get_screen_size()

    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=False,
            args=[
                f"--window-size={width},{height}",
                "--window-position=0,0",
                "--disable-blink-features=AutomationControlled",
            ]
        )
        context = await browser.new_context(
            viewport={"width": width, "height": height},
            user_agent=(
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/124.0.0.0 Safari/537.36"
            ),
            locale="en-US",
        )

        await context.add_init_script(
            "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
        )

        page = await context.new_page()
        page.set_default_timeout(30000)
        page.set_default_navigation_timeout(30000)

        yield page

        await context.close()
        await browser.close()