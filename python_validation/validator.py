import sys
from lxml import etree

def validate(dtd_or_xsd, xml):
    if not dtd_or_xsd.validate(xml):
        errors = dtd_or_xsd.error_log.filter_from_errors()
        sys.exit(f"error de validació:\n\t{errors[0]}") # mostro el primer tan sols

def validate_dtd(dtd_file_name, xml):
    try:
        dtd = etree.DTD(dtd_file_name)
    except Exception as e:
        sys.exit(f"Error en el format del DTD:\n\t{e}")

    print("DTD CORRECTE!")

    # XML i DTD són correctes, validem l'XML contra el DTD
    print("Validant l'XML amb el DTD... ", end = "")
    validate(dtd_or_xsd = dtd, xml = xml)
    print("OK!")

def validate_xsd(xsd_file_name, xml):
    # Un XSD és també un XML
    try:
        xsd_as_xml = etree.parse(xsd_file_name)
    except Exception as e:
        sys.exit(f"Error en el format XML del XSD:\n\t{e}")

    try:
        xsd = etree.XMLSchema(xsd_as_xml)
    except Exception as e:
        sys.exit(f"Error en el format XSD:\n\t{e}")

    print("XSD CORRECTE!")

    # XML i DTD són correctes, validem l'XML contra el DTD
    print("Validant l'XML amb el XSD... ", end = "")
    validate(dtd_or_xsd = xsd, xml = xml)
    print("OK!")

def validator(file_names):
    xml_file_name = None
    dtd_file_name = None
    xsd_file_name = None

    for file_name in file_names:
        if file_name.endswith(".xml"):
            xml_file_name = file_name
            print(f"Fitxer XML: {xml_file_name}")
        elif file_name.endswith(".dtd"):
            dtd_file_name = file_name
            print(f"Fitxer DTD: {dtd_file_name}")
        elif file_name.endswith(".xsd"):
            xsd_file_name = file_name
            print(f"Fitxer XSD: {xsd_file_name}")

    if xml_file_name is None:
        sys.exit("No s'ha proporcionat cap fitxer amb extensió xml")

    print("-------------------------------------------------------")

    try:
        xml = etree.parse(xml_file_name)
    except Exception as e:
        sys.exit(f"Error en el format del XML:\n\t{e}")

    print("XML CORRECTE!")

    if dtd_file_name is not None:
        validate_dtd(dtd_file_name = dtd_file_name, xml = xml)

    if xsd_file_name is not None:
        validate_xsd(xsd_file_name = xsd_file_name, xml = xml)

if __name__ == "__main__":
    # crido a la funció validator amb els paràmetres
    validator(sys.argv)