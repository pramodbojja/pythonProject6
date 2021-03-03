import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

    @classmethod
    def setUp(self):
        print("setUp")

    @classmethod
    def tearDown(self):
        print("tearDown/n")


    def setUp(self):
        print("setUp")
        self.emp_1 = Employee("Nilly", "willy",85200)
        self.emp_2 = Employee("Rilly", "rally", 56000)

    def tearDown(self):
        print("tearDown/n")
        pass


    def test_fullname(self):
        print("test_fullname")
        emp_1 = Employee("Nilly", "willy",85200)
        emp_2 = Employee("Rilly", "rally",56000)

        self.assertEqual(emp_1.fullname,"Nilly willy")
        self.assertEqual(emp_2.fullname, "Rilly rally")

        emp_1.first = "Jamanzi"
        emp_2.first= "Pithaji"

        self.assertEqual(emp_1.fullname,"Jamanzi willy")
        self.assertEqual(emp_2.fullname,"Pithaji rally")


    def test_apply_raise(self):
        print("test_apply_raise")
        emp_1 = Employee("Nilly", "willy", 85200)
        emp_2 = Employee("Rilly", "rally", 56000)


        emp_1.apply_raise()
        emp_2.apply_raise()

        self.assertEqual(emp_1.pay,88608 )
        self.assertEqual(emp_2.pay,58240 )



    def test_email(self):
        print("test_email")
        emp_1 = Employee("Nilly", "willy", 85200)
        emp_2 = Employee("Rilly", "rally", 56000)

        self.assertEqual(emp_1.email, "Nilly.willy@email.com")
        self.assertEqual(emp_2.email, "Rilly.rally@email.com")

        emp_1.first = "Jamanzi"
        emp_2.first = "Pithaji"

        self.assertEqual(emp_1.email, "Jamanzi.willy@email.com")
        self.assertEqual(emp_2.email, "Pithaji.rally@email.com")

if __name__ =="__main__":
    unittest.main()