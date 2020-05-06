import os
import logging
import tempfile
import subprocess

from .utils import _setup_logging

logger = logging.getLogger(__name__)
_setup_logging(logger)

SOURCE_IMAP_HOST = os.getenv('SOURCE_IMAP_HOST', '')
SOURCE_IMAP_PORT = os.getenv('SOURCE_IMAP_PORT', None)
TARGET_AUTH_FILE = os.getenv('TARGET_AUTH_FILE')

class ImapSyncRuntimeError(RuntimeError):
    def __init__(self, output):
        msg = f'\n===BEGIN OF COMMAND OUTPUT===\n{output}'
        super().__init__(msg)

def imapsync(source_username, source_password, target_email):
    logger.info('Received migration task from %s to %s', source_username, target_email)
    cmd = [
        'imapsync',
        '--no-modulesversion', '--noreleasecheck',
        '--host1', SOURCE_IMAP_HOST, '--ssl1',
        '--user1', source_username,
        '--password1', source_password,
        '--gmail2',
        '--user2', target_email,
        '--password2', TARGET_AUTH_FILE,
        '--authmech2', 'XOAUTH2',
    ]
    process_output_filename = tempfile.mktemp(suffix='subprocess_tmp_file_')
    try:
        with open(process_output_filename, 'w') as process_output:
            subprocess.check_call(cmd, stdout=process_output, stderr=process_output)
    except subprocess.CalledProcessError as err:
        for i, ci in enumerate(err.cmd):
            err.cmd[i] = ci.replace(source_password, '*********')
        logger.error('Error in process %s', err)
        with open(process_output_filename) as process_output:
            result_output = process_output.read()
            result_output = result_output.replace(source_password, '*********')
        logger.error('Output was:\n%s', result_output)
        raise ImapSyncRuntimeError(result_output) from err
    finally:
        with open(process_output_filename) as process_output:
            result_output = process_output.read()
        os.remove(process_output_filename)

    return result_output
