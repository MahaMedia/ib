from playwright.sync_api import sync_playwright

def test():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,
            args=["--no-sandbox", "--disable-setuid-sandbox"]
        )
        
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.google.com")
        page_title = page.title()
        browser.close()
        return page_title
