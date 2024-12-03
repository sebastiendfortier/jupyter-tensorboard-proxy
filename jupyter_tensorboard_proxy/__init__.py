import os
import shutil

def get_icon_path():
    """Get the path to the TensorBoard icon"""
    return os.path.join(
        os.path.dirname(os.path.abspath(__file__)), 'icons', 'tensorboard.svg'
    )

def setup_tensorboard():
    """Set up and return TensorBoard UI process configuration"""
    def _get_cmd(port):
        """Get the TensorBoard command"""
        # Find tensorboard executable in the current environment
        tensorboard_path = shutil.which('tensorboard')
        if not tensorboard_path:
            raise FileNotFoundError('Could not find tensorboard in PATH')

        return [
            tensorboard_path,
            '--port', str(port),
            '--bind_all',  # Allow external connections
            '--logdir', '~/tensorboard_logs/'
        ]

    return {
        'command': _get_cmd,
        'absolute_url': False,
        'launcher_entry': {
            'title': 'TensorBoard',
            'icon_path': get_icon_path()
        },
        'timeout': 90,           # Timeout in seconds
        'new_browser_tab': True  # Opens in a new tab
    } 
