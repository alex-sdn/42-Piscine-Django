from elem import *
from elements import *

class Page:

    def __init__(self, elem: Elem):
        self.elem = elem
    
    def is_valid(self):
        # recursive loop for all content
        if len(self.elem.content) > 0:
            for content in self.elem.content:
                if isinstance(content, Elem) and not Page(content).is_valid():
                        return False

        # if not just Elem type
        if type(self.elem) is Elem:
            return False

        # if Html, content is Head+Body
        if isinstance(self.elem, Html) and (
            len(self.elem.content) != 2 or
                not isinstance(self.elem.content[0], Head) or
                not isinstance(self.elem.content[1], Body)
            ):
            return False
        
        # if Head, content is Title
        if isinstance(self.elem, Head) and (
            len(self.elem.content) != 1 or not isinstance(self.elem.content[0], Title)):
            return False
        
        # if Body or Div, only these elements
        if (isinstance(self.elem, Body) or isinstance(self.elem, Div)) and len(self.elem.content) > 0:
            for element in self.elem.content:
                if not isinstance(element, (H1, H2, Div, Table, Ul, Ol, Span, Text)):
                    return False
        
        # unique Text as content
        if isinstance(self.elem, (Title, H1, H2, Li, Th, Td)) and not (
            len(self.elem.content) == 1 and isinstance(self.elem.content[0], Text)):
            return False
        
        # if P only Text in contents
        if isinstance(self.elem, P):
            for content in self.elem.content:
                if not isinstance(content, Text):
                    return False
                
        # if Span only Text or P
        if isinstance(self.elem, Span):
            for content in self.elem.content:
                if not isinstance(content, (Text, P)):
                    return False
                
        # if Ul or Ol, only Li + at least one
        if isinstance(self.elem, (Ul, Ol)):
            if len(self.elem.content) == 0:
                return False
            for content in self.elem.content:
                if not isinstance(content, Li):
                    return False
                
        # if Tr, only Th or Td + at least one + mutually exclusive
        if isinstance(self.elem, Tr):
            if len(self.elem.content) == 0:
                return False
            for content in self.elem.content:
                if not isinstance(content, (Th, Td)) or not isinstance(content, type(self.elem.content[0])):
                    return False

        # if Table only Tr
        if isinstance(self.elem, Table):
            for content in self.elem.content:
                if not isinstance(content, Tr):
                    return False

        # OK
        return True

    def __str__(self):
        if (isinstance(self.elem, Html)):
            return '<!DOCTYPE html>\n' + str(self.elem)
        return str(self.elem)

    def write_to_file(self, filename):
        try:
            with open(filename, 'w') as file:
                file.write(str(self))
        except:
            print('An error occured when opening the file')


if __name__ == '__main__':
    # test = Page(Html([Head(Title(Text('test'))), Body([H1(Text('test')), Ol([Li(Text('Li test')), Li(Text('Li2'))]), Span(), Text(), Span()])]))
    
    test = Page(Span([P([Text('aaa'), Text('222'), Text('333')]), Text('test')]))
    
    # test = Page(Table([Tr(), Tr()]))

    # test = Page(Tr([Td(Text('aaa')), Td(Text('aa')), Td(Text('aaa'))]))

    print(test.is_valid())
    # print(test)

    try:
        test.write_to_file('testing.html')
    except Exception as e:
        print(e)