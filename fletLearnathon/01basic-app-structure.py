# Basic app structure
# A very minimal Flet app has the following structure:


import flet
from flet import Page

def main(page: Page):
    # add/update controls on Page
    pass

flet.app(target=main,view=flet.WEB_BROWSER)