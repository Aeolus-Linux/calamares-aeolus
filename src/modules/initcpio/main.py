import libcalamares
import subprocess
from libcalamares.utils import check_target_env_call, target_env_call
from libcalamares.utils import *


def run_mkinitcpio():
    """ Runs mkinitcpio with given kernel profile """
    kernel = libcalamares.job.configuration['kernel']
    check_target_env_call(['mkinitcpio', '-p', kernel])


def run():
    """ Calls routine to create kernel initramfs image.

    :return:
    """
    root_mount_point = libcalamares.globalstorage.value("rootMountPoint")
    subprocess.check_call(["cp", "/run/archiso/bootmnt/arch/boot/x86_64/vmlinuz", root_mount_point + "/boot/vmlinuz-linux"])
    run_mkinitcpio()

    return None


