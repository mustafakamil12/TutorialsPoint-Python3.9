#Import required library
import xml.etree.ElementTree as ET

def parseXML(file_name):
   # Parse XML with ElementTree
   tree = ET.ElementTree(file=file_name)
   print(tree.getroot())
   root = tree.getroot()
   print("tag=%s, attrib=%s" % (root.tag, root.attrib))

   # get the information via the children!
   print("-" * 25)
   print("Iterating using getchildren()")
   print("-" * 25)
   users = root.getchildren()
   for user in users:
      user_children = user.getchildren()
      for user_child in user_children:
         print("%s=%s" % (user_child.tag, user_child.text))

if __name__ == "__main__":
   parseXML("newdata.xml")
