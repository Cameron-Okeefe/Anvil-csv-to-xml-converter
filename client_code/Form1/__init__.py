from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

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

    def file_loader_1_change(self, file, **event_args):
        """This method is called when a new file is loaded into this FileLoader"""
        """Runs when a CSV file is uploaded through the file uploader."""
        if file.name.endswith('.csv'):  # Checks if the file uploaded is a CSV
            print("CSV File Uploaded")
            self.uploaded_CSV = True
            csvData = file.get_bytes().decode("utf-8")  # Keep it as a single string
            self.dataXML = anvil.server.call('parse_csv', csvData)  # Sending a string
            animal_List = []
            animalNumber = 0
            for line in csvData.splitlines()[1:]:  # Split into lines, skipping the header
                columns = line.split(",")
                if len(columns) == 10:  # Check if the row has 10 columns
                    Name, Species, Age, Sex, Source_name, Source_address, Note_1, Note_1_date, Note_2, Note_2_date = columns
                    animal = AnimalData(Name, Species, Age, Sex, Source_name, Source_address, Note_1, Note_1_date, Note_2, Note_2_date)
                    animal_List.append(animal)
                else:
                    print(f"Skipping row with incorrect number of columns: {line}")
            displayText = ""
            for animal in animal_List:
                animalNumber += 1
                displayText = f"{displayText}Animal {animalNumber} ({animal.Name})\nspecies: {animal.Species}  age: {animal.Age}  sex: {animal.Sex}\nsource: {animal.Source_name}, {animal.Source_address}\nnote ({animal.Note_1_date}): {animal.Note_1}\nnote ({animal.Note_2_date}): {animal.Note_2}\n\n"
            self.txt_area_1.text = displayText

        else:
            print("Wrong file type")
            alert("Incorrect file type. Please make sure a CSV file is uploaded.")

 
    def button_1_click(self, **event_args):
      """This method is called when the 'Convert to XML' button is clicked."""
      if self.dataXML:  # Ensure dataXML is available
          xml_file = anvil.server.call('convert_to_xml', self.dataXML)  # Get the BlobMedia object
          
          if xml_file:  # Check if conversion was successful
              self.link_1.url = xml_file  # Set BlobMedia directly to the link's URL
              self.link_1.text = "Download XML File"  # Set the display text for the link
              self.link_1.visible = True  # Make the link visible
          else:
              alert("Conversion failed. Please try again.")
      else:
          alert("You need to upload a CSV file first.")
