import unittest

from myflaskproj import app
app.config['TESTING'] = True

from myflaskproj.commands import power, repeat

class TestPowerCommand(unittest.TestCase):
    
    def setUp(self):
        self.runner = app.test_cli_runner()
        
    def test_power_command(self):
        result = self.runner.invoke(power, args=['2', '4'])
        self.assertEqual('16', result.output.strip())
        
    def test_power_with_extra_arguments(self):
        result = self.runner.invoke(power, args=['2', '4', '5'])
        self.assertIn('Error: Got unexpected extra argument', result.output)
         
    def test_power_with_no_arguments(self):
        result = self.runner.invoke(power)
        self.assertIn('Error: Missing argument', result.output)
        
    def test_power_with_argument_x_as_str(self):
        result = self.runner.invoke(power, args=['apple', '3' ])
        self.assertIn('Error: Invalid value for "X"', result.output)
        
    def test_power_with_argument_y_as_str(self):
        result = self.runner.invoke(power, args=['3', 'apple' ])
        self.assertIn('Error: Invalid value for "Y"', result.output)
        
    def test_power_with_arguments_xy_as_str(self):
        result = self.runner.invoke(power, args=['car', 'apple' ])
        self.assertIn('Error: Invalid value for "X"', result.output)
        
        
class TestRepeatCommand(unittest.TestCase):
    
    def setUp(self):
        self.runner = app.test_cli_runner()
        
    def test_repeat_command(self):
        result = self.runner.invoke(repeat, args=['Hello', '3'])
        self.assertEqual('HelloHelloHello', result.output.strip())
        
    def test_repeat_with_extra_arguments(self):
        result = self.runner.invoke(repeat, args=['Hello', '3', '5'])
        self.assertIn('Error: Got unexpected extra argument', result.output)
         
    def test_repeat_with_no_arguments(self):
        result = self.runner.invoke(repeat)
        self.assertIn('Error: Missing argument', result.output)
        
    def test_repeat_with_argument_s_as_float(self):
        result = self.runner.invoke(repeat, args=['5.6', '4' ])
        self.assertEqual('5.65.65.65.6', result.output.strip())
        
    def test_repeat_with_argument_n_as_str(self):
        result = self.runner.invoke(repeat, args=['3', 'apple' ])
        self.assertIn('Error: Invalid value for "N"', result.output)
        
    def test_repeat_with_arguments_sn_as_str(self):
        result = self.runner.invoke(repeat, args=['hello', 'car' ])
        self.assertIn('Error: Invalid value for "N"', result.output)  