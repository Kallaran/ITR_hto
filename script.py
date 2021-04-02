import xml.etree.ElementTree as ET

LIST_FUNC = { "navigation_function" , "Detection_contact_function" , "Detection_distance_function"}


tree = ET.parse('TP2bis-res.xml')
root = tree.getroot()


"""

for CFG in root.findall('CFG'):
    name = CFG.get('name')
    if name in LIST_FUNC:
        root = name.findall(".")
        print(root)
        
"""

"""

list_CFG = root.findall("./CFG")

for CFG in list_CFG:
    print(CFG.tag, CFG.attrib)

"""



"""

for fun in LIST_FUNC:

    path = "./CFG[@name='" + fun + "']"
    list_CFG = root.findall(path)

    for CFG in list_CFG:
        #print(CFG.tag, CFG.attrib)
        for i in CFG :
            print(i.tag)
        
""" 
    


for fun in LIST_FUNC:

    path = "./CFG[@name='" + fun + "']/ATTRS_LIST/ATTR[@name='WCET']"
    l = root.findall(path)

    for i in l:
        WCET = i.get('value')
        print(fun, WCET)























