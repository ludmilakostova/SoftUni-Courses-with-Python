from unittest import TestCase, main

from project.hero import Hero


class TestHero(TestCase):
    def setUp(self):
        self.hero = Hero("Mila", 10, 100, 5.0)

    def test_init_attributes(self):
        self.assertEqual("Mila", self.hero.username)
        self.assertEqual(10, self.hero.level)
        self.assertEqual(100, self.hero.health)
        self.assertEqual(5.0, self.hero.damage)

    def test_battle_enemy_hero_set_up_with_same_username(self):
        enemy_hero = Hero("Mila", 5, 50, 7)
        with self.assertRaises(Exception) as ex:
            self.hero.battle(enemy_hero)
        self.assertEqual('You cannot fight yourself', str(ex.exception))

    def test_battle_enemy_hero_set_up_with_negative_health(self):
        enemy_hero = Hero("BiBi", 5, -5, 7)
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(enemy_hero)
        self.assertEqual('You cannot fight BiBi. He needs to rest', str(ex.exception))

    def test_battle_with_hero_health_negative(self):
        self.hero.health = -5
        enemy_hero = Hero("BiBi", 5, 3, 7)
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(enemy_hero)
        self.assertEqual('Your health is lower than or equal to 0. You need to rest', str(ex.exception))

    def test_battle_both_loses(self):
        enemy_hero = Hero("Bibi", 3, 50, 50)
        result = self.hero.battle(enemy_hero)
        self.assertEqual("Draw", result)

    def test_battle_hero_wins(self):
        enemy_hero = Hero("Bibi", 1, 50, 1)
        result = self.hero.battle(enemy_hero)
        self.assertEqual(0, enemy_hero.health)
        self.assertEqual(11, self.hero.level)
        self.assertEqual(104, self.hero.health)
        self.assertEqual(10.0, self.hero.damage)
        self.assertEqual('You win', result)

    def test_battle_hero_looses(self):
        enemy_hero = Hero("Bibi", 20, 100, 10)
        result = self.hero.battle(enemy_hero)
        self.assertEqual(-100, self.hero.health)
        self.assertEqual(21, enemy_hero.level)
        self.assertEqual(55, enemy_hero.health)
        self.assertEqual(15.0, enemy_hero.damage)
        self.assertEqual('You lose', result)

    def test_str_representation(self):
        self.assertEqual('Hero Mila: 10 lvl\nHealth: 100\nDamage: 5.0\n', str(self.hero))


if __name__ == '__main__':
    main()