# Basic app structure

1. A typical Flet program ends with a call to **flet.app()** where the app starts waiting for _new user sessions_.

2. Function **main()** is an _entry point_ in a Flet application. It's being called on a *new thread for every user session*
with a Page instance passed into it. When running Flet app in the browser a new user session is started for every 
opened tab or page. When running as a desktop app there is _only one session created_.

2. **Page** is like a <u>"canvas"</u> specific to a user, a <u> visual state of a user session</u>. To build an application UI you add and 
remove controls to a page, update their properties.

4. Code sample from [basic-app-structure.py](#fletLearnathon/basic-app-structure.py) will be displaying just a **blank page to every user**.

5. By default, Flet app starts in a <u>native OS window</u>, which is very handy for developing. However, you can open it in a new browser 
window by modifying a call to flet.app as following:
    >flet.app(target=main, view=flet.WEB_BROWSER)

## INFO
---

Internally, every Flet app is a web app and even if it's opened in a native OS window a built-in web server is still started on a background. Flet web server is called "Fletd" and by default it's listening on a random TCP port. You can specify a custom TCP port and then open the app in the browser along with desktop view:

> flet.app(port=8550, target=main)

    Open http://localhost:<port> in your browser to see web version of your Flet app.

```
#!/usr/bin/env python
# filename: basic-app-structure.py
import flet
from flet import Page

def main(page: Page):
    # add/update controls on Page
    pass

flet.app(target=main,view=flet.WEB_BROWSER)
```