#
# Copyright (c) 2022 Ada Logics ltd.
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#
from .base import BaseFormatter

class Fuzz(BaseFormatter):
    def __init__(self, cg_generator):
        self.cg_generator = cg_generator

    def generate(self):
        output = self.cg_generator.cg.get_extended()

        #output = self.cg_generator.output()
        output_cg = {}
        for node in output:
            output_cg[node] = output[node]#list(output[node])

        res = {}

        res['cg'] = output_cg
        res['ep'] = {
            "name" : self.cg_generator.cg.ep,
            "mod"  : self.cg_generator.cg.ep_mod 
        }
        return res
