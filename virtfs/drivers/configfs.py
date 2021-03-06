# Copyright 2012 Christopher MacGown. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from virtfs import drivers


class ConfigFS(drivers.VirtFSDriver):
    '''VirtFSDriver that provides access to the configfs virtual filesystem'''

    def __init__(self, configfs_path=None, contents=None):
        if not configfs_path:
            configfs_path = drivers.resolve_virtfs_path(ConfigFS)

        super(ConfigFS, self).__init__(virtfs_path=configfs_path,
                                       contents=contents)
