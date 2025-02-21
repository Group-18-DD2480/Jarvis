import unittest
from tests import PluginTest
from plugins.mips_conv import MipsConverter


class TestMipsConverter(PluginTest):
    def setUp(self):
        self.test = self.load_plugin(MipsConverter)

    def test_hex_to_assembly(self):
        """Test basic I-type instruction (ADDI)"""
        self.test.run("212A0012")
        self.assertIn("ADDI $t2 $t1 0x0012", self.history_say().last_text())

    def test_r_type_instruction(self):
        """Test R-type instruction (ADD)"""
        self.test.run("014B4820")
        self.assertIn("ADD $t1 $t2 $t3", self.history_say().last_text())

    def test_i_type_branch(self):
        """Test I-type branch instruction (BEQ)"""
        self.test.run("11290003")
        self.assertIn("BEQ $t1 $t1 0x0003", self.history_say().last_text())

    def test_j_type_jump(self):
        """Test J-type instruction (J)"""
        self.test.run("08100000")
        self.assertIn("J 0x0100000", self.history_say().last_text())

    def test_r_type_shift(self):
        """Test R-type shift instruction (SLL)"""
        self.test.run("00094940")
        self.assertIn("SLL $t1 $t1 0x05", self.history_say().last_text())

    def test_load_store(self):
        """Test load/store instruction (LW)"""
        self.test.run("8C090004")
        self.assertIn("LW $t1 0x0004($zero)", self.history_say().last_text())

    def test_r_type_move(self):
        """Test R-type move instruction (MOVZ)"""
        self.test.run("0149482A")
        self.assertIn("SLT $t1 $t2 $t1", self.history_say().last_text())

    def test_i_type_immediate(self):
        """Test I-type instruction with immediate (LUI)"""
        self.test.run("3C011234")
        self.assertIn("LUI $at 0x1234", self.history_say().last_text())

    def test_invalid_instruction(self):
        """Test invalid hex instruction"""
        self.test.run("FFFFFFFF")
        self.assertIn("No such command exists", self.history_say().last_text())


if __name__ == "__main__":
    unittest.main()
