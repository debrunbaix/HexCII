import pefile

def get_pe_sections(file_content):
    pe = pefile.PE(data=file_content)
    
    sections_info = []
    for section in pe.sections:
        sections_info.append({
            'name': section.Name.decode().strip('\x00'),
            'virtual_address': hex(section.VirtualAddress),
            'virtual_size': section.Misc_VirtualSize,
            'raw_data_size': section.SizeOfRawData,
            'characteristics': section.Characteristics
        })
    
    return sections_info