from unittest import TestLoader, TestSuite
from pyunitreport import HTMLTestRunner #para generar el reporte
from assertions import AssertionsTest
from search_tests_suite import SearchTests


assertions_test = TestLoader().loadTestsFromTestCase(AssertionsTest)
search_tests = TestLoader().loadTestsFromTestCase(SearchTests)

#construimos la suite de pruebas
smoke_test = TestSuite([assertions_test, search_tests])


#para generar los reporters
kwargs = {
    "output": 'smoke-report'
    }

#la variable runner almacena un reporte generado por HTMLTestRunner
#usa como argumento "kwargs"
runner = HTMLTestRunner(**kwargs)

#corro el runner con la suite de prueba
runner.run(smoke_test) 