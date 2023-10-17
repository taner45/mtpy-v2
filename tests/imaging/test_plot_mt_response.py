# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 14:39:46 2023

@author: jpeacock
"""
# =============================================================================
# Imports
# =============================================================================
import unittest
from mtpy import MT
from mtpy.imaging import plot_mt_response

from mt_metadata import TF_EDI_CGG


# =============================================================================


class TestPlotMTResponse(unittest.TestCase):
    @classmethod
    def setUpClass(self):

        m1 = MT(TF_EDI_CGG)
        m1.read()

        self.z_object = m1.Z.copy()
        self.t_object = m1.Tipper.copy()
        self.pt_object = m1.pt.copy()
        self.station = m1.station

        self.plot_object = plot_mt_response.PlotMTResponse(
            z_object=self.z_object,
            t_object=self.t_object,
            pt_obj=self.pt_object,
            station=self.station,
            show_plot=False,
        )

    def test_z_object(self):
        self.assertEqual(self.z_object, self.plot_object.Z)

    def test_t_object(self):
        self.assertEqual(self.t_object, self.plot_object.Tipper)

    def test_pt_object(self):
        self.assertEqual(self.pt_object, self.plot_object.pt)

    def test_period(self):
        self.assertEqual(
            True, (self.z_object.period == self.plot_object.period).all()
        )

    def test_set_model_error_to_true(self):
        self.plot_object.plot_model_error = True
        with self.subTest("set to true"):
            self.assertEqual(self.plot_model_error, True)
        with self.subTest("error string"):
            self.assertEqual(self._error_str, "model_error")

    def test_set_model_error_to_false(self):
        self.plot_object.plot_model_error = False
        with self.subTest("set to true"):
            self.assertEqual(self.plot_model_error, False)
        with self.subTest("error string"):
            self.assertEqual(self._error_str, "error")

    @unittest.mock.patch(f"{__name__}.plot_mt_response.plt")
    def test_plot(self, mock_plt):
        self.plot_object.plot()

        assert mock_plt.figure.called


# =============================================================================
# run
# =============================================================================
if __name__ == "__main__":
    unittest.main()
