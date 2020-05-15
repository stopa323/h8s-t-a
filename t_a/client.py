import os
import subprocess

from typing import List, Tuple


class TerraformClient(object):

    def __init__(self, work_dir: str):
        self._work_dir = work_dir

    def _run_cmd(self, cmd: List[str]) -> Tuple[str, str]:
        p = subprocess.Popen(cmd, cwd=self._work_dir,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
        out, err = p.communicate()
        return out.decode("utf-8"), err.decode("utf-8")

    def init(self):
        cmd = ["terraform", "init"]
        out, err = self._run_cmd(cmd)
        print(out)
        print(err)

    def plan(self):
        cmd = ["terraform", "plan"]
        out, err = self._run_cmd(cmd)
        print(out)
        print(err)
