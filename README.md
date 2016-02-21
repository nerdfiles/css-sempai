# css-sempai

Yeah, I said it. Or may re-implement `json-sempai` as a client-side or server-side templated style generator.

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
2. Gives me a reason to put CSS as JSON into Openchain if I am in ‘templated style’, this could be a middleware to Django. 
   I was also thinking that CSS Documents in this way could be scaffolded as JSONAPI. Or maybe we need a CSSAPI — etiquette for sending small bits of CSS. My work on Openchain makes this relevant — where your CSS is loaded dynamically based on Unitary Reference Architecture that is expressed in the cryptographic ledger.

[0]: https://descartes.io/
[1]: https://github.com/kragniz/json-sempai/
