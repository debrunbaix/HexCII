import subprocess
import tempfile
import json
import os

def checksec_cmd(FILENAME: str) -> dict:
    """
    Fonction to get the Checksec's output of the user's binary.

    Args:
        FILENAME (str): filename of the binary.

    Returns:
        checksec_dict: Dictionnary of the output.
    """
    CHECKSEC_CMD = ['/usr/bin/checksec', '--output=json', '--file=' + FILENAME]
    checksec_cmd_output = subprocess.check_output(CHECKSEC_CMD, universal_newlines=True)

    checksec_dict = json.loads(checksec_cmd_output)[FILENAME]
    return checksec_dict

def get_security_info(file_content):
    """
    Function to analyse binary's security mechanism.

    Args:
        file_content (bytes): content of the file.

    Returns:
        dict: dictionnary that contain infos of the binary.
    """
    temp_dir = os.path.join(os.getcwd(), 'temp')
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)

    with tempfile.NamedTemporaryFile(dir=temp_dir, delete=False) as temp_file:
        temp_filename = temp_file.name
        temp_file.write(file_content)

    try:
        security_info = checksec_cmd(temp_filename)
    except Exception as e:
        print(f"Erreur lors de l'exécution de checksec: {e}")
        security_info = {}
    finally:
        if os.path.exists(temp_filename):
            os.remove(temp_filename)

    return security_info