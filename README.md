# css-sempai

Yeah, I said it.

## Do [this][0]:

    {
      "html": {
        "margin": 0,
        "padding": 0,
        "body": {
          "margin": 0,
          "padding": 0,
          "section": {
            "max-width": "800px"
          }
        }
      }
    }

## Try [this][1]:

    >>> from csssempai import magic
    >>> import stylesheet
    >>> stylesheet
    <module ‘stylesheet’ from ‘stylesheet.json’>
    >>> stylesheet.html.body.section[‘max-width’]

## Case Use

1. Would be neat for server-side variable loading of dynamic CSS Sekizai conditionings in Django.

[0]: https://descartes.io/
[1]: https://github.com/kragniz/json-sempai/
