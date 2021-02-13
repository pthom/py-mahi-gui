# Copyright 2020 Joel Linn
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this
# list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation
# and/or other materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its contributors
# may be used to endorse or promote products derived from this software
# without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# You are under no obligation whatsoever to provide any bug fixes, patches, or
# upgrades to the features, functionality or performance of the source code
# ("Enhancements") to anyone; however, if you choose to make your Enhancements
# available either publicly, or directly to the author of this software, without
# imposing a separate written license agreement for such Enhancements, then you
# hereby grant the following license: a non-exclusive, royalty-free perpetual
# license to install, use, modify, prepare derivative works, incorporate into
# other computer software, distribute, and sublicense such enhancements or
# derivative works thereof, in binary and source code form.

import mahi_gui
from mahi_gui import imgui
from mahi_gui import implot
import numpy as np

class HelloWorld(mahi_gui.Application):

    def __init__(self):
        super().__init__(700, 400, "Hello World")
        imgui.get_io().ini_filename = None
        imgui.disable_viewports()
        self._random = np.random.randn(1000)

    def _update(self):
        # Remove first value, shift left and append new random number
        self._random = np.append(self._random[1:], np.random.randn())

        imgui.begin("Hello World", imgui.Bool(True),
            imgui.WindowFlags.NoTitleBar | imgui.WindowFlags.NoResize | imgui.WindowFlags.NoMove)
        imgui.set_window_pos(imgui.Vec2(0,0))
        width, height = self.get_window_size()
        imgui.set_window_size(imgui.Vec2(width, height))

        imgui.text("Hello World from ImGui!")

        implot.set_next_plot_limits(0, 1000, -2, 2)
        if (implot.begin_plot("##Plot", flags= implot.Flags.NoChild)):
            implot.plot_line("Random data (normally distributed)", self._random)
            implot.end_plot()

        imgui.end()

if __name__ == "__main__":
    app = HelloWorld()
    app.run()
