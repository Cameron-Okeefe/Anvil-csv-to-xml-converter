import anvil.server
import io
import csv
import xml.etree.ElementTree as ET
import anvil

@anvil.server.callable
def parse_csv(csv_data):
    """Reads CSV and turns it into a list of dictionaries."""
    reader = csv.DictReader(io.StringIO(csv_data))  # Read CSV rows
    return list(reader)  # Return as a list of dictionaries

@anvil.server.callable
def convert_to_xml(data_list):
    """Converts dictionary data to XML and returns a downloadable file."""
    root = ET.Element("root")  # Create root XML tag

    for row in data_list:
        item = ET.SubElement(root, "record") 
        for key, value in row.items():
            child = ET.SubElement(item, key) #  
            child.text = value if value else ""  #Adds an empty value in the place where there are no values

    xml_data = ET.tostring(root, encoding='utf-8').decode("utf-8")

    # Convert XML data to a downloadable file
    xml_file = anvil.BlobMedia("text/xml", xml_data.encode("utf-8"), name="converted.xml")
    return xml_file  # Return BlobMedia directly
