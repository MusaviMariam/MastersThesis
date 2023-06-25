#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Video Transmitter (GMSK)
# Author: Reproduce by Mariam.
# Generated: Wed Jun 29 21:26:44 2016
##################################################
from __future__ import division
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import uhd
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import fftsink2
from grc_gnuradio import blks2 as grc_blks2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
from random import *
from numpy import *
from sets import Set
import time
import wx
import math
import numpy as np
import random
import poisson_process_v1
from random import *
import time
import random
import numpy as np
#import networkx as nx

frequ = [828e6, 833e6, 838e6, 843e6, 848e6, 853e6, 858e6, 863e6, 868e6, 873e6, 878e6, 883e6, 888e6, 893e6, 898e6, 903e6, 908e6, 913e6, 918e6]
freq = random.sample(xrange(19),6)


class Tx_1(grc_wxgui.top_block_gui):

	def __init__(self):
		grc_wxgui.top_block_gui.__init__(self, title="Video Transmitter (GMSK)")
		_icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
		self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

		##################################################
		# Variables
		##################################################
		self.samp_rate_1 = samp_rate_1 = 0.25e6
		self.sam_sym = sam_sym = 2
		self.freq6 = freq6 = frequ[freq[5]]
		self.freq5 = freq5 = frequ[freq[4]]
		self.freq4 = freq4 = frequ[freq[3]]
		self.freq3 = freq3 = frequ[freq[2]]
		self.freq2 = freq2 = frequ[freq[1]]
		self.freq1 = freq1 = frequ[freq[0]]

		##################################################
		# Blocks
		##################################################
		#self.wxgui_fftsink2_1 = fftsink2.fft_sink_c(
		#	self.GetWin(),
		#	baseband_freq=0,
		#	y_per_div=10,
		#	y_divs=10,
		#	ref_level=0,
		#	ref_scale=2.0,
		#	sample_rate=samp_rate_1,
		#	fft_size=1024,
		#	fft_rate=15,
		#	average=False,
		#	avg_alpha=None,
		#	title="FFT Plot",
		#	peak_hold=False,
		#)
		#self.Add(self.wxgui_fftsink2_1.win)

		self.uhd_usrp_sink_1 = uhd.usrp_sink(
			device_addr="addr=192.168.10.2",
			stream_args=uhd.stream_args(
				cpu_format="fc32",
				channels=range(1),
			),
		)
		self.uhd_usrp_sink_1.set_samp_rate(samp_rate_1)
		self.uhd_usrp_sink_1.set_center_freq(freq1, 0)
		self.uhd_usrp_sink_1.set_gain(1, 0)
		self.uhd_usrp_sink_1.set_antenna("TX/RX", 0)
		self.digital_gmsk_mod_1 = digital.gmsk_mod(
			samples_per_symbol=sam_sym,
			bt=0.35,
			verbose=False,
			log=False,
		)
		self.blocks_udp_source_1 = blocks.udp_source(gr.sizeof_char*1, "127.0.0.1", 1234, 12000, True)
		self.blks2_packet_encoder_1 = grc_blks2.packet_mod_b(grc_blks2.packet_encoder(
				samples_per_symbol=sam_sym,
				bits_per_symbol=1,
				preamble="",
				access_code="",
				pad_for_usrp=True,
			),
			payload_length=0,
		)

		##################################################
		# Connections
		##################################################
		#self.connect((self.digital_gmsk_mod_1, 0), (self.wxgui_fftsink2_1, 0))
		self.connect((self.digital_gmsk_mod_1, 0), (self.uhd_usrp_sink_1, 0))
		self.connect((self.blks2_packet_encoder_1, 0), (self.digital_gmsk_mod_1, 0))
		self.connect((self.blocks_udp_source_1, 0), (self.blks2_packet_encoder_1, 0))


# QT sink close method reimplementation

	def get_samp_rate_1(self):
		return self.samp_rate_1

	def set_samp_rate_1(self, samp_rate_1):
		self.samp_rate_1 = samp_rate_1
		self.uhd_usrp_sink_1.set_samp_rate(self.samp_rate_1)
	#	self.wxgui_fftsink2_1.set_sample_rate(self.samp_rate_1)

	def get_sam_sym(self):
		return self.sam_sym

	def set_sam_sym(self, sam_sym):
		self.sam_sym = sam_sym

	def get_freq6(self):
		return self.freq6

	def set_freq6(self, freq6):
		self.freq6 = freq6

	def get_freq5(self):
		return self.freq5

	def set_freq5(self, freq5):
		self.freq5 = freq5

	def get_freq4(self):
		return self.freq4

	def set_freq4(self, freq4):
		self.freq4 = freq4

	def get_freq3(self):
		return self.freq3

	def set_freq3(self, freq3):
		self.freq3 = freq3

	def get_freq2(self):
		return self.freq2

	def set_freq2(self, freq2):
		self.freq2 = freq2

	def get_freq1(self):
		return self.freq1

	def set_freq1(self, freq1):
		self.freq1 = freq1
		self.uhd_usrp_sink_1.set_center_freq(self.freq1, 0)

class Rx_Tx_2(grc_wxgui.top_block_gui):

	def __init__(self):
		grc_wxgui.top_block_gui.__init__(self, title="Rx Tx 2")
		_icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
		self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

		##################################################
		# Variables
		##################################################
		self.samp_rate_2 = samp_rate_2 = .25e6
		self.sam_sym = sam_sym = 2
		self.freq2 = freq2 = frequ[freq[1]]
		self.freq1 = freq1 = frequ[freq[0]]

		##################################################
		# Blocks
		##################################################
		self.uhd_usrp_source_2 = uhd.usrp_source(
			device_addr="addr=192.168.10.3",
			stream_args=uhd.stream_args(
				cpu_format="fc32",
				channels=range(1),
			),
		)
		self.uhd_usrp_source_2.set_samp_rate(samp_rate_2)
		self.uhd_usrp_source_2.set_center_freq(freq1, 0)
		self.uhd_usrp_source_2.set_gain(1, 0)
		self.uhd_usrp_source_2.set_antenna("RX2", 0)
		self.uhd_usrp_sink_2 = uhd.usrp_sink(
			device_addr="addr=192.168.10.3",
			stream_args=uhd.stream_args(
				cpu_format="fc32",
				channels=range(1),
			),
		)
		self.uhd_usrp_sink_2.set_samp_rate(samp_rate_2)
		self.uhd_usrp_sink_2.set_center_freq(freq2, 0)
		self.uhd_usrp_sink_2.set_gain(1, 0)
		self.uhd_usrp_sink_2.set_antenna("TX/RX", 0)
		self.digital_gmsk_mod_2 = digital.gmsk_mod(
			samples_per_symbol=sam_sym,
			bt=0.5,
			verbose=False,
			log=False,
		)
		self.digital_gmsk_demod_2 = digital.gmsk_demod(
			samples_per_symbol=sam_sym,
			gain_mu=0.175,
			mu=0.5,
			omega_relative_limit=0.005,
			freq_error=0.0,
			verbose=False,
			log=False,
		)
		self.blocks_multiply_const_vxx_2 = blocks.multiply_const_vcc((1, ))
		self.blks2_packet_encoder_2 = grc_blks2.packet_mod_c(grc_blks2.packet_encoder(
				samples_per_symbol=sam_sym,
				bits_per_symbol=1,
				preamble="",
				access_code="",
				pad_for_usrp=True,
			),
			payload_length=0,
		)
		self.blks2_packet_decoder_2 = grc_blks2.packet_demod_c(grc_blks2.packet_decoder(
				access_code="",
				threshold=-1,
				callback=lambda ok, payload: self.blks2_packet_decoder_2.recv_pkt(ok, payload),
			),
		)

		##################################################
		# Connections
		##################################################
		self.connect((self.digital_gmsk_mod_2, 0), (self.blocks_multiply_const_vxx_2, 0))
		self.connect((self.blocks_multiply_const_vxx_2, 0), (self.uhd_usrp_sink_2, 0))
		self.connect((self.blks2_packet_encoder_2, 0), (self.digital_gmsk_mod_2, 0))
		self.connect((self.uhd_usrp_source_2, 0), (self.digital_gmsk_demod_2, 0))
		self.connect((self.blks2_packet_decoder_2, 0), (self.blks2_packet_encoder_2, 0))
		self.connect((self.digital_gmsk_demod_2, 0), (self.blks2_packet_decoder_2, 0))


# QT sink close method reimplementation

	def get_samp_rate_2(self):
		return self.samp_rate_2

	def set_samp_rate_2(self, samp_rate_2):
		self.samp_rate_2 = samp_rate_2
		self.uhd_usrp_source_2.set_samp_rate(self.samp_rate_2)
		self.uhd_usrp_sink_2.set_samp_rate(self.samp_rate_2)

	def get_sam_sym(self):
		return self.sam_sym

	def set_sam_sym(self, sam_sym):
		self.sam_sym = sam_sym

	def get_freq2(self):
		return self.freq2

	def set_freq2(self, freq2):
		self.freq2 = freq2
		self.uhd_usrp_sink_2.set_center_freq(self.freq2, 0)

	def get_freq1(self):
		return self.freq1

	def set_freq1(self, freq1):
		self.freq1 = freq1
		self.uhd_usrp_source_2.set_center_freq(self.freq1, 0)

class Rx_Tx_3(grc_wxgui.top_block_gui):

	def __init__(self):
		grc_wxgui.top_block_gui.__init__(self, title="Rx Tx 3")
		_icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
		self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

		##################################################
		# Variables
		##################################################
		self.samp_rate_3 = samp_rate_3 = .25e6
		self.sam_sym = sam_sym = 2
		self.freq2 = freq2 = frequ[freq[1]]
		self.freq1 = freq1 = frequ[freq[0]]

		##################################################
		# Blocks
		##################################################
		self.uhd_usrp_source_3 = uhd.usrp_source(
			device_addr="addr=192.168.10.4",
			stream_args=uhd.stream_args(
				cpu_format="fc32",
				channels=range(1),
			),
		)
		self.uhd_usrp_source_3.set_samp_rate(samp_rate_3)
		self.uhd_usrp_source_3.set_center_freq(freq1, 0)
		self.uhd_usrp_source_3.set_gain(1, 0)
		self.uhd_usrp_source_3.set_antenna("RX2", 0)
		self.uhd_usrp_sink_3 = uhd.usrp_sink(
			device_addr="addr=192.168.10.4",
			stream_args=uhd.stream_args(
				cpu_format="fc32",
				channels=range(1),
			),
		)
		self.uhd_usrp_sink_3.set_samp_rate(samp_rate_3)
		self.uhd_usrp_sink_3.set_center_freq(freq2, 0)
		self.uhd_usrp_sink_3.set_gain(1, 0)
		self.uhd_usrp_sink_3.set_antenna("TX/RX", 0)
		self.digital_gmsk_mod_3 = digital.gmsk_mod(
			samples_per_symbol=sam_sym,
			bt=0.5,
			verbose=False,
			log=False,
		)
		self.digital_gmsk_demod_3 = digital.gmsk_demod(
			samples_per_symbol=sam_sym,
			gain_mu=0.175,
			mu=0.5,
			omega_relative_limit=0.005,
			freq_error=0.0,
			verbose=False,
			log=False,
		)
		self.blocks_multiply_const_vxx_3 = blocks.multiply_const_vcc((1, ))
		self.blks2_packet_encoder_3 = grc_blks2.packet_mod_c(grc_blks2.packet_encoder(
				samples_per_symbol=sam_sym,
				bits_per_symbol=1,
				preamble="",
				access_code="",
				pad_for_usrp=True,
			),
			payload_length=0,
		)
		self.blks2_packet_decoder_3 = grc_blks2.packet_demod_c(grc_blks2.packet_decoder(
				access_code="",
				threshold=-1,
				callback=lambda ok, payload: self.blks2_packet_decoder_3.recv_pkt(ok, payload),
			),
		)

		##################################################
		# Connections
		##################################################
		self.connect((self.digital_gmsk_demod_3, 0), (self.blks2_packet_decoder_3, 0))
		self.connect((self.blks2_packet_decoder_3, 0), (self.blks2_packet_encoder_3, 0))
		self.connect((self.uhd_usrp_source_3, 0), (self.digital_gmsk_demod_3, 0))
		self.connect((self.blks2_packet_encoder_3, 0), (self.digital_gmsk_mod_3, 0))
		self.connect((self.blocks_multiply_const_vxx_3, 0), (self.uhd_usrp_sink_3, 0))
		self.connect((self.digital_gmsk_mod_3, 0), (self.blocks_multiply_const_vxx_3, 0))


# QT sink close method reimplementation

	def get_samp_rate_3(self):
		return self.samp_rate_3

	def set_samp_rate_3(self, samp_rate_3):
		self.samp_rate_3 = samp_rate_3
		self.uhd_usrp_source_3.set_samp_rate(self.samp_rate_3)
		self.uhd_usrp_sink_3.set_samp_rate(self.samp_rate_3)

	def get_sam_sym(self):
		return self.sam_sym

	def set_sam_sym(self, sam_sym):
		self.sam_sym = sam_sym

	def get_freq2(self):
		return self.freq2

	def set_freq2(self, freq2):
		self.freq2 = freq2
		self.uhd_usrp_sink_3.set_center_freq(self.freq2, 0)

	def get_freq1(self):
		return self.freq1

	def set_freq1(self, freq1):
		self.freq1 = freq1
		self.uhd_usrp_source_3.set_center_freq(self.freq1, 0)

class Rx_Tx_4(grc_wxgui.top_block_gui):

	def __init__(self):
		grc_wxgui.top_block_gui.__init__(self, title="Rx Tx 4")
		_icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
		self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

		##################################################
		# Variables
		##################################################
		self.samp_rate_4 = samp_rate_4 = .25e6
		self.sam_sym = sam_sym = 2
		self.freq3 = freq3 = frequ[freq[2]]
		self.freq2 = freq2 = frequ[freq[1]]

		##################################################
		# Blocks
		##################################################
		self.uhd_usrp_source_4 = uhd.usrp_source(
			device_addr="addr=192.168.10.5",
			stream_args=uhd.stream_args(
				cpu_format="fc32",
				channels=range(1),
			),
		)
		self.uhd_usrp_source_4.set_samp_rate(samp_rate_4)
		self.uhd_usrp_source_4.set_center_freq(freq2, 0)
		self.uhd_usrp_source_4.set_gain(1, 0)
		self.uhd_usrp_source_4.set_antenna("RX2", 0)
		self.uhd_usrp_sink_4 = uhd.usrp_sink(
			device_addr="addr=192.168.10.5",
			stream_args=uhd.stream_args(
				cpu_format="fc32",
				channels=range(1),
			),
		)
		self.uhd_usrp_sink_4.set_samp_rate(samp_rate_4)
		self.uhd_usrp_sink_4.set_center_freq(freq3, 0)
		self.uhd_usrp_sink_4.set_gain(1, 0)
		self.uhd_usrp_sink_4.set_antenna("TX/RX", 0)
		self.digital_gmsk_mod_4 = digital.gmsk_mod(
			samples_per_symbol=sam_sym,
			bt=0.5,
			verbose=False,
			log=False,
		)
		self.digital_gmsk_demod_4 = digital.gmsk_demod(
			samples_per_symbol=sam_sym,
			gain_mu=0.175,
			mu=0.5,
			omega_relative_limit=0.005,
			freq_error=0.0,
			verbose=False,
			log=False,
		)
		self.blocks_multiply_const_vxx_4 = blocks.multiply_const_vcc((1, ))
		self.blks2_packet_encoder_4 = grc_blks2.packet_mod_c(grc_blks2.packet_encoder(
				samples_per_symbol=sam_sym,
				bits_per_symbol=1,
				preamble="",
				access_code="",
				pad_for_usrp=True,
			),
			payload_length=0,
		)
		self.blks2_packet_decoder_4 = grc_blks2.packet_demod_c(grc_blks2.packet_decoder(
				access_code="",
				threshold=-1,
				callback=lambda ok, payload: self.blks2_packet_decoder_4.recv_pkt(ok, payload),
			),
		)

		##################################################
		# Connections
		##################################################
		self.connect((self.digital_gmsk_mod_4, 0), (self.blocks_multiply_const_vxx_4, 0))
		self.connect((self.blocks_multiply_const_vxx_4, 0), (self.uhd_usrp_sink_4, 0))
		self.connect((self.blks2_packet_encoder_4, 0), (self.digital_gmsk_mod_4, 0))
		self.connect((self.uhd_usrp_source_4, 0), (self.digital_gmsk_demod_4, 0))
		self.connect((self.blks2_packet_decoder_4, 0), (self.blks2_packet_encoder_4, 0))
		self.connect((self.digital_gmsk_demod_4, 0), (self.blks2_packet_decoder_4, 0))


# QT sink close method reimplementation

	def get_samp_rate_4(self):
		return self.samp_rate_4

	def set_samp_rate_4(self, samp_rate_4):
		self.samp_rate_4 = samp_rate_4
		self.uhd_usrp_source_4.set_samp_rate(self.samp_rate_4)
		self.uhd_usrp_sink_4.set_samp_rate(self.samp_rate_4)

	def get_sam_sym(self):
		return self.sam_sym

	def set_sam_sym(self, sam_sym):
		self.sam_sym = sam_sym

	def get_freq3(self):
		return self.freq3

	def set_freq3(self, freq3):
		self.freq3 = freq3
		self.uhd_usrp_sink_4.set_center_freq(self.freq3, 0)

	def get_freq2(self):
		return self.freq2

	def set_freq2(self, freq2):
		self.freq2 = freq2
		self.uhd_usrp_source_4.set_center_freq(self.freq2, 0)

class Rx_Tx_5(grc_wxgui.top_block_gui):

	def __init__(self):
		grc_wxgui.top_block_gui.__init__(self, title="Rx Tx 5")
		_icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
		self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

		##################################################
		# Variables
		##################################################
		self.samp_rate_5 = samp_rate_5 = .25e6
		self.sam_sym = sam_sym = 2
		self.freq3 = freq3 = frequ[freq[2]]
		self.freq2 = freq2 = frequ[freq[1]]

		##################################################
		# Blocks
		##################################################
		self.uhd_usrp_source_5 = uhd.usrp_source(
			device_addr="addr=192.168.10.6",
			stream_args=uhd.stream_args(
				cpu_format="fc32",
				channels=range(1),
			),
		)
		self.uhd_usrp_source_5.set_samp_rate(samp_rate_5)
		self.uhd_usrp_source_5.set_center_freq(freq2, 0)
		self.uhd_usrp_source_5.set_gain(1, 0)
		self.uhd_usrp_source_5.set_antenna("RX2", 0)
		self.uhd_usrp_sink_5 = uhd.usrp_sink(
			device_addr="addr=192.168.10.6",
			stream_args=uhd.stream_args(
				cpu_format="fc32",
				channels=range(1),
			),
		)
		self.uhd_usrp_sink_5.set_samp_rate(samp_rate_5)
		self.uhd_usrp_sink_5.set_center_freq(freq3, 0)
		self.uhd_usrp_sink_5.set_gain(1, 0)
		self.uhd_usrp_sink_5.set_antenna("TX/RX", 0)
		self.digital_gmsk_mod_5 = digital.gmsk_mod(
			samples_per_symbol=sam_sym,
			bt=0.5,
			verbose=False,
			log=False,
		)
		self.digital_gmsk_demod_5 = digital.gmsk_demod(
			samples_per_symbol=sam_sym,
			gain_mu=0.175,
			mu=0.5,
			omega_relative_limit=0.005,
			freq_error=0.0,
			verbose=False,
			log=False,
		)
		self.blocks_multiply_const_vxx_5 = blocks.multiply_const_vcc((1, ))
		self.blks2_packet_encoder_5 = grc_blks2.packet_mod_c(grc_blks2.packet_encoder(
				samples_per_symbol=sam_sym,
				bits_per_symbol=1,
				preamble="",
				access_code="",
				pad_for_usrp=True,
			),
			payload_length=0,
		)
		self.blks2_packet_decoder_5 = grc_blks2.packet_demod_c(grc_blks2.packet_decoder(
				access_code="",
				threshold=-1,
				callback=lambda ok, payload: self.blks2_packet_decoder_5.recv_pkt(ok, payload),
			),
		)

		##################################################
		# Connections
		##################################################
		self.connect((self.digital_gmsk_demod_5, 0), (self.blks2_packet_decoder_5, 0))
		self.connect((self.blks2_packet_decoder_5, 0), (self.blks2_packet_encoder_5, 0))
		self.connect((self.uhd_usrp_source_5, 0), (self.digital_gmsk_demod_5, 0))
		self.connect((self.blks2_packet_encoder_5, 0), (self.digital_gmsk_mod_5, 0))
		self.connect((self.blocks_multiply_const_vxx_5, 0), (self.uhd_usrp_sink_5, 0))
		self.connect((self.digital_gmsk_mod_5, 0), (self.blocks_multiply_const_vxx_5, 0))


# QT sink close method reimplementation

	def get_samp_rate_5(self):
		return self.samp_rate_5

	def set_samp_rate_5(self, samp_rate_5):
		self.samp_rate_5 = samp_rate_5
		self.uhd_usrp_source_5.set_samp_rate(self.samp_rate_5)
		self.uhd_usrp_sink_5.set_samp_rate(self.samp_rate_5)

	def get_sam_sym(self):
		return self.sam_sym

	def set_sam_sym(self, sam_sym):
		self.sam_sym = sam_sym

	def get_freq3(self):
		return self.freq3

	def set_freq3(self, freq3):
		self.freq3 = freq3
		self.uhd_usrp_sink_5.set_center_freq(self.freq3, 0)

	def get_freq2(self):
		return self.freq2

	def set_freq2(self, freq2):
		self.freq2 = freq2
		self.uhd_usrp_source_5.set_center_freq(self.freq2, 0)

class Rx_Tx_6(grc_wxgui.top_block_gui):

	def __init__(self):
		grc_wxgui.top_block_gui.__init__(self, title="Rx Tx 6")
		_icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
		self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

		##################################################
		# Variables
		##################################################
		self.samp_rate_6 = samp_rate_6 = .25e6
		self.sam_sym = sam_sym = 2
		self.freq3 = freq3 = frequ[freq[2]]
		self.freq2 = freq2 = frequ[freq[1]]

		##################################################
		# Blocks
		##################################################
		self.uhd_usrp_source_6 = uhd.usrp_source(
			device_addr="addr=192.168.10.7",
			stream_args=uhd.stream_args(
				cpu_format="fc32",
				channels=range(1),
			),
		)
		self.uhd_usrp_source_6.set_samp_rate(samp_rate_6)
		self.uhd_usrp_source_6.set_center_freq(freq2, 0)
		self.uhd_usrp_source_6.set_gain(1, 0)
		self.uhd_usrp_source_6.set_antenna("RX2", 0)
		self.uhd_usrp_sink_6 = uhd.usrp_sink(
			device_addr="addr=192.168.10.7",
			stream_args=uhd.stream_args(
				cpu_format="fc32",
				channels=range(1),
			),
		)
		self.uhd_usrp_sink_6.set_samp_rate(samp_rate_6)
		self.uhd_usrp_sink_6.set_center_freq(freq3, 0)
		self.uhd_usrp_sink_6.set_gain(1, 0)
		self.uhd_usrp_sink_6.set_antenna("TX/RX", 0)
		self.digital_gmsk_mod_6 = digital.gmsk_mod(
			samples_per_symbol=sam_sym,
			bt=0.5,
			verbose=False,
			log=False,
		)
		self.digital_gmsk_demod_6 = digital.gmsk_demod(
			samples_per_symbol=sam_sym,
			gain_mu=0.175,
			mu=0.5,
			omega_relative_limit=0.005,
			freq_error=0.0,
			verbose=False,
			log=False,
		)
		self.blocks_multiply_const_vxx_6 = blocks.multiply_const_vcc((1, ))
		self.blks2_packet_encoder_6 = grc_blks2.packet_mod_c(grc_blks2.packet_encoder(
				samples_per_symbol=sam_sym,
				bits_per_symbol=1,
				preamble="",
				access_code="",
				pad_for_usrp=True,
			),
			payload_length=0,
		)
		self.blks2_packet_decoder_6 = grc_blks2.packet_demod_c(grc_blks2.packet_decoder(
				access_code="",
				threshold=-1,
				callback=lambda ok, payload: self.blks2_packet_decoder_6.recv_pkt(ok, payload),
			),
		)

		##################################################
		# Connections
		##################################################
		self.connect((self.digital_gmsk_mod_6, 0), (self.blocks_multiply_const_vxx_6, 0))
		self.connect((self.blocks_multiply_const_vxx_6, 0), (self.uhd_usrp_sink_6, 0))
		self.connect((self.blks2_packet_encoder_6, 0), (self.digital_gmsk_mod_6, 0))
		self.connect((self.uhd_usrp_source_6, 0), (self.digital_gmsk_demod_6, 0))
		self.connect((self.blks2_packet_decoder_6, 0), (self.blks2_packet_encoder_6, 0))
		self.connect((self.digital_gmsk_demod_6, 0), (self.blks2_packet_decoder_6, 0))


# QT sink close method reimplementation

	def get_samp_rate_6(self):
		return self.samp_rate_6

	def set_samp_rate_6(self, samp_rate_6):
		self.samp_rate_6 = samp_rate_6
		self.uhd_usrp_source_6.set_samp_rate(self.samp_rate_6)
		self.uhd_usrp_sink_6.set_samp_rate(self.samp_rate_6)

	def get_sam_sym(self):
		return self.sam_sym

	def set_sam_sym(self, sam_sym):
		self.sam_sym = sam_sym

	def get_freq3(self):
		return self.freq3

	def set_freq3(self, freq3):
		self.freq3 = freq3
		self.uhd_usrp_sink_6.set_center_freq(self.freq3, 0)

	def get_freq2(self):
		return self.freq2

	def set_freq2(self, freq2):
		self.freq2 = freq2
		self.uhd_usrp_source_6.set_center_freq(self.freq2, 0)



class Rx_Tx_7(grc_wxgui.top_block_gui):

	def __init__(self):
		grc_wxgui.top_block_gui.__init__(self, title="Rx Tx 7")
		_icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
		self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

		##################################################
		# Variables
		##################################################
		self.samp_rate_7 = samp_rate_7 = .25e6
		self.sam_sym = sam_sym = 2
		self.freq4 = freq4 = frequ[freq[3]]
		self.freq3 = freq3 = frequ[freq[2]]

		##################################################
		# Blocks
		##################################################
		self.uhd_usrp_source_7 = uhd.usrp_source(
			device_addr="addr=192.168.10.8",
			stream_args=uhd.stream_args(
				cpu_format="fc32",
				channels=range(1),
			),
		)
		self.uhd_usrp_source_7.set_samp_rate(samp_rate_7)
		self.uhd_usrp_source_7.set_center_freq(freq3, 0)
		self.uhd_usrp_source_7.set_gain(1, 0)
		self.uhd_usrp_source_7.set_antenna("RX2", 0)
		self.uhd_usrp_sink_7 = uhd.usrp_sink(
			device_addr="addr=192.168.10.8",
			stream_args=uhd.stream_args(
				cpu_format="fc32",
				channels=range(1),
			),
		)
		self.uhd_usrp_sink_7.set_samp_rate(samp_rate_7)
		self.uhd_usrp_sink_7.set_center_freq(freq4, 0)
		self.uhd_usrp_sink_7.set_gain(1, 0)
		self.uhd_usrp_sink_7.set_antenna("TX/RX", 0)
		self.digital_gmsk_mod_7 = digital.gmsk_mod(
			samples_per_symbol=sam_sym,
			bt=0.5,
			verbose=False,
			log=False,
		)
		self.digital_gmsk_demod_7 = digital.gmsk_demod(
			samples_per_symbol=sam_sym,
			gain_mu=0.175,
			mu=0.5,
			omega_relative_limit=0.005,
			freq_error=0.0,
			verbose=False,
			log=False,
		)
		self.blocks_multiply_const_vxx_7 = blocks.multiply_const_vcc((1, ))
		self.blks2_packet_encoder_7 = grc_blks2.packet_mod_c(grc_blks2.packet_encoder(
				samples_per_symbol=sam_sym,
				bits_per_symbol=1,
				preamble="",
				access_code="",
				pad_for_usrp=True,
			),
			payload_length=0,
		)
		self.blks2_packet_decoder_7 = grc_blks2.packet_demod_c(grc_blks2.packet_decoder(
				access_code="",
				threshold=-1,
				callback=lambda ok, payload: self.blks2_packet_decoder_7.recv_pkt(ok, payload),
			),
		)

		##################################################
		# Connections
		##################################################
		self.connect((self.digital_gmsk_demod_7, 0), (self.blks2_packet_decoder_7, 0))
		self.connect((self.blks2_packet_decoder_7, 0), (self.blks2_packet_encoder_7, 0))
		self.connect((self.uhd_usrp_source_7, 0), (self.digital_gmsk_demod_7, 0))
		self.connect((self.blks2_packet_encoder_7, 0), (self.digital_gmsk_mod_7, 0))
		self.connect((self.blocks_multiply_const_vxx_7, 0), (self.uhd_usrp_sink_7, 0))
		self.connect((self.digital_gmsk_mod_7, 0), (self.blocks_multiply_const_vxx_7, 0))


# QT sink close method reimplementation

	def get_samp_rate_7(self):
		return self.samp_rate_7

	def set_samp_rate_7(self, samp_rate_7):
		self.samp_rate_7 = samp_rate_7
		self.uhd_usrp_source_7.set_samp_rate(self.samp_rate_7)
		self.uhd_usrp_sink_7.set_samp_rate(self.samp_rate_7)

	def get_sam_sym(self):
		return self.sam_sym

	def set_sam_sym(self, sam_sym):
		self.sam_sym = sam_sym

	def get_freq4(self):
		return self.freq4

	def set_freq4(self, freq4):
		self.freq4 = freq4
		self.uhd_usrp_sink_7.set_center_freq(self.freq4, 0)

	def get_freq3(self):
		return self.freq3

	def set_freq3(self, freq3):
		self.freq3 = freq3
		self.uhd_usrp_source_7.set_center_freq(self.freq3, 0)

class Rx_Tx_8(grc_wxgui.top_block_gui):

	def __init__(self):
		grc_wxgui.top_block_gui.__init__(self, title="Rx Tx 8")
		_icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
		self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

		##################################################
		# Variables
		##################################################
		self.samp_rate_8 = samp_rate_8 = .25e6
		self.sam_sym = sam_sym = 2
		self.freq4 = freq4 = frequ[freq[3]]
		self.freq3 = freq3 = frequ[freq[2]]

		##################################################
		# Blocks
		##################################################
		self.uhd_usrp_source_8 = uhd.usrp_source(
			device_addr="addr=192.168.10.9",
			stream_args=uhd.stream_args(
				cpu_format="fc32",
				channels=range(1),
			),
		)
		self.uhd_usrp_source_8.set_samp_rate(samp_rate_8)
		self.uhd_usrp_source_8.set_center_freq(freq3, 0)
		self.uhd_usrp_source_8.set_gain(1, 0)
		self.uhd_usrp_source_8.set_antenna("RX2", 0)
		self.uhd_usrp_sink_8 = uhd.usrp_sink(
			device_addr="addr=192.168.10.9",
			stream_args=uhd.stream_args(
				cpu_format="fc32",
				channels=range(1),
			),
		)
		self.uhd_usrp_sink_8.set_samp_rate(samp_rate_8)
		self.uhd_usrp_sink_8.set_center_freq(freq4, 0)
		self.uhd_usrp_sink_8.set_gain(1, 0)
		self.uhd_usrp_sink_8.set_antenna("TX/RX", 0)
		self.digital_gmsk_mod_8 = digital.gmsk_mod(
			samples_per_symbol=sam_sym,
			bt=0.5,
			verbose=False,
			log=False,
		)
		self.digital_gmsk_demod_8 = digital.gmsk_demod(
			samples_per_symbol=sam_sym,
			gain_mu=0.175,
			mu=0.5,
			omega_relative_limit=0.005,
			freq_error=0.0,
			verbose=False,
			log=False,
		)
		self.blocks_multiply_const_vxx_8 = blocks.multiply_const_vcc((1, ))
		self.blks2_packet_encoder_8 = grc_blks2.packet_mod_c(grc_blks2.packet_encoder(
				samples_per_symbol=sam_sym,
				bits_per_symbol=1,
				preamble="",
				access_code="",
				pad_for_usrp=True,
			),
			payload_length=0,
		)
		self.blks2_packet_decoder_8 = grc_blks2.packet_demod_c(grc_blks2.packet_decoder(
				access_code="",
				threshold=-1,
				callback=lambda ok, payload: self.blks2_packet_decoder_8.recv_pkt(ok, payload),
			),
		)

		##################################################
		# Connections
		##################################################
		self.connect((self.digital_gmsk_mod_8, 0), (self.blocks_multiply_const_vxx_8, 0))
		self.connect((self.blocks_multiply_const_vxx_8, 0), (self.uhd_usrp_sink_8, 0))
		self.connect((self.blks2_packet_encoder_8, 0), (self.digital_gmsk_mod_8, 0))
		self.connect((self.uhd_usrp_source_8, 0), (self.digital_gmsk_demod_8, 0))
		self.connect((self.blks2_packet_decoder_8, 0), (self.blks2_packet_encoder_8, 0))
		self.connect((self.digital_gmsk_demod_8, 0), (self.blks2_packet_decoder_8, 0))


# QT sink close method reimplementation

	def get_samp_rate_8(self):
		return self.samp_rate_8

	def set_samp_rate_8(self, samp_rate_8):
		self.samp_rate_8 = samp_rate_8
		self.uhd_usrp_source_8.set_samp_rate(self.samp_rate_8)
		self.uhd_usrp_sink_8.set_samp_rate(self.samp_rate_8)

	def get_sam_sym(self):
		return self.sam_sym

	def set_sam_sym(self, sam_sym):
		self.sam_sym = sam_sym

	def get_freq4(self):
		return self.freq4

	def set_freq4(self, freq4):
		self.freq4 = freq4
		self.uhd_usrp_sink_8.set_center_freq(self.freq4, 0)

	def get_freq3(self):
		return self.freq3

	def set_freq3(self, freq3):
		self.freq3 = freq3
		self.uhd_usrp_source_8.set_center_freq(self.freq3, 0)

class Rx_Tx_9(grc_wxgui.top_block_gui):

	def __init__(self):
		grc_wxgui.top_block_gui.__init__(self, title="Rx Tx 9")
		_icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
		self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

		##################################################
		# Variables
		##################################################
		self.samp_rate_9 = samp_rate_9 = .25e6
		self.sam_sym = sam_sym = 2
		self.freq6 = freq6 = frequ[freq[5]]
		self.freq4 = freq4 = frequ[freq[3]]

		##################################################
		# Blocks
		##################################################
		self.uhd_usrp_source_9 = uhd.usrp_source(
			device_addr="addr=192.168.10.10",
			stream_args=uhd.stream_args(
				cpu_format="fc32",
				channels=range(1),
			),
		)
		self.uhd_usrp_source_9.set_samp_rate(samp_rate_9)
		self.uhd_usrp_source_9.set_center_freq(freq4, 0)
		self.uhd_usrp_source_9.set_gain(1, 0)
		self.uhd_usrp_source_9.set_antenna("RX2", 0)
		self.uhd_usrp_sink_9 = uhd.usrp_sink(
			device_addr="addr=192.168.10.10",
			stream_args=uhd.stream_args(
				cpu_format="fc32",
				channels=range(1),
			),
		)
		self.uhd_usrp_sink_9.set_samp_rate(samp_rate_9)
		self.uhd_usrp_sink_9.set_center_freq(freq6, 0)
		self.uhd_usrp_sink_9.set_gain(1, 0)
		self.uhd_usrp_sink_9.set_antenna("TX/RX", 0)
		self.digital_gmsk_mod_9 = digital.gmsk_mod(
			samples_per_symbol=sam_sym,
			bt=0.5,
			verbose=False,
			log=False,
		)
		self.digital_gmsk_demod_9 = digital.gmsk_demod(
			samples_per_symbol=sam_sym,
			gain_mu=0.175,
			mu=0.5,
			omega_relative_limit=0.005,
			freq_error=0.0,
			verbose=False,
			log=False,
		)
		self.blocks_multiply_const_vxx_9 = blocks.multiply_const_vcc((1, ))
		self.blks2_packet_encoder_9 = grc_blks2.packet_mod_c(grc_blks2.packet_encoder(
				samples_per_symbol=sam_sym,
				bits_per_symbol=1,
				preamble="",
				access_code="",
				pad_for_usrp=True,
			),
			payload_length=0,
		)
		self.blks2_packet_decoder_9 = grc_blks2.packet_demod_c(grc_blks2.packet_decoder(
				access_code="",
				threshold=-1,
				callback=lambda ok, payload: self.blks2_packet_decoder_9.recv_pkt(ok, payload),
			),
		)

		##################################################
		# Connections
		##################################################
		self.connect((self.digital_gmsk_mod_9, 0), (self.blocks_multiply_const_vxx_9, 0))
		self.connect((self.blocks_multiply_const_vxx_9, 0), (self.uhd_usrp_sink_9, 0))
		self.connect((self.blks2_packet_encoder_9, 0), (self.digital_gmsk_mod_9, 0))
		self.connect((self.uhd_usrp_source_9, 0), (self.digital_gmsk_demod_9, 0))
		self.connect((self.blks2_packet_decoder_9, 0), (self.blks2_packet_encoder_9, 0))
		self.connect((self.digital_gmsk_demod_9, 0), (self.blks2_packet_decoder_9, 0))


# QT sink close method reimplementation

	def get_samp_rate_9(self):
		return self.samp_rate_9

	def set_samp_rate_9(self, samp_rate_9):
		self.samp_rate_9 = samp_rate_9
		self.uhd_usrp_source_9.set_samp_rate(self.samp_rate_9)
		self.uhd_usrp_sink_9.set_samp_rate(self.samp_rate_9)

	def get_sam_sym(self):
		return self.sam_sym

	def set_sam_sym(self, sam_sym):
		self.sam_sym = sam_sym

	def get_freq6(self):
		return self.freq6

	def set_freq6(self, freq6):
		self.freq6 = freq6
		self.uhd_usrp_sink_9.set_center_freq(self.freq6, 0)

	def get_freq4(self):
		return self.freq4

	def set_freq4(self, freq4):
		self.freq4 = freq4
		self.uhd_usrp_source_9.set_center_freq(self.freq4, 0)


class Rx_Tx_10(grc_wxgui.top_block_gui):

	def __init__(self):
		grc_wxgui.top_block_gui.__init__(self, title="Rx Tx 10")
		_icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
		self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

		##################################################
		# Variables
		##################################################
		self.samp_rate_10 = samp_rate_10 = .25e6
		self.sam_sym = sam_sym = 2
		self.freq5 = freq5 = frequ[freq[4]]
		self.freq4 = freq4 = frequ[freq[3]]

		##################################################
		# Blocks
		##################################################
		self.uhd_usrp_source_10 = uhd.usrp_source(
			device_addr="addr=192.168.10.11",
			stream_args=uhd.stream_args(
				cpu_format="fc32",
				channels=range(1),
			),
		)
		self.uhd_usrp_source_10.set_samp_rate(samp_rate_10)
		self.uhd_usrp_source_10.set_center_freq(freq4, 0)
		self.uhd_usrp_source_10.set_gain(1, 0)
		self.uhd_usrp_source_10.set_antenna("RX2", 0)
		self.uhd_usrp_sink_10 = uhd.usrp_sink(
			device_addr="addr=192.168.10.11",
			stream_args=uhd.stream_args(
				cpu_format="fc32",
				channels=range(1),
			),
		)
		self.uhd_usrp_sink_10.set_samp_rate(samp_rate_10)
		self.uhd_usrp_sink_10.set_center_freq(freq5, 0)
		self.uhd_usrp_sink_10.set_gain(1, 0)
		self.uhd_usrp_sink_10.set_antenna("TX/RX", 0)
		self.digital_gmsk_mod_10 = digital.gmsk_mod(
			samples_per_symbol=sam_sym,
			bt=0.5,
			verbose=False,
			log=False,
		)
		self.digital_gmsk_demod_10 = digital.gmsk_demod(
			samples_per_symbol=sam_sym,
			gain_mu=0.175,
			mu=0.5,
			omega_relative_limit=0.005,
			freq_error=0.0,
			verbose=False,
			log=False,
		)
		self.blocks_multiply_const_vxx_10 = blocks.multiply_const_vcc((1, ))
		self.blks2_packet_encoder_10 = grc_blks2.packet_mod_c(grc_blks2.packet_encoder(
				samples_per_symbol=sam_sym,
				bits_per_symbol=1,
				preamble="",
				access_code="",
				pad_for_usrp=True,
			),
			payload_length=0,
		)
		self.blks2_packet_decoder_10 = grc_blks2.packet_demod_c(grc_blks2.packet_decoder(
				access_code="",
				threshold=-1,
				callback=lambda ok, payload: self.blks2_packet_decoder_10.recv_pkt(ok, payload),
			),
		)

		##################################################
		# Connections
		##################################################
		self.connect((self.digital_gmsk_mod_10, 0), (self.blocks_multiply_const_vxx_10, 0))
		self.connect((self.blocks_multiply_const_vxx_10, 0), (self.uhd_usrp_sink_10, 0))
		self.connect((self.blks2_packet_encoder_10, 0), (self.digital_gmsk_mod_10, 0))
		self.connect((self.uhd_usrp_source_10, 0), (self.digital_gmsk_demod_10, 0))
		self.connect((self.blks2_packet_decoder_10, 0), (self.blks2_packet_encoder_10, 0))
		self.connect((self.digital_gmsk_demod_10, 0), (self.blks2_packet_decoder_10, 0))


# QT sink close method reimplementation

	def get_samp_rate_10(self):
		return self.samp_rate_10

	def set_samp_rate_10(self, samp_rate_10):
		self.samp_rate_10 = samp_rate_10
		self.uhd_usrp_sink_10.set_samp_rate(self.samp_rate_10)
		self.uhd_usrp_source_10.set_samp_rate(self.samp_rate_10)

	def get_sam_sym(self):
		return self.sam_sym

	def set_sam_sym(self, sam_sym):
		self.sam_sym = sam_sym

	def get_freq5(self):
		return self.freq5

	def set_freq5(self, freq5):
		self.freq5 = freq5
		self.uhd_usrp_sink_10.set_center_freq(self.freq5, 0)

	def get_freq4(self):
		return self.freq4

	def set_freq4(self, freq4):
		self.freq4 = freq4
		self.uhd_usrp_source_10.set_center_freq(self.freq4, 0)


class Rx_Tx_11(grc_wxgui.top_block_gui):

	def __init__(self):
		grc_wxgui.top_block_gui.__init__(self, title="Rx Tx 11")
		_icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
		self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

		##################################################
		# Variables
		##################################################
		self.samp_rate_11 = samp_rate_11 = .25e6
		self.sam_sym = sam_sym = 2
		self.freq5 = freq5 = frequ[freq[4]]
		self.freq4 = freq4 = frequ[freq[3]]

		##################################################
		# Blocks
		##################################################
		self.uhd_usrp_source_11 = uhd.usrp_source(
			device_addr="addr=192.168.10.12",
			stream_args=uhd.stream_args(
				cpu_format="fc32",
				channels=range(1),
			),
		)
		self.uhd_usrp_source_11.set_samp_rate(samp_rate_11)
		self.uhd_usrp_source_11.set_center_freq(freq4, 0)
		self.uhd_usrp_source_11.set_gain(1, 0)
		self.uhd_usrp_source_11.set_antenna("RX2", 0)
		self.uhd_usrp_sink_11 = uhd.usrp_sink(
			device_addr="addr=192.168.10.12",
			stream_args=uhd.stream_args(
				cpu_format="fc32",
				channels=range(1),
			),
		)
		self.uhd_usrp_sink_11.set_samp_rate(samp_rate_11)
		self.uhd_usrp_sink_11.set_center_freq(freq5, 0)
		self.uhd_usrp_sink_11.set_gain(1, 0)
		self.uhd_usrp_sink_11.set_antenna("TX/RX", 0)
		self.digital_gmsk_mod_11 = digital.gmsk_mod(
			samples_per_symbol=sam_sym,
			bt=0.5,
			verbose=False,
			log=False,
		)
		self.digital_gmsk_demod_11 = digital.gmsk_demod(
			samples_per_symbol=sam_sym,
			gain_mu=0.175,
			mu=0.5,
			omega_relative_limit=0.005,
			freq_error=0.0,
			verbose=False,
			log=False,
		)
		self.blocks_multiply_const_vxx_11 = blocks.multiply_const_vcc((1, ))
		self.blks2_packet_encoder_11 = grc_blks2.packet_mod_c(grc_blks2.packet_encoder(
				samples_per_symbol=sam_sym,
				bits_per_symbol=1,
				preamble="",
				access_code="",
				pad_for_usrp=True,
			),
			payload_length=0,
		)
		self.blks2_packet_decoder_11 = grc_blks2.packet_demod_c(grc_blks2.packet_decoder(
				access_code="",
				threshold=-1,
				callback=lambda ok, payload: self.blks2_packet_decoder_11.recv_pkt(ok, payload),
			),
		)

		##################################################
		# Connections
		##################################################
		self.connect((self.digital_gmsk_mod_11, 0), (self.blocks_multiply_const_vxx_11, 0))
		self.connect((self.blocks_multiply_const_vxx_11, 0), (self.uhd_usrp_sink_11, 0))
		self.connect((self.blks2_packet_encoder_11, 0), (self.digital_gmsk_mod_11, 0))
		self.connect((self.uhd_usrp_source_11, 0), (self.digital_gmsk_demod_11, 0))
		self.connect((self.blks2_packet_decoder_11, 0), (self.blks2_packet_encoder_11, 0))
		self.connect((self.digital_gmsk_demod_11, 0), (self.blks2_packet_decoder_11, 0))


# QT sink close method reimplementation

	def get_samp_rate_11(self):
		return self.samp_rate_11

	def set_samp_rate_11(self, samp_rate_11):
		self.samp_rate_11 = samp_rate_11
		self.uhd_usrp_sink_11.set_samp_rate(self.samp_rate_11)
		self.uhd_usrp_source_11.set_samp_rate(self.samp_rate_11)

	def get_sam_sym(self):
		return self.sam_sym

	def set_sam_sym(self, sam_sym):
		self.sam_sym = sam_sym

	def get_freq5(self):
		return self.freq5

	def set_freq5(self, freq5):
		self.freq5 = freq5
		self.uhd_usrp_sink_11.set_center_freq(self.freq5, 0)

	def get_freq4(self):
		return self.freq4

	def set_freq4(self, freq4):
		self.freq4 = freq4
		self.uhd_usrp_source_11.set_center_freq(self.freq4, 0)

class Rx_Tx_12(grc_wxgui.top_block_gui):

	def __init__(self):
		grc_wxgui.top_block_gui.__init__(self, title="Rx Tx 12")
		_icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
		self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

		##################################################
		# Variables
		##################################################
		self.samp_rate_12 = samp_rate_12 = .25e6
		self.sam_sym = sam_sym = 2
		self.freq6 = freq6 = frequ[freq[5]]
		self.freq5 = freq5 = frequ[freq[4]]

		##################################################
		# Blocks
		##################################################
		self.uhd_usrp_source_12 = uhd.usrp_source(
			device_addr="addr=192.168.10.13",
			stream_args=uhd.stream_args(
				cpu_format="fc32",
				channels=range(1),
			),
		)
		self.uhd_usrp_source_12.set_samp_rate(samp_rate_12)
		self.uhd_usrp_source_12.set_center_freq(freq6, 0)
		self.uhd_usrp_source_12.set_gain(1, 0)
		self.uhd_usrp_source_12.set_antenna("RX2", 0)
		self.uhd_usrp_sink_12 = uhd.usrp_sink(
			device_addr="addr=192.168.10.13",
			stream_args=uhd.stream_args(
				cpu_format="fc32",
				channels=range(1),
			),
		)
		self.uhd_usrp_sink_12.set_samp_rate(samp_rate_12)
		self.uhd_usrp_sink_12.set_center_freq(freq5, 0)
		self.uhd_usrp_sink_12.set_gain(1, 0)
		self.uhd_usrp_sink_12.set_antenna("TX/RX", 0)
		self.digital_gmsk_mod_12 = digital.gmsk_mod(
			samples_per_symbol=sam_sym,
			bt=0.5,
			verbose=False,
			log=False,
		)
		self.digital_gmsk_demod_12 = digital.gmsk_demod(
			samples_per_symbol=sam_sym,
			gain_mu=0.175,
			mu=0.5,
			omega_relative_limit=0.005,
			freq_error=0.0,
			verbose=False,
			log=False,
		)
		self.blocks_multiply_const_vxx_12 = blocks.multiply_const_vcc((1, ))
		self.blks2_packet_encoder_12 = grc_blks2.packet_mod_c(grc_blks2.packet_encoder(
				samples_per_symbol=sam_sym,
				bits_per_symbol=1,
				preamble="",
				access_code="",
				pad_for_usrp=True,
			),
			payload_length=0,
		)
		self.blks2_packet_decoder_12 = grc_blks2.packet_demod_c(grc_blks2.packet_decoder(
				access_code="",
				threshold=-1,
				callback=lambda ok, payload: self.blks2_packet_decoder_12.recv_pkt(ok, payload),
			),
		)

		##################################################
		# Connections
		##################################################
		self.connect((self.digital_gmsk_mod_12, 0), (self.blocks_multiply_const_vxx_12, 0))
		self.connect((self.blocks_multiply_const_vxx_12, 0), (self.uhd_usrp_sink_12, 0))
		self.connect((self.blks2_packet_encoder_12, 0), (self.digital_gmsk_mod_12, 0))
		self.connect((self.uhd_usrp_source_12, 0), (self.digital_gmsk_demod_12, 0))
		self.connect((self.blks2_packet_decoder_12, 0), (self.blks2_packet_encoder_12, 0))
		self.connect((self.digital_gmsk_demod_12, 0), (self.blks2_packet_decoder_12, 0))


# QT sink close method reimplementation

	def get_samp_rate_12(self):
		return self.samp_rate_12

	def set_samp_rate_12(self, samp_rate_12):
		self.samp_rate_12 = samp_rate_12
		self.uhd_usrp_source_12.set_samp_rate(self.samp_rate_12)
		self.uhd_usrp_sink_12.set_samp_rate(self.samp_rate_12)

	def get_sam_sym(self):
		return self.sam_sym

	def set_sam_sym(self, sam_sym):
		self.sam_sym = sam_sym

	def get_freq6(self):
		return self.freq6

	def set_freq6(self, freq6):
		self.freq6 = freq6
		self.uhd_usrp_source_12.set_center_freq(self.freq6, 0)

	def get_freq5(self):
		return self.freq5

	def set_freq5(self, freq5):
		self.freq5 = freq5
		self.uhd_usrp_sink_12.set_center_freq(self.freq5, 0)

class Rx_13(grc_wxgui.top_block_gui):

	def __init__(self):
		grc_wxgui.top_block_gui.__init__(self, title="Rx 13")
		_icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
		self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

		##################################################
		# Variables
		##################################################
		self.samp_rate_13 = samp_rate_13 = 0.25e6
		self.sam_sym = sam_sym = 2
		self.freq5 = freq5 = frequ[freq[4]]

		##################################################
		# Blocks
		##################################################
		self.uhd_usrp_source_13 = uhd.usrp_source(
			device_addr="addr=192.168.10.14",
			stream_args=uhd.stream_args(
				cpu_format="fc32",
				channels=range(1),
			),
		)
		self.uhd_usrp_source_13.set_samp_rate(samp_rate_13)
		self.uhd_usrp_source_13.set_center_freq(freq5, 0)
		self.uhd_usrp_source_13.set_gain(1, 0)
		self.uhd_usrp_source_13.set_antenna("RX2", 0)
		self.digital_gmsk_demod_13 = digital.gmsk_demod(
			samples_per_symbol=sam_sym,
			gain_mu=0.175,
			mu=0.5,
			omega_relative_limit=0.005,
			freq_error=0.0,
			verbose=False,
			log=False,
		)
		self.blocks_udp_sink_13 = blocks.udp_sink(gr.sizeof_char*1, "127.0.0.1", 1236, 1472, True)
		self.blks2_packet_decoder_13 = grc_blks2.packet_demod_b(grc_blks2.packet_decoder(
				access_code="",
				threshold=-1,
				callback=lambda ok, payload: self.blks2_packet_decoder_13.recv_pkt(ok, payload),
			),
		)

		##################################################
		# Connections
		##################################################
		self.connect((self.blks2_packet_decoder_13, 0), (self.blocks_udp_sink_13, 0))
		self.connect((self.digital_gmsk_demod_13, 0), (self.blks2_packet_decoder_13, 0))
		self.connect((self.uhd_usrp_source_13, 0), (self.digital_gmsk_demod_13, 0))


# QT sink close method reimplementation

	def get_samp_rate_13(self):
		return self.samp_rate_13

	def set_samp_rate_13(self, samp_rate_13):
		self.samp_rate_13 = samp_rate_13
		self.uhd_usrp_source_13.set_samp_rate(self.samp_rate_13)

	def get_sam_sym(self):
		return self.sam_sym

	def set_sam_sym(self, sam_sym):
		self.sam_sym = sam_sym

	def get_freq5(self):
		return self.freq5

	def set_freq5(self, freq5):
		self.freq5 = freq5
		self.uhd_usrp_source_13.set_center_freq(self.freq5, 0)



if __name__ == '__main__':
	import ctypes
	import sys
	if sys.platform.startswith('linux'):
		try:
			x11 = ctypes.cdll.LoadLibrary('libX11.so')
			x11.XInitThreads()
		except:
			print "Warning: failed to XInitThreads()"
	parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
	(options, args) = parser.parse_args()


	tb1 = Tx_1()
	tb1.start()
	tb2 = Rx_Tx_2()
	tb3 = Rx_Tx_3()
	tb4 = Rx_Tx_4()
	tb5 = Rx_Tx_5()
	tb6 = Rx_Tx_6()
	tb7 = Rx_Tx_7()
	tb8 = Rx_Tx_8()
	tb9 = Rx_Tx_9()
	tb10 = Rx_Tx_10()
	tb11 = Rx_Tx_11()
	tb12 = Rx_Tx_12()
	tb13 = Rx_13()
	tb13.start()	

	k=random.sample(frequ,6) #6 Channels with 6 PUS

	kPU = k[0:7]

	kSU1 = [0]*6
	kSU2 = [0]*6
	kSU3 = [0]*6
	kSU4 = [0]*6
	kSU5 = [0]*6
	kSU6 = [0]*6
	kSU7 = [0]*6
	kSU8 = [0]*6
	kSU9 = [0]*6
	kSU10 = [0]*6
	kSU11 = [0]*6
	kSU12 = [0]*6
	kSU13 = [0]*6

	timeSU1=[0]*6
	timeSU2=[0]*6
	timeSU3=[0]*6
	timeSU4=[0]*6
	timeSU5=[0]*6
	timeSU6=[0]*6
	timeSU7=[0]*6
	timeSU8=[0]*6
	timeSU9=[0]*6
	timeSU10=[0]*6
	timeSU11=[0]*6
	timeSU12=[0]*6
	timeSU13 = [0]*6	#Time array

	avgON =  [15]*6		#Avg ON time is fix 15
	#avgOFF = [5]*6
	avgOFF = [10]*6
	#avgOFF = [15]*6
	#avgOFF = [20]*6
	#avgOFF = [25]*6

	#avgOFF = [30]*6
	#avgOFF = [35]*6
	#avgOFF = [40]*6
	#avgOFF = [45]*6
	#avgOFF = [50]*6
	#avgOFF = [55]*6
	#avgOFF = [60]*6
	#avgOFF = [65]*6
	#avgOFF = [70]*6
	#avgOFF = [75]*6
	#avgOFF = [80]*6
	#avgOFF = [85]*6
	#avgOFF = [90]*6
	#avgOFF = [95]*6
	#avgOFF = [100]*6
	#avgOFF = [105]*6
	
	sensingTime=3
	routeBreak=0
	routeSwitch=0
	count_SA_Routes = [0]*12
	old_Q_Values= [0]*12
	count=0
	t=-1
	ep=time.time()
	time.sleep(1)



	while 1:
		print '\n#####################################################################################\n'	
		print '\t		Available Channels at each Node in the presence of PUS Activities'	
		print '\n#####################################################################################\n'	
		time.sleep(1)
		PU = lambda n: [randint(0,1) for i in range (1, n+1)]	#generating array randomly either 0/1 

		#print '##################################### AVAILABLE CHANNELS DURING PUs ACTIVITIES ################################################'	

		val_PU = PU(6)
		#print '\n','states of PUs @ SU Node1 on each of', len(k), 'Channels in th Network', val_PU,'\n' 
		for i in range(0,len(kPU)):
			if val_PU[i]==1:
				timeSU1[i]=poisson_process_v1.poisson_process(avgON[i])#mean=2
				#print 'PU', i+1, 'is active', 'on the channel',i+1, kPU[i], 'for the time=', timeSU1[i],'\n'
			elif val_PU[i]==0:
				timeSU1[i]=poisson_process_v1.poisson_process(avgOFF[i])
				#print 'PU', i+1, 'is inactive', 'on the channel',i+1, kPU[i], 'for the time=', timeSU1[i],'\n'			
		for i in range (0,len(kPU)):
			if (val_PU[i]==0): 
				kSU1[i]=kPU[i]
			elif(val_PU[i]==1):
				kSU1[i]=None
		#print '\n','There are',len(filter(lambda x: x is not None, kSU1)),'available channels from the pool of', len(k),'for SUs.','Listed as:', kSU1, '\n' 
		#print "------------------------------------------------------------------------------------------------------------------------------------------------",'\n'

		val_PU = PU(6)
		#print '\n','states of PUs at SU Node 2 on each of', len(k), 'Channels in th Network', val_PU,'\n' 
		for i in range(0,len(kPU)):
			if val_PU[i]==1:
				timeSU2[i]=np.random.poisson(avgON[i])#mean=2
				#print 'PU', i+1, 'is active', 'on the channel',i+1, kPU[i], 'for the time=', timeSU2[i],'\n'
			elif val_PU[i]==0:
				timeSU2[i]=np.random.poisson(avgOFF[i])
				#print 'PU', i+1, 'is inactive', 'on the channel',i+1, kPU[i], 'for the time=', timeSU2[i],'\n'		
		for i in range (0,len(kPU)):
			if (val_PU[i]==0): 
				kSU2[i]=kPU[i]
			elif(val_PU[i]==1):
				kSU2[i]=None
		#print '\n','There are',len(filter(lambda x: x is not None, kSU2)),'available channels from the pool of', len(k),'for SUs.','Listed as:', kSU2, '\n' 
		#print "------------------------------------------------------------------------------------------------------------------------------------------------",'\n'


		val_PU = PU(6)
		#print '\n','states of PUs at SU Node 3 on each of', len(k), 'Channels in th Network', val_PU,'\n' 
		for i in range(0,len(kPU)):
			if val_PU[i]==1:
				timeSU3[i]=np.random.poisson(avgON[i])#mean=2
				#print 'PU', i+1, 'is active', 'on the channel',i+1, kPU[i], 'for the time=', timeSU3[i],'\n'
			elif val_PU[i]==0:
				timeSU3[i]=np.random.poisson(avgOFF[i])
				#print 'PU', i+1, 'is inactive', 'on the channel',i+1, kPU[i], 'for the time=', timeSU3[i],'\n'		
		for i in range (0,len(kPU)):
			if (val_PU[i]==0): 
				kSU3[i]=kPU[i]
			elif(val_PU[i]==1):
				kSU3[i]=None
		#print '\n','There are',len(filter(lambda x: x is not None, kSU3)),'available channels from the pool of', len(k),'for SUs.','Listed as:', kSU3, '\n' 
		#print "------------------------------------------------------------------------------------------------------------------------------------------------",'\n'



		val_PU = PU(6)
		#print '\n','states of PUs at SU Node 4 on each of', len(k), 'Channels in th Network', val_PU,'\n' 
		for i in range(0,len(kPU)):
			if val_PU[i]==1:
				timeSU4[i]=np.random.poisson(avgON[i])#mean=2
				#print 'PU', i+1, 'is active', 'on the channel',i+1, kPU[i], 'for the time=', timeSU4[i],'\n'
			elif val_PU[i]==0:
				timeSU4[i]=np.random.poisson(avgOFF[i])
				#print 'PU', i+1, 'is inactive', 'on the channel',i+1, kPU[i], 'for the time=', timeSU4[i],'\n'		

		for i in range (0,len(kPU)):
			if (val_PU[i]==0): 
				kSU4[i]=kPU[i]
			elif(val_PU[i]==1):
				kSU4[i]=None
		#print '\n','There are',len(filter(lambda x: x is not None, kSU4)),'available channels from the pool of', len(k),'for SUs.','Listed as:', kSU4, '\n' 
		#print "------------------------------------------------------------------------------------------------------------------------------------------------",'\n'


		val_PU = PU(6)
		#print '\n','states of PUs at SU Node 5 on each of', len(k), 'Channels in th Network', val_PU,'\n' 
		for i in range(0,len(kPU)):
			if val_PU[i]==1:
				timeSU5[i]=np.random.poisson(avgON[i])#mean=2
				#print 'PU', i+1, 'is active', 'on the channel',i+1, kPU[i], 'for the time=', timeSU5[i],'\n'
			elif val_PU[i]==0:
				timeSU5[i]=np.random.poisson(avgOFF[i])
				#print 'PU', i+1, 'is inactive', 'on the channel',i+1, kPU[i], 'for the time=', timeSU5[i],'\n'		
		for i in range (0,len(kPU)):
			if (val_PU[i]==0): 
				kSU5[i]=kPU[i]
			elif(val_PU[i]==1):
				kSU5[i]=None
		#print '\n','There are',len(filter(lambda x: x is not None, kSU5)),'available channels from the pool of', len(k),'for SUs.','Listed as:', kSU5, '\n' 
		#print "------------------------------------------------------------------------------------------------------------------------------------------------",'\n'


		val_PU = PU(6)
		#print '\n','states of PUs at SU Node 6 on each of', len(k), 'Channels in th Network', val_PU,'\n' 
		for i in range(0,len(kPU)):
			if val_PU[i]==1:
				timeSU6[i]=np.random.poisson(avgON[i])#mean=2
				#print 'PU', i+1, 'is active', 'on the channel',i+1, kPU[i], 'for the time=', timeSU6[i],'\n'
			elif val_PU[i]==0:
				timeSU6[i]=np.random.poisson(avgOFF[i])
				#print 'PU', i+1, 'is inactive', 'on the channel',i+1, kPU[i], 'for the time=', timeSU6[i],'\n'		
		for i in range (0,len(kPU)):
			if (val_PU[i]==0): 
				kSU6[i]=kPU[i]
			elif(val_PU[i]==1):
				kSU6[i]=None
		#print '\n','There are',len(filter(lambda x: x is not None, kSU6)),'available channels from the pool of', len(k),'for SUs.','Listed as:', kSU6, '\n' 
		#print "------------------------------------------------------------------------------------------------------------------------------------------------",'\n'


		val_PU = PU(6)
		#print '\n','states of PUs at SU Node 7 on each of', len(k), 'Channels in th Network', val_PU,'\n' 
		for i in range(0,len(kPU)):
			if val_PU[i]==1:
				timeSU7[i]=np.random.poisson(avgON[i])#mean=2
				#print 'PU', i+1, 'is active', 'on the channel',i+1, kPU[i], 'for the time=', timeSU7[i],'\n'
			elif val_PU[i]==0:
				timeSU7[i]=np.random.poisson(avgOFF[i])
				#print 'PU', i+1, 'is inactive', 'on the channel',i+1, kPU[i], 'for the time=', timeSU7[i],'\n'		
		for i in range (0,len(kPU)):
			if (val_PU[i]==0): 
				kSU7[i]=kPU[i]
			elif(val_PU[i]==1):
				kSU7[i]=None
		#print '\n','There are',len(filter(lambda x: x is not None, kSU7)),'available channels from the pool of', len(k),'for SUs.','Listed as:', kSU7, '\n' 
		#print "------------------------------------------------------------------------------------------------------------------------------------------------",'\n'


		val_PU = PU(6)
		#print '\n','states of PUs at SU Node 8 on each of', len(k), 'Channels in th Network', val_PU,'\n' 
		for i in range(0,len(kPU)):
			if val_PU[i]==1:
				timeSU8[i]=np.random.poisson(avgON[i])#mean=2
				#print 'PU', i+1, 'is active', 'on the channel',i+1, kPU[i], 'for the time=', timeSU8[i],'\n'
			elif val_PU[i]==0:
				timeSU8[i]=np.random.poisson(avgOFF[i])
				#print 'PU', i+1, 'is inactive', 'on the channel',i+1, kPU[i], 'for the time=', timeSU8[i],'\n'		
		for i in range (0,len(kPU)):
			if (val_PU[i]==0): 
				kSU8[i]=kPU[i]
			elif(val_PU[i]==1):
				kSU8[i]=None
		#print '\n','There are',len(filter(lambda x: x is not None, kSU8)),'available channels from the pool of', len(k),'for SUs.','Listed as:', kSU8, '\n' 
		#print "------------------------------------------------------------------------------------------------------------------------------------------------",'\n'


		val_PU = PU(6)
		#print '\n','states of PUs at SU Node 9 on each of', len(k), 'Channels in th Network', val_PU,'\n' 
		for i in range(0,len(kPU)):
			if val_PU[i]==1:
				timeSU9[i]=np.random.poisson(avgON[i])#mean=2
				#print 'PU', i+1, 'is active', 'on the channel',i+1, kPU[i], 'for the time=', timeSU9[i],'\n'
			elif val_PU[i]==0:
				timeSU9[i]=np.random.poisson(avgOFF[i])
				#print 'PU', i+1, 'is inactive', 'on the channel',i+1, kPU[i], 'for the time=', timeSU9[i],'\n'		
		for i in range (0,len(kPU)):
			if (val_PU[i]==0): 
				kSU9[i]=kPU[i]
			elif(val_PU[i]==1):
				kSU9[i]=None
		#print '\n','There are',len(filter(lambda x: x is not None, kSU9)),'available channels from the pool of', len(k),'for SUs.','Listed as:', kSU9, '\n' 
		#print "------------------------------------------------------------------------------------------------------------------------------------------------",'\n'



		val_PU = PU(6)
		#print '\n','states of PUs at SU Node 10 on each of', len(k), 'Channels in th Network', val_PU,'\n' 
		for i in range(0,len(kPU)):
			if val_PU[i]==1:
				timeSU10[i]=np.random.poisson(avgON[i])#mean=2
				#print 'PU', i+1, 'is active', 'on the channel',i+1, kPU[i], 'for the time=', timeSU10[i],'\n'
			elif val_PU[i]==0:
				timeSU10[i]=np.random.poisson(avgOFF[i])
				#print 'PU', i+1, 'is inactive', 'on the channel',i+1, kPU[i], 'for the time=', timeSU10[i],'\n'		
		for i in range (0,len(kPU)):
			if (val_PU[i]==0): 
				kSU10[i]=kPU[i]
			elif(val_PU[i]==1):
				kSU10[i]=None
		#print '\n','There are',len(filter(lambda x: x is not None, kSU10)),'available channels from the pool of', len(k),'for SUs.','Listed as:', kSU10, '\n' 
		#print "------------------------------------------------------------------------------------------------------------------------------------------------",'\n'



		val_PU = PU(6)
		#print '\n','states of PUs at SU Node 11 on each of', len(k), 'Channels in th Network', val_PU,'\n' 
		for i in range(0,len(kPU)):
			if val_PU[i]==1:
				timeSU11[i]=np.random.poisson(avgON[i])#mean=2
				#print 'PU', i+1, 'is active', 'on the channel',i+1, kPU[i], 'for the time=', timeSU11[i],'\n'
			elif val_PU[i]==0:
				timeSU11[i]=np.random.poisson(avgOFF[i])
				#print 'PU', i+1, 'is inactive', 'on the channel',i+1, kPU[i], 'for the time=', timeSU11[i],'\n'		
		for i in range (0,len(kPU)):
			if (val_PU[i]==0): 
				kSU11[i]=kPU[i]
			elif(val_PU[i]==1):
				kSU11[i]=None
		#print '\n','There are',len(filter(lambda x: x is not None, kSU11)),'available channels from the pool of', len(k),'for SUs.','Listed as:', kSU11, '\n' 
		#print "------------------------------------------------------------------------------------------------------------------------------------------------",'\n'



		val_PU = PU(6)
		#print '\n','states of PUs at SU Node 12 on each of', len(k), 'Channels in th Network', val_PU,'\n' 
		for i in range(0,len(kPU)):
			if val_PU[i]==1:
				timeSU12[i]=np.random.poisson(avgON[i])#mean=2
				#print 'PU', i+1, 'is active', 'on the channel',i+1, kPU[i], 'for the time=', timeSU12[i],'\n'
			elif val_PU[i]==0:
				timeSU12[i]=np.random.poisson(avgOFF[i])
				#print 'PU', i+1, 'is inactive', 'on the channel',i+1, kPU[i], 'for the time=', timeSU12[i],'\n'		
		for i in range (0,len(kPU)):
			if (val_PU[i]==0): 
				kSU12[i]=kPU[i]
			elif(val_PU[i]==1):
				kSU12[i]=None
		#print '\n','There are',len(filter(lambda x: x is not None, kSU12)),'available channels from the pool of', len(k),'for SUs.','Listed as:', kSU12, '\n' 
		#print "------------------------------------------------------------------------------------------------------------------------------------------------",'\n'


		val_PU = PU(6)
		#print '\n','states of PUs at SU Node 13 on each of', len(k), 'Channels in th Network', val_PU,'\n' 
		for i in range(0,len(kPU)):
			if val_PU[i]==1:
				timeSU13[i]=np.random.poisson(avgON[i])#mean=2
				#print 'PU', i+1, 'is active', 'on the channel',i+1, kPU[i], 'for the time=', timeSU13[i],'\n'
			elif val_PU[i]==0:
				timeSU13[i]=np.random.poisson(avgOFF[i])
				#print 'PU', i+1, 'is inactive', 'on the channel',i+1, kPU[i], 'for the time=', timeSU13[i],'\n'		
		for i in range (0,len(kPU)):
			if (val_PU[i]==0): 
				kSU13[i]=kPU[i]
			elif(val_PU[i]==1):
				kSU13[i]=None
		#print '\n','There are',len(filter(lambda x: x is not None, kSU13)),'available channels from the pool of', len(k),'for SUs.','Listed as:', kSU13, '\n' 
		#print "------------------------------------------------------------------------------------------------------------------------------------------------",'\n'
	
	
		#RANDOM CHANNEL ASSIGNMENT TO EACH SU NODE
		kN1 = filter(lambda x: x is not None, kSU1)
		kN2 = filter(lambda x: x is not None, kSU2)
		kN3 = filter(lambda x: x is not None, kSU3)
		kN4 = filter(lambda x: x is not None, kSU4)
		kN5 = filter(lambda x: x is not None, kSU5)
		kN6 = filter(lambda x: x is not None, kSU6)
		kN7 = filter(lambda x: x is not None, kSU7)
		kN8 = filter(lambda x: x is not None, kSU8)
		kN9 = filter(lambda x: x is not None, kSU9)
		kN10 = filter(lambda x: x is not None, kSU10)
		kN11 = filter(lambda x: x is not None, kSU11)
		kN12 = filter(lambda x: x is not None, kSU12)
		kN13 = filter(lambda x: x is not None, kSU13)
	
	
		nodeID = ['addr=192.168.10.2','addr=192.168.10.3','addr=192.168.10.4','addr=192.168.10.5','addr=192.168.10.6','addr=192.168.10.7','addr=192.168.10.8','addr=192.168.10.9','addr=192.168.10.10','addr=192.168.10.11','addr=192.168.10.12','addr=192.168.10.13','addr=192.168.10.14',]
		nodeState = []
		nneighbor_nodeID =[
		[ nodeID[1], nodeID[2] ],
		[ nodeID[3], nodeID[4] ],
		[ nodeID[4], nodeID[5] ],
		[ nodeID[6] ],
		[ nodeID[6], nodeID[7]], 
		[ nodeID[7] ], 
		[ nodeID[8], nodeID[9]],
		[ nodeID[9], nodeID[10]],
		[nodeID[11] ], 
		[nodeID[11], nodeID[12] ], 
		[ nodeID[12] ],
		[ nodeID[12] ],
		[None]]
		#NEIGHBOR TABLE
		nTable = [
		[1,	nodeID[0], kN1,	len(kN1),	[2,3],	"NNi",	nneighbor_nodeID[0]], 
		[2,	nodeID[1], kN2,	len(kN2),	[4,5],	"NNi",	nneighbor_nodeID[1]],
		[3,	nodeID[2], kN3,	len(kN3),	[5,6],	"NNi",	nneighbor_nodeID[2]],
		[4,	nodeID[3], kN4,	len(kN4),	[7],	"NNi",	nneighbor_nodeID[3]],
		[5,	nodeID[4], kN5,	len(kN5),	[7,8],"NNi",	nneighbor_nodeID[4]],
		[6,	nodeID[5], kN6,	len(kN6),	[8],	"NNi",	nneighbor_nodeID[5]],	
		[7,	nodeID[6], kN7,	len(kN7),	[9,10],"NNi",	nneighbor_nodeID[6]],
		[8,	nodeID[7], kN8,	len(kN8),	[10,11],"NNi",	nneighbor_nodeID[7]],
		[9, nodeID[8], kN9,	len(kN9),	[12],	"NNi",	nneighbor_nodeID[8]],
		[10,	nodeID[9], kN10,len(kN10),	[12,13],"NNi",	nneighbor_nodeID[9]],
		[11,	nodeID[10],kN11,len(kN11),	[13],	"NNi",	nneighbor_nodeID[10]],
		[12,	nodeID[11],kN12,len(kN12),	[13],	"NNi",	nneighbor_nodeID[11]],
		[13,	nodeID[12],kN13,len(kN13),	[None],	"NNi",	nneighbor_nodeID[12]]]
	
		t+=1
				
		print '-------------------------------------------------------------------------------------'
		print '@t=',t,'and at time in sec',(time.time()-ep)
		print '-------------------------------------------------------------------------------------'
		for i in range (0,13):
			print 'Available channels at',nTable[i][0],':', nTable[i][3]
		time.sleep(1)	
		print '\n#####################################################################################\n'	
		print '\t		CH-ELECTION AND MN-JOINING PROCEDURE'	
		print '\n #####################################################################################\n'
		time.sleep(1)
		#print '\n','----------------------------------------------------------------------------------------------'
		#print 'Node States before CLUSTERING'	
		#print '----------------------------------------------------------------------------------------------'
		#for i in range(0,13):
		#	print 'State of Node',i+1,nTable[i][5],nTable[i][3]	
		if (len(kN1)>(len(kN2) and len(kN3))) and (nTable[0][5]=="NNi"):
			nTable[0][5]="CH"
		elif(len(kN1)!=0):
			nTable[0][5]="MN"
		else:
			nTable[0][5]="NNi"
		
		if (len(kN2)>(len(kN1) and len(kN3) and len(kN4) and len(kN5))) and (nTable[1][5]=="NNi"):
			nTable[1][5]="CH"		
		elif(len(kN2)!=0):
			nTable[1][5]="MN"
		else:
			nTable[1][5]="NNi"
				
		if (len(kN3)>(len(kN1) and len(kN2) and len(kN5) and len(kN6))) and (nTable[2][5]=="NNi"):
			nTable[2][5]="CH"
		elif(len(kN3)!=0):
			nTable[2][5]="MN"
		else:
			nTable[2][5]="NNi"
		
		if (len(kN4)>(len(kN2) and len(kN5) and len(kN7))) and (nTable[3][5]=="NNi"):
			nTable[3][5]="CH"
		elif(len(kN4)!=0):
			nTable[3][5]="MN"
		else:
			nTable[3][5]="NNi"
		
		if (len(kN5)>(len(kN2) and len(kN3) and len(kN4) and len(kN6) and len(kN7) and len(kN8)))  and (nTable[4][5]=="NNi"):	
			nTable[4][5]="CH"
		elif(len(kN5)!=0):
			nTable[4][5]="MN"
		else:
			nTable[4][5]="NNi"

		
		if (len(kN6)>(len(kN3) and len(kN5) and len(kN8)))  and (nTable[5][5]=="NNi"):
			nTable[5][5]="CH"
		elif(len(kN6)!=0):
			nTable[5][5]="MN"
		else:
			nTable[5][5]="NNi"
		
		if (len(kN7)>(len(kN4) and len(kN5) and len(kN8) and len(kN9) and len(kN10)))  and (nTable[6][5]=="NNi"):	
			nTable[6][5]="CH"
		elif(len(kN7)!=0):
			nTable[6][5]="MN"
		else:
			nTable[6][5]="NNi"

		if (len(kN8)>(len(kN5) and len(kN6) and len(kN7) and len(kN10) and len(kN11)))  and (nTable[7][5]=="NNi"):
			nTable[7][5]="CH"
		elif(len(kN8)!=0):
			nTable[7][5]="MN"
		else:
			nTable[7][5]="NNi"
		
		if (len(kN9)>(len(kN7) and len(kN10) and len(kN12)))  and (nTable[8][5]=="NNi"):
			nTable[8][5]="CH"
		elif(len(kN9)!=0):
			nTable[8][5]="MN"
		else:
			nTable[8][5]="NNi"
		
		if (len(kN10)>(len(kN7) and len(kN8) and len(kN9) and len(kN11) and len(kN12) and len(kN13)))  and (nTable[9][5]=="NNi"):
			nTable[9][5]="CH"
		elif(len(kN10)!=0):
			nTable[9][5]="MN"
		else:
			nTable[9][5]="NNi"
		
		if (len(kN11)>(len(kN8) and len(kN10) and len(kN13)))  and (nTable[10][5]=="NNi"):	
			nTable[10][5]="CH"
		elif(len(kN11)!=0):
			nTable[10][5]="MN"
		else:
			nTable[10][5]="NNi"
			
		if (len(kN12)>(len(kN9) and len(kN10)))  and (nTable[11][5]=="NNi"):
			nTable[11][5]="CH"
		elif(len(kN12)!=0):
			nTable[11][5]="MN"
		else:
			nTable[11][5]="NNi"
		
		if (len(kN13)>(len(kN10) and len(kN11) and len(kN12)))  and (nTable[12][5]=="NNi"):
			nTable[12][5]="CH"
		elif(len(kN13)!=0):
			nTable[12][5]="MN"
		else:
			nTable[12][5]="NNi"


		for i in range (0,13):
			nodeState.append(nTable[i][5])
		time.sleep(1)		

		#print '\n-------------------------------------------------------------------------------------\n'
		#print '\t		Node States after CLUSTERING'	
		#print '\n-------------------------------------------------------------------------------------\n'
		#time.sleep(1)
		#for i in range(0,13):
		#	print 'State of Node',i+1,nTable[i][5],nTable[i][3]
		#time.sleep(1)
		#for i in range (0,13):
		#	nodeState.append(nTable[i][5])
		#time.sleep(1)
	
		#print '\n#####################################################################################\n'	
		#print '\t		ROUTING PROCEDURE '	
		#print '\n#####################################################################################\n'
		time.sleep(1)	
		old_graph = {1: [2,3],
		2: [4,5],
		3: [5,6],
		4: [7],
		5: [7,8],
		6: [8],
		7: [9,10],
		8: [10,11],
		9: [12],
		10: [13],
		11: [13],
		12: [13],
		13: [0]}
	
	
		OFFtimeoflink={
			1: [timeSU1[i] for i,x in enumerate(kSU1) if x != None],
			2: [timeSU2[i] for i,x in enumerate(kSU2) if x != None],
			3: [timeSU3[i] for i,x in enumerate(kSU3) if x != None],
			4: [timeSU4[i] for i,x in enumerate(kSU4) if x != None],
			5: [timeSU5[i] for i,x in enumerate(kSU5) if x != None],
			6: [timeSU6[i] for i,x in enumerate(kSU6) if x != None],
			7: [timeSU7[i] for i,x in enumerate(kSU7) if x != None],
			8: [timeSU8[i] for i,x in enumerate(kSU8) if x != None],
			9: [timeSU9[i] for i,x in enumerate(kSU9) if x != None],
			10:[timeSU10[i] for i,x in enumerate(kSU10) if x != None],
			11:[timeSU11[i] for i,x in enumerate(kSU11) if x != None],
			12:[timeSU12[i] for i,x in enumerate(kSU12) if x != None],
			13:[timeSU13[i] for i,x in enumerate(kSU13) if x != None]}

		ONtimeoflink={
			1: [timeSU1[i] for i,x in enumerate(kSU1) if x == None],
			2: [timeSU2[i] for i,x in enumerate(kSU2) if x == None],
			3: [timeSU3[i] for i,x in enumerate(kSU3) if x == None],
			4: [timeSU4[i] for i,x in enumerate(kSU4) if x == None],
			5: [timeSU5[i] for i,x in enumerate(kSU5) if x == None],
			6: [timeSU6[i] for i,x in enumerate(kSU6) if x == None],
			7: [timeSU7[i] for i,x in enumerate(kSU7) if x == None],
			8: [timeSU8[i] for i,x in enumerate(kSU8) if x == None],
			9: [timeSU9[i] for i,x in enumerate(kSU9) if x == None],
			10:[timeSU10[i] for i,x in enumerate(kSU10) if x == None],
			11:[timeSU11[i] for i,x in enumerate(kSU11) if x == None],
			12:[timeSU12[i] for i,x in enumerate(kSU12) if x == None],
			13:[timeSU13[i] for i,x in enumerate(kSU13) if x == None]}

		#Channelcapacity
		Psi={
		1: [ sum(OFFtimeoflink[1]) / (sum(ONtimeoflink[1]) + sum(OFFtimeoflink[1])) + ((sum(ONtimeoflink[1]) / (sum(ONtimeoflink[1])+sum(OFFtimeoflink[1]))) * (e** - ((1/(sum(ONtimeoflink[1]))) + (1/(sum(OFFtimeoflink[1])))))) ],


		2: [ sum(OFFtimeoflink[2]) / (sum(ONtimeoflink[2]) + sum(OFFtimeoflink[2])) + ((sum(ONtimeoflink[2]) / (sum(ONtimeoflink[1])+sum(OFFtimeoflink[2]))) * (e** - ((1/(sum(ONtimeoflink[2]))) + (1/(sum(OFFtimeoflink[2])))))) ],

		3: [ sum(OFFtimeoflink[3]) / (sum(ONtimeoflink[3]) + sum(OFFtimeoflink[3])) + ((sum(ONtimeoflink[3]) / (sum(ONtimeoflink[3])+sum(OFFtimeoflink[3]))) * (e** - ((1/(sum(ONtimeoflink[3]))) + (1/(sum(OFFtimeoflink[3])))))) ],

		4: [ sum(OFFtimeoflink[4]) / (sum(ONtimeoflink[4]) + sum(OFFtimeoflink[4])) + ((sum(ONtimeoflink[4]) / (sum(ONtimeoflink[4])+sum(OFFtimeoflink[4]))) * (e** - ((1/(sum(ONtimeoflink[4]))) + (1/(sum(OFFtimeoflink[4])))))) ],

		5: [ sum(OFFtimeoflink[5]) / (sum(ONtimeoflink[5]) + sum(OFFtimeoflink[5])) + ((sum(ONtimeoflink[5]) / (sum(ONtimeoflink[5])+sum(OFFtimeoflink[5]))) * (e** - ((1/(sum(ONtimeoflink[5]))) + (1/(sum(OFFtimeoflink[5])))))) ],

		6: [ sum(OFFtimeoflink[6]) / (sum(ONtimeoflink[6]) + sum(OFFtimeoflink[6])) + ((sum(ONtimeoflink[6]) / (sum(ONtimeoflink[6])+sum(OFFtimeoflink[6]))) * (e** - ((1/(sum(ONtimeoflink[6]))) + (1/(sum(OFFtimeoflink[6])))))) ],

		7: [ sum(OFFtimeoflink[7]) / (sum(ONtimeoflink[7]) + sum(OFFtimeoflink[7])) + ((sum(ONtimeoflink[7]) / (sum(ONtimeoflink[7])+sum(OFFtimeoflink[7]))) * (e** - ((1/(sum(ONtimeoflink[7]))) + (1/(sum(OFFtimeoflink[7])))))) ],

		8: [ sum(OFFtimeoflink[8]) / (sum(ONtimeoflink[8]) + sum(OFFtimeoflink[8])) + ((sum(ONtimeoflink[8]) / (sum(ONtimeoflink[8])+sum(OFFtimeoflink[8]))) * (e** - ((1/(sum(ONtimeoflink[8]))) + (1/(sum(OFFtimeoflink[8])))))) ],

		9: [ sum(OFFtimeoflink[9]) / (sum(ONtimeoflink[9]) + sum(OFFtimeoflink[9])) + ((sum(ONtimeoflink[9]) / (sum(ONtimeoflink[9])+sum(OFFtimeoflink[9]))) * (e** - ((1/(sum(ONtimeoflink[9]))) + (1/(sum(OFFtimeoflink[9])))))) ],

		10:[ sum(OFFtimeoflink[10]) / (sum(ONtimeoflink[10]) + sum(OFFtimeoflink[10])) + ((sum(ONtimeoflink[10]) / (sum(ONtimeoflink[10])+sum(OFFtimeoflink[10]))) * (e** - ((1/(sum(ONtimeoflink[10]))) + (1/(sum(OFFtimeoflink[10])))))) ],

		11:[ sum(OFFtimeoflink[11]) / (sum(ONtimeoflink[11]) + sum(OFFtimeoflink[11])) + ((sum(ONtimeoflink[11]) / (sum(ONtimeoflink[11])+sum(OFFtimeoflink[11]))) * (e** - ((1/(sum(ONtimeoflink[11]))) + (1/(sum(OFFtimeoflink[11])))))) ],

		12:[ sum(OFFtimeoflink[12]) / (sum(ONtimeoflink[12]) + sum(OFFtimeoflink[12])) + ((sum(ONtimeoflink[12]) / (sum(ONtimeoflink[12])+sum(OFFtimeoflink[12]))) * (e** - ((1/(sum(ONtimeoflink[12]))) + (1/(sum(OFFtimeoflink[12])))))) ],

		13:[ sum(OFFtimeoflink[13]) / (sum(ONtimeoflink[13]) + sum(OFFtimeoflink[13])) + ((sum(ONtimeoflink[13]) / (sum(ONtimeoflink[13])+sum(OFFtimeoflink[13]))) * (e** - ((1/(sum(ONtimeoflink[13]))) + (1/(sum(OFFtimeoflink[13])))))) ]}	

		CHnodes=[]
		idx=[i for i,x in enumerate(nodeState) if x == 'CH' or x== 'MN'] #Index of elements in nodeState whose value is CH
		CHnodes=[x+1 for x in idx]
		graph={}
		graph=dict((k,old_graph[k]) for k in CHnodes if k in old_graph)
		 
		def find_all_paths(graph, start, end, path=[]):
			path = path + [start]
			if start == end:
				return [path]
			if not graph.has_key(start):
				return []
			paths = []
			for node in graph[start]:
				if node not in path:
					newpaths = find_all_paths(graph, node, end, path)
					for newpath in newpaths:
						paths.append(newpath)
			return paths

		def find_shortest_path(graph, start, end, path=[]):
			path = path + [start]
			if start == end:
				return path
			if not graph.has_key(start):
				return None
			shortest = None
			for node in graph[start]:
				if node not in path:
					newpath = find_shortest_path(graph, node, end, path)
					if newpath:
						if not shortest or len(newpath) < len(shortest):
							shortest = newpath
			return shortest
		
		Routes = []
		Routes = find_all_paths(graph,CHnodes[0],CHnodes[len(CHnodes)-1])



		if Routes>0:
			#Links (i,j)
			SA_Routes=Routes
			SA_Values=[] 
			for i in range (0,len(SA_Routes)):
				SA_Values.append(zip(SA_Routes[i][0:-1:1],SA_Routes[i][1::1]))
		
			SA_links=[]
			for j in range (0, len(SA_Routes)):
				SA_links.append([sum(OFFtimeoflink[i]) for i in SA_Routes[j]])

			SA_Links=[]
			for i in range (0,len(SA_Routes)):
				SA_Links.append(SA_links[i][0:-1])			
		
			SA_Times=[]
			for i in range (0,len(SA_Routes)):
				SA_Times.append(min(SA_Links[i]))


			freqyy=[]
			for i in range (0,len(SA_Routes)):
				freqyy.append(random.sample(xrange(19),len(SA_Routes[i])-1))

			Q_Values=[0]*len(SA_Routes)



			#print Q_Values,'Mariam'
			#alpha = 0.5
			#alpha = (max([Psi[j] for j in (SA_Routes[i]])]))
			alpha=[0]*len(SA_Routes)
			epsilon = 5

			for i in range (0,len(SA_Routes)):
				alpha[i] = (max([Psi[j] for j in (SA_Routes[i])]))
			#print 'Dynamic learning rate for each Route:', alpha
			#for i in range (0,len(SA_Routes)):
				#Q_Values[i]= (((1-alpha)*np.array(old_Q_Values[i])) + ((alpha)*((min([Psi[j] for j in (SA_Routes[i])]))/(np.array(len(SA_Routes[i]))-1)))).tolist()

			for i in range (0,len(SA_Routes)):
				Q_Values[i]= ((([1 - x for x in alpha[i]])*np.array(old_Q_Values[i])) + ((alpha[i])*((min([Psi[j] for j in (SA_Routes[i])]))/(np.array(len(SA_Routes[i]))-1)))).tolist()



		
			SA_Q_Route=[]

			index=[i for i, x in enumerate (Q_Values) if x==max(Q_Values)]

			freqy=[]
			for i in range (0,len(freq)-1):
				freqy.append(frequ[freq[i]])


			ind=0
			ind=index[0]
			if len(index)>1 or count_SA_Routes[ind]==epsilon:
				index=random.choice(index)
				SA_Q_Route=SA_Routes[index]
				SA_Q_link=SA_links[index]
				SA_Q_Link=SA_Links[index]
				SA_Q_Time=SA_Times[index]
				SA_Q_Route_Q=Q_Values[index]
			elif len(index)==1:
				index=index[0]
				SA_Q_Route=SA_Routes[index]
				SA_Q_link=SA_links[index]
				SA_Q_Link=SA_Links[index]
				SA_Q_Time=SA_Times[index]
				SA_Q_Route_Q=Q_Values[index]
			#print index

			count_SA_Routes[index]+=1
			old_Q_Values[index]=(np.array(old_Q_Values[index])+SA_Q_Route_Q).tolist()






			freqyy[index]=freq

			elements=[]
			for i in range (0,len(freqyy)):
				elements.append([])
				for j in range (0,len(freqyy[i])):
					elements[i].append([])


			for i in range (0,len(freqyy)):
				for j in range (0,len(freqyy[i])):
					elements[i][j].append(frequ[freqyy[i][j]])

			kN1.append(frequ[freq[0]])

			kN2.append(frequ[freq[0]])
			kN2.append(frequ[freq[1]])

			kN3.append(frequ[freq[0]])
			kN3.append(frequ[freq[1]])

			kN4.append(frequ[freq[1]])
			kN4.append(frequ[freq[2]])

			kN5.append(frequ[freq[1]])
			kN5.append(frequ[freq[2]])

			kN6.append(frequ[freq[1]])
			kN6.append(frequ[freq[2]])

			kN7.append(frequ[freq[2]])
			kN7.append(frequ[freq[3]])

			kN8.append(frequ[freq[2]])
			kN8.append(frequ[freq[3]])

			kN9.append(frequ[freq[3]])
			kN9.append(frequ[freq[4]])
			kN9.append(frequ[freq[5]])

			kN10.append(frequ[freq[3]])
			kN10.append(frequ[freq[4]])
			kN10.append(frequ[freq[5]])

			kN11.append(frequ[freq[3]])
			kN11.append(frequ[freq[4]])
			kN11.append(frequ[freq[5]])

			kN12.append(frequ[freq[4]])
			kN12.append(frequ[freq[5]])

			kN13.append(frequ[freq[4]])
			kN13.append(frequ[freq[5]])

			kN1.sort()
			kN2.sort()
			kN3.sort()
			kN4.sort()
			kN5.sort()
			kN6.sort()
			kN7.sort()
			kN8.sort()
			kN9.sort()
			kN10.sort()
			kN11.sort()
			kN12.sort()
			kN13.sort()


			kN=[kN1,kN2,kN3,kN4,kN5,kN6,kN7,kN8,kN9,kN10,kN11,kN12,kN13]


			print '\n-------------------------------------------------------------------------------------\n'
			print '\t		Node States after CLUSTERING'	
			print '\n-------------------------------------------------------------------------------------\n'
			time.sleep(1)
			for i in range(0,13):
				print 'State of Node',i+1,nTable[i][5],nTable[i][2]
			time.sleep(1)

			print '\n#####################################################################################\n'	
			print '\t		ROUTING PROCEDURE '	
			print '\n#####################################################################################\n'



			time.sleep(1)
			print '\n -------------------------------------------------------------------------------------\n'
			print '\t		SPECTRUM-AWARE ROUTE DISCOVERY'
			print '\n-------------------------------------------------------------------------------------\n'
			time.sleep(1)
			print "There are",len(SA_Routes),"Spectrum-Aware Routes."
			for i in range (0,len(SA_Routes)):
				print "\n Route",i+1,":", SA_Routes[i] 

			print '\n -------------------------------------------------------------------------------------\n'
			print '\t		ROUTES WITH LINKS'
			print '\n-------------------------------------------------------------------------------------\n'
			for i in range (0,len(SA_Routes)):
				print "\n Route",i+1,"has set of links:", SA_Values[i], "with ceneterd frequencies:","\n\n",elements[i]
				#,"and Q-Value:", ['%.2f' % elem for elem in Q_Values[i]]#, "with capacity metric", min([Psi[j] for j 					in (SA_Routes[i])]), "hopcounts:", len(SA_Routes[i])-1, "Q-Value:", Q_Values[i], '\n'#, "for 					bottleneck link time" ,SA_Times[i], "seconds"
			time.sleep(1)

			print '\n -------------------------------------------------------------------------------------\n'
			print '\t		Q-TABLE for Routes'
			print '\n-------------------------------------------------------------------------------------\n'
			time.sleep(1)
			for i in range (0,len(SA_Routes)):
				print "\n Route",i+1, "has Q-Value:", ['%.2f' % elem for elem in Q_Values[i]]
			print "\n Old Q-Values:",old_Q_Values,'\n'
			print "\n Updated Q-Values:", [['%.2f' % elem for elem in Q_s]for Q_s in Q_Values],'\n'	
			time.sleep(1)

			print '\n','----------------------------------------------------------------------------------------------\n'
			print '\t        	SPECTRUM-AWARE RL-BASED ROUTE SELECTION @ Source Node using RL'
			print '\n','----------------------------------------------------------------------------------------------\n'

			if count_SA_Routes[ind]==epsilon:
				print 'Exploration with probability [epsilon = 0.1]'
			else:
				print 'Exploitation with probability [1 - epsilon = 0.9]'

			print "Route",index+1,"is selected:", SA_Q_Route, "with links:", SA_Values[index],"with centered frequencies:",'\n',elements[index],"and Q value:", ['%.2f' % elem for elem in SA_Q_Route_Q], "for", count_SA_Routes[index],"times"

			time.sleep(1)
			txTime=SA_Q_Time



			print '\n-------------------------------------------------------------------------------------'
			print '\t		RF-FRONT END FOR TRANSMISSION'	
			print '\n-------------------------------------------------------------------------------------'
			time.sleep(1)
			thenn=time.time()
			then=time.time()
			now=time.time()
			if (SA_Q_Route==[1,2,4,7,10,13]):
				tb10.start()
				tb7.start()
				tb4.start()
				tb2.start()
				while (int(now-thenn)<=txTime):
					#print "Data transmission"
					now=time.time()
					if int(now-then)==3:
						time.sleep(2)
						print "\n Sensing PUs' activities"
						then=time.time()
				print 'Closing'
				tb2.stop()
				tb2.wait()
				tb4.stop()
				tb4.wait()
				tb7.stop()
				tb7.wait()
				tb10.stop()
				tb10.wait()
			elif (SA_Q_Route==[1,2,5,7,10,13]):
				tb10.start()
				tb7.start()
				tb5.start()
				tb2.start()
				while (int(now-thenn)<=txTime):
					#print "Data transmission"
					now=time.time()
					if int(now-then)==3:
						time.sleep(2)
						print "\n Sensing PUs' activities"
						then=time.time()
				print 'Closing' 
				tb2.stop()
				tb2.wait()
				tb5.stop()
				tb5.wait()
				tb7.stop()
				tb7.wait()
				tb10.stop()
				tb10.wait()
			elif (SA_Q_Route==[1,2,5,8,10,13]):
				tb10.start()
				tb8.start()
				tb5.start()
				tb2.start()
				while (int(now-thenn)<=txTime):
					#print "Data transmission"
					now=time.time()
					if int(now-then)==3:
						time.sleep(2)
						print "\n Sensing PUs' activities"
						then=time.time()
				print 'Closing'
				tb2.stop()
				tb2.wait()
				tb5.stop()
				tb5.wait()
				tb8.stop()
				tb8.wait()
				tb10.stop()
				tb10.wait()
			elif (SA_Q_Route==[1,2,5,8,11,13]):
				tb11.start()
				tb8.start()
				tb5.start()
				tb2.start()
				while (int(now-thenn)<=txTime):
					#print "Data transmission"
					now=time.time()
					if int(now-then)==3:
						time.sleep(2)
						print "\n Sensing PUs' activities"
						then=time.time()
				print "Closing"
				tb2.stop()
				tb2.wait()
				tb5.stop()
				tb5.wait()
				tb8.stop()
				tb8.wait()
				tb11.stop()
				tb11.wait()
			elif (SA_Q_Route==[1,3,5,7,10,13]):
				tb10.start()
				tb7.start()
				tb5.start()
				tb3.start()
				while (int(now-thenn)<=txTime):
					#print "Data transmission"
					now=time.time()
					if int(now-then)==3:
						time.sleep(2)
						print "\n Sensing PUs' activities"
						then=time.time()
				print 'Closing'
				tb3.stop()
				tb3.wait()
				tb5.stop()
				tb5.wait()
				tb7.stop()
				tb7.wait()
				tb10.stop()
				tb10.wait()
			elif (SA_Q_Route==[1,3,5,8,10,13]):
				tb10.start()
				tb8.start()
				tb5.start()
				tb3.start()
				while (int(now-thenn)<=txTime):
					#print "Data transmission"
					now=time.time()
					if int(now-then)==3:
						time.sleep(2)
						print "\n Sensing PUs' activities"
						then=time.time()
				print 'closing'
				tb3.stop()
				tb3.wait()
				tb5.stop()
				tb5.wait()
				tb8.stop()
				tb8.wait()
				tb10.stop()
				tb10.wait()
			elif (SA_Q_Route==[1,3,5,8,11,13]):
				tb11.start()
				tb8.start()
				tb5.start()
				tb3.start()
				while (int(now-thenn)<=txTime):
					#print "Data transmission"
					now=time.time()
					if int(now-then)==3:
						time.sleep(3)
						print "\n Sensing PUs' activities"
						then=time.time()
				print 'Closing'
				tb3.stop()
				tb3.wait()
				tb5.stop()
				tb5.wait()
				tb8.stop()
				tb8.wait()
				tb11.stop()
				tb11.wait()
			elif (SA_Q_Route==[1,3,6,8,10,13]):
				tb10.start()
				tb8.start()
				tb6.start()
				tb3.start()
				while (int(now-thenn)<=txTime):
					#print "Data transmission"
					now=time.time()
					if int(now-then)==3:
						time.sleep(2)
						print "\n Sensing PUs' activities"
						then=time.time()
				print 'Closing'
				tb3.stop()
				tb3.wait()
				tb6.stop()
				tb6.wait()
				tb8.stop()
				tb8.wait()
				tb10.stop()
				tb10.wait()
			elif (SA_Q_Route==[1,3,6,8,11,13]):
				tb11.start()
				tb8.start()
				tb6.start()
				tb3.start()
				while (int(now-thenn)<=txTime):
					#print "Data transmission"
					now=time.time()
					if int(now-then)==3:
						time.sleep(2)
						print "\n Sensing PUs' activities"
						then=time.time()
				print 'Closing'
				tb3.stop()
				tb3.wait()
				tb6.stop()
				tb6.wait()
				tb8.stop()
				tb8.wait()
				tb11.stop()
				tb11.wait()
			elif (SA_Q_Route==[1,2,4,7,9,12,13]):
				tb12.start()
				tb9.start()
				tb7.start()
				tb4.start()
				tb2.start()
				while (int(now-thenn)<=txTime):
					#print "Data transmission"
					now=time.time()
					if int(now-then)==3:
						time.sleep(2)
						print "\n Sensing PUs' activities"
						then=time.time()
				print 'Closing'
				tb2.stop()
				tb2.wait()
				tb4.stop()
				tb4.wait()
				tb7.stop()
				tb7.wait()
				tb9.stop()
				tb9.wait()
				tb12.stop()
				tb12.wait()

			elif (SA_Q_Route==[1,2,5,7,9,12,13]):
				tb12.start()
				tb9.start()
				tb7.start()
				tb5.start()
				tb2.start()
				while (int(now-thenn)<=txTime):
					#print "Data transmission"
					now=time.time()
					if int(now-then)==3:
						time.sleep(2)
						print "\n Sensing PUs' activities"
						then=time.time()
				print 'Closing'
				tb2.stop()
				tb2.wait()
				tb5.stop()
				tb5.wait()
				tb7.stop()
				tb7.wait()
				tb9.stop()
				tb9.wait()
				tb12.stop()
				tb12.wait()

			elif (SA_Q_Route==[1,3,5,7,9,12,13]):
				tb12.start()
				tb9.start()
				tb7.start()
				tb5.start()
				tb3.start()
				while (int(now-thenn)<=txTime):
					#print "Data transmission"
					now=time.time()
					if int(now-then)==3:
						time.sleep(2)
						print "\n Sensing PUs' activities"
						then=time.time()
				print 'Closing'
				tb3.stop()
				tb3.wait()
				tb5.stop()
				tb5.wait()
				tb7.stop()
				tb7.wait()
				tb9.stop()
				tb9.wait()
				tb12.stop()
				tb12.wait()


		routeBreak+=1
		print 'Route Break', routeBreak
		routeSwitch+=1
		print 'Route Switch', routeSwitch
		count+=1
		print "Count",count

	else:
		routeBreak+=1
		print 'Route Break', routeBreak
		routeSwitch+=1
		print 'Route Switch', routeSwitch
		count+=1
		print "Count",count
	
print ("Route Breaks",routeBreak)
print ("Route Switches",routeSwitch)
print ("Count",count)








