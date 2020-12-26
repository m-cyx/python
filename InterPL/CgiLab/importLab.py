import xml.etree.ElementTree as ET

"""text1 = 'xiaomi'
text2 = 'mi note 10 lite'

# Element (название эл) используется для создания элементов XML
phones_firms = ET.Element('phones') #корневой тег телефоны

# SubElement ((родитель, название эл)), используемая для создания вложенных тегов 
phone_firm = ET.SubElement(phones_firms, text1) 
model = ET.SubElement(phone_firm, text2)

# dump() используется для вывода элементов xml
ET.dump(phones_firms)

# Cохраняю в файл, используя метод write()
tree = ET.ElementTree(phones_firms)
tree.write("sample.xml")

#-----------------------
"""
text1 = 'модель телефона1'
text2 = 'название телефона1'

tree = ET.parse('sample.xml')
root=tree.getroot()

# SubElement ((родитель, название эл)), используемая для создания вложенных тегов 
phone_firm = ET.SubElement(root, text1) 
model = ET.SubElement(phone_firm, text2)

# dump() используется для вывода элементов xml
ET.dump(root)

# Cохраняю в файл, используя метод write()
tree = ET.ElementTree(root)
tree.write("sample.xml")

#----------