from .get_section import get_sections_infos

def get_elf_info(analysis_result: dict, file_content) -> dict:

    sections = get_sections_infos(file_content)

    return sections