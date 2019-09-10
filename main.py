import dataclasses
import datetime

JST = datetime.timezone(datetime.timedelta(hours=9), 'JST')


@dataclasses.dataclass(frozen=True)
class Movie:
    title: str
    dimension: str


@dataclasses.dataclass(frozen=True)
class Screen:
    movie: Movie
    schedule: datetime.datetime


@dataclasses.dataclass(frozen=True)
class ReservingPerson:
    screen: Screen
    person_type: str


@dataclasses.dataclass(frozen=True)
class ScreenPrice:
    screen: Screen
    person_type: str
    price: int

    @property
    def amount(self) -> int:
        return self.price


@dataclasses.dataclass(frozen=True)
class ScreenPriceCalculator:
    screen: Screen
    reserving_person: ReservingPerson

    def price(self) -> ScreenPrice:
        if self.screen.movie.dimension == '2d' and self.screen.schedule.weekday() <= 4 and self.reserving_person.person_type == 'normal':
            return ScreenPrice(
                screen=self.screen,
                person_type=self.reserving_person.person_type,
                price=1800
            )

        if self.screen.movie.dimension == '3d' and self.screen.schedule.weekday() >= 5 and self.reserving_person.person_type == 'normal':
            return ScreenPrice(
                screen=self.screen,
                person_type=self.reserving_person.person_type,
                price=2200
            )


def sample_laputa_weekday_normal_person():
    movie = Movie(title='天空の城ラピュタ', dimension='2d')
    screen = Screen(movie=movie, schedule=datetime.datetime(2019, 9, 2, 10, 0, tzinfo=JST))
    reserving = ReservingPerson(screen=screen, person_type='normal')

    screen_price = ScreenPriceCalculator(screen=screen, reserving_person=reserving).price()

    print('-' * 80)
    print(f'movie = {movie}')
    print(f'screen = {screen}')
    print(f'reserving_person = {reserving}')
    print(f'screen_price = {screen_price}')
    print(f'screen_price.amount = {screen_price.amount}')


def sample_avatar_holiday_late_show_normal_person():
    movie = Movie(title='アバター', dimension='3d')
    screen = Screen(movie=movie, schedule=datetime.datetime(2019, 9, 8, 20, 0, tzinfo=JST))
    reserving = ReservingPerson(screen=screen, person_type='normal')

    screen_price = ScreenPriceCalculator(screen=screen, reserving_person=reserving).price()

    print('-' * 80)
    print(f'movie = {movie}')
    print(f'screen = {screen}')
    print(f'reserving_person = {reserving}')
    print(f'screen_price = {screen_price}')
    print(f'screen_price.amount = {screen_price.amount}')


if __name__ == '__main__':
    sample_laputa_weekday_normal_person()
    sample_avatar_holiday_late_show_normal_person()
