'''
    Copyright (C) 2013  Povilas Kanapickas <povilas@radix.lt>
    Copyright (C) 2018  Monika Kairaityte <monika@kibit.lt>

    This file is part of cppreference-doc

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see http://www.gnu.org/licenses/.
'''

from index_transform.common import IndexTransform
from xml_utils import xml_escape

class Index2Browser(IndexTransform):

    def __init__(self, out_file):
        super().__init__()
        self.out_file = out_file

    def output_item(self, el, full_name, full_link):
        mark = ''
        if el.tag == 'const': mark = '(const)'
        elif el.tag == 'function': mark = '(function)'
        elif el.tag == 'constructor': mark = '(function)'
        elif el.tag == 'destructor': mark = '(function)'
        elif el.tag == 'class': mark = '(class)'
        elif el.tag == 'enum': mark = '(enum)'
        elif el.tag == 'variable': mark = '(variable)'
        elif el.tag == 'typedef': mark = '(typedef)'
        elif el.tag == 'specialization': mark = '(class)'
        elif el.tag == 'overload': mark = '(function)'

        res = u''
        res += '<tt><b>' + xml_escape(full_name) + '</b></tt> [<span class="link">'
        res += '<a href="http://en.cppreference.com/w/' + xml_escape(full_link) + '">'
        res += full_link + '</a></span>] <span class="mark">' + mark + '</span>\n'
        return res

    def process_item_hook(self, el, full_name, full_link):
        self.out_file.write('<li>' + self.output_item(el, full_name, full_link) + '<ul>')
        IndexTransform.process_item_hook(self, el, full_name, full_link)
        self.out_file.write('</ul></li>\n')
