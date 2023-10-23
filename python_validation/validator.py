import sys
from lxml import etree
from io import StringIO

def validator(file_names):
    xml_file_name = None
    dtd_file_name = None
    xsd_file_name = None

    for file_name in file_names:
        if file_name.endswith(".xml"):
            xml_file_name = file_name
        elif file_name.endswith(".dtd"):
            dtd_file_name = file_name
        elif file_name.endswith(".xsd"):
            xsd_file_name = file_name

    if xml_file_name is None:
        sys.exit("No s'ha proporcionat cap fitxer amb extensió xml")
    else:
        xml = load_xml_file(file_name = xml_file_name)
        
        if dtd_file_name is None:   
            if xsd_file_name is not None:
                # un xsd és un tipus de XML
                xsd = etree.XMLSchema(load_xml_file(xsd_file_name))    
                return lxml_validator(xml = xml, dtd_or_xsd = xsd)

            # si es None, entenem que sols volia comprobar si l'XML és sintacticament correcte
        else:
            if xsd_file_name is None:
                dtd_string = read_file_as_string(file_name)
                dtd = etree.DTD(StringIO(dtd_string))
                return lxml_validator(xml = xml, dtd_or_xsd = dtd)
            else:
                sys.exit("S'ha de proporcionat un fitxer amb extensió dtd o xsd, no els dos a la vegada")

def read_file_as_string(file_name):
    text_file = open(file_name, "r")
    data = text_file.read()
    text_file.close()
    return data

def load_xml_file(file_name):
    xml_string = read_file_as_string(file_name)
    # per evitar un error de codificació si l'XML té un paràmetre d'encoding
    # https://stackoverflow.com/a/59215281
    xml = etree.XML(xml_string.encode())
    return xml

def lxml_validator(xml, dtd_or_xsd):
    if not dtd_or_xsd.validate(xml):
        errors = dtd_or_xsd.error_log.filter_from_errors()
        sys.exit(errors[0]) # mostro el primer tan sols

if __name__ == "__main__":
    # crido a la funció validator amb els paràmetres
    validator(sys.argv)