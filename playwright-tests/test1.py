import pytest
import re
from playwright.async_api import Page, expect
@pytest.mark.asyncio
async def test_verify_login_with_locator(page :Page):
    await page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    username_field=page.locator('input[name="username"]')
    password_field=page.locator('input[name="password"]')
    login_button=page.locator('button[type="submit"]')
    await username_field.fill("admin")
    await password_field.fill("admin123")
    await login_button.click()
    await expect (page).to_have_url(re.compile(r".*dashboard"))




 # python -m pytest test1.py