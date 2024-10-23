from elftools.elf.elffile import ELFFile
from io import BytesIO

def get_sections_infos(file_content):
    elffile = ELFFile(BytesIO(file_content))
    
    sections_info = []
    for section in elffile.iter_sections():
        sections_info.append({
            'name': section.name,
            'type': section['sh_type'],
            'address': hex(section['sh_addr']),
            'size': section['sh_size'],
            'flags': section['sh_flags']
        })
    
    return sections_info
