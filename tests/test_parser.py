from pretty_dbt.parser import parse_event


class TestParseEvents:
    def test_it_parses_the_model_name(self):
        msg = '19:38:37 | 1 of 12 START table model ETL.SWINE [RUN]'
        assert parse_event(msg).model_name == 'ETL.SWINE'

        msg = '19:38:37 | 2 of 12 START table model ETL.PEARLS [RUN]'
        assert parse_event(msg).model_name == 'ETL.PEARLS'

    def test_it_parses_the_model_name_with_trailling_elipses(self):
        msg = '19:38:37 | 1 of 12 START table model ETL.SWINE.... [RUN]'
        assert parse_event(msg).model_name == 'ETL.SWINE'

    def test_it_parses_START_event_type(self):
        msg = '19:38:37 | 1 of 12 START table model ETL.SWINE [RUN]'
        assert parse_event(msg).event_type == 'START'

    def test_it_parses_OK_event_type(self):
        msg = '19:38:46 | 1 of 12 OK created table model ETL.SWINE [SUCCESS 1 in 8.75s]'
        assert parse_event(msg).event_type == 'OK'

    def test_it_parses_time_for_OK_event_type(self):
        msg = '19:38:46 | 1 of 12 OK created table model ETL.SWINE [SUCCESS 1 in 8.75s]'
        assert parse_event(msg).duration_seconds == 8.75
