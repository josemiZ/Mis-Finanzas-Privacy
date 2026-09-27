#!/usr/bin/env python3
"""Compare Android's generated Spanish policy with this site, without writing files."""
import argparse
from datetime import date
from html.parser import HTMLParser
from pathlib import Path
import re
import sys


class Policy(HTMLParser):
    def __init__(self, html):
        super().__init__(convert_charrefs=True)
        self.sections = []
        self.fields = {}
        self.section = None
        self.capture = None
        self.time = []
        self.feed(html)
        self.close()
        if self.capture or self.section is not None:
            raise ValueError('Contenido de política incompleto')
        if len(self.sections) != 9 or set(self.fields) != {'summary', 'updated'}:
            raise ValueError('Se requieren nueve secciones, un resumen y una fecha')
        for i, section in enumerate(self.sections, 1):
            if not section.get('h2') or not section.get('p'):
                raise ValueError(f'Sección {i} incompleta')
            title = section['h2'][0]
            match = re.fullmatch(r'0?(\d+)[.]?\s+(.+)', title)
            if len(section['h2']) != 1 or not match or int(match[1]) != i:
                raise ValueError(f'Título o numeración inesperados en sección {i}')
            section['h2'] = [match[2]]

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'section':
            if self.section is not None:
                raise ValueError('Secciones anidadas no admitidas')
            self.section = {}
        if tag == 'time':
            self.time.append(attrs.get('datetime'))
        classes = attrs.get('class', '').split()
        field = next((c for c in ('summary', 'updated') if c in classes), None)
        if (tag in ('h2', 'p') and self.section is not None) or field:
            if self.capture:
                raise ValueError('Bloques anidados no admitidos')
            self.capture = (tag, field, [])

    def handle_data(self, data):
        if self.capture:
            self.capture[2].append(data)

    def handle_endtag(self, tag):
        if self.capture and tag == self.capture[0]:
            _, field, parts = self.capture
            value = ' '.join(''.join(parts).split())
            if field:
                if field in self.fields:
                    raise ValueError(f'Campo duplicado: {field}')
                self.fields[field] = value
            else:
                self.section.setdefault(tag, []).append(value)
            self.capture = None
        if tag == 'section' and self.section is not None:
            self.sections.append(self.section)
            self.section = None


def compare(source, target):
    differences = []
    for field in ('summary', 'updated'):
        if source.fields[field] != target.fields[field]:
            differences.append(field)
    for i, (a, b) in enumerate(zip(source.sections, target.sections), 1):
        if a != b:
            differences.append(f'sección {i}')
    months = 'enero febrero marzo abril mayo junio julio agosto septiembre octubre noviembre diciembre'.split()
    match = re.fullmatch(r'Última actualización: (\d{1,2}) de (\w+) de (\d{4})', target.fields['updated'])
    if not match or match[2] not in months:
        raise ValueError('Formato de fecha visible no reconocido')
    iso = date(int(match[3]), months.index(match[2]) + 1, int(match[1])).isoformat()
    if target.time != [iso]:
        differences.append('atributo datetime del sitio')
    return differences


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source', type=Path, help='HTML generado en el proyecto Android')
    parser.add_argument('--target', type=Path, default=Path(__file__).resolve().parents[1] / 'index.html')
    args = parser.parse_args()
    try:
        differences = compare(Policy(args.source.read_text(encoding='utf-8')),
                              Policy(args.target.read_text(encoding='utf-8')))
    except (OSError, ValueError) as error:
        print(f'Error: {error}', file=sys.stderr)
        return 2
    if differences:
        print('Diferencias: ' + ', '.join(differences))
        return 1
    print('Coinciden las nueve secciones, el resumen y la fecha; datetime correcto.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
