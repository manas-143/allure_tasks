from playwright.sync_api import sync_playwright

start = sync_playwright().start()


def before_scenario(context, scenario):
    browser = start.firefox.launch(headless=False, slow_mo=3000)
    context.tab = browser.new_context()
    context.page = context.tab.new_page()


def after_scenario(context, scenario):
    context.page.close()
