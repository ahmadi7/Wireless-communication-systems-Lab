#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Costa Loop Demonstration
# Author: Alexandros-Apostolos A. Boulogeorgos
# Generated: Mon Aug 12 16:51:38 2019
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import blocks
from gnuradio import channels
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import numpy
import sip
import sys


class costa_loop(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Costa Loop Demonstration")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Costa Loop Demonstration")
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "costa_loop")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.sps = sps = 4
        self.nfilts = nfilts = 32
        self.timing_loop_bw = timing_loop_bw = 6.28/100.0
        self.time_offset = time_offset = 1.00
        self.taps = taps = [1.0 + 0.0j, ]
        self.samp_rate = samp_rate = 32000
        self.rrc_taps = rrc_taps = firdes.root_raised_cosine(nfilts, nfilts, 1.0/float(sps), 0.35, 11*sps*nfilts)
        self.phase_bw = phase_bw = 6.28/100.0
        self.noise_volt = noise_volt = 0.0001
        self.freq_offset = freq_offset = 0
        self.eq_gain = eq_gain = 0.01
        self.arity = arity = 4

        ##################################################
        # Blocks
        ##################################################
        self._timing_loop_bw_range = Range(0.0, 0.2, 0.01, 6.28/100.0, 200)
        self._timing_loop_bw_win = RangeWidget(self._timing_loop_bw_range, self.set_timing_loop_bw, 'Time: BW', "slider", float)
        self.top_grid_layout.addWidget(self._timing_loop_bw_win, 0,3,1,1)
        self._time_offset_range = Range(0.999, 1.001, 0.0001, 1.00, 200)
        self._time_offset_win = RangeWidget(self._time_offset_range, self.set_time_offset, 'Channel: Timing Offset', "slider", float)
        self.top_grid_layout.addWidget(self._time_offset_win, 0,2,1,1)
        self._phase_bw_range = Range(0.0, 1.0, 0.01, 6.28/100.0, 200)
        self._phase_bw_win = RangeWidget(self._phase_bw_range, self.set_phase_bw, 'Phase: Bandwidth', "slider", float)
        self.top_grid_layout.addWidget(self._phase_bw_win, 1,2,1,1)
        self._noise_volt_range = Range(0, 1, 0.01, 0.0001, 200)
        self._noise_volt_win = RangeWidget(self._noise_volt_range, self.set_noise_volt, 'Channel: Noise Voltage', "slider", float)
        self.top_grid_layout.addWidget(self._noise_volt_win, 0,0,1,1)
        self._freq_offset_range = Range(-0.1, 0.1, 0.001, 0, 200)
        self._freq_offset_win = RangeWidget(self._freq_offset_range, self.set_freq_offset, 'Channel: Frequency Offset', "slider", float)
        self.top_grid_layout.addWidget(self._freq_offset_win, 0,1,1,1)
        self._eq_gain_range = Range(0.0, 0.1, 0.001, 0.01, 200)
        self._eq_gain_win = RangeWidget(self._eq_gain_range, self.set_eq_gain, 'Equalizer: rate', "slider", float)
        self.top_grid_layout.addWidget(self._eq_gain_win, 1,0,1,1)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	4000, #size
        	samp_rate, #samp_rate
        	'After Costas Loop', #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.01)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)
        
        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")
        
        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_0.disable_legend()
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_win, 3,2,1,1)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	4096, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	'QT GUI Plot', #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(0.05)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_freq_sink_x_0.disable_legend()
        
        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_win, 3,3,1,1)
        self.qtgui_const_sink_x_1_1 = qtgui.const_sink_c(
        	1024, #size
        	'After CMA equalizer', #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_1_1.set_update_time(0.10)
        self.qtgui_const_sink_x_1_1.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_1_1.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_1_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_1_1.enable_autoscale(False)
        self.qtgui_const_sink_x_1_1.enable_grid(False)
        self.qtgui_const_sink_x_1_1.enable_axis_labels(True)
        
        if not True:
          self.qtgui_const_sink_x_1_1.disable_legend()
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_1_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_1_1.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_1_1.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_1_1.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_1_1.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_1_1.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_1_1.set_line_alpha(i, alphas[i])
        
        self._qtgui_const_sink_x_1_1_win = sip.wrapinstance(self.qtgui_const_sink_x_1_1.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_1_1_win, 3,0,1,1)
        self.qtgui_const_sink_x_1_0_0_0 = qtgui.const_sink_c(
        	1024, #size
        	'After constant multiplication', #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_1_0_0_0.set_update_time(0.10)
        self.qtgui_const_sink_x_1_0_0_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_1_0_0_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_1_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_1_0_0_0.enable_autoscale(False)
        self.qtgui_const_sink_x_1_0_0_0.enable_grid(False)
        self.qtgui_const_sink_x_1_0_0_0.enable_axis_labels(True)
        
        if not True:
          self.qtgui_const_sink_x_1_0_0_0.disable_legend()
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_1_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_1_0_0_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_1_0_0_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_1_0_0_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_1_0_0_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_1_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_1_0_0_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_const_sink_x_1_0_0_0_win = sip.wrapinstance(self.qtgui_const_sink_x_1_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_1_0_0_0_win, 2,1,1,1)
        self.qtgui_const_sink_x_1_0_0 = qtgui.const_sink_c(
        	1024, #size
        	'Transmitted constellation', #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_1_0_0.set_update_time(0.10)
        self.qtgui_const_sink_x_1_0_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_1_0_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_1_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_1_0_0.enable_autoscale(False)
        self.qtgui_const_sink_x_1_0_0.enable_grid(False)
        self.qtgui_const_sink_x_1_0_0.enable_axis_labels(True)
        
        if not True:
          self.qtgui_const_sink_x_1_0_0.disable_legend()
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_1_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_1_0_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_1_0_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_1_0_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_1_0_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_1_0_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_1_0_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_const_sink_x_1_0_0_win = sip.wrapinstance(self.qtgui_const_sink_x_1_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_1_0_0_win, 2,0,1,1)
        self.qtgui_const_sink_x_1_0 = qtgui.const_sink_c(
        	1024, #size
        	'Before time synchronization ', #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_1_0.set_update_time(0.10)
        self.qtgui_const_sink_x_1_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_1_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_1_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_1_0.enable_autoscale(False)
        self.qtgui_const_sink_x_1_0.enable_grid(False)
        self.qtgui_const_sink_x_1_0.enable_axis_labels(True)
        
        if not True:
          self.qtgui_const_sink_x_1_0.disable_legend()
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_1_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_1_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_1_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_1_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_1_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_1_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_1_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_const_sink_x_1_0_win = sip.wrapinstance(self.qtgui_const_sink_x_1_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_1_0_win, 2,2,1,1)
        self.qtgui_const_sink_x_1 = qtgui.const_sink_c(
        	1024, #size
        	'After time sinchronization', #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_1.set_update_time(0.10)
        self.qtgui_const_sink_x_1.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_1.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_1.enable_autoscale(False)
        self.qtgui_const_sink_x_1.enable_grid(False)
        self.qtgui_const_sink_x_1.enable_axis_labels(True)
        
        if not True:
          self.qtgui_const_sink_x_1.disable_legend()
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_1.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_1.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_1.set_line_alpha(i, alphas[i])
        
        self._qtgui_const_sink_x_1_win = sip.wrapinstance(self.qtgui_const_sink_x_1.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_1_win, 2,3,1,1)
        self.qtgui_const_sink_x_0 = qtgui.const_sink_c(
        	1024, #size
        	'After Costas Loop', #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0.enable_grid(False)
        self.qtgui_const_sink_x_0.enable_axis_labels(True)
        
        if not True:
          self.qtgui_const_sink_x_0.disable_legend()
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_const_sink_x_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_0_win, 3,1,1,1)
        self.digital_psk_mod_0 = digital.psk.psk_mod(
          constellation_points=arity,
          mod_code="gray",
          differential=True,
          samples_per_symbol=sps,
          excess_bw=0.35,
          verbose=False,
          log=False,
          )
        self.digital_pfb_clock_sync_xxx_0 = digital.pfb_clock_sync_ccf(sps, timing_loop_bw, (rrc_taps), nfilts, nfilts/2, 1.5, 2)
        self.digital_costas_loop_cc_0 = digital.costas_loop_cc(phase_bw, arity, False)
        self.digital_cma_equalizer_cc_0 = digital.cma_equalizer_cc(15, 1, eq_gain, 2)
        self.channels_channel_model_0 = channels.channel_model(
        	noise_voltage=noise_volt,
        	frequency_offset=freq_offset,
        	epsilon=time_offset,
        	taps=(taps),
        	noise_seed=0,
        	block_tags=False
        )
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((.5+.5j, ))
        self.analog_random_source_x_0 = blocks.vector_source_b(map(int, numpy.random.randint(0, 256, 1000)), True)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_random_source_x_0, 0), (self.digital_psk_mod_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_throttle_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.qtgui_const_sink_x_1_0_0_0, 0))    
        self.connect((self.blocks_multiply_xx_0, 0), (self.qtgui_freq_sink_x_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.channels_channel_model_0, 0))    
        self.connect((self.channels_channel_model_0, 0), (self.blocks_multiply_xx_0, 0))    
        self.connect((self.channels_channel_model_0, 0), (self.blocks_multiply_xx_0, 1))    
        self.connect((self.channels_channel_model_0, 0), (self.blocks_multiply_xx_0, 2))    
        self.connect((self.channels_channel_model_0, 0), (self.blocks_multiply_xx_0, 3))    
        self.connect((self.channels_channel_model_0, 0), (self.digital_pfb_clock_sync_xxx_0, 0))    
        self.connect((self.channels_channel_model_0, 0), (self.qtgui_const_sink_x_1_0, 0))    
        self.connect((self.digital_cma_equalizer_cc_0, 0), (self.digital_costas_loop_cc_0, 0))    
        self.connect((self.digital_cma_equalizer_cc_0, 0), (self.qtgui_const_sink_x_1_1, 0))    
        self.connect((self.digital_costas_loop_cc_0, 0), (self.qtgui_const_sink_x_0, 0))    
        self.connect((self.digital_costas_loop_cc_0, 1), (self.qtgui_time_sink_x_0, 0))    
        self.connect((self.digital_pfb_clock_sync_xxx_0, 0), (self.digital_cma_equalizer_cc_0, 0))    
        self.connect((self.digital_pfb_clock_sync_xxx_0, 0), (self.qtgui_const_sink_x_1, 0))    
        self.connect((self.digital_psk_mod_0, 0), (self.blocks_multiply_const_vxx_0, 0))    
        self.connect((self.digital_psk_mod_0, 0), (self.qtgui_const_sink_x_1_0_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "costa_loop")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.set_rrc_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0/float(self.sps), 0.35, 11*self.sps*self.nfilts))

    def get_nfilts(self):
        return self.nfilts

    def set_nfilts(self, nfilts):
        self.nfilts = nfilts
        self.set_rrc_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0/float(self.sps), 0.35, 11*self.sps*self.nfilts))

    def get_timing_loop_bw(self):
        return self.timing_loop_bw

    def set_timing_loop_bw(self, timing_loop_bw):
        self.timing_loop_bw = timing_loop_bw
        self.digital_pfb_clock_sync_xxx_0.set_loop_bandwidth(self.timing_loop_bw)

    def get_time_offset(self):
        return self.time_offset

    def set_time_offset(self, time_offset):
        self.time_offset = time_offset
        self.channels_channel_model_0.set_timing_offset(self.time_offset)

    def get_taps(self):
        return self.taps

    def set_taps(self, taps):
        self.taps = taps
        self.channels_channel_model_0.set_taps((self.taps))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_rrc_taps(self):
        return self.rrc_taps

    def set_rrc_taps(self, rrc_taps):
        self.rrc_taps = rrc_taps
        self.digital_pfb_clock_sync_xxx_0.update_taps((self.rrc_taps))

    def get_phase_bw(self):
        return self.phase_bw

    def set_phase_bw(self, phase_bw):
        self.phase_bw = phase_bw
        self.digital_costas_loop_cc_0.set_loop_bandwidth(self.phase_bw)

    def get_noise_volt(self):
        return self.noise_volt

    def set_noise_volt(self, noise_volt):
        self.noise_volt = noise_volt
        self.channels_channel_model_0.set_noise_voltage(self.noise_volt)

    def get_freq_offset(self):
        return self.freq_offset

    def set_freq_offset(self, freq_offset):
        self.freq_offset = freq_offset
        self.channels_channel_model_0.set_frequency_offset(self.freq_offset)

    def get_eq_gain(self):
        return self.eq_gain

    def set_eq_gain(self, eq_gain):
        self.eq_gain = eq_gain
        self.digital_cma_equalizer_cc_0.set_gain(self.eq_gain)

    def get_arity(self):
        return self.arity

    def set_arity(self, arity):
        self.arity = arity


def main(top_block_cls=costa_loop, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()