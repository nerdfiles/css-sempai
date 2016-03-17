import re


class Pyzzle:

    def isInstanceOf(x):
        return x

    def isEmpty(x):
        return x.length is 0

    def __init__(self):
        print(self)

    selX = re.match('[^\s\;\{\}][^\;\{\}]*)\{')
    endX = re.match('\}')
    lineX = re.match('([^\;\{\}]*)\;')
    commentX = re.match('\/\*[\s\S]*?\*\/')
    lineAttrX = re.match('([^\:]+):([^\;]*);')

    altX = re.match(
        '(\/\*[\s\S]*?\*\/)|([^\s\;\{\}][^\;\{\}]*(?=\{))|(\})|([^\;\{\}]+\;(?!\s*\*\/))')  # gmi

    # Capture groups
    capComment = 1
    capSelector = 2
    capEnd = 3
    capAttr = 4
    HTMLStyleElement = None

    def isCssJson(node):
        return (node.attributes and node.children) if not isEmpty(
            node) else False

    def isValidStyleNode(node):
        return (
            isInstanceOf(
                node,
                HTMLStyleElement)) and node.sheet.cssRules.length > 0

    def timestamp():
        return Date.now() or Date()

    def strAttr(name, value, depth):
        return '\t'.repeat(depth) + name + ': ' + value + ';\n'

    def strNode(name, value, depth):
        cssString = '\t'.repeat(depth) + name + ' {\n'
        cssString += self.toCSS(value, depth + 1)
        cssString += '\t'.repeat(depth) + '}\n'
        return cssString

    class Base(object):
        content = ""

        def get_content(self):
            return self.content

        def to_json(self):
            node = Dict()
            node['children'] = {}
            node['attributes'] = {}
            match = None
            count = 0
            return self.json

        def to_css(self):
            return self.css

        def to_head(self):
            return self.head

    class CSS(Base):
        content = "html {}"

    class JSON(Base):
        content = "{}"

    class BaseFactory():

        def convert(self, typ):
            targetclass = typ.capitalize()
            return globals()[targetclass]()

    base_obj = BaseFactory()
    base = ['css', 'json']
    for b in base:
        print base_obj.convert(b).get_content()
