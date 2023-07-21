"""
serie
<serie>123</serie>

identificação do cliente
<idDest>3</idDest>

cod do produto
<cProd>8926.02.201</cProd>

erro: nota fiscal que vem com o imposto errado.
"""

xml_string = '''<root>
    <elemento1>Valor 1</elemento1>
    <elemento2>Valor 2</elemento2>
</root>'''

import nota 
from lxml import etree
import xml.etree.ElementTree as ET

try:
    arquivo = ET.fromstring(nota.xml)

    raiz = arquivo.find('.//{http://www.portalfiscal.inf.br/nfe}ide')
    serie = raiz.findtext('{http://www.portalfiscal.inf.br/nfe}serie')
    idDest = raiz.findtext('{http://www.portalfiscal.inf.br/nfe}idDest')

    # Encontrar o elemento <prod> e extrair o valor de <cProd>
    det = arquivo.find('.//{http://www.portalfiscal.inf.br/nfe}det')
    prod = det.find('.//{http://www.portalfiscal.inf.br/nfe}prod')
    cProd = prod.findtext('{http://www.portalfiscal.inf.br/nfe}cProd')

    # Imprimir os valores extraídos
    print("Valor de <serie>: ", serie)
    print("Valor de <idDest>: ", idDest)
    print("Valor de <cProd>: ", cProd)

except etree.XMLSyntaxError:
    print("URL inválida")











