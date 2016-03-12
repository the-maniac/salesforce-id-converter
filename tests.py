from unittest import TestCase

from salesforce_id_converter import convert_id_15_to_18


class TestConvertIdConverter(TestCase):
    def test_convert_id_15_to_18(self):
        #given

        given_sf_ids_15 = ('00636000004eEwU', '001A000010khO8J')
        expected_sf_ids_18 = ('00636000004eEwUAAU', '001A000010khO8JIAU')

        #when

        results = [convert_id_15_to_18(sf_id) for sf_id in given_sf_ids_15]

        #then

        for index, sf_id in enumerate(expected_sf_ids_18):
            self.assertEqual(sf_id, results[index])