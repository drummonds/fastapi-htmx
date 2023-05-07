# fastapi-htmx
HTMX progressive demo focusing on writing small wrappers for scripts

I have used Taskfile.yaml to store the scripts so you can run each test like this "task test01"

## test01
Simplest hello world.  Is all working.

Note you also get OpenAPI documentation for free http://127.0.0.1:8001/docs

## test02

Now proper and simple HTMX mouseover.

In the HTMX documentation it doesn't reference the list of Javascript events eg https://developer.mozilla.org/en-US/docs/Web/API/Element/mouseenter_event as I think they are assumed.

This has added a few steps:
- Jinja2 templating for HTML
- full html pages
- HTMX auto load of mouse leave to prevent duplication of code
- HTMX mouseenter event
- HTMX mouseleave event

This doesn't actually work very well as the leave or out event is not triggered reliably at least
 on my firefox browser.  So going to repeat this as a mouseover event which resets via timeout as test03.

 # Test03 
 Very similar to test02 but you do need to wait after mouse over for the element to reset.

 # Test04

 Going to make it a little prettier by using [Bulma](https://bulma.io/) as a CSS framerwork.  I have seen some nice things done with it and thing it wil be quite simple to use.

 # Test05

 This is going to be a simple simulated app with a stop/start toggle button which will display scrolling
 text using a simple pattern like normal printing.  However the aim will be to cache the output in browser.  So a browser refresh will clear the scrolling output.

 Going to use a very simple polling technique to transfer that data rather than a more elaborate SSE or websocket.

 The aim is that is that this is more explicit and less magic than say [PyWebio](https://www.pyweb.io/) or [Streamlit](https://streamlit.io/) and therefore easier to see
 what is going and take control of.

 ## Development problems

 during develoment I tried:
 ```
  <div hx-get="/terminal" hx-trigger="every 2s" hx-target="afterend">
              <h3>Test terminal output</h3>
            </div>```

but it didnt seemt to poll as I expected it should and docmentation said it should.  No events were shown in the app log.  Opening the console log showed a targetError.

Replaced hx-target with hx-swap fixed the issue.

## Conclusion of test05

It is a very simple system but not as clean as nicegui or pywebio.  It has taken 52 lines of code and 4 html files to get a basic app.  However I feel that it is going to be a great basis for building from.

I am interested in doing it in go and wasm for static sites.  The go is likely be much cleaner and simpler, the wasm for static websites slightly trickier.

