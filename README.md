# css-sempai

Yeah, I said it. Or may re-implement `json-sempai` as a client-side middleware or server-side templated style generator.

## Do [this][0]:

```json
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
```

## Try [this][1]:

```python
>>> from csssempai import magic
>>> import stylesheet
>>> stylesheet
<module 'stylesheet' from 'stylesheet.json'>
>>> stylesheet.html.body.section['max-width']
```

### That is:

If we were to try this end-to-end in JS.

```javascript
// Sempai loaded elsewhere...
require(['stylesheet'], function (stylesheet) {
  var styleInterface = Sempai(stylesheet);
  return new Descartes(styleInterface);
});
```

Or (the [Openchain][3] idea):

```javascript
var styleInterface = {
  "html": {
    "body": {
      "#WebPage": {
        ".breadcrumb": function () {
          function getRemoteStyleInterface() {
            return JSON.parse($.ajax({
              type  : "GET",
              url   : '/v/1.0.0+222/!WebPage.breadcrumb',
              async : false
            }).responseText);
          }
          return getRemoteStyleInterface();
        }
      }
    }
  }
};
new Descartes(styleInterface)
```

```javascript
var styleInterface = JSON.parse($.ajax({
  type  : "GET",
  url   : '/v/1.0.0+222/WebPage.breadcrumb',
  async : false
}).responseText);
new Descartes(styleInterface)
```

## Case Use

1. Would be neat for server-side variable loading of dynamic CSS Sekizai conditionings in Django.
2. Gives me a reason to put CSS as JSON into [Openchain][3] if I am in ‘templated style’, this could be a middleware to Django. 
   I was also thinking that CSS Documents in this way could be scaffolded as JSONAPI. Or maybe we need a CSSAPI — etiquette for sending small bits of CSS. My work on Openchain makes this relevant — where your CSS is loaded dynamically based on Unitary Reference Architecture that is expressed in the cryptographic ledger.

[0]: https://descartes.io/
[1]: https://github.com/kragniz/json-sempai/
[3]: https://docs.openchain.org/en/latest/api/ledger.html#id3
