#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Exp3_Equalizer
# Author: Jatin
# GNU Radio version: 3.10.9.2

from PyQt5 import Qt
from gnuradio import qtgui
from PyQt5 import QtCore
from gnuradio import audio
from gnuradio import blocks
from gnuradio import filter
from gnuradio.filter import firdes
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import sip



class Exp3_Equalizer(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Exp3_Equalizer", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Exp3_Equalizer")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except BaseException as exc:
            print(f"Qt GUI: Could not set Icon: {str(exc)}", file=sys.stderr)
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

        self.settings = Qt.QSettings("GNU Radio", "Exp3_Equalizer")

        try:
            geometry = self.settings.value("geometry")
            if geometry:
                self.restoreGeometry(geometry)
        except BaseException as exc:
            print(f"Qt GUI: Could not restore geometry: {str(exc)}", file=sys.stderr)

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 48000
        self.g5 = g5 = 5
        self.g4 = g4 = 5
        self.g3 = g3 = 5
        self.g2 = g2 = 5
        self.g1 = g1 = 5

        ##################################################
        # Blocks
        ##################################################

        self._g5_range = qtgui.Range(0, 10, 1, 5, 200)
        self._g5_win = qtgui.RangeWidget(self._g5_range, self.set_g5, "'g5'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._g5_win)
        self._g4_range = qtgui.Range(0, 10, 1, 5, 200)
        self._g4_win = qtgui.RangeWidget(self._g4_range, self.set_g4, "'g4'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._g4_win)
        self._g3_range = qtgui.Range(0, 10, 1, 5, 200)
        self._g3_win = qtgui.RangeWidget(self._g3_range, self.set_g3, "'g3'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._g3_win)
        self._g2_range = qtgui.Range(0, 10, 1, 5, 200)
        self._g2_win = qtgui.RangeWidget(self._g2_range, self.set_g2, "'g2'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._g2_win)
        self._g1_range = qtgui.Range(0, 10, 1, 5, 200)
        self._g1_win = qtgui.RangeWidget(self._g1_range, self.set_g1, "'g1'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._g1_win)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_f(
            1024, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "", #name
            1,
            None # parent
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis((-140), 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)
        self.qtgui_freq_sink_x_0.set_fft_window_normalized(False)


        self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self.blocks_wavfile_source_0 = blocks.wavfile_source('/home/jatin/Desktop/IITB_Files/EE341/22B3922_Lab01/Bach.wav', True)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.band_pass_filter_0_3 = filter.fir_filter_fff(
            1,
            firdes.band_pass(
                g5,
                samp_rate,
                9000,
                15000,
                400,
                window.WIN_RECTANGULAR,
                6.76))
        self.band_pass_filter_0_2 = filter.fir_filter_fff(
            1,
            firdes.band_pass(
                g4,
                samp_rate,
                6000,
                9000,
                200,
                window.WIN_RECTANGULAR,
                6.76))
        self.band_pass_filter_0_1 = filter.fir_filter_fff(
            1,
            firdes.band_pass(
                g3,
                samp_rate,
                3000,
                6000,
                100,
                window.WIN_RECTANGULAR,
                6.76))
        self.band_pass_filter_0_0 = filter.fir_filter_fff(
            1,
            firdes.band_pass(
                g2,
                samp_rate,
                500,
                3000,
                100,
                window.WIN_RECTANGULAR,
                6.76))
        self.band_pass_filter_0 = filter.fir_filter_fff(
            1,
            firdes.band_pass(
                g1,
                samp_rate,
                20,
                500,
                20,
                window.WIN_RECTANGULAR,
                6.76))
        self.audio_sink_0 = audio.sink(samp_rate, '', True)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.band_pass_filter_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.band_pass_filter_0_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.band_pass_filter_0_1, 0), (self.blocks_add_xx_0, 2))
        self.connect((self.band_pass_filter_0_2, 0), (self.blocks_add_xx_0, 3))
        self.connect((self.band_pass_filter_0_3, 0), (self.blocks_add_xx_0, 4))
        self.connect((self.blocks_add_xx_0, 0), (self.audio_sink_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.band_pass_filter_0, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.band_pass_filter_0_0, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.band_pass_filter_0_1, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.band_pass_filter_0_2, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.band_pass_filter_0_3, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "Exp3_Equalizer")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.band_pass_filter_0.set_taps(firdes.band_pass(self.g1, self.samp_rate, 20, 500, 20, window.WIN_RECTANGULAR, 6.76))
        self.band_pass_filter_0_0.set_taps(firdes.band_pass(self.g2, self.samp_rate, 500, 3000, 100, window.WIN_RECTANGULAR, 6.76))
        self.band_pass_filter_0_1.set_taps(firdes.band_pass(self.g3, self.samp_rate, 3000, 6000, 100, window.WIN_RECTANGULAR, 6.76))
        self.band_pass_filter_0_2.set_taps(firdes.band_pass(self.g4, self.samp_rate, 6000, 9000, 200, window.WIN_RECTANGULAR, 6.76))
        self.band_pass_filter_0_3.set_taps(firdes.band_pass(self.g5, self.samp_rate, 9000, 15000, 400, window.WIN_RECTANGULAR, 6.76))
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)

    def get_g5(self):
        return self.g5

    def set_g5(self, g5):
        self.g5 = g5
        self.band_pass_filter_0_3.set_taps(firdes.band_pass(self.g5, self.samp_rate, 9000, 15000, 400, window.WIN_RECTANGULAR, 6.76))

    def get_g4(self):
        return self.g4

    def set_g4(self, g4):
        self.g4 = g4
        self.band_pass_filter_0_2.set_taps(firdes.band_pass(self.g4, self.samp_rate, 6000, 9000, 200, window.WIN_RECTANGULAR, 6.76))

    def get_g3(self):
        return self.g3

    def set_g3(self, g3):
        self.g3 = g3
        self.band_pass_filter_0_1.set_taps(firdes.band_pass(self.g3, self.samp_rate, 3000, 6000, 100, window.WIN_RECTANGULAR, 6.76))

    def get_g2(self):
        return self.g2

    def set_g2(self, g2):
        self.g2 = g2
        self.band_pass_filter_0_0.set_taps(firdes.band_pass(self.g2, self.samp_rate, 500, 3000, 100, window.WIN_RECTANGULAR, 6.76))

    def get_g1(self):
        return self.g1

    def set_g1(self, g1):
        self.g1 = g1
        self.band_pass_filter_0.set_taps(firdes.band_pass(self.g1, self.samp_rate, 20, 500, 20, window.WIN_RECTANGULAR, 6.76))




def main(top_block_cls=Exp3_Equalizer, options=None):

    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
