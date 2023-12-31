"""
serie
<serie>123</serie>

identificação do cliente
<idDest>3</idDest>

cod do produto
<cProd>8926.02.201</cProd>

erro: nota fiscal que vem com o imposto errado.
"""

import nota 
from lxml import etree
import xml.etree.ElementTree as ET
import mysql.connector as mc

def consumindoXml():

    try:
        arquivo = ET.fromstring(nota.xml)

        raiz = arquivo.find('.//{http://www.portalfiscal.inf.br/nfe}ide')
        serie = raiz.findtext('{http://www.portalfiscal.inf.br/nfe}serie')
        idDest = raiz.findtext('{http://www.portalfiscal.inf.br/nfe}idDest')

        # Encontrar o elemento <prod> e extrair o valor de <cProd>
        det = arquivo.find('.//{http://www.portalfiscal.inf.br/nfe}det')
        prod = det.find('.//{http://www.portalfiscal.inf.br/nfe}prod')
        cProd = prod.findtext('{http://www.portalfiscal.inf.br/nfe}cProd')

        def enviandoProBanco():

            conexao = mc.connect(
            host="localhost",
            user="thiago",
            password="123",
            database="nfse",
            autocommit="True"
            )

        
            if conexao.is_connected():
                print("Conexão com o banco estabelecida!")

                cursor = conexao.cursor()

                cursor.execute("INSERT INTO notas VALUES (default, '%d', '%d', '%s')" % (int(serie), int(idDest), str(cProd)))
                
        
        enviandoProBanco()


    except etree.XMLSyntaxError:
        print("URL inválida")


consumindoXml()












