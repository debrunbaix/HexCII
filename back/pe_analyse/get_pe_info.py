from .get_section import get_pe_sections

def get_pe_info(analysis_result: dict, file_content) -> dict:

    pe_infos = {}

    sections = get_pe_sections(file_content)

    return pe_infos