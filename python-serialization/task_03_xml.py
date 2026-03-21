import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    root = ET.Element("data")
    
    for key, val in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(val)
        
    tree = ET.ElementTree(root)
    tree.write(filename)

def deserialize_from_xml(filename):
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        
        deserialized_dict = {}
        
        for child in root:
            deserialized_dict[child.tag] = child.text
            
        return deserialized_dict
        
    except FileNotFoundError:
        return None