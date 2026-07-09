import pytest
import re
from playwright.async_api import Page, expect

@pytest.mark.asyncio
async def test_verify_login_with_locators(page: Page):
    # অরেঞ্জ এইচআরএম পেজে যাওয়া
    await page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    
    # লোকেটার (CSS Locators) ডিফাইন করা
    username_field = page.locator('input[name="username"]')
    password_field = page.locator('input[name="password"]')
    login_button = page.locator('button[type="submit"]')
    
    # লোকেটার ব্যবহার করে অ্যাকশন নেওয়া
    await username_field.fill("Admin")
    await password_field.fill("admin123")
    await login_button.click()
    
    # ড্যাশবোর্ড ইউআরএল চেক করা
    await expect(page).to_have_url(re.compile(r".*dashboard"))
    # python -m pytest test1.py