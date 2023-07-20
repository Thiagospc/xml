from test import xml
from lxml import etree

arquivo = etree.fromstring(xml) 

for  child in arquivo:
    
    print("sku:", child.attrib["sku"])

    print("min:", child.find(".//min-order-quantity").text)  

    print("step-quantity:", child.find(".//min-order-quantity").text)  

    print("step:" ,child.find(".//step-quantity").text)  

    print("\n")
