import anvil.server
import io
import csv
import xml.etree.ElementTree as ET
import anvil

@anvil.server.callable
def parse_csv(csv_data):
    """Reads CSV and turns it into a list of dictionaries, handling missing values."""
    if not isinstance(csv_data, str):  # Ensure csv_data is a string
        raise TypeError("csv_data must be a string")

    reader = csv.DictReader(io.StringIO(csv_data))  # Read CSV from string
    rows = [row for row in reader]  # Convert to a list of dictionaries

    return rows  # Return as a list
    for row in reader:
        cleaned_row = {key: row[key] if key in row and row[key] else "" for key in reader.fieldnames}  # Ensure all keys exist and replace None/missing values with ""
        rows.append(cleaned_row)

    return rows  # Return as a list of dictionaries

@anvil.server.callable
def convert_to_xml(data_list):
    """Converts dictionary data to XML and returns a downloadable file."""
    root = ET.Element("root")  # Create root XML tag

    for row in data_list:
        item = ET.SubElement(root, "record")
        for key, value in row.items():
            child = ET.SubElement(item, key)
            child.text = value if value else ""  # Handle empty values

    xml_data = ET.tostring(root, encoding='utf-8').decode("utf-8")

    # Convert XML data to a downloadable file
    xml_file = anvil.BlobMedia("text/xml", xml_data.encode("utf-8"), name="converted.xml")
    return xml_file  # Return BlobMedia directly
