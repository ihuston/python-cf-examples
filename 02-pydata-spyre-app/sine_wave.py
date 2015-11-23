"""Example Spyre app from https://github.com/adamhajari/spyre"""
import matplotlib
# Needed to use headless
matplotlib.use('Agg')

from spyre import server

import os


import matplotlib.pyplot as plt
import numpy as np

class SimpleSineApp(server.App):
    title = "Simple Sine App"
    inputs = [{ "input_type":"text",
                "variable_name":"freq",
                "value":5,
                "action_id":"sine_wave_plot"}]

    outputs = [{"output_type":"plot",
                "output_id":"sine_wave_plot",
                "on_page_load":True }]

    def getPlot(self, params):
        f = float(params['freq'])
        print f
        x = np.arange(0,2*np.pi,np.pi/150)
        y = np.sin(f*x)
        fig = plt.figure()
        splt1 = fig.add_subplot(1,1,1)
        splt1.plot(x,y)
        return fig

# Need to specify port for Cloud Foundry
port = int(os.getenv("PORT", 9099))

app = SimpleSineApp()
app.launch(port=port, host='0.0.0.0')

