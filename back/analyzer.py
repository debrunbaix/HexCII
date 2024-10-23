import magic

from security.infos import get_security_info
from elf_analyse.get_elf_info import get_elf_info
from pe_analyse.get_pe_info import get_pe_info

analysis_result: dict = {
        'filename':'',
        'filesize':'',
        'informations':{},
        'security':{},
        'code':{
            'assembly':'path',
            'pseudo_code':'path'
        }
    }

def get_endianness(endianness: str) -> str:
    """
    Function to put Little/Big by the endianness's binary.

    Args:
        endianness: string with magic.from_buffer()'s content.

    Returns:
        str
    """
    if endianness == "LSB":
        return 'Little'
    elif endianness == "MSB":
        return 'Big'

def get_basic_info(file_content: str):
    """
    Function to get binary's basic infos.

    Args:
        file_content: Binary's byte content..

    Returns:
        (str, int, str, str)
    """
    magic_output: str = magic.from_buffer(file_content)
    magic_output_list: list[str] = magic_output.split()

    file_format: str = magic_output_list[0]
    file_platform: str = magic_output_list[5]
    file_arch: int = int(magic_output_list[1].split('-')[0])
    file_endianness: str = get_endianness(magic_output_list[2])

    return file_format, file_arch, file_endianness, file_platform

def analyze_file(file) -> dict:
    """
    Function to analyse uploaded binary.

    Args:
        file (werkzeug.datastructures.FileStorage): uploaded file.

    Returns:
        dict: result analyse.
    """
    filename = file.filename
    file_content = file.read()
    filesize = len(file_content)
    file_format, file_arch, file_endianness, file_platform = get_basic_info(file_content)

    analysis_result["filename"] = filename
    analysis_result["filesize"] = filesize
    analysis_result['informations']['format'] = file_format
    analysis_result['informations']['platform'] = file_platform
    analysis_result['informations']['architecture'] = file_arch
    analysis_result['informations']['endianness'] = file_endianness

    security_info = get_security_info(file_content)
    analysis_result['security'] = security_info

    # TODO: getting disassembly code
    if file_format == 'ELF':
        sections_info = get_elf_info(analysis_result, file_content)
    elif file_format.startswith('PE'):
        sections_info = get_pe_info(analysis_result, file_content)
    else:
        sections_info = []

    analysis_result['section_infos'] = sections_info

    print(analysis_result)
    # TODO: getting decompiled code

    return analysis_result