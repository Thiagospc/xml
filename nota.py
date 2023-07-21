
xml="""

<NFe xmlns="http://www.portalfiscal.inf.br/nfe">

    <infNFe versao="3.10">

        <ide>
            <cUF>41</cUF>
            <cNF>00000000</cNF>
            <natOp>Venda de mercadoria adquirida ou recebida de terceiros</natOp>
            <indPag>1</indPag>
            <mod>55</mod>
            <serie>123</serie>
            <nNF>12345678</nNF>
            <dhEmi>2018-03-08T08:38:41-03:00</dhEmi>
            <tpNF>1</tpNF>
            <idDest>3</idDest>
            <cMunFG>4128104</cMunFG>
            <tpImp>1</tpImp>
            <tpEmis>1</tpEmis>
            <cDV>6</cDV>
            <tpAmb>2</tpAmb>
            <finNFe>1</finNFe>
            <indFinal>1</indFinal>
            <indPres>1</indPres>
            <procEmi>3</procEmi>
            <verProc>6.3.0.26776</verProc>
        </ide>

        <emit>
            <CNPJ>11111111111111</CNPJ>
            <xNome>Inventti</xNome>
            <xFant>Inventti</xFant>
            <enderEmit>
                <xLgr>Avenida Londrina</xLgr>
                <nro>4056</nro>
                <xBairro>Zona II</xBairro>
                <cMun>4128104</cMun>
                <xMun>Umuarama</xMun>
                <UF>PR</UF>
                <CEP>87502250</CEP>
                <cPais>1058</cPais>
                <xPais>BRASIL</xPais>
                <fone>9999999999</fone>
            </enderEmit>
            <IE>9999999999</IE>
            <CRT>1</CRT>
        </emit>

        <dest>
            <CNPJ/>
            <xNome>NF-E EMITIDA EM AMBIENTE DE HOMOLOGACAO - SEM VALOR FISCAL</xNome>
            <enderDest>
                <xLgr>24 Bessemer Street</xLgr>
                <nro>24</nro>
                <xCpl>Unit 21 Amalgam Industrial Estate</xCpl>
                <xBairro>AMALGAM - JOHANNESBURG</xBairro>
                <cMun>9999999</cMun>
                <xMun>EXTERIOR</xMun>
                <UF>EX</UF>
                <CEP>00000024</CEP>
                <cPais>7560</cPais>
                <xPais>AFRICA DO SUL</xPais>
            </enderDest>
            <IE/>
        </dest>

        <det nItem="1">

            <prod>
                <cProd>8926.02.201</cProd>
                <cEAN/>
                <xProd>LANTERNA DIR D96MM AMB 08D005</xProd>
                <NCM>85122022</NCM>
                <CFOP>7102</CFOP>
                <uCom>UN</uCom>
                <qCom>50.0000</qCom>
                <vUnCom>5.30</vUnCom>
                <vProd>265.00</vProd>
                <cEANTrib/>
                <uTrib>UN</uTrib>
                <qTrib>50.0000</qTrib>
                <vUnTrib>5.30</vUnTrib>
                <vOutro>134.74</vOutro>
                <indTot>1</indTot>
            </prod>

            <imposto>
                <vTotTrib>102.74</vTotTrib>
                <ICMS>
                    <ICMSSN102>
                        <orig>0</orig>
                        <CSOSN>300</CSOSN>
                    </ICMSSN102>
                </ICMS>
                <PIS>
                    <PISOutr>
                        <CST>99</CST>
                        <qBCProd>0</qBCProd>
                        <vAliqProd>0</vAliqProd>
                        <vPIS>0</vPIS>
                    </PISOutr>
                </PIS>
                <COFINS>
                    <COFINSOutr>
                        <CST>99</CST>
                        <qBCProd>0</qBCProd>
                        <vAliqProd>0</vAliqProd>
                        <vCOFINS>0</vCOFINS>
                    </COFINSOutr>
                </COFINS>
            </imposto>

        </det>

        <total>
            <ICMSTot>
                <vBC>0</vBC>
                <vICMS>0</vICMS>
                <vBCST>0</vBCST>
                <vST>0</vST>
                <vProd>265.00</vProd>
                <vFrete>0</vFrete>
                <vSeg>0</vSeg>
                <vDesc>0</vDesc>
                <vII>0</vII>
                <vIPI>0</vIPI>
                <vPIS>0</vPIS>
                <vCOFINS>0</vCOFINS>
                <vOutro>134.74</vOutro>
                <vNF>399.74</vNF>
                <vTotTrib>102.74</vTotTrib>
            </ICMSTot>
        </total>

        <transp>
            <modFrete>0</modFrete>
            <transporta>
                <CNPJ>11111111111111</CNPJ>
                <xNome>Inventti</xNome>
                <IE>9999999999</IE>
                <xEnder>Rua Santa Catarina n.812, Água Verde, APTO 31</xEnder>
                <xMun>Curitiba</xMun>
                <UF>PR</UF>
            </transporta>
            <vol>
                <qVol>1</qVol>
                <esp>CAIXA DE MADEIRA</esp>
                <marca>ANDALUCIA</marca>
                <pesoL>104.500</pesoL>
                <pesoB>165.000</pesoB>
            </vol>
        </transp>

        <infAdic>
            <infAdFisco>PRODUTO COM FIM DA EXPORTAÇÃO:\lA ISENÇÃO DE PIS CONFORME LEI 10637/2002 ART. 5º INCISO III E COFINS LEI 10833/2003 ART. 6º INCISO I E III.\lCOMMERCIAL INVOICE AT08/2014</infAdFisco>
        </infAdic>

        <exporta>
            <UFSaidaPais>PR</UFSaidaPais>
            <xLocExporta>CURITIBA</xLocExporta>
            <xLocDespacho>CURITIBA</xLocDespacho>
        </exporta>
        
    </infNFe>
</NFe>
"""