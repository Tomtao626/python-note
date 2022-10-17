import xml.etree.ElementTree as ET

new_xml = ET.Element('personinfo')  #根节点
personinfo = ET.SubElement(new_xml,'personinfo',attrib = {'enrolled':'yes'})  #子节点
name = ET.SubElement(personinfo,'name')
name.text = "tomtao"
age = ET.SubElement(personinfo,'age',attrib = {'checked':'no'})
sex = ET.SubElement(personinfo,'sex',attrib = {'yes':'no'})
age.text = '20'
personinfo2 = ET.SubElement(new_xml,'personinfo',sttrib={'enrolled':'no'})
name = ET.SubElement(personinfo,'name')
name.text = 'TOM_tao'
age = ET.SubElement(personinfo,'age')
age.text = '19'

et = ET.ElementTree(new_xml)  # 生成文档对象
et.write("test.xml",encoding='utf-8',xml_declaration=True)

ET.dump(new_xml) # 打印生成格式