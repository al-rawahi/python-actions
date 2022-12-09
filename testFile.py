from unittest import TestCase
import racesAndRunners


class Test(TestCase):
    def test_display_races(self): # pass
        self.assertIn('KY-43 won the race.',racesAndRunners.display_races(
            ['KY-43', 'CK-11', 'CK-23', 'WD-32', 'TP-02', 'WD-19', 'LK-73']
            , [1915, 2045, 2020, 1928, 2020, 1926, 2131], 'Adrigole', 'KY-43'))

    def test_displaying_runners_who_have_won_at_least_one_race(self): # pass
        self.assertIn('WD-32',racesAndRunners.displaying_runners_who_have_won_at_least_one_race(
            ['Currabinny, 30', 'Adrigole, 32', 'Conna, 29', 'Dunmanway, 29.5', 'Glengarriff, 32.5'],
            ['Anna Fox', 'Des Kelly', 'Ann Cahill', 'Joe Flynn', 'Sally Fox', 'Joe Shine',
             'Lisa Collins', 'Sil Murphy', 'Des Kelly'],['CK-24', 'CK-23 ', 'KY-43 ', 'CK-11 ',
                                                         'KY-12 ', 'TP-02', 'WD-32', 'LK-73', 'WD-19']))

    def test_displaying_runners_who_have_not_won_any_race(self): # pass
        self.assertIn('Anna Fox', racesAndRunners.displaying_runners_who_have_not_won_any_race(
            ['Currabinny, 30', 'Adrigole, 32', 'Conna, 29', 'Dunmanway, 29.5', 'Glengarriff, 32.5']))


if __name__ == "__main__":
    Test()

    
    
