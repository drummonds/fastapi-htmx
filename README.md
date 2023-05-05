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

 
