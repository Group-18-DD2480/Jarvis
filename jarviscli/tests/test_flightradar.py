import unittest
from tests import PluginTest
from unittest.mock import patch, MagicMock
from plugins.flightradar import flightradar


class TestFlightRadarPlugin(PluginTest):

    def setUp(self):
        super().setUp()
        self.plugin = self.load_plugin(flightradar)

    @patch('FlightRadar24.api.FlightRadar24API.get_flights')
    @patch('FlightRadar24.api.FlightRadar24API.get_airlines')
    @patch('FlightRadar24.api.FlightRadar24API.get_airports')
    @patch('builtins.input')
    def test_check_airline_flights_by_icao(
        self, 
        mock_input, 
        mock_get_airports, 
        mock_get_airlines, 
        mock_get_flights
    ):
        mock_input.side_effect = ['1','1','UAL']

        
        mock_get_airports.return_value = []
        mock_get_airlines.return_value = []
        mock_get_flights.return_value = [
            MagicMock(
                airline_icao="UAL",
                registration="N12345",
                origin_airport_iata="JFK",
                destination_airport_iata="LAX",
                latitude=40.7128,
                longitude=-74.0060,
                time="12:00",
                altitude=35000
            )
        ]

        self.plugin.run('flightradar')

        self.assertTrue(
            any("UAL" in entry[0] for entry in self.history_say()._storage_by_index),
            "Airline ICAO not found in output"
        )
        self.assertTrue(
            any("N12345" in entry[0] for entry in self.history_say()._storage_by_index),
            "Registration number not found"
        )

    @patch('FlightRadar24.api.FlightRadar24API.get_flights')
    @patch('FlightRadar24.api.FlightRadar24API.get_airlines')
    @patch('FlightRadar24.api.FlightRadar24API.get_airports')
    @patch('builtins.input')  
    def test_check_flights_between_destinations_by_iata(
        self, 
        mock_input, 
        mock_get_airports, 
        mock_get_airlines, 
        mock_get_flights
    ):
        mock_input.side_effect = ['2','1','JFK','LAX']

        mock_get_airports.return_value = []
        mock_get_airlines.return_value = []
        mock_get_flights.return_value = [
            MagicMock(
                airline_icao="UAL",
                registration="N12345",
                origin_airport_iata="JFK",
                destination_airport_iata="LAX",
                latitude=40.7128,
                longitude=-74.0060,
                time="12:00",
                altitude=35000
            )
        ]

        # Run the plugin
        self.plugin.run('flightradar')

        # Verify outputs
        self.assertTrue(
            any("JFK" in entry[0] and "LAX" in entry[0] 
                for entry in self.history_say()._storage_by_index),
            "Route JFK->LAX not displayed"
        )

if __name__ == '__main__':
    unittest.main()
