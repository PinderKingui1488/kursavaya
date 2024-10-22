import pytest

from src.hhapi import HeadHunterAPI
from src.vacancys import Vacancy


@pytest.fixture
def hh_data() -> HeadHunterAPI:
    return HeadHunterAPI()


@pytest.fixture
def vacancies() -> Vacancy:
    vacancy_data = {
        "name": "Таролог в Футбольный клуб «Сокол»",
        "url": "https://api.hh.ru/areas/88",
        "salary": {"from": 300000},
        "description": "Ну да",
    }
    return Vacancy(vacancy_data)


def test_head_hunter_api(hh_data) -> None:
    assert hh_data is not None


def test_vacancy_init(vacancies) -> None:
    assert vacancies.name == "Таролог в Футбольный клуб «Сокол»"
    assert vacancies.url == "https://api.hh.ru/areas/88"
    assert vacancies.salary == 300000
    assert vacancies.description == "Ну да"

