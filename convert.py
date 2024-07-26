import re

def parse_line(line):
    pattern = re.compile(r'(\S+)\s+(.+)\s+(-?\d+\.\d+)\s+(-?\d+\.\d+)\s+(-?\d+\.\d+)\s+(-?\d+\.\d+)\s+(-?\d+\.\d+)\s+(-?\d+\.\d+)')
    match = pattern.match(line.strip())
    if not match:
        raise ValueError(f"Ligne ne correspondant pas au format attendu : {line}")
    
    prop_type, model_path = match.group(1), match.group(2)
    position = (float(match.group(3)), float(match.group(4)), float(match.group(5)))
    angles = (float(match.group(6)), float(match.group(7)), float(match.group(8)))
    
    return prop_type, model_path, position, angles

def convert_to_vmf(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    with open(output_file, 'w') as f:
        f.write("versioninfo\n{\n")
        f.write("\t\"editorversion\" \"400\"\n")
        f.write("\t\"editorbuild\" \"6006\"\n")
        f.write("\t\"mapversion\" \"1\"\n")
        f.write("\t\"formatversion\" \"100\"\n")
        f.write("\t\"prefab\" \"0\"\n")
        f.write("}\n")
        f.write("visgroups\n{\n}\n")
        f.write("viewsettings\n{\n")
        f.write("\t\"bSnapToGrid\" \"1\"\n")
        f.write("\t\"bShowGrid\" \"1\"\n")
        f.write("\t\"bShowLogicalGrid\" \"0\"\n")
        f.write("\t\"nGridSpacing\" \"64\"\n")
        f.write("\t\"bShow3DGrid\" \"0\"\n")
        f.write("}\n")
        f.write("world\n{\n")
        f.write("\t\"id\" \"1\"\n")
        f.write("\t\"mapversion\" \"1\"\n")
        f.write("\t\"classname\" \"worldspawn\"\n")
        f.write("\t\"detailmaterial\" \"detail/detailsprites\"\n")
        f.write("\t\"detailvbsp\" \"detail.vbsp\"\n")
        f.write("\t\"maxpropscreenwidth\" \"-1\"\n")
        f.write("\t\"skyname\" \"sky_day01_01\"\n")
        f.write("}\n")
        
        for line in lines:
            prop_type, model_path, pos, angles = parse_line(line)
            f.write("entity\n{\n")
            f.write("\t\"id\" \"1\"\n")
            f.write(f"\t\"classname\" \"{prop_type}\"\n")
            f.write(f"\t\"model\" \"{model_path}\"\n")
            f.write(f"\t\"origin\" \"{pos[0]} {pos[1]} {pos[2]}\"\n")
            f.write(f"\t\"angles\" \"{angles[0]} {angles[1]} {angles[2]}\"\n")
            f.write("}\n")

if __name__ == "__main__":
    convert_to_vmf("props_export.txt", "output.vmf")
