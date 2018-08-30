#
#  Copyright (C) 2017 Codethink Limited
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU Lesser General Public
#  License as published by the Free Software Foundation; either
#  version 2 of the License, or (at your option) any later version.
#
#  This library is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.	 See the GNU
#  Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public
#  License along with this library. If not, see <http://www.gnu.org/licenses/>.
#
#  Authors:
#        Tristan Maat <tristan.maat@codethink.co.uk>

import os
import sys
import resource

from .._exceptions import PlatformError, ImplError


class Platform():
    _instance = None

    # Platform()
    #
    # A class to manage platform-specific details. Currently holds the
    # sandbox factory as well as platform helpers.
    #
    def __init__(self):
        self.set_resource_limits()

    @classmethod
    def _create_instance(cls):
        # Meant for testing purposes and therefore hidden in the
        # deepest corners of the source code. Try not to abuse this,
        # please?
        if os.getenv('BST_FORCE_BACKEND'):
            backend = os.getenv('BST_FORCE_BACKEND')
        elif sys.platform.startswith('linux'):
            backend = 'linux'
        elif sys.platform.startswith('darwin'):
            backend = 'darwin'
        else:
            backend = 'unix'

        if backend == 'linux':
            from .linux import Linux as PlatformImpl
        elif backend == 'darwin':
            from .darwin import Darwin as PlatformImpl
        elif backend == 'unix':
            from .unix import Unix as PlatformImpl
        else:
            raise PlatformError("No such platform: '{}'".format(backend))

        cls._instance = PlatformImpl()

    @classmethod
    def get_platform(cls):
        if not cls._instance:
            cls._create_instance()
        return cls._instance

    def get_cpu_count(self, cap=None):
        return min(len(os.sched_getaffinity(0)), cap)

    ##################################################################
    #                        Sandbox functions                       #
    ##################################################################

    # create_sandbox():
    #
    # Create a build sandbox suitable for the environment
    #
    # Args:
    #     args (dict): The arguments to pass to the sandbox constructor
    #     kwargs (file): The keyword arguments to pass to the sandbox constructor
    #
    # Returns:
    #     (Sandbox) A sandbox
    #
    def create_sandbox(self, *args, **kwargs):
        raise ImplError("Platform {platform} does not implement create_sandbox()"
                        .format(platform=type(self).__name__))

    def check_sandbox_config(self, config):
        raise ImplError("Platform {platform} does not implement check_sandbox_config()"
                        .format(platform=type(self).__name__))

    def set_resource_limits(self, soft_limit=None, hard_limit=None):
        # Need to set resources for _frontend/app.py as this is dependent on the platform
        # SafeHardlinks FUSE needs to hold file descriptors for all processes in the sandbox.
        # Avoid hitting the limit too quickly.
        limits = resource.getrlimit(resource.RLIMIT_NOFILE)
        if limits[0] != limits[1]:
            if soft_limit is None:
                soft_limit = limits[1]
            if hard_limit is None:
                hard_limit = limits[1]
            resource.setrlimit(resource.RLIMIT_NOFILE, (soft_limit, hard_limit))
