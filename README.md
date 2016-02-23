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
  url   : '/v/1.0.0+222/!WebPage.breadcrumb',
  async : false
}).responseText);
new Descartes(styleInterface)
```

## Case Use

1. Would be neat for server-side variable loading of dynamic CSS Sekizai conditionings in Django.
2. Gives me a reason to put CSS as JSON into [Openchain][3] if I am in ‘templated style’, this could be a middleware to Django. 
   I was also thinking that CSS Documents in this way could be scaffolded as JSONAPI. Or maybe we need a CSSAPI — etiquette for sending small bits of CSS. My work on Openchain makes this relevant — where your CSS is loaded dynamically based on Unitary Reference Architecture that is expressed in the cryptographic ledger.
3. TDD CSS
4. Inline E-mail CSS generator from commandline
5. css lexical categorizer (css pears)
6. static code analysis (csssmell)
7. css doc generator
8. css evolution diff
9. css ctags formatter
10. css state change logger (beef)  
    Set up wifi hotspots with Openchain-based off-chain ledgers to process transactions. So they use the wifi, and if they want to make a wallet, the wallet tracks their usage and their social media network usage that's published anonymously. Pull the social data, process it, publish it through the chain. Set up css loggers to track states of elements as users surf. Track products. Give real-time "vision" of other users navigational habits and interactions with products. Pitch as bitcoin enabling "product vision" like night vision. Censorship resistence enables digital clairvoyance.
11. css-sass-utils like XML-HTML-utils[0].

## CSS2AngularJS

Sometimes I want to do like `$ cp` on parts of the CSS document and paste into another CSS doc. Or use a CSS doc as a config to hxextract from an HTML doc. Or use a CSS doc to generate jQuery canonical event code like Yeoman. It'd be cool to generate Controllers/Directives in AngularJS from CSS docs using DOM events as symbol hooks. So styling an element with a particular BEM schema would entail Controller or Directive relations and macro triggers. 

    ul > li > a.MainCtrl--section__paymentDirective { }

Or:

    [ng-controller="MainCtrl"] section [paymentDirective] a { }

Runs:

    yo ang:controller MainCtrl
    yo ang:directive paymentDirective

Basically treat keys in CSS like `cmd` fields in Grunt to pre/post hook operations.

## Dealing with Pseudoselectors

Your CSS wants to say this to sempai:

```json
{
  "links": {
    "self": "/url"
  },
  "data": [{
    "relationships": {
      "div": {
        "links": {
          "hover": "/uri"
        },
        "data": [{
          "id": 1,
          "relationships": {
            "h1": {
              "links": {
                "target": "/uri"
              },
              "data": [{
                "id": 2
              }]
            }
          }
        }],
        "included": [{
          "id": 2,
          "type": "h1"
        }]
      }
    }
  }],
  "included": [{
    "id": 1,
    "type": "div"
  }]
}
```

—

[0]: https://descartes.io/
[1]: https://github.com/kragniz/json-sempai/
[3]: https://docs.openchain.org/en/latest/api/ledger.html#id3
[4]: http://www.w3.org/Tools/HTML-XML-utils/README
