import unittest
from tournament import Runner, Tournament  # Импортируем классы из другого модуля


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner("Усэйн", speed=10)
        self.andrey = Runner("Андрей", speed=9)
        self.nik = Runner("Ник", speed=3)

    @classmethod
    def tearDownClass(cls):
        # Изменим вывод, чтобы показать имена бегунов, а не объекты
        for key in sorted(cls.all_results.keys()):
            result = cls.all_results[key]
            formatted_result = {place: runner.name for place, runner in result.items()}
            print(formatted_result)

    def test_usain_and_nik(self):
        tournament = Tournament(90, self.usain, self.nik)
        results = tournament.start()
        TournamentTest.all_results["test_usain_and_nik"] = results
        self.assertTrue(results[max(results.keys())].name == "Ник")

    def test_andrey_and_nik(self):
        tournament = Tournament(90, self.andrey, self.nik)
        results = tournament.start()
        TournamentTest.all_results["test_andrey_and_nik"] = results
        self.assertTrue(results[max(results.keys())].name == "Ник")

    def test_usain_andrey_and_nik(self):
        tournament = Tournament(90, self.usain, self.andrey, self.nik)
        results = tournament.start()
        TournamentTest.all_results["test_usain_andrey_and_nik"] = results
        self.assertTrue(results[max(results.keys())].name == "Ник")


if __name__ == '__main__':
    unittest.main()
