from ._anvil_designer import Form1Template
from anvil import *
import anvil.server


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.data_dict = {}  # Store CSV data
    # Any code you write here will run before the form opens.

  def file_loader_1_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    """Runs when a CSV file is uploaded."""
    if file is not None:
            csv_data = file.get_bytes().decode("utf-8")  # Read file as text
            self.data_dict = anvil.server.call('parse_csv', csv_data)  # Process CSV
            self.text_area_1.text = "\n".join([str(row) for row in self.data_dict])  # Show each row

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    """Runs when 'Convert to XML' is clicked."""
    if self.data_dict:
       xml_file = anvil.server.call('convert_to_xml', self.data_dict)
       if xml_file:
         self.link_1.url = xml_file  # Set BlobMedia directly
         self.link_1.text = "Download XML"  # Show a proper link name
         self.link_1.visible = True  # Show the link
    else:
        alert("Must upload a CSV file first")

