from ._anvil_designer import Form1Template
from anvil import *
import anvil.server #Importing the server module
import re #used to remove certain characters from text

class AnimalData: #Define a class to handle the animal data
  
   def __init__(self, Name, Species, Age, Sex, Source_name, Source_address, Note_1, Note_1_date, Note_2, Note_2_date):
        self.Name = Name
        self.Species = Species
        self.Age = Age
        self.Sex = Sex
        self.Source_name = Source_name
        self.Source_address = Source_address
        self.Note_1 = Note_1
        self.Note_1_date = Note_1_date
        self.Note_2 = Note_2
        self.Note_2_date = Note_2_date

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
            ##self.data_dict = line.translate(None, ''{}) # used to remove certain characters when displaying (Never worked)
            self.txt_area_1.text = "\n".join([str(row) for row in self.data_dict])  # Show each row
            alert("File uploaded") #Alerts the user that the file has been uploaded
      
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    """Runs when the 'Convert to XML' button is clicked."""
    if self.data_dict:
       xml_file = anvil.server.call('convert_to_xml', self.data_dict) #
       if xml_file:
         self.link_1.url = xml_file  # Set BlobMedia directly
         self.link_1.text = "Download XML"  # Show a proper link name
         self.link_1.visible = True  # un-hides the link
    else:
        alert("You need to upload a CSV file") #Alerts the user that either the incorrect file or no file has been uploaded.

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    alert("XML file converted and downloaded") #Alerts the user that the file has been downloaded